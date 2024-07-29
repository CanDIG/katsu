from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from chord_metadata_service.mohpackets.models import Exposure, Program
from chord_metadata_service.mohpackets.permissible_values import SMOKING_STATUS
from chord_metadata_service.mohpackets.tests.factories import ExposureFactory


class ExposureModelTest(TestCase):
    def setUp(self):
        self.instance = ExposureFactory()

    def test_fields(self):
        """
        This test ensures each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.tobacco_smoking_status, (str, type(None)))
        self.assertIsInstance(self.instance.tobacco_type, (list, type(None)))
        self.assertIsInstance(self.instance.pack_years_smoked, (float, type(None)))

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_status = SMOKING_STATUS[0]
        self.instance.tobacco_smoking_status = update_status
        self.instance.save()
        updated_object = Exposure.objects.get(
            submitter_donor_id=self.instance.submitter_donor_id
        )
        self.assertEqual(updated_object.tobacco_smoking_status, update_status)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_donor_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            Exposure.objects.get(submitter_donor_id=delete_id)