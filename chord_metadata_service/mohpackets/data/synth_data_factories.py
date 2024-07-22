import random
import uuid
import math

import factory

import chord_metadata_service.mohpackets.permissible_values as PERM_VAL
import chord_metadata_service.mohpackets.data.synth_data_values as SYNTH_VAL

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
    days_to_months
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

