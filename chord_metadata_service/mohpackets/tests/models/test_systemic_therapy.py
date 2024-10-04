from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from chord_metadata_service.mohpackets.models import Program, SystemicTherapy
from chord_metadata_service.mohpackets.permissible_values import SYSTEMIC_THERAPY_TYPE
from chord_metadata_service.mohpackets.tests.factories import SystemicTherapyFactory


class DonorModelTest(TestCase):
    def setUp(self):
        self.instance = SystemicTherapyFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_treatment_id, str)
        self.assertIsInstance(self.instance.systemic_therapy_type, (str, type(None)))
        self.assertIsInstance(self.instance.days_per_cycle, (int, type(None)))
        self.assertIsInstance(self.instance.number_of_cycles, (int, type(None)))
        self.assertIsInstance(self.instance.start_date, (dict, type(None)))
        self.assertIsInstance(self.instance.end_date, (dict, type(None)))
        self.assertIsInstance(self.instance.drug_reference_database, (str, type(None)))
        self.assertIsInstance(self.instance.drug_name, (str, type(None)))
        self.assertIsInstance(
            self.instance.drug_reference_identifier, (str, type(None))
        )
        self.assertIsInstance(self.instance.drug_dose_units, (str, type(None)))
        self.assertIsInstance(
            self.instance.prescribed_cumulative_drug_dose, (float, type(None))
        )
        self.assertIsInstance(
            self.instance.actual_cumulative_drug_dose, (float, type(None))
        )

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_therapy_type = SYSTEMIC_THERAPY_TYPE[0]  # Chemotherapy
        self.instance.systemic_therapy_type = update_therapy_type
        self.instance.save()
        updated_object = SystemicTherapy.objects.get(uuid=self.instance.uuid)
        self.assertEqual(updated_object.systemic_therapy_type, update_therapy_type)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_treatment_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            SystemicTherapy.objects.get(submitter_treatment_id=delete_id)
