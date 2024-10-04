from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase
from pydantic import ValidationError as SchemaValidationError

from chord_metadata_service.mohpackets.models import Program, Specimen
from chord_metadata_service.mohpackets.permissible_values import STORAGE
from chord_metadata_service.mohpackets.schemas.model import SpecimenModelSchema
from chord_metadata_service.mohpackets.tests.factories import SpecimenFactory
from chord_metadata_service.mohpackets.tests.utils import INVALID_ID_LIST


class SpecimenModelTest(TestCase):
    def setUp(self):
        self.instance = SpecimenFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_primary_diagnosis_id, str)
        self.assertIsInstance(self.instance.submitter_specimen_id, str)
        self.assertIsInstance(self.instance.submitter_treatment_id, (str, type(None)))
        self.assertIsInstance(
            self.instance.specimen_collection_date, (dict, type(None))
        )
        self.assertIsInstance(self.instance.specimen_storage, (str, type(None)))
        self.assertIsInstance(self.instance.specimen_processing, (str, type(None)))
        self.assertIsInstance(self.instance.tumour_histological_type, (str, type(None)))
        self.assertIsInstance(
            self.instance.specimen_anatomic_location, (str, type(None))
        )
        self.assertIsInstance(self.instance.specimen_laterality, (str, type(None)))
        self.assertIsInstance(
            self.instance.reference_pathology_confirmed_diagnosis, (str, type(None))
        )
        self.assertIsInstance(
            self.instance.reference_pathology_confirmed_tumour_presence,
            (str, type(None)),
        )
        self.assertIsInstance(self.instance.tumour_grading_system, (str, type(None)))
        self.assertIsInstance(self.instance.tumour_grade, (str, type(None)))
        self.assertIsInstance(
            self.instance.percent_tumour_cells_range, (str, type(None))
        )
        self.assertIsInstance(
            self.instance.percent_tumour_cells_measurement_method, (str, type(None))
        )

    def test_invalid_id(self):
        """
        This test iterates over a list of invalid id values,
        validating each one with the ModelSchema and expecting a
        SchemaValidationError to be raised.
        """
        for invalid_value in INVALID_ID_LIST:
            with self.subTest(value=invalid_value):
                data = {"submitter_specimen_id": invalid_value}
                with self.assertRaises(
                    SchemaValidationError,
                    msg=f"ValidationError not raised for value: {invalid_value}",
                ):
                    SpecimenModelSchema.model_validate(data)

    def test_unique_together(self):
        """
        This test creates a second instance with the same ids as an existing instance,
        and expects an IntegrityError to be raised due to the unique constraint.
        """
        program_id = self.instance.program_id
        specimen_id = self.instance.submitter_specimen_id
        with self.assertRaises(IntegrityError):
            SpecimenFactory.create(
                submitter_specimen_id=specimen_id, program_id=program_id
            )

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_storage = STORAGE[0]  # "Cut slide"
        self.instance.specimen_storage = update_storage
        self.instance.save()
        updated_object = Specimen.objects.get(
            submitter_specimen_id=self.instance.submitter_specimen_id
        )
        self.assertEqual(updated_object.specimen_storage, update_storage)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_specimen_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            Specimen.objects.get(submitter_specimen_id=delete_id)
