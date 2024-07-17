import random
import uuid
import math

import factory

import chord_metadata_service.mohpackets.permissible_values as PERM_VAL
import chord_metadata_service.mohpackets.data.synth_data_values as SYNTH_VAL
from chord_metadata_service.mohpackets.models import (
    Biomarker,
    Comorbidity,
    Donor,
    Exposure,
    FollowUp,
    PrimaryDiagnosis,
    Program,
    Radiation,
    SampleRegistration,
    Specimen,
    Surgery,
    SystemicTherapy,
    Treatment,
)

"""
    This file contains factory classes for generating test data.

    These factories make it easy to create mock instances of various models
    with customizable attributes, which simplifies the process of setting up
    test data for unit and integration tests.

    Example Usage:
        # This will create a Program instance with the specified program_id.
        program = ProgramFactory(program_id='CUSTOM_PROGRAM')

        # This will create a Donor instance and a Program instance
        donor = DonorFactory()

    Note:
        These factories use the Factory Boy library (https://factoryboy.readthedocs.io/)
        to generate test data.
        Some business logic is not strictly enforced. For example,
        date_of_birth could have mismatched month_interval and day_interval.

    Author: Son Chau
"""


#######################
## Utility functions ##
#######################

def days_to_months(day_interval):
    """ Convert a day interval to a month inverval."""
    return int(math.floor(day_interval * 0.032855))


def twenty_percent_true():
    """ Generate True 20% of the time. """
    return random.randrange(100) < 20


def add_nulls(complete_list: list, prop=0.2):
    """ Returns a list with 20% of the list as 'None' """
    num_nulls = math.ceil(len(complete_list) * prop)
    complete_list.extend([None] * num_nulls)
    return complete_list


###############
## Factories ##
###############


class ProgramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Program
        django_get_or_create = ("program_id",)

    # default values
    program_id = factory.Sequence(lambda n: f"PROGRAM_{str(n).zfill(2)}")


class DonorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Donor
        django_get_or_create = ("submitter_donor_id",)
        exclude = ("fill_dob",)

    # default values
    submitter_donor_id = factory.Sequence(lambda n: f"DONOR_{str(n).zfill(4)}")

    # add 20% nulls to all enum lists:
    PERM_VAL.GENDER = add_nulls(PERM_VAL.GENDER)
    PERM_VAL.SEX_AT_BIRTH = add_nulls(PERM_VAL.SEX_AT_BIRTH)

    gender = factory.Faker("random_element", elements=PERM_VAL.GENDER)
    sex_at_birth = factory.Faker("random_element", elements=PERM_VAL.SEX_AT_BIRTH)
    is_deceased = factory.Faker("random_element", elements=[True, False, None])
    lost_to_followup_reason = None
    lost_to_followup_after_clinical_event_identifier = None
    date_alive_after_lost_to_followup = None
    date_resolution = "day"
    cause_of_death = factory.Maybe(
        "is_deceased",
        yes_declaration=factory.Faker(
            "random_element",
            elements=PERM_VAL.CAUSE_OF_DEATH
        ),
        no_declaration=None,
    )
    fill_dob = factory.Faker("pybool", truth_probability=80)
    date_of_birth = factory.Maybe(
        "fill_dob",
        yes_declaration=factory.LazyFunction(lambda: {
            "day_interval": random.randint(-21900, -18220),
        }),
        no_declaration=None
    )
    date_of_death = factory.Maybe(
        "is_deceased",
        yes_declaration=factory.LazyFunction(
            lambda: {
                "day_interval": random.randint(25551, 32850)
            }
        ),
        no_declaration=None,
    )
    # set foreign key
    program_id = factory.SubFactory(ProgramFactory)

    @factory.post_generation
    def consistent_dates(self, create, extracted, **kwargs):
        if self.date_of_birth:
            self.date_of_birth['month_interval'] = days_to_months(self.date_of_birth['day_interval'])
        if self.date_of_death:
            self.date_of_death['month_interval'] = days_to_months(self.date_of_death['day_interval'])


class PrimaryDiagnosisFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PrimaryDiagnosis
        django_get_or_create = ("submitter_primary_diagnosis_id",)
        exclude = ("fill_dod")

    # Default values
    submitter_primary_diagnosis_id = factory.Sequence(lambda n: f"DIAG_{str(n).zfill(4)}")
    fill_dod = factory.Faker("pybool", truth_probability=80)
    date_of_diagnosis = factory.Maybe(
        "fill_dod",
        yes_declaration={"month_interval": 0, "day_interval": 0},
        no_declaration=None
    )
    cancer_type_code = factory.Faker("random_element", elements=SYNTH_VAL.CANCER_CODES)

    # add 20% nulls to all enum lists
    PERM_VAL.BASIS_OF_DIAGNOSIS = add_nulls(PERM_VAL.BASIS_OF_DIAGNOSIS)
    PERM_VAL.PRIMARY_DIAGNOSIS_LATERALITY = add_nulls(PERM_VAL.PRIMARY_DIAGNOSIS_LATERALITY)
    PERM_VAL.TUMOUR_STAGING_SYSTEM = add_nulls(PERM_VAL.TUMOUR_STAGING_SYSTEM)
    PERM_VAL.T_CATEGORY = add_nulls(PERM_VAL.T_CATEGORY)
    PERM_VAL.N_CATEGORY = add_nulls(PERM_VAL.N_CATEGORY)
    PERM_VAL.M_CATEGORY = add_nulls(PERM_VAL.M_CATEGORY)
    PERM_VAL.STAGE_GROUP = add_nulls(PERM_VAL.STAGE_GROUP)

    basis_of_diagnosis = factory.Faker("random_element", elements=PERM_VAL.BASIS_OF_DIAGNOSIS)
    laterality = factory.Faker("random_element", elements=PERM_VAL.PRIMARY_DIAGNOSIS_LATERALITY)
    clinical_tumour_staging_system = factory.Faker("random_element", elements=PERM_VAL.TUMOUR_STAGING_SYSTEM)
    clinical_t_category = factory.Faker("random_element", elements=PERM_VAL.T_CATEGORY)
    clinical_n_category = factory.Faker("random_element", elements=PERM_VAL.N_CATEGORY)
    clinical_m_category = factory.Faker("random_element", elements=PERM_VAL.M_CATEGORY)
    clinical_stage_group = factory.Faker("random_element", elements=PERM_VAL.STAGE_GROUP)
    pathological_tumour_staging_system = factory.Faker("random_element", elements=PERM_VAL.TUMOUR_STAGING_SYSTEM)
    pathological_t_category = factory.Faker("random_element", elements=PERM_VAL.T_CATEGORY)
    pathological_n_category = factory.Faker("random_element", elements=PERM_VAL.N_CATEGORY)
    pathological_m_category = factory.Faker("random_element", elements=PERM_VAL.M_CATEGORY)
    pathological_stage_group = factory.Faker("random_element", elements=PERM_VAL.STAGE_GROUP)
    primary_site = factory.Iterator(SYNTH_VAL.PRIMARY_SITE)

    # Set the foreign keys
    program_id = factory.SelfAttribute("donor_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("donor_uuid.submitter_donor_id")
    donor_uuid = factory.SubFactory(DonorFactory)

    @factory.post_generation
    def set_clinical_event_identifier(self, create, extracted, **kwargs):
        if twenty_percent_true():
            pass
        else:
            donor = self.donor_uuid
            if not donor.is_deceased:
                donor.lost_to_followup_after_clinical_event_identifier = (
                    self.submitter_primary_diagnosis_id
                )
                donor.lost_to_followup_reason = random.choice(
                    PERM_VAL.LOST_TO_FOLLOWUP_REASON
                )
                donor.date_alive_after_lost_to_followup = {
                    "day_interval": random.randint(25551, 32850),
                }
                donor.date_alive_after_lost_to_followup["month_interval"] = (
                    days_to_months(donor.date_alive_after_lost_to_followup["day_interval"]))
                donor.save()


class SpecimenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Specimen
        django_get_or_create = ("submitter_specimen_id",)

    # default values
    submitter_specimen_id = factory.Sequence(lambda n: f"SPECIMEN_{str(n).zfill(4)}")
    specimen_collection_date = None

    # add 20% nulls to all enum lists
    PERM_VAL.STORAGE = add_nulls(PERM_VAL.STORAGE)
    PERM_VAL.SPECIMEN_PROCESSING = add_nulls(PERM_VAL.SPECIMEN_PROCESSING)
    PERM_VAL.TOPOGRAPHY_CODES = add_nulls(PERM_VAL.TOPOGRAPHY_CODES)
    PERM_VAL.SPECIMEN_LATERALITY = add_nulls(PERM_VAL.SPECIMEN_LATERALITY)
    PERM_VAL.CONFIRMED_DIAGNOSIS_TUMOUR = add_nulls(PERM_VAL.CONFIRMED_DIAGNOSIS_TUMOUR)
    PERM_VAL.TUMOUR_GRADE = add_nulls(PERM_VAL.TUMOUR_GRADE)
    PERM_VAL.TUMOUR_GRADING_SYSTEM = add_nulls(PERM_VAL.TUMOUR_GRADING_SYSTEM)
    PERM_VAL.PERCENT_CELLS_RANGE = add_nulls(PERM_VAL.PERCENT_CELLS_RANGE)
    PERM_VAL.CELLS_MEASURE_METHOD = add_nulls(PERM_VAL.CELLS_MEASURE_METHOD)

    specimen_storage = factory.Faker("random_element", elements=PERM_VAL.STORAGE)
    specimen_processing = factory.Faker("random_element", elements=PERM_VAL.SPECIMEN_PROCESSING)
    tumour_histological_type = None
    specimen_anatomic_location = factory.Faker("random_element", elements=PERM_VAL.TOPOGRAPHY_CODES)
    specimen_laterality = factory.Faker("random_element", elements=PERM_VAL.SPECIMEN_LATERALITY)
    reference_pathology_confirmed_diagnosis = factory.Faker(
        "random_element", elements=PERM_VAL.CONFIRMED_DIAGNOSIS_TUMOUR
    )
    reference_pathology_confirmed_tumour_presence = factory.Faker(
        "random_element", elements=PERM_VAL.CONFIRMED_DIAGNOSIS_TUMOUR
    )
    tumour_grading_system = factory.Faker(
        "random_element", elements=PERM_VAL.TUMOUR_GRADING_SYSTEM
    )
    tumour_grade = factory.Faker("random_element", elements=PERM_VAL.TUMOUR_GRADE)
    percent_tumour_cells_range = factory.Faker(
        "random_element", elements=PERM_VAL.PERCENT_CELLS_RANGE
    )
    percent_tumour_cells_measurement_method = factory.Faker(
        "random_element", elements=PERM_VAL.CELLS_MEASURE_METHOD
    )

    # set foreign keys
    program_id = factory.SelfAttribute("primary_diagnosis_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute(
        "primary_diagnosis_uuid.submitter_donor_id"
    )
    donor_uuid = factory.SelfAttribute("primary_diagnosis_uuid.donor_uuid")
    submitter_primary_diagnosis_id = factory.SelfAttribute(
        "primary_diagnosis_uuid.submitter_primary_diagnosis_id"
    )
    primary_diagnosis_uuid = factory.SubFactory(PrimaryDiagnosisFactory)
    submitter_treatment_id = None

    @factory.post_generation
    def set_date(self, create, extracted, **kwargs):
        if twenty_percent_true():
            self.specimen_collection_date = None
        else:
            self.specimen_collection_date = {"day_interval": random.randint(0, 90)}
            self.specimen_collection_date['month_interval'] = days_to_months(
                self.specimen_collection_date['day_interval'])

    @factory.post_generation
    def generate_histology_code(self, create, extracted, **kwargs):
        if twenty_percent_true():
            self.tumour_histological_type = None
        else:
            one = str(random.randint(8, 9))
            two = str(random.randint(0, 999)).rjust(3, "0")
            code = one + two + "/3"
            self.tumour_histological_type = code


class SampleRegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SampleRegistration
        django_get_or_create = ("submitter_sample_id",)

    # default values
    submitter_sample_id = factory.Sequence(lambda n: f"SAMPLE_{str(n).zfill(4)}")

    # add 20% nulls to all enum lists
    PERM_VAL.SPECIMEN_TISSUE_SOURCE = add_nulls(PERM_VAL.SPECIMEN_TISSUE_SOURCE)
    PERM_VAL.SPECIMEN_TYPE = add_nulls(PERM_VAL.SPECIMEN_TYPE)
    PERM_VAL.SAMPLE_TYPE = add_nulls(PERM_VAL.SAMPLE_TYPE)

    specimen_tissue_source = factory.Faker(
        "random_element", elements=PERM_VAL.SPECIMEN_TISSUE_SOURCE
    )
    tumour_normal_designation = factory.Iterator(["Normal", "Tumour", None])
    specimen_type = factory.Faker("random_element", elements=PERM_VAL.SPECIMEN_TYPE)
    sample_type = factory.Faker("random_element", elements=PERM_VAL.SAMPLE_TYPE)

    # set foreign keys
    program_id = factory.SelfAttribute("specimen_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("specimen_uuid.submitter_donor_id")
    donor_uuid = factory.SelfAttribute("specimen_uuid.donor_uuid")
    submitter_specimen_id = factory.SelfAttribute("specimen_uuid.submitter_specimen_id")
    specimen_uuid = factory.SubFactory(SpecimenFactory)


class TreatmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Treatment
        django_get_or_create = ("submitter_treatment_id",)

    # default values
    submitter_treatment_id = factory.Sequence(lambda n: f"TREATMENT_{str(n).zfill(4)}")

    # add 20% nulls to all enum lists
    PERM_VAL.TREATMENT_INTENT = add_nulls(PERM_VAL.TREATMENT_INTENT)
    PERM_VAL.TREATMENT_RESPONSE_METHOD = add_nulls(PERM_VAL.TREATMENT_RESPONSE_METHOD)
    PERM_VAL.TREATMENT_RESPONSE = add_nulls(PERM_VAL.TREATMENT_RESPONSE)
    PERM_VAL.TREATMENT_STATUS = add_nulls(PERM_VAL.TREATMENT_STATUS)

    treatment_type = factory.Faker(
        "random_elements",
        elements=PERM_VAL.TREATMENT_TYPE,
        length=random.randint(1, 3),
        unique=True,
    )
    is_primary_treatment = factory.Faker("random_element", elements=["Yes", "No", None])
    treatment_start_date = None
    treatment_end_date = None
    treatment_intent = factory.Faker(
        "random_element", elements=PERM_VAL.TREATMENT_INTENT
    )
    # days_per_cycle = factory.Faker("random_int", min=1, max=30)
    # number_of_cycles = factory.Faker("random_int", min=1, max=10)
    response_to_treatment_criteria_method = factory.Faker(
        "random_element", elements=PERM_VAL.TREATMENT_RESPONSE_METHOD
    )
    response_to_treatment = factory.Faker(
        "random_element", elements=PERM_VAL.TREATMENT_RESPONSE
    )
    status_of_treatment = factory.Faker(
        "random_element", elements=PERM_VAL.TREATMENT_STATUS
    )

    # set foreign keys
    program_id = factory.SelfAttribute("primary_diagnosis_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute(
        "primary_diagnosis_uuid.submitter_donor_id"
    )
    donor_uuid = factory.SelfAttribute("primary_diagnosis_uuid.donor_uuid")
    submitter_primary_diagnosis_id = factory.SelfAttribute(
        "primary_diagnosis_uuid.submitter_primary_diagnosis_id"
    )
    primary_diagnosis_uuid = factory.SubFactory(PrimaryDiagnosisFactory)

    @factory.post_generation
    def set_treatment_dates(self, create, extracted, **kwargs):
        treatment = self
        if twenty_percent_true():
            treatment.treatment_start_date = None
        else:
            day_int = random.randint(5, 180)
            treatment.treatment_start_date = {"day_interval": day_int,
                                              "month_interval": days_to_months(day_int)}
        if twenty_percent_true():
            treatment.treatment_end_date = None
        else:
            if treatment.treatment_start_date:
                min_start = treatment.treatment_start_date["day_interval"] + 30
            else:
                min_start = 5
            min_end = min_start + 365
            day_int = random.randint(min_start, min_end)
            treatment.treatment_end_date = {"day_interval": day_int,
                                            "month_interval": days_to_months(day_int)}
        treatment.save()

    @factory.post_generation
    def correct_treatment_type(self, create, extracted, **kwargs):
        if twenty_percent_true():
            self.treatment_type = None
        elif self.treatment_type and "No treatment" in self.treatment_type:
            self.treatment_type = ["No treatment"]

    # @factory.post_generation
    # def set_treatment_identifier(self, create, extracted, **kwargs):
    #     specimen = self.specimen_uuid  # this won't work because no specimen uuid on treatment
    #     if self.treatment_type == "Surgery":
    #         specimen.submitter_treatment_id = (
    #             self.submitter_treatment_id
    #         )
    #         specimen.save()


class SystemicTherapyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SystemicTherapy
        exclude = ("null_drug_dose", )

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)
    drug_reference_database = None
    drug_name = None
    drug_reference_identifier = None

    # add 20% nulls to all enum lists
    PERM_VAL.DOSAGE_UNITS = add_nulls(PERM_VAL.DOSAGE_UNITS)
    PERM_VAL.DRUG_REFERENCE_DB = add_nulls(PERM_VAL.DRUG_REFERENCE_DB)

    drug_dose_units = factory.Faker("random_element", elements=PERM_VAL.DOSAGE_UNITS)
    null_drug_dose = twenty_percent_true()
    prescribed_cumulative_drug_dose = factory.Maybe("null_drug_dose",
                                                    None,
                                                    factory.Faker("pyfloat", left_digits=2, right_digits=1,
                                                                  positive=True, min_value=20, max_value=50))
    actual_cumulative_drug_dose = factory.Maybe("null_drug_dose",
                                                None,
                                                factory.Faker("pyfloat", left_digits=2, right_digits=1,
                                                              positive=True, min_value=51, max_value=100))
    systemic_therapy_type = factory.Faker("random_element", elements=PERM_VAL.SYSTEMIC_THERAPY_TYPE)
    start_date = None
    end_date = None

    # set foreign keys
    program_id = factory.SelfAttribute("treatment_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("treatment_uuid.submitter_donor_id")
    donor_uuid = factory.SelfAttribute("treatment_uuid.donor_uuid")
    submitter_treatment_id = factory.SelfAttribute(
        "treatment_uuid.submitter_treatment_id"
    )
    treatment_uuid = factory.SubFactory(TreatmentFactory)

    @factory.post_generation
    def add_dates(self, create, extracted, **kwargs):
        if twenty_percent_true():
            pass
        else:
            treatment = self.treatment_uuid
            if treatment.treatment_start_date and treatment.treatment_end_date:
                self.start_date = {"day_interval": random.randint(
                    treatment.treatment_start_date['day_interval'], treatment.treatment_end_date['day_interval'])}
                self.start_date["month_interval"] = days_to_months(self.start_date["day_interval"])
            elif treatment.treatment_start_date:
                self.start_date = {"day_interval": random.randint(
                    treatment.treatment_start_date['day_interval'], treatment.treatment_start_date['day_interval'] + 50)}
                self.start_date["month_interval"] = days_to_months(self.start_date["day_interval"])
            elif treatment.treatment_end_date:
                self.start_date = {"day_interval": random.randint(
                    treatment.treatment_end_date['day_interval'] - 50,
                    treatment.treatment_end_date['day_interval'])}
                self.start_date["month_interval"] = days_to_months(self.start_date["day_interval"])
            if twenty_percent_true():
                pass
            else:
                if treatment.treatment_end_date:
                    self.end_date = {"day_interval": random.randint(
                        self.start_date["day_interval"], treatment.treatment_end_date['day_interval'])}
                    self.end_date["month_interval"] = days_to_months(self.end_date["day_interval"])

    @factory.post_generation
    def add_systemic_therapy_treatment_type(self, create, extracted, **kwargs):
        treatment = self.treatment_uuid
        if treatment.treatment_type == [None] or treatment.treatment_type == None:
            treatment.treatment_type = ["Systemic therapy"]
        elif "Systemic therapy" not in treatment.treatment_type:
            treatment.treatment_type.append("Systemic therapy")
        if "No treatment" in treatment.treatment_type:
            treatment.treatment_type.remove("No treatment")

    @factory.post_generation
    def add_drug_info(self, create, extracted, **kwargs):
        if twenty_percent_true():
            pass
        else:
            self.drug_reference_database = random.choice(PERM_VAL.DRUG_REFERENCE_DB)
            if self.drug_reference_database:
                if self.systemic_therapy_type == "Chemotherapy":
                    self.drug_name = random.choice(list(SYNTH_VAL.CHEMO_DRUGS.keys()))
                    if self.drug_name:
                        self.drug_reference_identifier = SYNTH_VAL.CHEMO_DRUGS[self.drug_name][self.drug_reference_database]
                elif self.systemic_therapy_type == "Hormone therapy":
                    self.drug_name = random.choice(list(SYNTH_VAL.HORMONE_DRUGS.keys()))
                    if self.drug_name:
                        self.drug_reference_identifier = SYNTH_VAL.HORMONE_DRUGS[self.drug_name][self.drug_reference_database]
                elif self.systemic_therapy_type == "Immunotherapy":
                    self.drug_name = random.choice(list(SYNTH_VAL.IMMUNO_DRUGS.keys()))
                    if self.drug_name:
                        self.drug_reference_identifier = SYNTH_VAL.IMMUNO_DRUGS[self.drug_name][self.drug_reference_database]


class RadiationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Radiation
        exclude = ("null_dosage_fraction")

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)

    # add 20% nulls to all enum lists
    PERM_VAL.RADIATION_THERAPY_MODALITY = add_nulls(PERM_VAL.RADIATION_THERAPY_MODALITY)
    PERM_VAL.RADIATION_ANATOMICAL_SITE = add_nulls(PERM_VAL.RADIATION_ANATOMICAL_SITE)

    radiation_therapy_modality = factory.Faker(
        "random_element", elements=PERM_VAL.RADIATION_THERAPY_MODALITY
    )
    radiation_therapy_type = factory.Faker(
        "random_element", elements=["External", "Internal", None]
    )
    null_dosage_fraction = twenty_percent_true()
    radiation_therapy_fractions = factory.Maybe("null_dosage_fraction",
                                                None,
                                                factory.Faker("random_int", min=1, max=30))
    radiation_therapy_dosage = factory.Maybe("null_dosage_fraction",
                                             None,
                                             factory.Faker("random_int", min=1, max=100))
    anatomical_site_irradiated = factory.Faker(
        "random_element", elements=PERM_VAL.RADIATION_ANATOMICAL_SITE
    )
    radiation_boost = False
    reference_radiation_treatment_id = None

    # set foreign keys
    program_id = factory.SelfAttribute("treatment_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("treatment_uuid.submitter_donor_id")
    donor_uuid = factory.SelfAttribute("treatment_uuid.donor_uuid")
    submitter_treatment_id = factory.SelfAttribute(
        "treatment_uuid.submitter_treatment_id"
    )
    treatment_uuid = factory.SubFactory(TreatmentFactory)

    @factory.post_generation
    def add_radiation_treatment_type(self, create, extracted, **kwargs):
        treatment = self.treatment_uuid
        if "Radiation therapy" not in treatment.treatment_type:
            treatment.treatment_type.append("Radiation therapy")
        if "No treatment" in treatment.treatment_type:
            treatment.treatment_type.remove("No treatment")


class SurgeryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Surgery
        exclude = ("null_dimensions", "null_margin_types")

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)

    # add 20% nulls
    PERM_VAL.SURGERY_LOCATION = add_nulls(PERM_VAL.SURGERY_LOCATION)
    PERM_VAL.TUMOUR_FOCALITY = add_nulls(PERM_VAL.TUMOUR_FOCALITY)
    PERM_VAL.TUMOUR_CLASSIFICATION = add_nulls(PERM_VAL.TUMOUR_CLASSIFICATION)
    PERM_VAL.LYMPHOVACULAR_INVASION = add_nulls(PERM_VAL.LYMPHOVACULAR_INVASION)
    PERM_VAL.PERINEURAL_INVASION = add_nulls(PERM_VAL.PERINEURAL_INVASION)

    surgery_reference_database = None
    surgery_reference_identifier = None
    surgery_type = None
    surgery_site = factory.Faker("random_element", elements=PERM_VAL.TOPOGRAPHY_CODES)
    surgery_location = factory.Faker(
        "random_element", elements=PERM_VAL.SURGERY_LOCATION
    )
    null_dimensions = twenty_percent_true()
    tumour_length = factory.Maybe("null_dimensions",
                                  None,
                                  factory.Faker("random_int", min=1, max=10))
    tumour_width = factory.Maybe("null_dimensions",
                                 None,
                                 factory.Faker("random_int", min=1, max=10))
    greatest_dimension_tumour = factory.Maybe("null_dimensions",
                                              None,
                                              factory.Faker("random_int", min=1, max=10))
    tumour_focality = factory.Faker("random_element", elements=PERM_VAL.TUMOUR_FOCALITY)
    residual_tumour_classification = factory.Faker("random_element", elements=PERM_VAL.TUMOUR_CLASSIFICATION)
    null_margin_types = twenty_percent_true()
    margin_types_involved = factory.Maybe(
        "null_margin_type",
        None,
        factory.Faker("random_elements",
                      elements=PERM_VAL.MARGIN_TYPES,
                      length=random.randint(1, 3),
                      unique=True))
    margin_types_not_involved = factory.Maybe(
        "null_margin_type",
        None,
        factory.Faker(
            "random_elements",
            elements=PERM_VAL.MARGIN_TYPES,
            length=random.randint(1, 3),
            unique=True))
    margin_types_not_assessed = factory.Maybe(
        "null_margin_type",
        None,
        factory.Faker(
            "random_elements",
            elements=PERM_VAL.MARGIN_TYPES,
            length=random.randint(1, 3),
            unique=True))
    lymphovascular_invasion = factory.Faker("random_element", elements=PERM_VAL.LYMPHOVACULAR_INVASION)
    perineural_invasion = factory.Faker("random_element", elements=PERM_VAL.PERINEURAL_INVASION)
    # submitter_specimen_id = None

    # set foreign keys
    program_id = factory.SelfAttribute("treatment_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("treatment_uuid.submitter_donor_id")
    donor_uuid = factory.SelfAttribute("treatment_uuid.donor_uuid")
    submitter_treatment_id = factory.SelfAttribute(
        "treatment_uuid.submitter_treatment_id"
    )
    treatment_uuid = factory.SubFactory(TreatmentFactory)

    @factory.post_generation
    def add_surgery_type(self, create, extracted, **kwargs):
        if twenty_percent_true():
            pass
        else:
            self.surgery_type = random.choice(list(SYNTH_VAL.SURGERY_TYPE.keys()))
            if self.surgery_type:
                self.surgery_reference_database = random.choice(list(SYNTH_VAL.SURGERY_TYPE[self.surgery_type].keys()))
                if self.surgery_reference_database:
                    self.surgery_reference_identifier = SYNTH_VAL.SURGERY_TYPE[self.surgery_type][self.surgery_reference_database]

    @factory.post_generation
    def add_surgery_treatment_type(self, create, extracted, **kwargs):
        treatment = self.treatment_uuid
        if "Surgery" not in treatment.treatment_type:
            treatment.treatment_type.append("Surgery")
        if "No treatment" in treatment.treatment_type:
            treatment.treatment_type.remove("No treatment")


class FollowUpFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FollowUp
        exclude = ("fill_pd", )

    # default values
    submitter_follow_up_id = factory.Sequence(lambda n: f"FOLLOW_UP_{str(n).zfill(4)}")
    date_of_followup = None
    disease_status_at_followup = factory.Faker(
        "random_element", elements=PERM_VAL.DISEASE_STATUS_FOLLOWUP
    )
    relapse_type = None
    date_of_relapse = None
    method_of_progression_status = factory.Faker(
        "random_elements",
        elements=PERM_VAL.PROGRESSION_STATUS_METHOD,
        length=random.randint(1, 5),
        unique=True,
    )
    anatomic_site_progression_or_recurrence = None

    # set foreign keys
    program_id = factory.SelfAttribute("donor_uuid.program_id")
    donor_uuid = factory.SubFactory(DonorFactory)
    submitter_donor_id = factory.SelfAttribute("donor_uuid.submitter_donor_id")

    fill_pd = factory.Faker("pybool",)
    primary_diagnosis_uuid = factory.Maybe(
        "fill_pd",
        yes_declaration=factory.SubFactory(PrimaryDiagnosisFactory),
        no_declaration=None
    )
    submitter_primary_diagnosis_id = factory.Maybe(
        "fill_pd",
        yes_declaration=factory.SelfAttribute(
            "primary_diagnosis_uuid.submitter_primary_diagnosis_id"),
        no_declaration=None
    )
    submitter_treatment_id = factory.SelfAttribute(
        "treatment_uuid.submitter_treatment_id")
    treatment_uuid = factory.SubFactory(TreatmentFactory)

    @factory.post_generation
    def set_relapse_type_date(self, create, extracted, **kwargs):
        if twenty_percent_true():
            pass
        elif self.disease_status_at_followup in ['Distant progression', 'Loco-regional progression',
                                               'Progression not otherwise specified']:
            donor = self.donor_uuid
            self.relapse_type = random.choice(PERM_VAL.RELAPSE_TYPE)
            if donor.date_of_death:
                relapse_day_int = random.randint(0, donor.date_of_death['day_interval'])
                relapse_month_int = days_to_months(relapse_day_int)
                self.date_of_relapse = {'day_interval': relapse_day_int,
                                        'month_interval': relapse_month_int}
            else:
                relapse_day_int = random.randint(0, 32850)
                relapse_month_int = days_to_months(relapse_day_int)
                self.date_of_relapse = {'day_interval': relapse_day_int,
                                        'month_interval': relapse_month_int}

    @factory.post_generation
    def correct_linkage(self, create, extracted, **kwargs):
        """ Link to either PD or Treatment, not both, 20% link only to Donor"""
        if twenty_percent_true():
            self.submitter_primary_diagnosis_id = None
            self.submitter_treatment_id = None
        elif self.submitter_primary_diagnosis_id:
            self.submitter_treatment_id = None


class BiomarkerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Biomarker
        exclude = ("null_hpv_strain", )

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)

    # add 20% null values to enums
    PERM_VAL.ER_PR_HPV_STATUS = add_nulls(PERM_VAL.ER_PR_HPV_STATUS)
    PERM_VAL.HER2_STATUS = add_nulls(PERM_VAL.HER2_STATUS)

    test_date = None
    psa_level = factory.Faker("pyfloat", min_value=0, max_value=20, right_digits=1)
    ca125 = factory.Faker("pyfloat", min_value=0, max_value=50, right_digits=1)
    cea = factory.Faker("pyfloat", min_value=0, max_value=10, right_digits=1)
    er_status = factory.Faker("random_element", elements=PERM_VAL.ER_PR_HPV_STATUS)
    er_percent_positive = None
    pr_status = factory.Faker("random_element", elements=PERM_VAL.ER_PR_HPV_STATUS)
    pr_percent_positive = None
    her2_ihc_status = factory.Faker("random_element", elements=PERM_VAL.HER2_STATUS)
    her2_ish_status = factory.Faker("random_element", elements=PERM_VAL.HER2_STATUS)
    hpv_ihc_status = factory.Faker("random_element", elements=PERM_VAL.ER_PR_HPV_STATUS)
    hpv_pcr_status = factory.Faker("random_element", elements=PERM_VAL.ER_PR_HPV_STATUS)
    null_hpv_strain = twenty_percent_true()
    hpv_strain = factory.Maybe("null_hpv_strain",
                               None,
                               factory.Faker(
                                   "random_elements",
                                   elements=PERM_VAL.HPV_STRAIN,
                                   length=random.randint(1, 5),
                                   unique=True,
                               ))
    # TODO: figure out how to link to objects below
    submitter_specimen_id = None
    submitter_primary_diagnosis_id = None
    submitter_treatment_id = None
    submitter_follow_up_id = None

    # set foreign keys
    program_id = factory.SelfAttribute("donor_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("donor_uuid.submitter_donor_id")
    donor_uuid = factory.SubFactory(DonorFactory)

    @factory.post_generation
    def set_date(self, create, extracted, **kwargs):
        donor = self.donor_uuid
        if twenty_percent_true():
            self.test_date = None
        elif donor.date_of_death and donor.date_of_birth:
            test_day_int = random.randint(donor.date_of_birth['day_interval'], donor.date_of_death['day_interval'])
            test_month_int = days_to_months(test_day_int)
            self.test_date = {'day_interval': test_day_int,
                              'month_interval': test_month_int}
        elif donor.date_of_birth:
            test_day_int = random.randint(donor.date_of_birth['day_interval'], 32850)
            test_month_int = days_to_months(test_day_int)
            self.test_date = {'day_interval': test_day_int,
                              'month_interval': test_month_int}
        else:
            test_day_int = random.randint(7500, 32850)
            test_month_int = days_to_months(test_day_int)
            self.test_date = {'day_interval': test_day_int,
                              'month_interval': test_month_int}

    @factory.post_generation
    def set_percents(self, create, extracted, **kwargs):
        if self.er_status in ["Cannot be determined", "Negative", "Not applicable", "Unknown"]:
            self.er_percent_positive = None
        else:
            self.er_percent_positive = round(random.random() * 100, 2)
        if self.pr_status in ["Cannot be determined", "Negative", "Not applicable", "Unknown"]:
            self.pr_percent_positive = None
        else:
            self.pr_percent_positive = round(random.random() * 100, 2)

    # @factory.post_generation
    # def set_linkage(self, create, extracted, **kwargs):
    #     linked_event = random.choice(['specimen', 'primary_diagnosis', 'treatment', None])
    #     biomarker = self
    #     # if biomarker.submitter_treatment_id:
    #     #     treatment = biomarker.submitter_treatment_id
    #     #     biomarker.submitter_treatment_id = treatment.submitter_treatment_id
    #     # if biomarker.submitter_primary_diagnosis_id:
    #     #     pd = biomarker.submitter_primary_diagnosis_id
    #     #     biomarker.submitter_primary_diagnosis_id = pd.submitter_treatment_id
    #     if linked_event == "specimen":
    #         specimen = self.specimen_uuid
    #         biomarker.submitter_specimen_id = specimen.submitter_specimen_id
    #     biomarker.save()


class ComorbidityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comorbidity

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)
    prior_malignancy = None
    laterality_of_prior_malignancy = None
    age_at_comorbidity_diagnosis = None
    comorbidity_type_code = factory.Faker("random_element", elements=SYNTH_VAL.ALL_CODES)
    comorbidity_treatment_status = None
    comorbidity_treatment = None

    # set foreign keys
    program_id = factory.SelfAttribute("donor_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("donor_uuid.submitter_donor_id")
    donor_uuid = factory.SubFactory(DonorFactory)

    @factory.post_generation
    def set_priors(self, create, extracted, **kwargs):
        comorbidity = self
        donor = self.donor_uuid
        cancer_treatments = ["Chemotherapy", "Hormone therapy", "Immunotherapy", "Radiation"]
        if donor.date_of_birth:
            age_at_diagnosis = math.floor(donor.date_of_birth['month_interval'] / -12)
        if comorbidity.comorbidity_type_code in SYNTH_VAL.CANCER_CODES:
            comorbidity.laterality_of_prior_malignancy = random.choice(PERM_VAL.MALIGNANCY_LATERALITY)
            if donor.date_of_birth:
                comorbidity.age_at_comorbidity_diagnosis = random.randint(10, age_at_diagnosis)
            comorbidity.prior_malignancy = 'Yes'
            comorbidity.comorbidity_treatment_status = random.choice(PERM_VAL.UBOOLEAN)
            if comorbidity.comorbidity_treatment_status == "Yes":
                comorbidity.comorbidity_treatment = random.choice(cancer_treatments)
        elif comorbidity.comorbidity_type_code:
            comorbidity.comorbidity_treatment_status = random.choice(PERM_VAL.UBOOLEAN)
            if donor.date_of_birth:
                comorbidity.age_at_comorbidity_diagnosis = random.randint(10, age_at_diagnosis)
        comorbidity.save()


class ExposureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exposure

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)
    tobacco_smoking_status = factory.Faker(
        "random_element", elements=PERM_VAL.SMOKING_STATUS
    )
    tobacco_type = None
    pack_years_smoked = None
    # set foreign keys
    program_id = factory.SelfAttribute("donor_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("donor_uuid.submitter_donor_id")
    donor_uuid = factory.SubFactory(DonorFactory)

    @factory.post_generation
    def set_smoking_information(self, create, extracted, **kwargs):
        if twenty_percent_true():
            pass
        elif self.tobacco_smoking_status:
            if self.tobacco_smoking_status not in ["Not applicable", "Smoking history not documented",
                                                   "Lifelong non-smoker (<100 cigarettes smoked in lifetime)"]:
                self.tobacco_type = random.choices(PERM_VAL.TOBACCO_TYPE, k=random.randint(1, 3))
                if self.tobacco_smoking_status == "Current reformed smoker, duration not specified":
                    self.pack_years_smoked = None
                else:
                    self.pack_years_smoked = random.randint(5, 70)
