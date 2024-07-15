
import os
import sys
import pprint
import json
import argparse
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
    SystemicTherapyFactory,
    TreatmentFactory,
)
import logging
import factory


class Dataset:
    """Create a set of programs with synthetic data"""
    @classmethod
    def __init__(cls, program_count=4, donor_count=80, pd_count=80, specimen_count=80, sample_count=240,
                 treatment_count=160, radiation_count=80, surgery_count=80, comorbidity_count=40, biomarker_count=40,
                 exposure_count=30, followup_count=2, sys_therapy_count=320):
        cls.Program = ProgramFactory.create_batch(program_count)
        logging.info("Creating Donors...")
        cls.Donor = DonorFactory.create_batch(
            donor_count, program_id=factory.Iterator(cls.Program)
        )
        logging.info("Creating Primary Diagnoses...")
        cls.PrimaryDiagnosis = PrimaryDiagnosisFactory.create_batch(
            pd_count, donor_uuid=factory.Iterator(cls.Donor)
        )
        logging.info("Creating Specimens...")
        cls.Specimen = SpecimenFactory.create_batch(
            specimen_count, primary_diagnosis_uuid=factory.Iterator(cls.PrimaryDiagnosis)
        )
        logging.info("Creating Sample registrations...")
        cls.SampleRegistration = SampleRegistrationFactory.create_batch(
            sample_count, specimen_uuid=factory.Iterator(cls.Specimen)
        )
        logging.info("Creating Treatments...")
        cls.Treatment = TreatmentFactory.create_batch(
            treatment_count, primary_diagnosis_uuid=factory.Iterator(cls.PrimaryDiagnosis)
        )
        cls.SystemicTherapy = SystemicTherapyFactory.create_batch(
            sys_therapy_count, treatment_uuid=factory.Iterator(cls.Treatment)
        )
        logging.info("Creating Radiations...")
        cls.Radiation = RadiationFactory.create_batch(
            radiation_count, treatment_uuid=factory.Iterator(cls.Treatment[0:int(treatment_count/2)])
        )
        logging.info("Creating Surgeries...")
        cls.Surgery = SurgeryFactory.create_batch(
            surgery_count, treatment_uuid=factory.Iterator(cls.Treatment[int(treatment_count/2):treatment_count])
        )
        logging.info("Creating Comorbidities...")
        cls.Comorbidity = ComorbidityFactory.create_batch(
            comorbidity_count, donor_uuid=factory.Iterator(cls.Donor)
        )
        logging.info("Creating Biomarkers...")
        cls.Biomarker = BiomarkerFactory.create_batch(
            biomarker_count, donor_uuid=factory.Iterator(cls.Donor)
        )
        logging.info("Creating Exposures...")
        cls.Exposure = ExposureFactory.create_batch(
            exposure_count, donor_uuid=factory.Iterator(cls.Donor)
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

    def __getitem__(self, item):
        return getattr(self, item)

    @staticmethod
    def clean_dict(dirty_dict):
        """Transforms the factory object into a dictionary and removes fields that cause errors during
        JSON serialisation"""
        clean_dict = model_to_dict(dirty_dict)
        if 'created' in clean_dict.keys():
            del clean_dict['created']
        if 'updated' in clean_dict.keys():
            del clean_dict['updated']
        if 'uuid' in clean_dict.keys():
            del clean_dict['uuid']
        if 'primary_diagnosis_uuid' in clean_dict.keys():
            del clean_dict['primary_diagnosis_uuid']
        if 'donor_uuid' in clean_dict.keys():
            del clean_dict['donor_uuid']
        if 'treatment_uuid' in clean_dict.keys():
            del clean_dict['treatment_uuid']
        if 'specimen_uuid' in clean_dict.keys():
            del clean_dict['specimen_uuid']
        return clean_dict

    def convert_to_dicts(self):
        """Convert all factory objects to dictionaries that can be output as JSON files"""
        self.Program = [self.clean_dict(x) for x in self.Program]
        self.Biomarker = [self.clean_dict(x) for x in self.Biomarker]
        self.Comorbidity = [self.clean_dict(x) for x in self.Comorbidity]
        self.Donor = [self.clean_dict(x) for x in self.Donor]
        self.Exposure = [self.clean_dict(x) for x in self.Exposure]
        self.PrimaryDiagnosis = [self.clean_dict(x) for x in self.PrimaryDiagnosis]
        self.Specimen = [self.clean_dict(x) for x in self.Specimen]
        self.SampleRegistration = [self.clean_dict(x) for x in self.SampleRegistration]
        self.Treatment = [self.clean_dict(x) for x in self.Treatment]
        self.SystemicTherapy = [self.clean_dict(x) for x in self.SystemicTherapy]
        self.Radiation = [self.clean_dict(x) for x in self.Radiation]
        self.Surgery = [self.clean_dict(x) for x in self.Surgery]
        # self.followups = [self.clean_dict(x) for x in self.followups]

    def setUp(self):
        logging.disable(logging.WARNING)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--size',
        type=str,
        choices=['s', 'm', 'l'],
        help="Size of the dataset to convert, options: 's' for small, 'm' for medium, 'l' for large (default: small)"
    )
    parser.add_argument(
        '-p', '--num-programs',
        type=int,
        help="Number of programs to generate (if not using size option)"
    )
    parser.add_argument(
        '-d', '--donors-per-program',
        type=int,
        default=50,
        help="Number of donors to generate per program"
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if args.num_programs:
        donor_count = args.num_programs * args.donors_per_program
        params = {"program_count": args.num_programs, "donor_count": donor_count,
                  "pd_count": donor_count, "specimen_count": donor_count,
                  "sample_count": 3*donor_count, "treatment_count": donor_count*2, "radiation_count": donor_count,
                  "surgery_count": donor_count, "comorbidity_count": int(donor_count/2),
                  "biomarker_count": int(donor_count/2), "exposure_count": int(donor_count/4),
                  "followup_count": int(donor_count/4), "sys_therapy_count": donor_count*4}
        programs = Dataset(**params)
        path = f"custom_{args.num_programs}P_{args.donors_per_program}D_dataset"
    else:
        size_mapping = {
            "s": {"size": "small",
                  "params": {"program_count": 4, "donor_count": 80, "pd_count": 80, "specimen_count": 80,
                             "sample_count": 240, "treatment_count": 160, "radiation_count": 80, "surgery_count": 80,
                             "comorbidity_count": 40, "biomarker_count": 40, "exposure_count": 30, "followup_count": 20,
                             "sys_therapy_count": 320}
                  },
            "m": {"size": "medium",
                  "params": {"program_count": 4, "donor_count": 800, "pd_count": 800, "specimen_count": 800,
                             "sample_count": 2400, "treatment_count": 1600, "radiation_count": 800,
                             "surgery_count": 800, "comorbidity_count": 400, "biomarker_count": 400,
                             "exposure_count": 300, "followup_count": 200, "sys_therapy_count": 3200}
                  },
            "l": {"size": "large",
                  "params": {"program_count": 4, "donor_count": 2000, "pd_count": 2000, "specimen_count": 2000,
                             "sample_count": 6000, "treatment_count": 4000, "radiation_count": 2000,
                             "surgery_count": 2000, "comorbidity_count": 1000, "biomarker_count": 1000,
                             "exposure_count": 300, "followup_count": 500, "sys_therapy_count": 8000}
                  }
        }
        if not args.size:
            args.size = "s"
        path = f"{size_mapping[args.size]["size"]}_dataset"
        programs = Dataset(**size_mapping[args.size]['params'])
    programs.convert_to_dicts()
    for schema, data in programs.__dict__.items():
        logging.info(f"Saving {schema} objects to file...")
        with open(f"{path}/v3_synthetic_data/{schema}.json", "w+") as f:
            json.dump(data, f)


if __name__ == "__main__":
    main()
