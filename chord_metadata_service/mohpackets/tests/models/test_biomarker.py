from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from chord_metadata_service.mohpackets.models import Biomarker, Program
from chord_metadata_service.mohpackets.permissible_values import HER2_STATUS
from chord_metadata_service.mohpackets.tests.factories import BiomarkerFactory


class BiomarkerModelTest(TestCase):
    def setUp(self):
        self.instance = BiomarkerFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_specimen_id, (str, type(None)))
        self.assertIsInstance(
            self.instance.submitter_primary_diagnosis_id, (str, type(None))
        )
        self.assertIsInstance(self.instance.submitter_treatment_id, (str, type(None)))
        self.assertIsInstance(self.instance.submitter_follow_up_id, (str, type(None)))
        self.assertIsInstance(self.instance.test_date, (dict, type(None)))
        self.assertIsInstance(self.instance.psa_level, (int, type(None)))
        self.assertIsInstance(self.instance.ca125, (int, type(None)))
        self.assertIsInstance(self.instance.cea, (int, type(None)))
        self.assertIsInstance(self.instance.er_status, (str, type(None)))
        self.assertIsInstance(self.instance.er_percent_positive, (float, type(None)))
        self.assertIsInstance(self.instance.pr_status, (str, type(None)))
        self.assertIsInstance(self.instance.pr_percent_positive, (float, type(None)))
        self.assertIsInstance(self.instance.her2_ihc_status, (str, type(None)))
        self.assertIsInstance(self.instance.her2_ish_status, (str, type(None)))
        self.assertIsInstance(self.instance.hpv_ihc_status, (str, type(None)))
        self.assertIsInstance(self.instance.hpv_pcr_status, (str, type(None)))
        self.assertIsInstance(self.instance.hpv_strain, (list, type(None)))

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_status = HER2_STATUS[0]
        self.instance.her2_ihc_status = update_status
        self.instance.save()
        updated_object = Biomarker.objects.get(
            submitter_donor_id=self.instance.submitter_donor_id
        )
        self.assertEqual(updated_object.her2_ihc_status, update_status)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_donor_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            Biomarker.objects.get(submitter_donor_id=delete_id)
