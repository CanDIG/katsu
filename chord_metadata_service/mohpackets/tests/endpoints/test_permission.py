from http import HTTPStatus

from django.conf import settings
from django.forms.models import model_to_dict

from chord_metadata_service.mohpackets.tests.endpoints.base import BaseTestCase
from chord_metadata_service.mohpackets.tests.factories import (
    DonorFactory,
    PrimaryDiagnosisFactory,
    ProgramFactory,
    TreatmentFactory,
)

"""
    This module tests users with different roles to ensure they
    can perform ingestion and deletion operations as appropriate.
    It is OPA responsibility to ensure authorized_datasets is up to date.

    - Site Admin and Curator: Can read and write within their authorized_datasets.
    - Normal User: Has read-only access.

    Author: Son Chau
"""


# INGEST API
# ----------
class IngestTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.donor_url = "/v3/ingest/donors/"

    def test_ingest_with_normal_user(self):
        """
        Test that a normal user attempting to create a donor receives a 401 response.

        Testing Strategy:
        - Build Donor data based on the existing program_id
        - An unauthorized user (user_0) with no permission.
        - User cannot perform a POST request for donor creation.
        """
        donor = DonorFactory.build(program_id=self.programs[0])
        data_dict = model_to_dict(donor)
        response = self.client.post(
            self.donor_url,
            data=[data_dict],
            content_type="application/json",
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_0.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_unauthorized_ingest_with_curator(self):
        """
        Test that a curator cannot to create a donor in unauthorized program

        Testing Strategy:
        - Build Donor data based on the existing program_id
        - An unauthorized curator (user_1) with no permission on that program_id
        - User cannot perform a POST request for donor creation.
        """
        donor = DonorFactory.build(program_id=self.programs[0])
        data_dict = model_to_dict(donor)
        response = self.client.post(
            self.donor_url,
            data=[data_dict],
            content_type="application/json",
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_0.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_authorized_ingest_with_curator(self):
        """
        Test that a curator can create a donor with authorized program

        Testing Strategy:
        - Build Donor data based on the existing program_id
        - An authorized curator (user_1) with permission on that program_id
        - User can perform a POST request for donor creation.
        """
        donor = DonorFactory.build(program_id=self.programs[1])
        data_dict = model_to_dict(donor)
        response = self.client.post(
            self.donor_url,
            data=[data_dict],
            content_type="application/json",
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_authorized_ingest_with_site_admin(self):
        """
        Test that an admin can ingest

        Testing Strategy:
        - Build Donor data based on the existing program_id
        - An authorized admin (user_2) with permission on that program_id
        - User can perform a POST request for donor creation.
        """
        donor = DonorFactory.build(program_id=self.programs[0])
        data_dict = model_to_dict(donor)
        response = self.client.post(
            self.donor_url,
            data=[data_dict],
            content_type="application/json",
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_unauthorized_ingest_with_site_admin(self):
        """
        Test that an admin cannot ingest without permission

        Testing Strategy:
        - Build Donor data based on new a program (not authorized in OPA yet)
        - An authorized admin (user_2) don't have permission on that program_id
        - User cannot perform a POST request for donor creation.
        """
        program = ProgramFactory.create()
        donor = DonorFactory.build(program_id=program)
        data_dict = model_to_dict(donor)
        response = self.client.post(
            self.donor_url,
            data=[data_dict],
            content_type="application/json",
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)


# DELETE API
# ----------
class DeleteTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.delete_url = "/v3/ingest/program/"

    def test_delete_with_normal_user(self):
        """
        Test a normal user cannot delete a program

        Testing Strategy:
        - A normal user (user_0) cannot delete
        - The request should receive a 401 response.
        """
        response = self.client.delete(
            f"{self.delete_url}{self.programs[0]}/",
            HTTP_AUTHORIZATION=f"Bearer {self.user_0.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_delete_with_unauthorized_curator(self):
        """
        Test a curator cannot delete an unauthorized program

        Testing Strategy:
        - A curator (user_1) attempts to delete a program
        - The request should receive a 401 response.
        """
        response = self.client.delete(
            f"{self.delete_url}{self.programs[0]}/",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_delete_with_authorized_curator(self):
        """
        Test a curator can delete a authorized program

        Testing Strategy:
        - A curator (user_1) attempts to delete a program
        - The request should receive a 204 response.
        """
        response = self.client.delete(
            f"{self.delete_url}{self.programs[1]}/",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

    def test_delete_with_site_admin(self):
        """
        Test a site admin can delete any program

        Testing Strategy:
        - Create a new program
        - A site admin (user_2) can perform delete
        - The request should receive a 204 response.
        """
        program_to_delete = ProgramFactory.create()
        response = self.client.delete(
            f"{self.delete_url}{program_to_delete}/",
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)


# GET API
# -------
class GETTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.treatments_url = "/v3/authorized/treatments/"

    def test_get_treatments_with_normal_user(self):
        """
        Test a normal user can only see authorized dataset

        Testing Strategy:
        - An authorized user (user_0) attempts a GET request for authorized treatments.
        - All the treatments only come from authorized programs
        """
        authorized_datasets = settings.LOCAL_OPA_DATASET.get(self.user_0.token, {}).get(
            "read_datasets", []
        )
        response = self.client.get(
            self.treatments_url,
            HTTP_AUTHORIZATION=f"Bearer {self.user_0.token}",
        )
        response = response.json()
        program_ids = list({treatment["program_id"] for treatment in response["items"]})
        self.assertCountEqual(program_ids, authorized_datasets)

    def test_get_treatments_with_curator(self):
        """
        Test a curator can only see authorized dataset

        Testing Strategy:
        - An curator (user_1) attempts a GET request for authorized treatments.
        - All the treatments only come from authorized programs
        """
        authorized_datasets = settings.LOCAL_OPA_DATASET.get(self.user_1.token, {}).get(
            "read_datasets", []
        )
        response = self.client.get(
            self.treatments_url,
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        response = response.json()
        program_ids = list({treatment["program_id"] for treatment in response["items"]})
        self.assertCountEqual(program_ids, authorized_datasets)

    def test_get_treatments_with_site_admin(self):
        """
        Test a site admin can only see authorized dataset, not all

        Testing Strategy:
        - Create a new treatment with a new program
        - A site admin (user_2) attempts a GET request for authorized treatments.
        - The new treatmnet is not in the return treatments
        """
        program = ProgramFactory.create()
        donor = DonorFactory.create(program_id=program)
        primary_diagnosis = PrimaryDiagnosisFactory.create(donor_uuid=donor)
        treatment = TreatmentFactory.create(
            primary_diagnosis_uuid=primary_diagnosis,
        )
        response = self.client.get(
            self.treatments_url,
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        response = response.json()
        self.assertNotIn(treatment, response["items"])
