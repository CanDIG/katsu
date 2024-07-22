import os
import sys
import json
import argparse
import pathlib

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
import logging
import factory
import factory.random

from chord_metadata_service.mohpackets.tests.endpoints.factories import (
    BiomarkerFactory,
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

from synth_data_factories import (
    SynthDonorFactory,
    SynthPrimaryDiagnosisFactory
)


class Dataset:
    """Create a set of programs with synthetic data"""

    @classmethod
    def __init__(cls, program_count=4, donor_count=80, pd_count=80, specimen_count=80, sample_count=240,
                 treatment_count=160, radiation_count=80, surgery_count=80, comorbidity_count=40, biomarker_count=40,
                 exposure_count=30, followup_count=20, sys_therapy_count=320):
        logging.info("Creating Programs...")
        ProgramFactory.reset_sequence(1)
        cls.Program = ProgramFactory.create_batch(program_count)
        logging.info("Creating Donors...")
        DonorFactory.reset_sequence(1)
        cls.Donor = DonorFactory.create_batch(
            donor_count, program_id=factory.Iterator(cls.Program)
        )
        cls.SynthDonor = SynthDonorFactory.create_batch(
            donor_count, program_id=factory.Iterator(cls.Program)
        )
        logging.info("Creating Primary Diagnoses...")
        PrimaryDiagnosisFactory.reset_sequence(1)
        cls.PrimaryDiagnosis = PrimaryDiagnosisFactory.create_batch(
            pd_count, donor_uuid=factory.Iterator(cls.Donor)
        )
        cls.SynthPrimaryDiagnosis = SynthPrimaryDiagnosisFactory.create_batch(
            pd_count, donor_uuid=factory.Iterator(cls.Donor)
        )
        logging.info("Creating Specimens...")
        SpecimenFactory.reset_sequence(1)
        cls.Specimen = SpecimenFactory.create_batch(
            specimen_count, primary_diagnosis_uuid=factory.Iterator(cls.PrimaryDiagnosis)
        )
        logging.info("Creating Sample registrations...")
        SampleRegistrationFactory.reset_sequence(1)
        cls.SampleRegistration = SampleRegistrationFactory.create_batch(
            sample_count, specimen_uuid=factory.Iterator(cls.Specimen)
        )
        logging.info("Creating Treatments...")
        TreatmentFactory.reset_sequence(1)
        cls.Treatment = TreatmentFactory.create_batch(
            treatment_count, primary_diagnosis_uuid=factory.Iterator(cls.PrimaryDiagnosis)
        )
        logging.info("Creating Systemic therapies...")
        cls.SystemicTherapy = SystemicTherapyFactory.create_batch(
            sys_therapy_count, treatment_uuid=factory.Iterator(cls.Treatment)
        )
        logging.info("Creating Radiations...")
        cls.Radiation = RadiationFactory.create_batch(
            radiation_count, treatment_uuid=factory.Iterator(cls.Treatment[0:int(treatment_count / 2)])
        )
        logging.info("Creating Surgeries...")
        cls.Surgery = SurgeryFactory.create_batch(
            surgery_count, treatment_uuid=factory.Iterator(cls.Treatment[int(treatment_count / 2):treatment_count])
        )
        logging.info("Creating Comorbidities...")
        cls.Comorbidity = ComorbidityFactory.create_batch(
            comorbidity_count, donor_uuid=factory.Iterator(cls.Donor[int(donor_count / 2):
                                                                     int(donor_count / 2) + comorbidity_count])
        )
        logging.info("Creating Biomarkers...")
        cls.Biomarker = BiomarkerFactory.create_batch(
            biomarker_count, donor_uuid=factory.Iterator(cls.Donor)
        )
        logging.info("Creating Exposures...")
        cls.Exposure = ExposureFactory.create_batch(
            exposure_count,
            donor_uuid=factory.Iterator(cls.Donor[int(exposure_count / 2):(int(exposure_count / 2) + exposure_count)])
        )
        logging.info("Creating Follow Ups...")
        FollowUpFactory.reset_sequence(1)
        cls.FollowUp = FollowUpFactory.create_batch(
            followup_count,
            donor_uuid=factory.Iterator(cls.Donor),
            primary_diagnosis_uuid=factory.Iterator(cls.PrimaryDiagnosis),
            treatment_uuid=factory.Iterator(cls.Treatment)
        )

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
        self.SynthDonor = [self.clean_dict(x) for x in self.SynthDonor]
        self.Exposure = [self.clean_dict(x) for x in self.Exposure]
        self.PrimaryDiagnosis = [self.clean_dict(x) for x in self.PrimaryDiagnosis]
        self.Specimen = [self.clean_dict(x) for x in self.Specimen]
        self.SampleRegistration = [self.clean_dict(x) for x in self.SampleRegistration]
        self.Treatment = [self.clean_dict(x) for x in self.Treatment]
        self.SystemicTherapy = [self.clean_dict(x) for x in self.SystemicTherapy]
        self.Radiation = [self.clean_dict(x) for x in self.Radiation]
        self.Surgery = [self.clean_dict(x) for x in self.Surgery]
        self.FollowUp = [self.clean_dict(x) for x in self.FollowUp]


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
        help="Number of programs to generate (if not using size option)."
    )
    parser.add_argument(
        '-d', '--total-donors',
        type=int,
        default=80,
        help="Number of donors to generate, will be distributed amongst the programs given by --num-programs. "
             "Default=80"
    )
    parser.add_argument(
        '--dont-minify',
        action='store_true',
        help='Use this flag to output jsons as indented jsons that are easier to read but are larger files.'
    )
    args = parser.parse_args()
    return args


def main():
    factory.random.reseed_random('mohccn synthetic data')
    args = parse_args()
    test_donor = DonorFactory(null_percent=20)
    if args.num_programs:
        params = {"program_count": args.num_programs, "donor_count": args.total_donors,
                  "pd_count": args.total_donors, "specimen_count": args.total_donors,
                  "sample_count": 3 * args.total_donors, "treatment_count": args.total_donors * 2,
                  "radiation_count": args.total_donors, "surgery_count": args.total_donors,
                  "comorbidity_count": int(args.total_donors / 2), "biomarker_count": int(args.total_donors / 2),
                  "exposure_count": int(args.total_donors / 4), "followup_count": int(args.total_donors / 4),
                  "sys_therapy_count": args.total_donors * 4}
        programs = Dataset(**params)
        path = f"custom_{args.num_programs}P_{args.total_donors}D_dataset"
    else:
        size_mapping = {
            "s": {"size": "small",
                  "params": {"program_count": 4, "donor_count": 80, "pd_count": 80, "specimen_count": 80,
                             "sample_count": 240, "treatment_count": 160, "radiation_count": 80, "surgery_count": 80,
                             "comorbidity_count": 40, "biomarker_count": 40, "exposure_count": 40, "followup_count": 20,
                             "sys_therapy_count": 320}
                  },
            "m": {"size": "medium",
                  "params": {"program_count": 4, "donor_count": 800, "pd_count": 800, "specimen_count": 800,
                             "sample_count": 2400, "treatment_count": 1600, "radiation_count": 800,
                             "surgery_count": 800, "comorbidity_count": 400, "biomarker_count": 400,
                             "exposure_count": 400, "followup_count": 200, "sys_therapy_count": 3200}
                  },
            "l": {"size": "large",
                  "params": {"program_count": 4, "donor_count": 2000, "pd_count": 2000, "specimen_count": 2000,
                             "sample_count": 6000, "treatment_count": 4000, "radiation_count": 2000,
                             "surgery_count": 2000, "comorbidity_count": 1000, "biomarker_count": 1000,
                             "exposure_count": 1000, "followup_count": 500, "sys_therapy_count": 8000}
                  }
        }
        if not args.size:
            args.size = "s"
        path = f"{size_mapping[args.size]["size"]}_dataset"
        programs = Dataset(**size_mapping[args.size]['params'])
    programs.convert_to_dicts()
    path = f"{path}/synthetic_data"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    for schema, data in programs.__dict__.items():
        logging.info(f"Saving {schema} objects to file...")
        with open(f"{path}/{schema}.json", "w+") as f:
            if args.dont_minify:
                json.dump(data, f, indent=4)
            else:
                json.dump(data, f)


if __name__ == "__main__":
    main()
