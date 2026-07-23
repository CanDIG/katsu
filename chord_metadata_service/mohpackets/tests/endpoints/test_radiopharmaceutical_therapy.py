from http import HTTPStatus

from django.conf import settings
from django.forms.models import model_to_dict

from chord_metadata_service.mohpackets.models import RadiopharmaceuticalTherapy
from chord_metadata_service.mohpackets.tests.endpoints.base import BaseTestCase
from chord_metadata_service.mohpackets.tests.factories import (
    RadiopharmaceuticalTherapyFactory,
)


# INGEST API
# ----------
class IngestTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = "/v3/ingest/radiopharmaceutical_therapies/"

    def test_create_authorized(self):
        therapy = RadiopharmaceuticalTherapyFactory.build(
            treatment_uuid=self.treatments[0]
        )
        data_dict = model_to_dict(therapy)
        response = self.client.post(
            self.url,
            data=[data_dict],
            format="json",
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        self.assertEqual(
            response.status_code,
            HTTPStatus.CREATED,
            f"Expected {HTTPStatus.CREATED}, got {response.status_code}. "
            f"Response content: {response.content}",
        )

    def test_create_unauthorized(self):
        therapy = RadiopharmaceuticalTherapyFactory.build(
            treatment_uuid=self.treatments[0]
        )
        data_dict = model_to_dict(therapy)
        response = self.client.post(
            self.url,
            data=[data_dict],
            content_type="application/json",
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_0.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_ingest_validator(self):
        therapy = RadiopharmaceuticalTherapyFactory.build(
            treatment_uuid=self.treatments[0]
        )
        data_dict = model_to_dict(therapy)
        data_dict["radionuclide"] = "invalid"
        response = self.client.post(
            self.url,
            data=[data_dict],
            content_type="application/json",
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        self.assertEqual(
            response.status_code,
            HTTPStatus.UNPROCESSABLE_ENTITY,
            f"Expected {HTTPStatus.UNPROCESSABLE_ENTITY}, got {response.status_code}. "
            f"Response content: {response.content}",
        )


# GET API
# -------
class GETTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = "/v3/authorized/radiopharmaceutical_therapies/"

    def test_get_200_ok(self):
        response = self.client.get(
            self.url,
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_301_redirect(self):
        response = self.client.get(
            "/v3/authorized/radiopharmaceutical_therapies",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.MOVED_PERMANENTLY)


# OTHERS
# ------
class RadiopharmaceuticalTherapyOthersTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = "/v3/authorized/radiopharmaceutical_therapies/"

    def test_get_datasets_match_permission(self):
        for user in self.users:
            authorized_datasets = settings.LOCAL_OPA_DATASET.get(user.token, {}).get(
                "read_datasets", []
            )
            expected_datasets = [
                str(dataset)
                for dataset in RadiopharmaceuticalTherapy.objects.filter(
                    program_id__in=authorized_datasets
                )
            ]
            response = self.client.get(
                self.url,
                HTTP_AUTHORIZATION=f"Bearer {user.token}",
            )
            response = response.json()
            response_data = [
                f'{t["program_id"]}: {t["submitter_treatment_id"]}'
                for t in response["items"]
            ]
            self.assertEqual(response_data, expected_datasets)

    def test_post_request_405(self):
        response = self.client.post(
            self.url, HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}"
        )
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_put_request_405(self):
        response = self.client.put(
            self.url, HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}"
        )
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_patch_request_405(self):
        response = self.client.patch(
            self.url, HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}"
        )
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_delete_request_404(self):
        therapy_to_delete = RadiopharmaceuticalTherapyFactory()
        response = self.client.delete(
            f"{self.url}{therapy_to_delete.uuid}/",
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)


# NESTED CLINICAL DATA
# --------------------
class NestedClinicalDataTestCase(BaseTestCase):
    def test_radiopharmaceutical_therapy_nested_in_clinical_data(self):
        """
        The donor_with_clinical_data endpoint must nest radiopharmaceutical
        therapies under their treatment (alias radiopharmaceuticaltherapy_set).
        """
        therapy = self.radiopharmaceutical_therapies[0]
        program_id = therapy.program_id_id
        donor_id = therapy.submitter_donor_id
        url = (
            f"/v3/authorized/donor_with_clinical_data/"
            f"program/{program_id}/donor/{donor_id}"
        )
        response = self.client.get(
            url, HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}"
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

        data = response.json()
        nested = [
            rt
            for pd in data["primary_diagnoses"]
            for tx in pd["treatments"]
            for rt in tx["radiopharmaceutical_therapies"]
        ]
        self.assertTrue(
            nested, "expected radiopharmaceutical_therapies nested under treatments"
        )
        self.assertIn(
            therapy.radionuclide, [rt["radionuclide"] for rt in nested]
        )
