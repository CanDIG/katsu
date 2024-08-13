from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase
from pydantic import ValidationError as SchemaValidationError

from chord_metadata_service.mohpackets.models import Program, SampleRegistration
from chord_metadata_service.mohpackets.permissible_values import SAMPLE_TYPE
from chord_metadata_service.mohpackets.schemas.model import (
    SampleRegistrationModelSchema,
)
from chord_metadata_service.mohpackets.tests.factories import SampleRegistrationFactory
from chord_metadata_service.mohpackets.tests.utils import INVALID_ID_LIST


class SampleRegistrationModelTest(TestCase):
    def setUp(self):
        self.instance = SampleRegistrationFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_specimen_id, str)
        self.assertIsInstance(self.instance.submitter_sample_id, str)
        self.assertIsInstance(self.instance.specimen_tissue_source, (str, type(None)))
        self.assertIsInstance(
            self.instance.tumour_normal_designation, (str, type(None))
        )
        self.assertIsInstance(self.instance.specimen_type, (str, type(None)))
        self.assertIsInstance(self.instance.sample_type, (str, type(None)))

    def test_invalid_id(self):
        """
            This test iterates over a list of invalid id values,
            validating each one with the ModelSchema and expecting a
        SchemaValidationError to be raised.
        """

        for invalid_value in INVALID_ID_LIST:
            with self.subTest(value=invalid_value):
                data = {"submitter_sample_id": invalid_value}
                with self.assertRaises(
                    SchemaValidationError,
                    msg=f"ValidationError not raised for value: {invalid_value}",
                ):
                    SampleRegistrationModelSchema.model_validate(data)

    def test_unique_together(self):
        """
        This test creates a second instance with the same ids as an existing instance,
        and expects an IntegrityError to be raised due to the unique constraint.
        """
        program_id = self.instance.program_id
        sample_id = self.instance.submitter_sample_id
        with self.assertRaises(IntegrityError):
            SampleRegistrationFactory.create(
                submitter_sample_id=sample_id, program_id=program_id
            )

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_source = SAMPLE_TYPE[0]  # Amplified DNA
        self.instance.specimen_tissue_source = update_source
        self.instance.save()
        updated_object = SampleRegistration.objects.get(
            submitter_sample_id=self.instance.submitter_sample_id
        )
        self.assertEqual(updated_object.specimen_tissue_source, update_source)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_sample_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            SampleRegistration.objects.get(submitter_sample_id=delete_id)
