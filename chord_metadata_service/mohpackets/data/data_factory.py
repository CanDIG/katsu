
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
    @classmethod
    def __init__(cls, program_count=4, donor_count=80, pd_count=80, specimen_count=80, sample_count=240,
                 treatment_count=160, radiation_count=80, surgery_count=80, comorbidity_count=40, biomarker_count=40,
                 exposure_count=30, followup_count=2, sys_therapy_count=320):
        cls.programs = ProgramFactory.create_batch(program_count)
        logging.info("Creating Donors...")
        cls.donors = DonorFactory.create_batch(
            donor_count, program_id=factory.Iterator(cls.programs)
        )
        logging.info("Creating Primary Diagnoses...")
        cls.primary_diagnoses = PrimaryDiagnosisFactory.create_batch(
            pd_count, donor_uuid=factory.Iterator(cls.donors)
        )
        logging.info("Creating Specimens...")
        cls.specimens = SpecimenFactory.create_batch(
            specimen_count, primary_diagnosis_uuid=factory.Iterator(cls.primary_diagnoses)
        )
        logging.info("Creating Sample registrations...")
        cls.sample_registrations = SampleRegistrationFactory.create_batch(
            sample_count, specimen_uuid=factory.Iterator(cls.specimens)
        )
        logging.info("Creating Treatments...")
        cls.treatments = TreatmentFactory.create_batch(
            treatment_count, primary_diagnosis_uuid=factory.Iterator(cls.primary_diagnoses)
        )
        cls.systemic_therapies = SystemicTherapyFactory.create_batch(
            sys_therapy_count, treatment_uuid=factory.Iterator(cls.treatments)
        )
        logging.info("Creating Radiations...")
        cls.radiations = RadiationFactory.create_batch(
            radiation_count, treatment_uuid=factory.Iterator(cls.treatments[0:int(treatment_count/2)])
        )
        logging.info("Creating Surgeries...")
        cls.surgeries = SurgeryFactory.create_batch(
            surgery_count, treatment_uuid=factory.Iterator(cls.treatments[int(treatment_count/2):treatment_count])
        )
        logging.info("Creating Comorbidities...")
        cls.comorbidities = ComorbidityFactory.create_batch(
            comorbidity_count, donor_uuid=factory.Iterator(cls.donors)
        )
        logging.info("Creating Biomarkers...")
        cls.biomarkers = BiomarkerFactory.create_batch(
            biomarker_count, donor_uuid=factory.Iterator(cls.donors)
        )
        logging.info("Creating Exposurs...")
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

    def __iter__(self):
        yield "programs", self.programs
        yield "donors", self.donors
        yield ""

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
        self.systemic_therapies = [model_to_dict(x) for x in self.systemic_therapies]
        self.radiations = [model_to_dict(x) for x in self.radiations]
        self.surgeries = [model_to_dict(x) for x in self.surgeries]
        # self.followups = [model_to_dict(x) for x in self.followups]

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
    for program in programs:
        print(program)

        print(programs)


if __name__ == "__main__":
    main()
