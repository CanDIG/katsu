from http import HTTPStatus

from django.conf import settings
from django.forms.models import model_to_dict

from chord_metadata_service.mohpackets.tests.endpoints.base import BaseTestCase
from chord_metadata_service.mohpackets.tests.factories import ProgramFactory

"""
    This file contains test cases for Program API endpoints.
    The tests cover various scenarios to ensure proper functionality and authorization
    for API endpoints.

"""


# INGEST API
# ----------
class IngestTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.ingest_url = "/v3/ingest/programs/"

    def test_ingest_authorized(self):
        """
        Test that an admin user can ingest and receive 201 Created response

        Testing Strategy:
        - An authorized user (user_2) with admin permission.
        - User can perform a POST request for program ingestion.
        """
        ingest_program = ProgramFactory.build(program_id="admin_authorized_program_id")
        data_dict = model_to_dict(ingest_program)
        response = self.client.post(
            self.ingest_url,
            data=[data_dict],
            content_type="application/json",
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        self.assertEqual(
            response.status_code,
            HTTPStatus.CREATED,
            f"Expected status code {HTTPStatus.CREATED}, but got {response.status_code}. "
            f"Response content: {response.content}",
        )

    def test_ingest_unauthorized(self):
        """
        Test that an non-admin user attempting to ingest programs receives a 401 response.

        Testing Strategy:
        - An unauthorized user (user_0) with no permission.
        - User cannot perform a POST request for program ingestion.
        """
        ingest_program = ProgramFactory.build()
        data_dict = model_to_dict(ingest_program)
        response = self.client.post(
            self.ingest_url,
            data=[data_dict],
            content_type="application/json",
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_0.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)


# DELETE API
# ----------
class DeleteTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.delete_url = "/v3/ingest/program/"

    def test_delete_authorized(self):
        """
        Test an authorized DELETE request to the 'authorized/program/{program_id}/' endpoint.

        Testing Strategy:
        - Create a new program to delete
        - Admin (user_2) can delete
        - The request should receive a 204 no content response.
        """
        program_to_delete = ProgramFactory()
        response = self.client.delete(
            f"{self.delete_url}{program_to_delete.program_id}/",
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

    def test_delete_unauthorized(self):
        """
        Test an unauthorized DELETE request 'ingest/programs/{program_id}/' endpoint.

        Testing Strategy:
        - Create a new program to delete
        - Non Admin (user_1) cannot delete
        - The request should receive a 401 response.
        """
        program_to_delete = ProgramFactory()
        response = self.client.delete(
            f"{self.delete_url}{program_to_delete.program_id}/",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)


# UPDATE API
# ----------
class UpdateTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        # user_1 has write access to programs[1]
        self.program = self.programs[1]
        self.update_url = f"/v3/ingest/programs/{self.program.program_id}/"

    def test_update_authorized(self):
        """A curator with write access can PATCH clinical fields (200)."""
        response = self.client.patch(
            self.update_url,
            data={"study_name": "Updated Study Name", "status": "Completed"},
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            f"Response content: {response.content}",
        )
        self.program.refresh_from_db()
        self.assertEqual(self.program.study_name, "Updated Study Name")
        self.assertEqual(self.program.status, "Completed")

    def test_update_unauthorized(self):
        """A user without write access cannot update (401)."""
        response = self.client.patch(
            self.update_url,
            data={"study_name": "Hacked"},
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_0.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_update_partial_only(self):
        """Fields omitted from the body are left untouched."""
        original_context = self.program.context
        response = self.client.patch(
            self.update_url,
            data={"study_name": "Only Name Changed"},
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.program.refresh_from_db()
        self.assertEqual(self.program.study_name, "Only Name Changed")
        self.assertEqual(self.program.context, original_context)

    def test_update_invalid_permissible_value(self):
        """A value outside the permissible list is rejected (422)."""
        response = self.client.patch(
            self.update_url,
            data={"status": "Paused"},
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def test_update_does_not_affect_metadata(self):
        """Updating clinical fields must not change the metadata field."""
        self.program.metadata = {"source": "service"}
        self.program.save(update_fields=["metadata"])
        response = self.client.patch(
            self.update_url,
            # metadata is excluded from the schema, so this key is ignored
            data={"study_name": "New Name", "metadata": {"source": "user"}},
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.program.refresh_from_db()
        self.assertEqual(self.program.study_name, "New Name")
        self.assertEqual(self.program.metadata, {"source": "service"})


# METADATA UPDATE API
# -------------------
class MetadataUpdateTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.program = self.programs[1]
        self.metadata_url = (
            f"/v3/ingest/programs/{self.program.program_id}/metadata/"
        )

    def test_metadata_update_with_service_token(self):
        """The ingest service token can update metadata (200)."""
        response = self.client.patch(
            self.metadata_url,
            data={"metadata": {"source": "service"}},
            content_type="application/json",
            HTTP_X_SERVICE_TOKEN="candig-ingest",
        )
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            f"Response content: {response.content}",
        )
        self.program.refresh_from_db()
        self.assertEqual(self.program.metadata, {"source": "service"})

    def test_metadata_update_user_forbidden(self):
        """A user bearer token cannot update metadata (401)."""
        response = self.client.patch(
            self.metadata_url,
            data={"metadata": {"source": "user"}},
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)
        self.program.refresh_from_db()
        self.assertNotEqual(self.program.metadata, {"source": "user"})


# GET API
# -------
class GETTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.authorized_url = "/v3/authorized/programs/"

    def test_get_200_ok(self):
        """
        Test a successful GET request to the 'authorized/programs/' endpoint.

        Testing Strategy:
        - An authorized user (user_1) attempts a GET request for authorized programs.
        - The request should receive a 200 OK response.
        """
        response = self.client.get(
            self.authorized_url,
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_301_redirect(self):
        """
        Test a GET request endpoint with a 301 redirection.

        Testing Strategy:
        - Send a GET request to the '/v3/authorized/programs' endpoint.
        - The request should receive a 301 redirection response.
        """
        response = self.client.get(
            "/v3/authorized/programs", HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}"
        )
        self.assertEqual(response.status_code, HTTPStatus.MOVED_PERMANENTLY)

    def test_get_404_not_found(self):
        """
        Test a GET request for a 404 Not Found response.

        Testing Strategy:
        - Send a GET request to a non-existent endpoint.
        - The request should receive a 404 Not Found response.
        """
        response = self.client.get(
            "/v3/authorized/invalid/",
            HTTP_AUTHORIZATION=f"Bearer {self.user_1.token}",
        )
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)


# OTHERS
# ------
class OthersTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.authorized_url = "/v3/authorized/programs/"

    def test_get_datasets_match_permission(self):
        """
        Test that the response datasets match the authorized datasets for each user.

        Testing Strategy:
        - Verify that the response datasets match the datasets in the authorized dataset
          for each of the test users.
        """
        for user in self.users:
            response = self.client.get(
                self.authorized_url,
                HTTP_AUTHORIZATION=f"Bearer {user.token}",
            )
            response = response.json()

            authorized_datasets = settings.LOCAL_OPA_DATASET.get(user.token, {}).get(
                "read_datasets", []
            )
            response_datasets = [program["program_id"] for program in response["items"]]
            self.assertEqual(response_datasets, authorized_datasets)

    def test_post_request_405(self):
        """
        Test a POST request to the '/authorized/programs/' endpoint.
        The request should receive a 405 Method Not Allowed response.
        """
        response = self.client.post(
            self.authorized_url, HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}"
        )
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_put_request_405(self):
        """
        Test a PUT request to the '/authorized/programs/' endpoint.
        The request should receive a 405 Method Not Allowed response.
        """
        response = self.client.put(
            self.authorized_url, HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}"
        )
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_patch_request_405(self):
        """
        Test a PATCH request to the '/authorized/programs/' endpoint.
        The request should receive a 405 Method Not Allowed response.
        """
        response = self.client.patch(
            self.authorized_url, HTTP_AUTHORIZATION=f"Bearer {self.user_2.token}"
        )
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)
