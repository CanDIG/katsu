from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase
from pydantic import ValidationError as SchemaValidationError

from chord_metadata_service.mohpackets.models import Treatment, Program
from chord_metadata_service.mohpackets.permissible_values import TREATMENT_INTENT
from chord_metadata_service.mohpackets.schemas.model import TreatmentModelSchema
from chord_metadata_service.mohpackets.tests.factories import TreatmentFactory
from chord_metadata_service.mohpackets.tests.utils import INVALID_ID_LIST


class DonorModelTest(TestCase):
    def setUp(self):
        self.instance = TreatmentFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_primary_diagnosis_id, str)
        self.assertIsInstance(self.instance.submitter_treatment_id, str)
        self.assertIsInstance(self.instance.treatment_type, (list, type(None)))
        self.assertIsInstance(self.instance.is_primary_treatment, (str, type(None)))
        self.assertIsInstance(self.instance.treatment_start_date, (dict, type(None)))
        self.assertIsInstance(self.instance.treatment_end_date, (dict, type(None)))
        self.assertIsInstance(self.instance.treatment_intent, (str, type(None)))
        self.assertIsInstance(
            self.instance.response_to_treatment_criteria_method, (str, type(None))
        )
        self.assertIsInstance(self.instance.response_to_treatment, (str, type(None)))
        self.assertIsInstance(self.instance.status_of_treatment, (str, type(None)))

    def test_invalid_id(self):
        """
        This test iterates over a list of invalid id values,
        validating each one with the ModelSchema and expecting a
        SchemaValidationError to be raised.
        """
        for invalid_value in INVALID_ID_LIST:
            with self.subTest(value=invalid_value):
                data = {"submitter_treatment_id": invalid_value}
                with self.assertRaises(
                    SchemaValidationError,
                    msg=f"ValidationError not raised for value: {invalid_value}",
                ):
                    TreatmentModelSchema.model_validate(data)

    def test_unique_together(self):
        """
        This test creates a second instance with the same ids as an existing instance,
        and expects an IntegrityError to be raised due to the unique constraint.
        """
        program_id = self.instance.program_id
        treatment_id = self.instance.submitter_treatment_id
        with self.assertRaises(IntegrityError):
            TreatmentFactory.create(
                submitter_treatment_id=treatment_id, program_id=program_id
            )

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_intent = TREATMENT_INTENT[0]  # Curative
        self.instance.treatment_intent = update_intent
        self.instance.save()
        updated_object = Treatment.objects.get(
            submitter_treatment_id=self.instance.submitter_treatment_id
        )
        self.assertEqual(updated_object.treatment_intent, update_intent)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_treatment_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            Treatment.objects.get(submitter_treatment_id=delete_id)
