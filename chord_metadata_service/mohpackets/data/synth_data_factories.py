import random
import math

import factory

import chord_metadata_service.mohpackets.permissible_values as PERM_VAL
import synth_data_values as SYNTH_VAL

from chord_metadata_service.mohpackets.tests.endpoints.factories import (
    BiomarkerFactory,
    DonorFactory,
    PrimaryDiagnosisFactory,
    RadiationFactory,
    SampleRegistrationFactory,
    SpecimenFactory,
    SurgeryFactory,
    SystemicTherapyFactory,
    TreatmentFactory,
)


#######################
## Utility functions ##
#######################


def twenty_percent_true():
    """ Generate True 20% of the time. """
    return random.randrange(100) < 20


def add_nulls(complete_list: list, prop=0.2):
    """ Returns a list with 20% of the list as 'None' """
    num_nulls = math.ceil(len(complete_list) * prop)
    complete_list.extend([None] * num_nulls)
    return complete_list


class SynthDonorFactory(DonorFactory):
    class Meta:
        exclude = ("fill_dob", "null_percent")

    PERM_VAL.GENDER = add_nulls(PERM_VAL.GENDER)
    PERM_VAL.SEX_AT_BIRTH = add_nulls(PERM_VAL.SEX_AT_BIRTH)

    fill_dob = factory.Faker("pybool", truth_probability=80)
    date_of_birth = factory.Maybe(
        "fill_dob",
        yes_declaration=factory.LazyFunction(lambda: {
            "day_interval": random.randint(-21900, -18220),
        }),
        no_declaration=None
    )


class SynthPrimaryDiagnosisFactory(PrimaryDiagnosisFactory):
    class Meta:
        exclude = ("fill_dod")

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
    primary_site = factory.Iterator(SYNTH_VAL.PRIMARY_SITE)


class SynthSpecimenFactory(SpecimenFactory):
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


class SynthSampleRegistrationFactory(SampleRegistrationFactory):
    # add 20% nulls to all enum lists
    PERM_VAL.SPECIMEN_TISSUE_SOURCE = add_nulls(PERM_VAL.SPECIMEN_TISSUE_SOURCE)
    PERM_VAL.SPECIMEN_TYPE = add_nulls(PERM_VAL.SPECIMEN_TYPE)
    PERM_VAL.SAMPLE_TYPE = add_nulls(PERM_VAL.SAMPLE_TYPE)


class SynthTreatmentFactory(TreatmentFactory):
    # add 20% nulls to all enum lists
    PERM_VAL.TREATMENT_INTENT = add_nulls(PERM_VAL.TREATMENT_INTENT)
    PERM_VAL.TREATMENT_RESPONSE_METHOD = add_nulls(PERM_VAL.TREATMENT_RESPONSE_METHOD)
    PERM_VAL.TREATMENT_RESPONSE = add_nulls(PERM_VAL.TREATMENT_RESPONSE)
    PERM_VAL.TREATMENT_STATUS = add_nulls(PERM_VAL.TREATMENT_STATUS)


class SynthSystemicTherapyFactory(SystemicTherapyFactory):
    class Meta:
        exclude = ("null_drug_dose", )

    # add 20% nulls to all enum lists

    PERM_VAL.DOSAGE_UNITS = add_nulls(PERM_VAL.DOSAGE_UNITS)
    PERM_VAL.DRUG_REFERENCE_DB = add_nulls(PERM_VAL.DRUG_REFERENCE_DB)

    null_drug_dose = factory.LazyFunction(lambda: random.random() > 0.15)
    prescribed_cumulative_drug_dose = factory.Maybe("null_drug_dose",
                                                    None,
                                                    factory.Faker("pyfloat", left_digits=2, right_digits=1,
                                                                  positive=True, min_value=20, max_value=50))
    actual_cumulative_drug_dose = factory.Maybe("null_drug_dose",
                                                None,
                                                factory.Faker("pyfloat", left_digits=2, right_digits=1,
                                                              positive=True, min_value=51, max_value=100))


class SynthRadiationFactory(RadiationFactory):
    class Meta:
        exclude = ("null_dosage_fraction")

    # add 20% nulls to all enum lists
    PERM_VAL.RADIATION_THERAPY_MODALITY = add_nulls(PERM_VAL.RADIATION_THERAPY_MODALITY)
    PERM_VAL.RADIATION_ANATOMICAL_SITE = add_nulls(PERM_VAL.RADIATION_ANATOMICAL_SITE)


class SynthSurgeryFactory(SurgeryFactory):
    class Meta:
        exclude = ("null_dimensions", "null_margin_types")

    # add 20% nulls
    PERM_VAL.SURGERY_LOCATION = add_nulls(PERM_VAL.SURGERY_LOCATION)
    PERM_VAL.TUMOUR_FOCALITY = add_nulls(PERM_VAL.TUMOUR_FOCALITY)
    PERM_VAL.TUMOUR_CLASSIFICATION = add_nulls(PERM_VAL.TUMOUR_CLASSIFICATION)
    PERM_VAL.LYMPHOVACULAR_INVASION = add_nulls(PERM_VAL.LYMPHOVACULAR_INVASION)
    PERM_VAL.PERINEURAL_INVASION = add_nulls(PERM_VAL.PERINEURAL_INVASION)

    null_dimensions = factory.LazyFunction(lambda: random.random() > 0.15)
    tumour_length = factory.Maybe("null_dimensions",
                                  None,
                                  factory.Faker("random_int", min=1, max=10))
    tumour_width = factory.Maybe("null_dimensions",
                                 None,
                                 factory.Faker("random_int", min=1, max=10))
    greatest_dimension_tumour = factory.Maybe("null_dimensions",
                                              None,
                                              factory.Faker("random_int", min=1, max=10))
    null_margin_types = factory.LazyFunction(lambda: random.random() > 0.15)
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


class SynthBiomarkerFactory(BiomarkerFactory):
    class Meta:
        exclude = ("null_hpv_strain",)

    # add 20% null values to enums
    PERM_VAL.ER_PR_HPV_STATUS = add_nulls(PERM_VAL.ER_PR_HPV_STATUS)
    PERM_VAL.HER2_STATUS = add_nulls(PERM_VAL.HER2_STATUS)

    null_hpv_strain = factory.LazyFunction(lambda: random.random() > 0.15)
    hpv_strain = factory.Maybe("null_hpv_strain",
                               None,
                               factory.Faker(
                                   "random_elements",
                                   elements=PERM_VAL.HPV_STRAIN,
                                   length=random.randint(1, 5),
                                   unique=True,
                               ))


