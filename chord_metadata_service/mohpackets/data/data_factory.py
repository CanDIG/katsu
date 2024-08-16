import argparse
import json
import logging

# import math
import os
import pathlib
import sys

# Initialize Django
import django
import factory
import factory.random
import tqdm
from django.forms.models import model_to_dict

# Add your Django project's root directory to the Python path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
)  # This assumes your script is in the data directory
# Set the DJANGO_SETTINGS_MODULE to your project's settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
os.environ.setdefault("INSTALLED_APPS", "config.settings.local")

django.setup()


# import original test factories
# import modified factories for synthetic data generation
from synth_data_factories import (  # noqa: E402
    AllSynthBiomarkerFactory,
    AllSynthComorbidityFactory,
    AllSynthDonorFactory,
    AllSynthExposureFactory,
    AllSynthFollowUpFactory,
    AllSynthPrimaryDiagnosisFactory,
    AllSynthRadiationFactory,
    AllSynthSampleRegistrationFactory,
    AllSynthSpecimenFactory,
    AllSynthSurgeryFactory,
    AllSynthSystemicTherapyFactory,
    AllSynthTreatmentFactory,
    NullSynthBiomarkerFactory,
    NullSynthComorbidityFactory,
    NullSynthDonorFactory,
    NullSynthExposureFactory,
    NullSynthFollowUpFactory,
    NullSynthPrimaryDiagnosisFactory,
    NullSynthRadiationFactory,
    NullSynthSampleRegistrationFactory,
    NullSynthSpecimenFactory,
    NullSynthSurgeryFactory,
    NullSynthSystemicTherapyFactory,
    NullSynthTreatmentFactory,
    SynthBiomarkerFactory,
    SynthComorbidityFactory,
    SynthDonorFactory,
    SynthExposureFactory,
    SynthFollowUpFactory,
    SynthPrimaryDiagnosisFactory,
    SynthProgramFactory,
    SynthRadiationFactory,
    SynthSampleRegistrationFactory,
    SynthSpecimenFactory,
    SynthSurgeryFactory,
    SynthSystemicTherapyFactory,
    SynthTreatmentFactory,
)

from chord_metadata_service.mohpackets.tests.factories import (  # noqa: E402
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


class Dataset:
    """Object to store a set of programs with synthetic data generated by factories"""

    @classmethod
    def __init__(
        cls,
        program_count=4,
        donor_count=80,
        pd_count=80,
        specimen_count=80,
        sample_count=240,
        treatment_count=160,
        exposure_count=40,
        followup_count=40,
        sys_therapy_count=320,
        all_type_donor_count=2,
        null_type_donor_count=2,
    ):
        logging.info("Creating Programs...")

        # reset sequences so all identifiers start with 1
        ProgramFactory.reset_sequence(1)
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

        # Initialize object attributes for each schema
        cls.Program = SynthProgramFactory.create_batch(program_count)
        cls.Donor = []
        cls.PrimaryDiagnosis = []
        cls.Specimen = []
        cls.SampleRegistration = []
        cls.Treatment = []
        cls.SystemicTherapy = []
        cls.Radiation = []
        cls.Surgery = []
        cls.Comorbidity = []
        cls.Biomarker = []
        cls.Exposure = []
        cls.FollowUp = []

        # Calculate counts for later iteration
        donors_per_program = int(donor_count / program_count)
        samples_per_specimen = int(sample_count / specimen_count)
        treatments_per_pd = int(treatment_count / pd_count)
        sys_therapy_per_treatment = int(sys_therapy_count / treatment_count)
        followups_per_program = int(followup_count / program_count)
        exposure_start_index = int(donors_per_program / 4)
        exposure_end_index = int(
            exposure_start_index + (exposure_count / program_count)
        )
        for i in range(0, program_count):
            logging.info(f"Creating data for SYNTH_0{i + 1}")
            logging.info("Creating Donors...")
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
                    samples_per_specimen, specimen_uuid=specimen_batch[j]
                )
                cls.SampleRegistration.extend(sample_batch)
                treatment_batch = SynthTreatmentFactory.create_batch(
                    treatments_per_pd, primary_diagnosis_uuid=pd_batch[j]
                )
                cls.Treatment.extend(treatment_batch)
                cls.Surgery.append(
                    SynthSurgeryFactory.create(treatment_uuid=treatment_batch[0])
                )
                cls.Radiation.append(
                    SynthRadiationFactory.create(treatment_uuid=treatment_batch[1])
                )
                for k in range(0, treatments_per_pd):
                    sys_therapy_batch = SynthSystemicTherapyFactory.create_batch(
                        sys_therapy_per_treatment, treatment_uuid=treatment_batch[k]
                    )
                    cls.SystemicTherapy.extend(sys_therapy_batch)
                if j < followups_per_program:
                    this_followup = SynthFollowUpFactory.create(
                        donor_uuid=donor_batch[j],
                        primary_diagnosis_uuid=pd_batch[j],
                        treatment_uuid=treatment_batch[0],
                    )
                    cls.FollowUp.append(this_followup)
                    cls.Biomarker.append(
                        SynthBiomarkerFactory.create(
                            donor_uuid=donor_batch[j],
                            specimen_uuid=specimen_batch[j],
                            pd_uuid=pd_batch[j],
                            treatment_uuid=treatment_batch[0],
                            followup_uuid=this_followup,
                        )
                    )

                if j >= followups_per_program:
                    cls.Comorbidity.append(
                        SynthComorbidityFactory.create(donor_uuid=donor_batch[j])
                    )
                if exposure_start_index < j <= exposure_end_index:
                    cls.Exposure.append(
                        SynthExposureFactory.create(donor_uuid=donor_batch[j])
                    )

        logging.info(
            f"generating {null_type_donor_count} donors with all nulled fields"
        )
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
        null_donors = NullSynthDonorFactory.create_batch(
            null_type_donor_count, program_id=cls.Program[0]
        )
        cls.Donor.extend(null_donors)
        null_pds = NullSynthPrimaryDiagnosisFactory.create_batch(
            null_type_donor_count, donor_uuid=factory.Iterator(null_donors)
        )
        cls.PrimaryDiagnosis.extend(null_pds)
        null_specimens = NullSynthSpecimenFactory.create_batch(
            null_type_donor_count, primary_diagnosis_uuid=factory.Iterator(null_pds)
        )
        cls.Specimen.extend(null_specimens)
        for i in range(0, null_type_donor_count):
            null_samples = NullSynthSampleRegistrationFactory.create_batch(
                samples_per_specimen, specimen_uuid=null_specimens[i]
            )
            cls.SampleRegistration.extend(null_samples)
            null_treatments = NullSynthTreatmentFactory.create_batch(
                treatments_per_pd, primary_diagnosis_uuid=null_pds[i]
            )
            cls.Treatment.extend(null_treatments)
            cls.Surgery.append(
                NullSynthSurgeryFactory.create(treatment_uuid=null_treatments[0])
            )
            cls.Radiation.append(
                NullSynthRadiationFactory.create(treatment_uuid=null_treatments[1])
            )
            for j in range(0, treatments_per_pd):
                sys_therapy_batch = NullSynthSystemicTherapyFactory.create_batch(
                    sys_therapy_per_treatment, treatment_uuid=null_treatments[j]
                )
                cls.SystemicTherapy.extend(sys_therapy_batch)
            if i < followups_per_program:
                this_followup = NullSynthFollowUpFactory.create(
                    donor_uuid=null_donors[i],
                    primary_diagnosis_uuid=null_pds[i],
                    treatment_uuid=null_treatments[0],
                )
                cls.FollowUp.append(this_followup)
                cls.Biomarker.append(
                    NullSynthBiomarkerFactory.create(
                        donor_uuid=null_donors[i],
                        specimen_uuid=null_specimens[i],
                        pd_uuid=null_pds[i],
                        treatment_uuid=null_treatments[0],
                        followup_uuid=this_followup,
                    )
                )
            if i >= followups_per_program:
                cls.Comorbidity.append(
                    NullSynthComorbidityFactory.create(donor_uuid=null_donors[i])
                )
            if exposure_start_index < i <= exposure_end_index:
                cls.Exposure.append(
                    NullSynthExposureFactory.create(donor_uuid=null_donors[i])
                )

        logging.info(
            f"generating {all_type_donor_count} donors with all fields filled in"
        )
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
        # num_other_linked = math.ceil(followups_per_program / 3)
        all_donors = AllSynthDonorFactory.create_batch(
            all_type_donor_count, program_id=cls.Program[0]
        )
        cls.Donor.extend(all_donors)
        all_pds = AllSynthPrimaryDiagnosisFactory.create_batch(
            all_type_donor_count, donor_uuid=factory.Iterator(all_donors)
        )
        cls.PrimaryDiagnosis.extend(all_pds)
        all_specimens = AllSynthSpecimenFactory.create_batch(
            all_type_donor_count, primary_diagnosis_uuid=factory.Iterator(all_pds)
        )
        cls.Specimen.extend(all_specimens)
        for i in range(0, all_type_donor_count):
            all_samples = AllSynthSampleRegistrationFactory.create_batch(
                samples_per_specimen, specimen_uuid=all_specimens[i]
            )
            cls.SampleRegistration.extend(all_samples)
            all_treatments = AllSynthTreatmentFactory.create_batch(
                treatments_per_pd, primary_diagnosis_uuid=all_pds[i]
            )
            cls.Treatment.extend(all_treatments)
            cls.Surgery.append(
                AllSynthSurgeryFactory.create(treatment_uuid=all_treatments[0])
            )
            cls.Radiation.append(
                AllSynthRadiationFactory.create(treatment_uuid=all_treatments[1])
            )
            for j in range(0, treatments_per_pd):
                sys_therapy_batch = AllSynthSystemicTherapyFactory.create_batch(
                    sys_therapy_per_treatment, treatment_uuid=all_treatments[j]
                )
                cls.SystemicTherapy.extend(sys_therapy_batch)
            if i < followups_per_program:
                this_followup = AllSynthFollowUpFactory.create(
                    donor_uuid=all_donors[i],
                    primary_diagnosis_uuid=all_pds[i],
                    treatment_uuid=all_treatments[0],
                )
                cls.FollowUp.append(this_followup)
                cls.Biomarker.append(
                    AllSynthBiomarkerFactory.create(
                        donor_uuid=all_donors[i],
                        specimen_uuid=all_specimens[i],
                        pd_uuid=all_pds[i],
                        treatment_uuid=all_treatments[0],
                        followup_uuid=this_followup,
                    )
                )
            if i >= followups_per_program or all_type_donor_count == 1:
                cls.Comorbidity.append(
                    AllSynthComorbidityFactory.create(donor_uuid=all_donors[i])
                )
            if (
                exposure_start_index < i <= exposure_end_index
                or all_type_donor_count == 1
            ):
                cls.Exposure.append(
                    AllSynthExposureFactory.create(donor_uuid=all_donors[i])
                )

    def __getitem__(self, item):
        return getattr(self, item)

    @staticmethod
    def clean_dict(dirty_dict):
        """Transforms the factory object into a dictionary and removes fields that cause errors during
        JSON serialisation"""
        clean_dict = model_to_dict(dirty_dict)
        if "created" in clean_dict.keys():
            del clean_dict["created"]
        if "updated" in clean_dict.keys():
            del clean_dict["updated"]
        if "uuid" in clean_dict.keys():
            del clean_dict["uuid"]
        if "primary_diagnosis_uuid" in clean_dict.keys():
            del clean_dict["primary_diagnosis_uuid"]
        if "donor_uuid" in clean_dict.keys():
            del clean_dict["donor_uuid"]
        if "treatment_uuid" in clean_dict.keys():
            del clean_dict["treatment_uuid"]
        if "specimen_uuid" in clean_dict.keys():
            del clean_dict["specimen_uuid"]
        return clean_dict

    def convert_to_dicts(self):
        """Convert all each object type to a list of dictionaries that can be output as JSON files"""
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
        self.FollowUp = [self.clean_dict(x) for x in self.FollowUp]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--size",
        type=str,
        choices=["xs", "s", "m", "l"],
        help="Size of the dataset to convert, options: 's' for small, 'm' for medium, 'l' for large (default: small)",
    )
    parser.add_argument(
        "-p",
        "--num-programs",
        type=int,
        help="Number of programs to generate (if not using size option).",
    )
    parser.add_argument(
        "-d",
        "--total-donors",
        type=int,
        default=80,
        help="Number of donors to generate, will be distributed amongst the programs given by --num-programs. "
        "Default=80",
    )
    parser.add_argument(
        "--dont-minify",
        action="store_true",
        help="Use this flag to output jsons as indented jsons that are easier to read but are larger files.",
    )
    args = parser.parse_args()
    return args


def main():
    factory.random.reseed_random("mohccn synthetic data")
    args = parse_args()
    if args.num_programs:
        params = {
            "program_count": args.num_programs,
            "donor_count": args.total_donors,
            "pd_count": args.total_donors,
            "specimen_count": args.total_donors,
            "sample_count": 3 * args.total_donors,
            "treatment_count": args.total_donors * 2,
            "exposure_count": int(args.total_donors / 4),
            "followup_count": int(args.total_donors / 4),
            "sys_therapy_count": args.total_donors * 4,
            "all_type_donor_count": 2,
            "null_type_donor_count": 2,
        }
        programs = Dataset(**params)
        path = f"custom_{args.num_programs}P_{args.total_donors}D_dataset"
    else:
        size_mapping = {
            "xs": {
                "size": "extra_small",
                "params": {
                    "program_count": 2,
                    "donor_count": 10,
                    "pd_count": 10,
                    "specimen_count": 10,
                    "sample_count": 30,
                    "treatment_count": 20,
                    "exposure_count": 5,
                    "followup_count": 6,
                    "sys_therapy_count": 40,
                    "all_type_donor_count": 1,
                    "null_type_donor_count": 1,
                },
            },
            "s": {
                "size": "small",
                "params": {
                    "program_count": 4,
                    "donor_count": 80,
                    "pd_count": 80,
                    "specimen_count": 80,
                    "sample_count": 240,
                    "treatment_count": 160,
                    "exposure_count": 40,
                    "followup_count": 40,
                    "sys_therapy_count": 320,
                    "all_type_donor_count": 2,
                    "null_type_donor_count": 2,
                },
            },
            "m": {
                "size": "medium",
                "params": {
                    "program_count": 4,
                    "donor_count": 800,
                    "pd_count": 800,
                    "specimen_count": 800,
                    "sample_count": 2400,
                    "treatment_count": 1600,
                    "exposure_count": 400,
                    "followup_count": 200,
                    "sys_therapy_count": 3200,
                    "all_type_donor_count": 2,
                    "null_type_donor_count": 2,
                },
            },
            "l": {
                "size": "large",
                "params": {
                    "program_count": 4,
                    "donor_count": 2000,
                    "pd_count": 2000,
                    "specimen_count": 2000,
                    "sample_count": 6000,
                    "treatment_count": 4000,
                    "exposure_count": 1000,
                    "followup_count": 500,
                    "sys_therapy_count": 8000,
                    "all_type_donor_count": 2,
                    "null_type_donor_count": 2,
                },
            },
        }
        if not args.size:
            args.size = "s"
        path = f"{size_mapping[args.size]["size"]}_dataset"
        programs = Dataset(**size_mapping[args.size]["params"])
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
