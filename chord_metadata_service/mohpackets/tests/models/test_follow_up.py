from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase
from pydantic import ValidationError as SchemaValidationError

from chord_metadata_service.mohpackets.models import FollowUp, Program
from chord_metadata_service.mohpackets.permissible_values import DISEASE_STATUS_FOLLOWUP
from chord_metadata_service.mohpackets.schemas.model import FollowUpModelSchema
from chord_metadata_service.mohpackets.tests.factories import FollowUpFactory
from chord_metadata_service.mohpackets.tests.utils import INVALID_ID_LIST


class FollowUpModelTest(TestCase):
    def setUp(self):
        self.instance = FollowUpFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_follow_up_id, str)
        self.assertIsInstance(
            self.instance.submitter_primary_diagnosis_id, (str, type(None))
        )
        self.assertIsInstance(self.instance.submitter_treatment_id, (str, type(None)))
        self.assertIsInstance(self.instance.date_of_followup, (dict, type(None)))
        self.assertIsInstance(
            self.instance.disease_status_at_followup, (str, type(None))
        )
        self.assertIsInstance(self.instance.relapse_type, (str, type(None)))
        self.assertIsInstance(self.instance.date_of_relapse, (dict, type(None)))
        self.assertIsInstance(
            self.instance.method_of_progression_status, (list, type(None))
        )
        self.assertIsInstance(
            self.instance.anatomic_site_progression_or_recurrence, (list, type(None))
        )

    def test_invalid_id(self):
        """
        This test iterates over a list of invalid id values,
        validating each one with the ModelSchema and expecting a
        SchemaValidationError to be raised.
        """
        for invalid_value in INVALID_ID_LIST:
            with self.subTest(value=invalid_value):
                data = {"submitter_follow_up_id": invalid_value}
                with self.assertRaises(
                    SchemaValidationError,
                    msg=f"ValidationError not raised for value: {invalid_value}",
                ):
                    FollowUpModelSchema.model_validate(data)

    def test_unique_together(self):
        """
        This test creates a second instance with the same ids as an existing instance,
        and expects an IntegrityError to be raised due to the unique constraint.
        """
        program_id = self.instance.program_id
        follow_up_id = self.instance.submitter_follow_up_id
        with self.assertRaises(IntegrityError):
            FollowUpFactory.create(
                submitter_follow_up_id=follow_up_id, program_id=program_id
            )

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_status = DISEASE_STATUS_FOLLOWUP[0]
        self.instance.disease_status_at_followup = update_status
        self.instance.save()
        updated_object = FollowUp.objects.get(
            submitter_follow_up_id=self.instance.submitter_follow_up_id
        )
        self.assertEqual(updated_object.disease_status_at_followup, update_status)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_follow_up_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            FollowUp.objects.get(submitter_follow_up_id=delete_id)