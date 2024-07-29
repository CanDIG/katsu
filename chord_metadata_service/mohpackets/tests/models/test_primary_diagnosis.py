from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase
from pydantic import ValidationError as SchemaValidationError

from chord_metadata_service.mohpackets.models import Program, PrimaryDiagnosis
from chord_metadata_service.mohpackets.permissible_values import PRIMARY_SITE
from chord_metadata_service.mohpackets.schemas.model import PrimaryDiagnosisModelSchema
from chord_metadata_service.mohpackets.tests.factories import PrimaryDiagnosisFactory
from chord_metadata_service.mohpackets.tests.utils import INVALID_ID_LIST


class PrimaryDiagnosisModelTest(TestCase):
    def setUp(self):
        self.instance = PrimaryDiagnosisFactory()

    def test_primary_diagnosis_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_primary_diagnosis_id, str)
        self.assertIsInstance(self.instance.primary_site, (str, type(None)))
        self.assertIsInstance(self.instance.date_of_diagnosis, (dict, type(None)))
        self.assertIsInstance(self.instance.cancer_type_code, (str, type(None)))
        self.assertIsInstance(self.instance.basis_of_diagnosis, (str, type(None)))
        self.assertIsInstance(self.instance.laterality, (str, type(None)))
        self.assertIsInstance(
            self.instance.clinical_tumour_staging_system, (str, type(None))
        )
        self.assertIsInstance(self.instance.clinical_t_category, (str, type(None)))
        self.assertIsInstance(self.instance.clinical_n_category, (str, type(None)))
        self.assertIsInstance(self.instance.clinical_m_category, (str, type(None)))
        self.assertIsInstance(self.instance.clinical_stage_group, (str, type(None)))
        self.assertIsInstance(
            self.instance.pathological_tumour_staging_system, (str, type(None))
        )
        self.assertIsInstance(self.instance.pathological_t_category, (str, type(None)))
        self.assertIsInstance(self.instance.pathological_n_category, (str, type(None)))
        self.assertIsInstance(self.instance.pathological_m_category, (str, type(None)))
        self.assertIsInstance(self.instance.pathological_stage_group, (str, type(None)))

    def test_invalid_id(self):
        """
        This test iterates over a list of invalid id values,
        validating each one with the ModelSchema and expecting a
        SchemaValidationError to be raised.
        """
        for invalid_value in INVALID_ID_LIST:
            with self.subTest(value=invalid_value):
                data = {"submitter_primary_diagnosis_id": invalid_value}
                with self.assertRaises(
                    SchemaValidationError,
                    msg=f"ValidationError not raised for value: {invalid_value}",
                ):
                    PrimaryDiagnosisModelSchema.model_validate(data)

    def test_unique_together(self):
        """
        This test creates a second instance with the same ids as an existing instance,
        and expects an IntegrityError to be raised due to the unique constraint.
        """
        program_id = self.instance.program_id
        diagnosis_id = self.instance.submitter_primary_diagnosis_id
        with self.assertRaises(IntegrityError):
            PrimaryDiagnosisFactory.create(
                submitter_primary_diagnosis_id=diagnosis_id, program_id=program_id
            )

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_site = PRIMARY_SITE[0]  # Accessory sinuses
        self.instance.primary_site = update_site
        self.instance.save()
        updated_object = PrimaryDiagnosis.objects.get(
            submitter_primary_diagnosis_id=self.instance.submitter_primary_diagnosis_id
        )
        self.assertEqual(updated_object.primary_site, update_site)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_primary_diagnosis_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            PrimaryDiagnosis.objects.get(submitter_primary_diagnosis_id=delete_id)