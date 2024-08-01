from django.core.exceptions import ObjectDoesNotExist

from django.test import TestCase

from chord_metadata_service.mohpackets.models import Surgery, Program
from chord_metadata_service.mohpackets.permissible_values import SURGERY_TYPE
from chord_metadata_service.mohpackets.tests.factories import SurgeryFactory


class DonorModelTest(TestCase):
    def setUp(self):
        self.instance = SurgeryFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model specifications.
        """
        self.assertIsInstance(self.instance.program_id, Program)
        self.assertIsInstance(self.instance.submitter_donor_id, str)
        self.assertIsInstance(self.instance.submitter_treatment_id, str)
        self.assertIsInstance(self.instance.surgery_type, (str, type(None)))
        self.assertIsInstance(self.instance.surgery_site, (str, type(None)))
        self.assertIsInstance(self.instance.surgery_location, (str, type(None)))
        self.assertIsInstance(self.instance.tumour_length, (int, type(None)))
        self.assertIsInstance(self.instance.tumour_width, (int, type(None)))
        self.assertIsInstance(
            self.instance.greatest_dimension_tumour, (int, type(None))
        )
        self.assertIsInstance(self.instance.tumour_focality, (str, type(None)))
        self.assertIsInstance(
            self.instance.residual_tumour_classification, (str, type(None))
        )
        self.assertIsInstance(self.instance.margin_types_involved, (list, type(None)))
        self.assertIsInstance(
            self.instance.margin_types_not_involved, (list, type(None))
        )
        self.assertIsInstance(
            self.instance.margin_types_not_assessed, (list, type(None))
        )
        self.assertIsInstance(self.instance.lymphovascular_invasion, (str, type(None)))
        self.assertIsInstance(self.instance.perineural_invasion, (str, type(None)))
        self.assertIsInstance(
            self.instance.surgery_reference_database, (str, type(None))
        )
        self.assertIsInstance(
            self.instance.surgery_reference_identifier, (str, type(None))
        )

    def test_update(self):
        """
        This test changes a field value, saves it, and then retrieves it from
        the database to verify the update.
        """
        update_surgery_type = SURGERY_TYPE[0]
        self.instance.surgery_type = update_surgery_type
        self.instance.save()
        updated_object = Surgery.objects.get(uuid=self.instance.uuid)
        self.assertEqual(updated_object.surgery_type, update_surgery_type)

    def test_delete(self):
        """
        This test deletes the object and then attempts to retrieve it,
        expecting an ObjectDoesNotExist exception to be raised.
        """
        delete_id = self.instance.submitter_treatment_id
        self.instance.delete()
        with self.assertRaises(ObjectDoesNotExist):
            Surgery.objects.get(submitter_treatment_id=delete_id)