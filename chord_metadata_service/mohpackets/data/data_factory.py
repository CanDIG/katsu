import os
import sys
import json
import argparse
import pathlib
import tqdm

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
    SynthPrimaryDiagnosisFactory,
    SynthSpecimenFactory,
    SynthSampleRegistrationFactory,
    SynthTreatmentFactory,
    SynthSystemicTherapyFactory,
    SynthSurgeryFactory,
    SynthRadiationFactory,
    SynthBiomarkerFactory,

)


class Dataset:
    """Create a set of programs with synthetic data"""

    @classmethod
    def __init__(cls, program_count=4, donor_count=80, pd_count=80, specimen_count=80, sample_count=240,
                 treatment_count=160, radiation_count=80, surgery_count=80, comorbidity_count=40, biomarker_count=40,
                 exposure_count=40, followup_count=40, sys_therapy_count=320):
        logging.info("Creating Programs...")
        ProgramFactory.reset_sequence(1)
        cls.Program = ProgramFactory.create_batch(program_count)

        DonorFactory.reset_sequence(1)
        PrimaryDiagnosisFactory.reset_sequence(1)
        SpecimenFactory.reset_sequence(1)
        SampleRegistrationFactory.reset_sequence(1)
        TreatmentFactory.reset_sequence(1)
        RadiationFactory.reset_sequence(1)
        SurgeryFactory.reset_sequence(1)
        SystemicTherapyFactory.reset_sequence(1)
        BiomarkerFactory.reset_sequence(1)
        ComorbidityFactory.reset_sequence(1)
        ExposureFactory.reset_sequence(1)
        FollowUpFactory.reset_sequence(1)

        cls.Donor = []
        cls.PrimaryDiagnosis = []
        cls.Specimen = []
        cls.SampleRegistration = []
        cls.Treatment = []
        cls.SysTherapy = []
        cls.Radiation = []
        cls.Surgery = []
        cls.Comorbidity = []
        cls.Biomarker = []
        cls.Exposure = []
        cls.FollowUp = []

        donors_per_program = int(donor_count / program_count)
        samples_per_specimen = int(sample_count / specimen_count)
        treatments_per_pd = int(treatment_count / pd_count)
        sys_therapy_per_treatment = int(sys_therapy_count / treatment_count)
        followups_per_program = int(followup_count / program_count)
        exposure_start_index = int(donors_per_program / 4)
        exposure_end_index = int(exposure_start_index + (exposure_count / program_count))
        for i in range(0, program_count):
            logging.info(f"Creating data for PROGRAM_0{i + 1}")
            logging.info(f"Creating Donors...")
            donor_batch = SynthDonorFactory.create_batch(
                donors_per_program, program_id=cls.Program[i]
            )
            cls.Donor.extend(donor_batch)
            logging.info("Primary Diagnoses...")
            pd_batch = SynthPrimaryDiagnosisFactory.create_batch(
                donors_per_program, donor_uuid=factory.Iterator(donor_batch)
            )
            cls.PrimaryDiagnosis.extend(pd_batch)
            logging.info("Specimens...")
            specimen_batch = SynthSpecimenFactory.create_batch(
                donors_per_program, primary_diagnosis_uuid=factory.Iterator(pd_batch)
            )
            cls.Specimen.extend(specimen_batch)
            logging.info("Creating linked objects per donor")
            for j in tqdm.tqdm(range(0, donors_per_program)):
                sample_batch = SynthSampleRegistrationFactory.create_batch(
                    samples_per_specimen, specimen_uuid=specimen_batch[j])
                cls.SampleRegistration.extend(sample_batch)
                treatment_batch = SynthTreatmentFactory.create_batch(
                    treatments_per_pd, primary_diagnosis_uuid=pd_batch[j]
                )
                cls.Treatment.extend(treatment_batch)
                cls.Surgery.append(SynthSurgeryFactory.create(treatment_uuid=treatment_batch[0]))
                cls.Radiation.append(SynthRadiationFactory.create(treatment_uuid=treatment_batch[1]))
                for k in range(0, treatments_per_pd):
                    sys_therapy_batch = SynthSystemicTherapyFactory.create_batch(
                        sys_therapy_per_treatment, treatment_uuid=treatment_batch[k]
                    )
                    cls.SysTherapy.extend(sys_therapy_batch)
                if j < followups_per_program:
                    cls.FollowUp.append(FollowUpFactory.create(donor_uuid=donor_batch[j],
                                                               primary_diagnosis_uuid=pd_batch[j],
                                                               treatment_uuid=treatment_batch[0]))
                    cls.Biomarker.append(SynthBiomarkerFactory.create(donor_uuid=donor_batch[j]))
                if j >= followups_per_program:
                    cls.Comorbidity.append(ComorbidityFactory.create(donor_uuid=donor_batch[j]))
                if exposure_start_index < j <= exposure_end_index:
                    cls.Exposure.append(ExposureFactory.create(donor_uuid=donor_batch[j]))

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
        self.SystemicTherapy = [self.clean_dict(x) for x in self.SysTherapy]
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
                             "comorbidity_count": 40, "biomarker_count": 40, "exposure_count": 40, "followup_count": 40,
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
    logging.info(f"Saving objects to file in: {path}")
    for schema, data in programs.__dict__.items():
        with open(f"{path}/{schema}.json", "w+") as f:
            if args.dont_minify:
                json.dump(data, f, indent=4)
            else:
                json.dump(data, f)
    logging.info("All done.")


if __name__ == "__main__":
    main()
