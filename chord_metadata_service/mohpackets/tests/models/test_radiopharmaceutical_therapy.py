from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from chord_metadata_service.mohpackets.models import (
    Program,
    RadiopharmaceuticalTherapy,
)
from chord_metadata_service.mohpackets.permissible_values import RADIONUCLIDE
from chord_metadata_service.mohpackets.tests.factories import (
    RadiopharmaceuticalTherapyFactory,
)


class RadiopharmaceuticalTherapyModelTest(TestCase):
    def setUp(self):
        self.instance = RadiopharmaceuticalTherapyFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_treatment_id, str)
        self.assertIsInstance(self.instance.rxnorm_code, (str, type(None)))
        self.assertIsInstance(self.instance.agent_name, (str, type(None)))
        self.assertIsInstance(self.instance.radionuclide, (str, type(None)))
        self.assertIsInstance(self.instance.radionuclide_other, (str, type(None)))
        self.assertIsInstance(self.instance.start_date, (dict, type(None)))
        self.assertIsInstance(self.instance.end_date, (dict, type(None)))
        self.assertIsInstance(self.instance.cumulative_drug_dose, (float, type(None)))
        self.assertIsInstance(self.instance.cumulative_drug_dose_not_available, bool)
        self.assertIsInstance(self.instance.drug_dose_units, (str, type(None)))
        self.assertIsInstance(self.instance.mass_value, (float, type(None)))
        self.assertIsInstance(self.instance.mass_value_not_available, bool)
        self.assertIsInstance(self.instance.mass_unit_ucum, (str, type(None)))
        self.assertIsInstance(self.instance.number_of_cycles, (int, type(None)))
        self.assertIsInstance(self.instance.number_of_cycles_not_available, bool)

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_value = RADIONUCLIDE[0]
        self.instance.radionuclide = update_value
        self.instance.save()
        updated_object = RadiopharmaceuticalTherapy.objects.get(uuid=self.instance.uuid)
        self.assertEqual(updated_object.radionuclide, update_value)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_treatment_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            RadiopharmaceuticalTherapy.objects.get(submitter_treatment_id=delete_id)
