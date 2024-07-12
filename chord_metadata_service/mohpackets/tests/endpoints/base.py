import logging
import os

import factory
from django.conf import settings
from django.test import Client, TestCase

from chord_metadata_service.mohpackets.tests.endpoints.factories import (
    ChemotherapyFactory,
    DonorFactory,
    ImmunotherapyFactory,
    PrimaryDiagnosisFactory,
    ProgramFactory,
    SampleRegistrationFactory,
    SpecimenFactory,
    TreatmentFactory,
)

"""
    This file contains the base test case class for testing endpoints.

    It sets up initial test data, including programs, donors with other models,
    and defines test users with different permission levels and dataset access.
    By utilizing this, there is no need to create the same test data
    for every individual test method, thereby speeding up the tests and promoting
    consistency.

    Example:
        To use this base test case, inherit from it in your test classes and use
        the provided attributes for testing API endpoints and permissions.

        class MyAPITestCase(BaseTestCase):
            def test_my_endpoint(self):
                # Write your test logic here using the initialized data and test users.

    Author: Son Chau
"""


class TestUser:
    def __init__(self, token, is_admin, write_datasets, read_datasets):
        self.token = token
        self.is_admin = is_admin
        self.write_datasets = write_datasets
        self.read_datasets = read_datasets


class BaseTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.programs = ProgramFactory.create_batch(
            2,
        )
        cls.donors = DonorFactory.create_batch(
            4, program_id=factory.Iterator(cls.programs)
        )
        cls.primary_diagnoses = PrimaryDiagnosisFactory.create_batch(
            8, donor_uuid=factory.Iterator(cls.donors)
        )
        cls.specimens = SpecimenFactory.create_batch(
            16, primary_diagnosis_uuid=factory.Iterator(cls.primary_diagnoses)
        )
        cls.sample_registrations = SampleRegistrationFactory.create_batch(
            32, specimen_uuid=factory.Iterator(cls.specimens)
        )
        cls.treatments = TreatmentFactory.create_batch(
            16, primary_diagnosis_uuid=factory.Iterator(cls.primary_diagnoses)
        )
        cls.chemotherapies = ChemotherapyFactory.create_batch(
            4, treatment_uuid=factory.Iterator(cls.treatments[0:4])
        )
        cls.immunotherapies = ImmunotherapyFactory.create_batch(
            4, treatment_uuid=factory.Iterator(cls.treatments[4:8])
        )

        # Define users permissions based on test data
        # The only different between a normal user and a curator is write permission
        cls.user_0 = TestUser(
            token="user_0",
            is_admin=False,
            write_datasets=[],
            read_datasets=[cls.programs[0].program_id],
        )
        cls.user_1 = TestUser(
            token="user_1",
            is_admin=False,
            write_datasets=[cls.programs[1].program_id],
            read_datasets=[
                cls.programs[0].program_id,
                cls.programs[1].program_id,
            ],
        )
        cls.user_2 = TestUser(
            token="site_admin",
            is_admin=True,
            write_datasets=[
                cls.programs[0].program_id,
                cls.programs[1].program_id,
                "admin_authorized_program_id",
            ],
            read_datasets=[
                cls.programs[0].program_id,
                cls.programs[1].program_id,
            ],
        )

        # remember to add all the custom users into this list
        cls.users = [cls.user_0, cls.user_1, cls.user_2]
        os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"

        # Overrides local settings to allow new testing data
        settings.LOCAL_OPA_DATASET = {
            cls.user_0.token: {
                "is_admin": cls.user_0.is_admin,
                "write_datasets": cls.user_0.write_datasets,
                "read_datasets": cls.user_0.read_datasets,
            },
            cls.user_1.token: {
                "is_admin": cls.user_1.is_admin,
                "write_datasets": cls.user_1.write_datasets,
                "read_datasets": cls.user_1.read_datasets,
            },
            cls.user_2.token: {
                "is_admin": cls.user_2.is_admin,
                "write_datasets": cls.user_2.write_datasets,
                "read_datasets": cls.user_2.read_datasets,
            },
        }

    def setUp(self):
        logging.disable(logging.WARNING)
        self.client = Client()
