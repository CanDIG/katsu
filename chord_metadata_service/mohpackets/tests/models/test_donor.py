from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase
from pydantic import ValidationError as SchemaValidationError

from chord_metadata_service.mohpackets.models import Donor, Program
from chord_metadata_service.mohpackets.permissible_values import LOST_TO_FOLLOWUP_REASON
from chord_metadata_service.mohpackets.schemas.model import DonorModelSchema
from chord_metadata_service.mohpackets.tests.factories import DonorFactory
from chord_metadata_service.mohpackets.tests.utils import INVALID_ID_LIST


class DonorModelTest(TestCase):
    def setUp(self):
        self.instance = DonorFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model v3 specifications.
        """
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.gender, (str, type(None)))
        self.assertIsInstance(self.instance.sex_at_birth, (str, type(None)))
        self.assertIsInstance(self.instance.is_deceased, (bool, type(None)))
        self.assertIsInstance(
            self.instance.lost_to_followup_after_clinical_event_identifier,
            (str, type(None)),
        )
        self.assertIsInstance(self.instance.lost_to_followup_reason, (str, type(None)))
        self.assertIsInstance(
            self.instance.date_alive_after_lost_to_followup, (dict, type(None))
        )
        self.assertIsInstance(self.instance.cause_of_death, (str, type(None)))
        self.assertIsInstance(self.instance.date_of_birth, (dict, type(None)))
        self.assertIsInstance(self.instance.date_of_death, (dict, type(None)))
        self.assertIsInstance(self.instance.date_resolution, (str, type(None)))

    def test_invalid_id(self):
        """
        This test iterates over a list of invalid id values,
        validating each one with the ModelSchema and expecting a
        SchemaValidationError to be raised.
        """
        for invalid_value in INVALID_ID_LIST:
            with self.subTest(value=invalid_value):
                data = {"submitter_donor_id": invalid_value}
                with self.assertRaises(
                    SchemaValidationError,
                    msg=f"ValidationError not raised for value: {invalid_value}",
                ):
                    DonorModelSchema.model_validate(data)

    def test_unique_together(self):
        """
        This test creates a second instance with the same ids as an existing instance,
        and expects an IntegrityError to be raised due to the unique constraint.
        """
        program_id = self.instance.program_id
        donor_id = self.instance.submitter_donor_id
        with self.assertRaises(IntegrityError):
            DonorFactory.create(submitter_donor_id=donor_id, program_id=program_id)

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_reason = LOST_TO_FOLLOWUP_REASON[0]  # Completed study
        self.instance.lost_to_followup_reason = update_reason
        self.instance.save()
        updated_object = Donor.objects.get(
            submitter_donor_id=self.instance.submitter_donor_id
        )
        self.assertEqual(updated_object.lost_to_followup_reason, update_reason)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_donor_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            Donor.objects.get(submitter_donor_id=delete_id)