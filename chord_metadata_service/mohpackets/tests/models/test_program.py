import datetime
from django.db.utils import IntegrityError
from django.test import TestCase
from pydantic import ValidationError as SchemaValidationError

from chord_metadata_service.mohpackets.models import (
    Program,
)
from chord_metadata_service.mohpackets.schemas.model import ProgramModelSchema

from chord_metadata_service.mohpackets.tests.factories import ProgramFactory
from chord_metadata_service.mohpackets.tests.utils import INVALID_ID_LIST


class ProgramModelTest(TestCase):
    def setUp(self):
        self.instance = ProgramFactory()

    def test_fields(self):
        """
        This test makes sure each field is present and has the correct data type
        according to the model v3 specifications.
        """
        self.assertIsInstance(self.instance.program_id, str)
        self.assertIsInstance(self.instance.metadata, (dict, type(None)))
        self.assertIsInstance(self.instance.created, datetime.datetime)
        self.assertIsInstance(self.instance.updated, datetime.datetime)

    def test_unique_id(self):
        """Check creating a program with a duplicate ID raises an error."""
        with self.assertRaises(IntegrityError):
            Program.objects.create(program_id=self.instance.program_id)

    def test_invalid_id(self):
        """Test that invalid program IDs raise a SchemaValidationError."""
        for invalid_value in INVALID_ID_LIST:
            with self.subTest(value=invalid_value):
                program_data = {"program_id": invalid_value}
                with self.assertRaises(
                    SchemaValidationError,
                    msg=f"ValidationError not raised for value: {invalid_value}",
                ):
                    ProgramModelSchema.model_validate(program_data)

    def test_program_update(self):
        """Check that a program's ID can be updated successfully."""
        new_program_id = "UPDATED_TEST"
        self.instance.program_id = new_program_id
        self.instance.save()
        updated_program = Program.objects.get(program_id=self.instance.program_id)
        self.assertEqual(updated_program.program_id, new_program_id)

    def test_program_delete(self):
        """Check that a deleted program cannot be retrieved."""
        program_id = self.instance.program_id
        self.instance.delete()
        with self.assertRaises(Program.DoesNotExist):
            Program.objects.get(program_id=program_id)
