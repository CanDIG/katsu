
import os
import sys
import pprint
# Add your Django project's root directory to the Python path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
)  # This assumes your script is in the data directory
# Set the DJANGO_SETTINGS_MODULE to your project's settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
os.environ.setdefault("INSTALLED_APPS", "config.settings.local")
# Initialize Django
import django
django.setup()
from django.forms.models import model_to_dict

from chord_metadata_service.mohpackets.tests.endpoints.factories import (
    BiomarkerFactory,
    # ChemotherapyFactory,
    ComorbidityFactory,
    DonorFactory,
    ExposureFactory,
    FollowUpFactory,
    PrimaryDiagnosisFactory,
    ProgramFactory,
    RadiationFactory,
    SampleRegistrationFactory,
    SpecimenFactory,
    SurgeryFactory,
    # SystemicTherapyFactory,
    TreatmentFactory,
)
import logging
import factory


class Dataset:
    @classmethod
    def __init__(cls, program_count=4, donor_count=80, pd_count=80, specimen_count=80, sample_count=240,
                 treatment_count=160, radiation_count=80, surgery_count=80, comorbidity_count=40, biomarker_count=40,
                 exposure_count=60, followup_count=2, sys_therapy_count=320):
        cls.programs = ProgramFactory.create_batch(program_count)
        cls.donors = DonorFactory.create_batch(
            donor_count, program_id=factory.Iterator(cls.programs)
        )
        cls.primary_diagnoses = PrimaryDiagnosisFactory.create_batch(
            pd_count, donor_uuid=factory.Iterator(cls.donors)
        )
        cls.specimens = SpecimenFactory.create_batch(
            specimen_count, primary_diagnosis_uuid=factory.Iterator(cls.primary_diagnoses)
        )
        cls.sample_registrations = SampleRegistrationFactory.create_batch(
            sample_count, specimen_uuid=factory.Iterator(cls.specimens)
        )
        cls.treatments = TreatmentFactory.create_batch(
            treatment_count, primary_diagnosis_uuid=factory.Iterator(cls.primary_diagnoses)
        )
        # cls.systemic_therapies = SystemicTherapyFactory.create_batch(
        #     sys_therapy_count, treatment_uuid=factory.Iterator(cls.treatments)
        # )
        cls.radiations = RadiationFactory.create_batch(
            radiation_count, treatment_uuid=factory.Iterator(cls.treatments[0:int(treatment_count/2)])
        )
        cls.surgeries = SurgeryFactory.create_batch(
            surgery_count, treatment_uuid=factory.Iterator(cls.treatments[int(treatment_count/2):treatment_count])
        )
        cls.comorbidities = ComorbidityFactory.create_batch(
            comorbidity_count, donor_uuid=factory.Iterator(cls.donors)
        )
        cls.biomarkers = BiomarkerFactory.create_batch(
            biomarker_count, donor_uuid=factory.Iterator(cls.donors)
        )
        cls.exposures = ExposureFactory.create_batch(
            exposure_count, donor_uuid=factory.Iterator(cls.donors)
        )
        # cls.followups = FollowUpFactory.create_batch(
        #     followup_count,
        #
        #     primary_diagnosis_uuid=factory.Faker("random_element", [None, cls.primary_diagnoses]),
        #     treatment_uuid=factory.Maybe(decider="primary_diagnosis_uuid",
        #                                  yes_declaration=None,
        #                                  no_declaration=factory.Faker("random_element",
        #                                                               [None, cls.primary_diagnoses]))
        # )

    def convert_to_dicts(self):
        self.programs = [model_to_dict(x) for x in self.programs]
        self.biomarkers = [model_to_dict(x) for x in self.biomarkers]
        self.comorbidities = [model_to_dict(x) for x in self.comorbidities]
        self.donors = [model_to_dict(x) for x in self.donors]
        self.exposures = [model_to_dict(x) for x in self.exposures]
        self.primary_diagnoses = [model_to_dict(x) for x in self.primary_diagnoses]
        self.specimens = [model_to_dict(x) for x in self.specimens]
        self.sample_registrations = [model_to_dict(x) for x in self.sample_registrations]
        self.treatments = [model_to_dict(x) for x in self.treatments]
        # self.systemic_therapies = [model_to_dict(x) for x in self.systemic_therapies]
        self.radiations = [model_to_dict(x) for x in self.radiations]
        self.surgeries = [model_to_dict(x) for x in self.surgeries]
        # self.followups = [model_to_dict(x) for x in self.followups]

    def setUp(self):
        logging.disable(logging.WARNING)


def main():
    programs = Dataset()
    programs.convert_to_dicts()
    pprint.pprint(programs.__dict__)


if __name__ == "__main__":
    main()
