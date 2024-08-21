from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from chord_metadata_service.mohpackets.models import Radiation, Program
from chord_metadata_service.mohpackets.permissible_values import (
    RADIATION_THERAPY_MODALITY,
)
from chord_metadata_service.mohpackets.tests.factories import RadiationFactory


class RadiationModelTest(TestCase):
    def setUp(self):
        self.instance = RadiationFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_treatment_id, str)
        self.assertIsInstance(
            self.instance.radiation_therapy_modality, (str, type(None))
        )
        self.assertIsInstance(self.instance.radiation_therapy_type, (str, type(None)))
        self.assertIsInstance(
            self.instance.radiation_therapy_fractions, (int, type(None))
        )
        self.assertIsInstance(self.instance.radiation_therapy_dosage, (int, type(None)))
        self.assertIsInstance(
            self.instance.anatomical_site_irradiated, (str, type(None))
        )
        self.assertIsInstance(self.instance.radiation_boost, (bool, type(None)))
        self.assertIsInstance(
            self.instance.reference_radiation_treatment_id, (str, type(None))
        )

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_modality = RADIATION_THERAPY_MODALITY[0]
        self.instance.radiation_therapy_modality = update_modality
        self.instance.save()
        updated_object = Radiation.objects.get(uuid=self.instance.uuid)
        self.assertEqual(updated_object.radiation_therapy_modality, update_modality)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_treatment_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            Radiation.objects.get(submitter_treatment_id=delete_id)
