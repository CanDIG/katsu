import random
import uuid

import factory

import chord_metadata_service.mohpackets.permissible_values as PERM_VAL
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

# ICD disease codes, not all are correct but will match regex in model
c_codes = ['C' + str(x).rjust(2, '0') for x in list(range(0, 97))]
d_codes = ['D' + str(x).rjust(2, '0') for x in list(range(0, 9)) + list(range(37, 48))]
cancer_codes = c_codes + d_codes
# some codes from diseases of the circulatory system, diseases of the blood
non_cancer_codes = ['D' + str(x) for x in list(range(50, 89)) + list(range(37, 48))] + \
                       ['I' + str(x).rjust(2, '0') for x in list(range(0, 99))]

# Systemic Therapy Drugs
chemotherapy_drugs = {
    "Methotrexate": {"RxNorm": "6851",
                     "PubChem": "126941",
                     "NCI Thesaurus": "C642"},
    "Fludarabine": {"RxNorm": "24698",
                    "PubChem": "657237",
                    "NCI Thesaurus": "C1094"},
    "Carboplatin": {"RxNorm": "40048",
                    "PubChem": "426756",
                    "NCI Thesaurus": "C1282"},
    "Idarubicin": {"RxNorm": "5650",
                   "PubChem": "42890",
                   "NCI Thesaurus": "C562"},
    "Paclitaxel": {"RxNorm": "56946",
                   "PubChem": "36314",
                   "NCI Thesaurus": "C1411"}

}

immunotherapy_drugs = {
    "Atezolizumab": {"RxNorm": "1792776",
                     "PubChem": "469690927",
                     "NCI Thesaurus": "C106250"},
    "Durvalumab": {"RxNorm": "1919503",
                   "PubChem": "481101604",
                   "NCI Thesaurus": "C103194"},
    "Nivolumab": {"RxNorm": "1597876",
                  "PubChem": "469753496",
                  "NCI Thesaurus": "C68814"},
    "Pembrolizumab": {"RxNorm": "1547545",
                      "PubChem": "469691028",
                      "NCI Thesaurus": "C106432"},
    "Ipilimumab": {"RxNorm": "1094833",
                   "PubChem": "472634117",
                   "NCI Thesaurus": "C2654"}

}

hormone_therapy_drugs = {
    "Tamoxifen": {"RxNorm": "1792776",
                  "PubChem": "469690927",
                  "NCI Thesaurus": "C106250"},
    "Fluoxymesterone": {"RxNorm": "1919503",
                        "PubChem": "481101604",
                        "NCI Thesaurus": "C103194"},
    "Diethylstilbestrol": {"RxNorm": "1597876",
                           "PubChem": "469753496",
                           "NCI Thesaurus": "C68814"},
    "Buserelin": {"RxNorm": "1547545",
                  "PubChem": "469691028",
                  "NCI Thesaurus": "C106432"},
    "Degarelix": {"RxNorm": "1094833",
                  "PubChem": "472634117",
                  "NCI Thesaurus": "C2654"}
}


def days_to_months(day_interval):
    return int(math.floor(day_interval * 0.032855))


class ProgramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Program
        # django_get_or_create = ("program_id",)

    # default values
    program_id = factory.Sequence(lambda n: "PROGRAM_%d" % n)


class DonorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Donor
        # django_get_or_create = ("submitter_donor_id",)

    # default values
    submitter_donor_id = factory.Sequence(lambda n: "DONOR_%d" % n)
    gender = factory.Faker("random_element", elements=PERM_VAL.GENDER)
    sex_at_birth = factory.Faker("random_element", elements=PERM_VAL.SEX_AT_BIRTH)
    is_deceased = factory.Faker("boolean")
    lost_to_followup_reason = factory.Faker(
        "random_element", elements=PERM_VAL.LOST_TO_FOLLOWUP_REASON
    )
    lost_to_followup_after_clinical_event_identifier = None
    date_alive_after_lost_to_followup = None
    cause_of_death = factory.Maybe(
        "is_deceased",
        yes_declaration=factory.Faker(
            "random_element", elements=PERM_VAL.CAUSE_OF_DEATH
        ),
        no_declaration=None,
    )
    date_of_birth = factory.LazyFunction(
        lambda: {
            "month_interval": random.randint(0, 1000),
            "day_interval": random.randint(0, 3000),
        }
    )
    date_of_death = factory.Maybe(
        "is_deceased",
        yes_declaration=factory.LazyFunction(
            lambda: {
                "month_interval": random.randint(0, 1000),
                "day_interval": random.randint(0, 3000),
            }
        ),
        no_declaration=None,
    )

    # set foregin key
    program_id = factory.SubFactory(ProgramFactory)


class PrimaryDiagnosisFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PrimaryDiagnosis
        # django_get_or_create = ("submitter_primary_diagnosis_id",)

    # Default values
    submitter_primary_diagnosis_id = factory.Sequence(lambda n: "DIAG_%d" % n)
    date_of_diagnosis = factory.LazyFunction(
        lambda: {
            "month_interval": random.randint(0, 1000),
            "day_interval": random.randint(0, 3000),
        }
    )
    cancer_type_code = factory.Faker("uuid4")
    basis_of_diagnosis = factory.Faker(
        "random_element", elements=PERM_VAL.BASIS_OF_DIAGNOSIS
    )
    laterality = factory.Faker(
        "random_element", elements=PERM_VAL.PRIMARY_DIAGNOSIS_LATERALITY
    )
    clinical_tumour_staging_system = factory.Faker(
        "random_element", elements=PERM_VAL.TUMOUR_STAGING_SYSTEM
    )
    clinical_t_category = factory.Faker("random_element", elements=PERM_VAL.T_CATEGORY)
    clinical_n_category = factory.Faker("random_element", elements=PERM_VAL.N_CATEGORY)
    clinical_m_category = factory.Faker("random_element", elements=PERM_VAL.M_CATEGORY)
    clinical_stage_group = factory.Faker(
        "random_element", elements=PERM_VAL.STAGE_GROUP
    )
    primary_site = factory.Faker(
        "random_element",
        elements=PERM_VAL.PRIMARY_SITE,
    )
    pathological_tumour_staging_system = factory.Faker(
        "random_element", elements=PERM_VAL.TUMOUR_STAGING_SYSTEM
    )
    pathological_t_category = factory.Faker(
        "random_element", elements=PERM_VAL.T_CATEGORY
    )
    pathological_n_category = factory.Faker(
        "random_element", elements=PERM_VAL.N_CATEGORY
    )
    pathological_m_category = factory.Faker(
        "random_element", elements=PERM_VAL.M_CATEGORY
    )
    pathological_stage_group = factory.Faker(
        "random_element", elements=PERM_VAL.STAGE_GROUP
    )

    # Set the foreign keys
    program_id = factory.SelfAttribute("donor_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("donor_uuid.submitter_donor_id")
    donor_uuid = factory.SubFactory(DonorFactory)

    @factory.post_generation
    def set_clinical_event_identifier(self, create, extracted, **kwargs):
        donor = self.donor_uuid
        if not donor.is_deceased:
            donor.lost_to_followup_after_clinical_event_identifier = (
                self.submitter_primary_diagnosis_id
            )
            donor.lost_to_followup_reason = random.choice(
                PERM_VAL.LOST_TO_FOLLOWUP_REASON
            )
            donor.date_alive_after_lost_to_followup = {
                "month_interval": random.randint(0, 1000),
                "day_interval": random.randint(0, 3000),
            }
            donor.save()


class SpecimenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Specimen
        # django_get_or_create = ("submitter_specimen_id",)

    # default values
    submitter_specimen_id = factory.Sequence(lambda n: "SPECIMEN_%d" % n)

    specimen_collection_date = None
    specimen_storage = factory.Faker("random_element", elements=PERM_VAL.STORAGE)
    specimen_processing = factory.Faker(
        "random_element", elements=PERM_VAL.SPECIMEN_PROCESSING
    )
    tumour_histological_type = None
    specimen_anatomic_location = None
    specimen_laterality = factory.Faker(
        "random_element", elements=PERM_VAL.SPECIMEN_LATERALITY
    )
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

    # set foregin keys
    program_id = factory.SelfAttribute("primary_diagnosis_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute(
        "primary_diagnosis_uuid.submitter_donor_id"
    )
    donor_uuid = factory.SelfAttribute("primary_diagnosis_uuid.donor_uuid")
    submitter_primary_diagnosis_id = factory.SelfAttribute(
        "primary_diagnosis_uuid.submitter_primary_diagnosis_id"
    )
    primary_diagnosis_uuid = factory.SubFactory(PrimaryDiagnosisFactory)


class SampleRegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SampleRegistration
        # django_get_or_create = ("submitter_sample_id",)

    # default values
    submitter_sample_id = factory.Sequence(lambda n: "SAMPLE_%d" % n)
    specimen_tissue_source = factory.Faker(
        "random_element", elements=PERM_VAL.SPECIMEN_TISSUE_SOURCE
    )
    tumour_normal_designation = factory.Faker(
        "random_element", elements=["Normal", "Tumour"]
    )
    specimen_type = factory.Faker("random_element", elements=PERM_VAL.SPECIMEN_TYPE)
    sample_type = factory.Faker("random_element", elements=PERM_VAL.SAMPLE_TYPE)

    # set foregin keys
    program_id = factory.SelfAttribute("specimen_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("specimen_uuid.submitter_donor_id")
    donor_uuid = factory.SelfAttribute("specimen_uuid.donor_uuid")
    submitter_specimen_id = factory.SelfAttribute("specimen_uuid.submitter_specimen_id")
    specimen_uuid = factory.SubFactory(SpecimenFactory)


class TreatmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Treatment
        # django_get_or_create = ("submitter_treatment_id",)

    # default values
    submitter_treatment_id = factory.Sequence(lambda n: "TREATMENT_%d" % n)
    treatment_type = factory.Faker(
        "random_elements",
        elements=PERM_VAL.TREATMENT_TYPE,
        length=random.randint(1, 5),
        unique=True,
    )
    is_primary_treatment = factory.Faker("random_element", elements=["Yes", "No"])
    treatment_start_date = None
    treatment_end_date = None
    treatment_intent = factory.Faker(
        "random_element", elements=PERM_VAL.TREATMENT_INTENT
    )
    response_to_treatment_criteria_method = factory.Faker(
        "random_element", elements=PERM_VAL.TREATMENT_RESPONSE_METHOD
    )
    response_to_treatment = factory.Faker(
        "random_element", elements=PERM_VAL.TREATMENT_RESPONSE
    )
    status_of_treatment = factory.Faker(
        "random_element", elements=PERM_VAL.TREATMENT_STATUS
    )

    # set foregin keys
    program_id = factory.SelfAttribute("primary_diagnosis_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute(
        "primary_diagnosis_uuid.submitter_donor_id"
    )
    donor_uuid = factory.SelfAttribute("primary_diagnosis_uuid.donor_uuid")
    submitter_primary_diagnosis_id = factory.SelfAttribute(
        "primary_diagnosis_uuid.submitter_primary_diagnosis_id"
    )
    primary_diagnosis_uuid = factory.SubFactory(PrimaryDiagnosisFactory)


class SystemicTherapyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SystemicTherapy

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)
    systemic_therapy_type = factory.Faker(
        "random_element", elements=PERM_VAL.SYSTEMIC_THERAPY_TYPE
    )
    days_per_cycle = factory.Faker("random_int", min=1, max=30)
    number_of_cycles = factory.Faker("random_int", min=1, max=10)
    start_date = None
    end_date = None
    drug_reference_database = factory.Faker(
        "random_element", elements=PERM_VAL.DRUG_REFERENCE_DB
    )
    drug_name = factory.Faker("word")
    drug_reference_identifier = factory.Faker("word")
    drug_dose_units = factory.Faker("random_element", elements=PERM_VAL.DOSAGE_UNITS)
    prescribed_cumulative_drug_dose = factory.Faker(
        "pyfloat",
        left_digits=2,
        right_digits=1,
        positive=True,
        min_value=20,
        max_value=50,
    )
    actual_cumulative_drug_dose = factory.Faker(
        "pyfloat",
        left_digits=2,
        right_digits=1,
        positive=True,
        min_value=51,
        max_value=100,
    )

    # set foregin keys
    program_id = factory.SelfAttribute("treatment_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("treatment_uuid.submitter_donor_id")
    donor_uuid = factory.SelfAttribute("treatment_uuid.donor_uuid")
    submitter_treatment_id = factory.SelfAttribute(
        "treatment_uuid.submitter_treatment_id"
    )
    treatment_uuid = factory.SubFactory(TreatmentFactory)


class RadiationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Radiation

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)
    radiation_therapy_modality = factory.Faker(
        "random_element", elements=PERM_VAL.RADIATION_THERAPY_MODALITY
    )
    radiation_therapy_type = factory.Faker(
        "random_element", elements=["External", "Internal"]
    )
    radiation_therapy_fractions = factory.Faker("random_int", min=1, max=30)
    radiation_therapy_dosage = factory.Faker("random_int", min=1, max=100)
    anatomical_site_irradiated = factory.Faker(
        "random_element", elements=PERM_VAL.RADIATION_ANATOMICAL_SITE
    )
    radiation_boost = factory.Faker("pybool")
    reference_radiation_treatment_id = factory.Faker("word")

    # set foreign keys
    program_id = factory.SelfAttribute("treatment_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("treatment_uuid.submitter_donor_id")
    donor_uuid = factory.SelfAttribute("treatment_uuid.donor_uuid")
    submitter_treatment_id = factory.SelfAttribute(
        "treatment_uuid.submitter_treatment_id"
    )
    treatment_uuid = factory.SubFactory(TreatmentFactory)


class SurgeryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Surgery

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)
    surgery_type = factory.Faker("random_element", elements=PERM_VAL.SURGERY_TYPE)
    surgery_site = factory.Faker("word")
    surgery_location = factory.Faker(
        "random_element", elements=PERM_VAL.SURGERY_LOCATION
    )
    tumour_length = factory.Faker("random_int", min=1, max=10)
    tumour_width = factory.Faker("random_int", min=1, max=10)
    greatest_dimension_tumour = factory.Faker("random_int", min=1, max=10)
    tumour_focality = factory.Faker("random_element", elements=PERM_VAL.TUMOUR_FOCALITY)
    residual_tumour_classification = factory.Faker(
        "random_element", elements=PERM_VAL.TUMOUR_CLASSIFICATION
    )
    margin_types_involved = factory.Faker(
        "random_elements",
        elements=PERM_VAL.MARGIN_TYPES,
        length=random.randint(1, 5),
        unique=True,
    )
    margin_types_not_involved = factory.Faker(
        "random_elements",
        elements=PERM_VAL.MARGIN_TYPES,
        length=random.randint(1, 5),
        unique=True,
    )
    margin_types_not_assessed = factory.Faker(
        "random_elements",
        elements=PERM_VAL.MARGIN_TYPES,
        length=random.randint(1, 5),
        unique=True,
    )
    lymphovascular_invasion = factory.Faker(
        "random_element", elements=PERM_VAL.LYMPHOVACULAR_INVASION
    )
    perineural_invasion = factory.Faker(
        "random_element", elements=PERM_VAL.PERINEURAL_INVASION
    )
    surgery_reference_database = factory.Faker(
        "random_element", elements=PERM_VAL.SYSTEMIC_THERAPY_TYPE
    )
    surgery_reference_identifier = None

    # set foreign keys
    program_id = factory.SelfAttribute("treatment_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("treatment_uuid.submitter_donor_id")
    donor_uuid = factory.SelfAttribute("treatment_uuid.donor_uuid")
    submitter_treatment_id = factory.SelfAttribute(
        "treatment_uuid.submitter_treatment_id"
    )
    treatment_uuid = factory.SubFactory(TreatmentFactory)


class FollowUpFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FollowUp

    # default values
    submitter_follow_up_id = factory.Sequence(lambda n: "FOLL_%d" % n)
    date_of_followup = None
    disease_status_at_followup = factory.Faker(
        "random_element", elements=PERM_VAL.DISEASE_STATUS_FOLLOWUP
    )
    relapse_type = factory.Faker("random_element", elements=PERM_VAL.RELAPSE_TYPE)
    date_of_relapse = None
    method_of_progression_status = factory.Faker(
        "random_elements",
        elements=PERM_VAL.PROGRESSION_STATUS_METHOD,
        length=random.randint(1, 5),
        unique=True,
    )
    anatomic_site_progression_or_recurrence = None

    # set foreign keys
    program_id = factory.SelfAttribute("treatment_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("treatment_uuid.submitter_donor_id")
    donor_uuid = factory.SelfAttribute("treatment_uuid.donor_uuid")
    submitter_primary_diagnosis_id = factory.SelfAttribute(
        "treatment_uuid.submitter_primary_diagnosis_id"
    )
    primary_diagnosis_uuid = factory.SelfAttribute(
        "treatment_uuid.primary_diagnosis_uuid"
    )
    submitter_treatment_id = factory.SelfAttribute(
        "treatment_uuid.submitter_treatment_id"
    )
    treatment_uuid = factory.SubFactory(TreatmentFactory)


class BiomarkerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Biomarker

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)
    test_date = factory.LazyFunction(
        lambda: {
            "month_interval": random.randint(0, 1000),
            "day_interval": random.randint(0, 3000),
        }
    )
    psa_level = factory.Faker("pyint", min_value=0, max_value=100)
    ca125 = factory.Faker("pyint", min_value=0, max_value=100)
    cea = factory.Faker("pyint", min_value=0, max_value=100)
    er_status = factory.Faker("random_element", elements=PERM_VAL.ER_PR_HPV_STATUS)
    er_percent_positive = factory.Faker(
        "pyfloat", positive=True, left_digits=2, right_digits=2
    )
    pr_status = factory.Faker("random_element", elements=PERM_VAL.ER_PR_HPV_STATUS)
    pr_percent_positive = factory.Faker(
        "pyfloat", positive=True, left_digits=2, right_digits=2
    )
    her2_ihc_status = factory.Faker("random_element", elements=PERM_VAL.HER2_STATUS)
    her2_ish_status = factory.Faker("random_element", elements=PERM_VAL.HER2_STATUS)
    hpv_ihc_status = factory.Faker("random_element", elements=PERM_VAL.ER_PR_HPV_STATUS)
    hpv_pcr_status = factory.Faker("random_element", elements=PERM_VAL.ER_PR_HPV_STATUS)
    hpv_strain = factory.Faker(
        "random_elements",
        elements=PERM_VAL.HPV_STRAIN,
        length=random.randint(1, 5),
        unique=True,
    )
    submitter_specimen_id = None
    submitter_primary_diagnosis_id = None
    submitter_treatment_id = None
    submitter_follow_up_id = None

    # set foreign keys
    program_id = factory.SelfAttribute("donor_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("donor_uuid.submitter_donor_id")
    donor_uuid = factory.SubFactory(DonorFactory)


class ComorbidityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comorbidity

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)
    prior_malignancy = factory.Faker("random_element", elements=PERM_VAL.UBOOLEAN)
    laterality_of_prior_malignancy = factory.Faker(
        "random_element", elements=PERM_VAL.MALIGNANCY_LATERALITY
    )
    age_at_comorbidity_diagnosis = factory.Faker("pyint", min_value=0, max_value=100)
    comorbidity_type_code = factory.Faker("word")
    comorbidity_treatment_status = factory.Faker(
        "random_element", elements=PERM_VAL.UBOOLEAN
    )
    comorbidity_treatment = factory.Faker("word")

    # set foreign keys
    program_id = factory.SelfAttribute("donor_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("donor_uuid.submitter_donor_id")
    donor_uuid = factory.SubFactory(DonorFactory)


class ExposureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exposure
        exclude = ('smoking_information',)

    # default values
    uuid = factory.LazyFunction(uuid.uuid4)
    tobacco_smoking_status = factory.Faker(
        "random_element", elements=PERM_VAL.SMOKING_STATUS
    )
    tobacco_type = factory.Faker("random_elements", elements=PERM_VAL.TOBACCO_TYPE)
    pack_years_smoked = factory.Faker(
        "pyfloat",
        left_digits=2,
        right_digits=1,
        positive=True,
        min_value=1,
        max_value=100,
    )

    # set foreign keys
    program_id = factory.SelfAttribute("donor_uuid.program_id")
    submitter_donor_id = factory.SelfAttribute("donor_uuid.submitter_donor_id")
    donor_uuid = factory.SubFactory(DonorFactory)
