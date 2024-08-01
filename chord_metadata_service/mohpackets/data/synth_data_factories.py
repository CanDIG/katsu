import random
import math
import factory
import chord_metadata_service.mohpackets.permissible_values as PERM_VAL
import synth_data_values as SYNTH_VAL

from chord_metadata_service.mohpackets.tests.endpoints.factories import (
    BiomarkerFactory,
    ComorbidityFactory,
    DonorFactory,
    FollowUpFactory,
    PrimaryDiagnosisFactory,
    RadiationFactory,
    SampleRegistrationFactory,
    SpecimenFactory,
    SurgeryFactory,
    SystemicTherapyFactory,
    TreatmentFactory,
    ProgramFactory,
    days_to_months
)

"""
    This file contains factory classes for generating synthetic data.

    They inherit from factories used for code testing at chord_metadata_service.mohpackets.tests.endpoints.factories but
    override some variables to make them more suitable for synthetic data testing.

    They are primarily used in the `data_factory.py` script to create a set of programs with linked MoHCCN data for 
    ingest into the CanDIG platform. 
    
    NullSynth*Factories have all nullable fields nulled
    AllSynthFactories have no null fields (within model constraints, e.g. if a donor has is_deceased False, there will 
    not be a cause_of_death)
    
    Example Usage:

        # This will create a Donor instance and a Program instance
        donor = SynthDonorFactory()

    Note:
        These factories use the Factory Boy library (https://factoryboy.readthedocs.io/)
        to generate test data.
        Some business logic is not strictly enforced.

    Author: Marion Shadbolt
"""


###############
## Factories ##
###############


class SynthProgramFactory(ProgramFactory):

    # default values
    program_id = factory.Sequence(lambda n: f"SYNTH_{str(n).zfill(2)}")


class SynthDonorFactory(DonorFactory):
    class Meta:
        exclude = ("fill_dob", "null_percent")

    gender = factory.Faker("random_element", elements=SYNTH_VAL.GENDER)
    sex_at_birth = factory.Faker("random_element", elements=SYNTH_VAL.SEX_AT_BIRTH)
    fill_dob = factory.Faker("pybool", truth_probability=80)
    date_of_birth = factory.Maybe(
        "fill_dob",
        yes_declaration=factory.LazyFunction(lambda: {
            "day_interval": random.randint(-21900, -18220),
        }),
        no_declaration=None
    )


class NullSynthDonorFactory(SynthDonorFactory):
    submitter_donor_id = factory.Sequence(lambda n: f"DONOR_NULL_{str(n).zfill(4)}")
    gender = None
    sex_at_birth = None
    is_deceased = None
    lost_to_followup_reason = None
    lost_to_followup_after_clinical_event_identifier = None
    date_alive_after_lost_to_followup = None
    date_resolution = "day"
    cause_of_death = None
    date_of_birth = None
    date_of_death = None


class AllSynthDonorFactory(DonorFactory):
    submitter_donor_id = factory.Sequence(lambda n: f"DONOR_ALL_{str(n).zfill(4)}")
    is_deceased = factory.Iterator([True, False])


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

    basis_of_diagnosis = factory.Faker("random_element", elements=SYNTH_VAL.BASIS_OF_DIAGNOSIS)
    laterality = factory.Faker("random_element", elements=SYNTH_VAL.PRIMARY_DIAGNOSIS_LATERALITY)
    clinical_tumour_staging_system = factory.Faker("random_element", elements=SYNTH_VAL.TUMOUR_STAGING_SYSTEM)
    clinical_t_category = factory.Faker("random_element", elements=SYNTH_VAL.T_CATEGORY)
    clinical_n_category = factory.Faker("random_element", elements=SYNTH_VAL.N_CATEGORY)
    clinical_m_category = factory.Faker("random_element", elements=SYNTH_VAL.M_CATEGORY)
    clinical_stage_group = factory.Faker("random_element", elements=SYNTH_VAL.STAGE_GROUP)
    pathological_tumour_staging_system = factory.Faker("random_element", elements=SYNTH_VAL.TUMOUR_STAGING_SYSTEM)
    pathological_t_category = factory.Faker("random_element", elements=SYNTH_VAL.T_CATEGORY)
    pathological_n_category = factory.Faker("random_element", elements=SYNTH_VAL.N_CATEGORY)
    pathological_m_category = factory.Faker("random_element", elements=SYNTH_VAL.M_CATEGORY)
    pathological_stage_group = factory.Faker("random_element", elements=SYNTH_VAL.STAGE_GROUP)

    primary_site = factory.Iterator(SYNTH_VAL.PRIMARY_SITE)


class NullSynthPrimaryDiagnosisFactory(PrimaryDiagnosisFactory):
    submitter_primary_diagnosis_id = factory.Sequence(lambda n: f"DIAG_NULL_{str(n).zfill(4)}")

    date_of_diagnosis = None
    cancer_type_code = None
    basis_of_diagnosis = None
    laterality = None
    clinical_tumour_staging_system = None
    clinical_t_category = None
    clinical_n_category = None
    clinical_m_category = None
    clinical_stage_group = None
    pathological_tumour_staging_system = None
    pathological_t_category = None
    pathological_n_category = None
    pathological_m_category = None
    pathological_stage_group = None
    primary_site = None

    @factory.post_generation
    def set_clinical_event_identifier(self, create, extracted, **kwargs):
        pass


class AllSynthPrimaryDiagnosisFactory(PrimaryDiagnosisFactory):
    submitter_primary_diagnosis_id = factory.Sequence(lambda n: f"DIAG_ALL_{str(n).zfill(4)}")
    cancer_type_code = "C06.9"
    primary_site = "Floor of mouth"

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
                "day_interval": random.randint(25551, 32850),
            }
            donor.date_alive_after_lost_to_followup["month_interval"] = (
                days_to_months(donor.date_alive_after_lost_to_followup["day_interval"]))
            donor.save()


class SynthSpecimenFactory(SpecimenFactory):
    specimen_storage = factory.Faker("random_element", elements=SYNTH_VAL.STORAGE)
    specimen_processing = factory.Faker("random_element", elements=SYNTH_VAL.SPECIMEN_PROCESSING)
    tumour_histological_type = None
    specimen_anatomic_location = factory.Faker("random_element", elements=SYNTH_VAL.TOPOGRAPHY_CODES)
    specimen_laterality = factory.Faker("random_element", elements=SYNTH_VAL.SPECIMEN_LATERALITY)
    reference_pathology_confirmed_diagnosis = factory.Faker(
        "random_element", elements=SYNTH_VAL.CONFIRMED_DIAGNOSIS_TUMOUR
    )
    reference_pathology_confirmed_tumour_presence = factory.Faker(
        "random_element", elements=SYNTH_VAL.CONFIRMED_DIAGNOSIS_TUMOUR
    )
    tumour_grading_system = factory.Faker(
        "random_element", elements=SYNTH_VAL.TUMOUR_GRADING_SYSTEM
    )
    tumour_grade = factory.Faker("random_element", elements=SYNTH_VAL.TUMOUR_GRADE)
    percent_tumour_cells_range = factory.Faker(
        "random_element", elements=SYNTH_VAL.PERCENT_CELLS_RANGE
    )
    percent_tumour_cells_measurement_method = factory.Faker(
        "random_element", elements=SYNTH_VAL.CELLS_MEASURE_METHOD
    )


class NullSynthSpecimenFactory(SpecimenFactory):
    submitter_specimen_id = factory.Sequence(lambda n: f"SPECIMEN_NULL_{str(n).zfill(4)}")

    specimen_collection_date = None
    specimen_storage = None
    specimen_processing = None
    tumour_histological_type = None
    specimen_anatomic_location = None
    specimen_laterality = None
    reference_pathology_confirmed_diagnosis = None
    reference_pathology_confirmed_tumour_presence = None
    tumour_grading_system = None
    tumour_grade = None
    percent_tumour_cells_measurement_method = None

    @factory.post_generation
    def set_date(self, create, extracted, **kwargs):
        """override method to keep null values"""
        pass

    @factory.post_generation
    def generate_histology_code(self, create, extracted, **kwargs):
        """override method to keep null values"""
        pass


class AllSynthSpecimenFactory(SpecimenFactory):
    submitter_specimen_id = factory.Sequence(lambda n: f"SPECIMEN_ALL_{str(n).zfill(4)}")

    @factory.post_generation
    def set_date(self, create, extracted, **kwargs):
        """override method to remove 15% nulls"""
        self.specimen_collection_date = {"day_interval": random.randint(0, 90)}
        self.specimen_collection_date['month_interval'] = days_to_months(
            self.specimen_collection_date['day_interval'])

    @factory.post_generation
    def generate_histology_code(self, create, extracted, **kwargs):
        """override method to remove 15% nulls"""
        one = str(random.randint(8, 9))
        two = str(random.randint(0, 999)).rjust(3, "0")
        code = one + two + "/3"
        self.tumour_histological_type = code


class SynthSampleRegistrationFactory(SampleRegistrationFactory):
    specimen_tissue_source = factory.Faker(
        "random_element", elements=SYNTH_VAL.SPECIMEN_TISSUE_SOURCE
    )
    tumour_normal_designation = factory.Iterator(SYNTH_VAL.TUMOUR_DESIGNATION)
    specimen_type = factory.Faker("random_element", elements=SYNTH_VAL.SPECIMEN_TYPE)
    sample_type = factory.Faker("random_element", elements=SYNTH_VAL.SAMPLE_TYPE)


class NullSynthSampleRegistrationFactory(SampleRegistrationFactory):
    submitter_sample_id = factory.Sequence(lambda n: f"SAMPLE_NULL_{str(n).zfill(4)}")

    specimen_tissue_source = None
    tumour_normal_designation = None
    specimen_type = None
    sample_type = None


class AllSynthSampleRegistrationFactory(SampleRegistrationFactory):
    submitter_sample_id = factory.Sequence(lambda n: f"SAMPLE_ALL_{str(n).zfill(4)}")


class SynthTreatmentFactory(TreatmentFactory):
    # add 20% nulls to all enum lists
    treatment_type = factory.Faker(
        "random_elements",
        elements=SYNTH_VAL.TREATMENT_TYPE,
        length=random.randint(1, 3),
        unique=True,
    )
    treatment_intent = factory.Faker(
        "random_element", elements=SYNTH_VAL.TREATMENT_INTENT
    )
    response_to_treatment_criteria_method = factory.Faker(
        "random_element", elements=SYNTH_VAL.TREATMENT_RESPONSE_METHOD
    )
    response_to_treatment = factory.Faker(
        "random_element", elements=SYNTH_VAL.TREATMENT_RESPONSE
    )
    status_of_treatment = factory.Faker(
        "random_element", elements=SYNTH_VAL.TREATMENT_STATUS
    )


class NullSynthTreatmentFactory(TreatmentFactory):
    submitter_treatment_id = factory.Sequence(lambda n: f"TREATMENT_NULL_{str(n).zfill(4)}")
    treatment_type = None
    is_primary_treatment = None
    treatment_start_date = None
    treatment_end_date = None
    treatment_intent = None
    response_to_treatment_criteria_method = None
    response_to_treatment = None
    status_of_treatment = None

    @factory.post_generation
    def set_treatment_dates(self, create, extracted, **kwargs):
        """override method to keep null values"""
        pass

    @factory.post_generation
    def correct_treatment_type(self, create, extracted, **kwargs):
        """override method to keep null values"""
        pass


class AllSynthTreatmentFactory(TreatmentFactory):
    submitter_treatment_id = factory.Sequence(lambda n: f"TREATMENT_ALL_{str(n).zfill(4)}")
    is_primary_treatment = factory.Faker("random_element", elements=["Yes", "No"])

    @factory.post_generation
    def set_treatment_dates(self, create, extracted, **kwargs):
        """override method to prevent 15% nulls"""
        treatment = self
        day_int = random.randint(5, 180)
        treatment.treatment_start_date = {"day_interval": day_int,
                                          "month_interval": days_to_months(day_int)}
        min_start = treatment.treatment_start_date["day_interval"] + 30
        min_end = min_start + 365
        day_int = random.randint(min_start, min_end)
        treatment.treatment_end_date = {"day_interval": day_int,
                                        "month_interval": days_to_months(day_int)}
        treatment.save()

    @factory.post_generation
    def correct_treatment_type(self, create, extracted, **kwargs):
        """override method to prevent 15% nulls"""
        if self.treatment_type and "No treatment" in self.treatment_type:
            self.treatment_type = ["No treatment"]


class SynthSystemicTherapyFactory(SystemicTherapyFactory):
    class Meta:
        exclude = ("null_drug_dose", )

    # add 20% nulls to all enum lists

    drug_dose_units = factory.Faker("random_element", elements=SYNTH_VAL.DOSAGE_UNITS)
    null_drug_dose = factory.LazyFunction(lambda: random.random() > 0.15)
    prescribed_cumulative_drug_dose = factory.Maybe("null_drug_dose",
                                                    None,
                                                    factory.Faker("pyfloat", left_digits=2, right_digits=1,
                                                                  positive=True, min_value=20, max_value=50))
    actual_cumulative_drug_dose = factory.Maybe("null_drug_dose",
                                                None,
                                                factory.Faker("pyfloat", left_digits=2, right_digits=1,
                                                              positive=True, min_value=51, max_value=100))


class NullSynthSystemicTherapyFactory(SystemicTherapyFactory):
    drug_dose_units = None
    prescribed_cumulative_drug_dose = None
    actual_cumulative_drug_dose = None

    @factory.post_generation
    def add_dates(self, create, extracted, **kwargs):
        """Override method to keep null values."""
        pass

    @factory.post_generation
    def add_drug_info(self, create, extracted, **kwargs):
        """Override method to keep null values."""
        pass


class AllSynthSystemicTherapyFactory(SystemicTherapyFactory):

    @factory.post_generation
    def add_dates(self, create, extracted, **kwargs):
        treatment = self.treatment_uuid
        if treatment.treatment_start_date and treatment.treatment_end_date:
            self.start_date = {"day_interval": random.randint(
                treatment.treatment_start_date['day_interval'], treatment.treatment_end_date['day_interval'])}
            self.start_date["month_interval"] = days_to_months(self.start_date["day_interval"])
        elif treatment.treatment_start_date:
            self.start_date = {"day_interval": random.randint(
                treatment.treatment_start_date['day_interval'],
                treatment.treatment_start_date['day_interval'] + 50)}
            self.start_date["month_interval"] = days_to_months(self.start_date["day_interval"])
        elif treatment.treatment_end_date:
            self.start_date = {"day_interval": random.randint(
                treatment.treatment_end_date['day_interval'] - 50,
                treatment.treatment_end_date['day_interval'])}
            self.start_date["month_interval"] = days_to_months(self.start_date["day_interval"])
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


class SynthRadiationFactory(RadiationFactory):
    class Meta:
        exclude = ("null_dosage_fraction")

    radiation_therapy_modality = factory.Faker(
        "random_element", elements=SYNTH_VAL.RADIATION_THERAPY_MODALITY
    )
    radiation_therapy_type = factory.Faker(
        "random_element", elements=SYNTH_VAL.THERAPY_TYPE
    )
    anatomical_site_irradiated = factory.Faker(
        "random_element", elements=SYNTH_VAL.RADIATION_ANATOMICAL_SITE
    )

    null_dosage_fraction = factory.LazyFunction(lambda: random.random() > 0.15)
    radiation_therapy_fractions = factory.Maybe("null_dosage_fraction",
                                                factory.Faker("random_int", min=1, max=30),
                                                None)
    radiation_therapy_dosage = factory.Maybe("null_dosage_fraction",
                                             factory.Faker("random_int", min=1, max=100),
                                             None)


class NullSynthRadiationFactory(RadiationFactory):
    radiation_therapy_modality = None
    radiation_therapy_type = None
    radiation_therapy_fractions = None
    radiation_therapy_dosage = None
    anatomical_site_irradiated = None
    radiation_boost = None


class SynthSurgeryFactory(SurgeryFactory):
    class Meta:
        exclude = ("null_dimensions", "null_margin_types")

    surgery_site = factory.Faker("random_element", elements=SYNTH_VAL.TOPOGRAPHY_CODES)
    surgery_location = factory.Faker(
        "random_element", elements=SYNTH_VAL.SURGERY_LOCATION
    )
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
    tumour_focality = factory.Faker("random_element", elements=SYNTH_VAL.TUMOUR_FOCALITY)
    residual_tumour_classification = factory.Faker("random_element", elements=SYNTH_VAL.TUMOUR_CLASSIFICATION)
    null_margin_types = factory.LazyFunction(lambda: random.random() > 0.15)
    margin_types_involved = factory.Maybe(
        "null_margin_type",
        None,
        factory.Faker("random_elements",
                      elements=SYNTH_VAL.MARGIN_TYPES,
                      length=random.randint(1, 3),
                      unique=True))
    margin_types_not_involved = factory.Maybe(
        "null_margin_type",
        None,
        factory.Faker(
            "random_elements",
            elements=SYNTH_VAL.MARGIN_TYPES,
            length=random.randint(1, 3),
            unique=True))
    margin_types_not_assessed = factory.Maybe(
        "null_margin_type",
        None,
        factory.Faker(
            "random_elements",
            elements=SYNTH_VAL.MARGIN_TYPES,
            length=random.randint(1, 3),
            unique=True))


class NullSynthSurgeryFactory(SurgeryFactory):
    surgery_site = None
    surgery_location = None
    tumour_length = None
    tumour_width = None
    greatest_dimension_tumour = None
    tumour_focality = None
    residual_tumour_classification = None
    margin_types_involved = None
    margin_types_not_involved = None
    margin_types_not_assessed = None
    lymphovascular_invasion = None
    perineural_invasion = None

    @factory.post_generation
    def add_surgery_type(self, create, extracted, **kwargs):
        """Override method to keep null values."""
        pass


class AllSynthSurgeryFactory(SurgeryFactory):
    @factory.post_generation
    def add_surgery_type(self, create, extracted, **kwargs):
        self.surgery_type = random.choice(list(SYNTH_VAL.SURGERY_TYPE.keys()))
        if self.surgery_type:
            self.surgery_reference_database = random.choice(list(SYNTH_VAL.SURGERY_TYPE[self.surgery_type].keys()))
            if self.surgery_reference_database:
                self.surgery_reference_identifier = SYNTH_VAL.SURGERY_TYPE[self.surgery_type][
                    self.surgery_reference_database]


class SynthBiomarkerFactory(BiomarkerFactory):
    class Meta:
        exclude = ("null_hpv_strain", "fill_specimen", "fill_pd", "fill_treatment", "fill_followup",
                   "specimen_uuid", "pd_uuid", "treatment_uuid", "followup_uuid")

    er_status = factory.Faker("random_element", elements=SYNTH_VAL.ER_PR_HPV_STATUS)
    pr_status = factory.Faker("random_element", elements=SYNTH_VAL.ER_PR_HPV_STATUS)
    her2_ihc_status = factory.Faker("random_element", elements=SYNTH_VAL.HER2_STATUS)
    her2_ish_status = factory.Faker("random_element", elements=SYNTH_VAL.HER2_STATUS)

    null_hpv_strain = factory.LazyFunction(lambda: random.random() > 0.15)
    hpv_strain = factory.Maybe("null_hpv_strain",
                               None,
                               factory.Faker(
                                   "random_elements",
                                   elements=PERM_VAL.HPV_STRAIN,
                                   length=random.randint(1, 5),
                                   unique=True,
                               ))


class NullSynthBiomarkerFactory(BiomarkerFactory):
    psa_level = None
    ca125 = None
    cea = None
    er_status = None
    er_percent_positive = None
    pr_status = None
    pr_percent_positive = None
    her2_ihc_status = None
    her2_ish_status = None
    hpv_ihc_status = None
    hpv_pcr_status = None
    hpv_strain = None

    @factory.post_generation
    def set_date(self, create, extracted, **kwargs):
        """Override method to keep null values."""
        pass

    @factory.post_generation
    def set_percents(self, create, extracted, **kwargs):
        """Override method to keep null values."""
        pass


class AllSynthBiomarkerFactory(BiomarkerFactory):
    @factory.post_generation
    def set_date(self, create, extracted, **kwargs):
        donor = self.donor_uuid
        if donor.date_of_death and donor.date_of_birth:
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


class SynthComorbidityFactory(ComorbidityFactory):
    prior_malignancy = factory.Faker("random_element", elements=SYNTH_VAL.UBOOLEAN)
    laterality_of_prior_malignancy = factory.Faker("random_element", elements=SYNTH_VAL.MALIGNANCY_LATERALITY)
    comorbidity_type_code = factory.Faker("random_element", elements=SYNTH_VAL.ALL_CODES)


class NullSynthComorbidityFactory(ComorbidityFactory):
    prior_malignancy = None
    laterality_of_prior_malignancy = None
    age_at_comorbidity_diagnosis = None
    comorbidity_type_code = None
    comorbidity_treatment_status = None
    comorbidity_treatment = None

    @factory.post_generation
    def set_priors(self, create, extracted, **kwargs):
        """Override method to keep null values."""
        pass


class SynthFollowUpFactory(FollowUpFactory):
    disease_status_at_followup = factory.Faker(
        "random_element", elements=PERM_VAL.DISEASE_STATUS_FOLLOWUP
    )
    method_of_progression_status = factory.Faker(
        "random_elements",
        elements=PERM_VAL.PROGRESSION_STATUS_METHOD,
        length=random.randint(1, 5),
        unique=True,
    )


class NullSynthFollowUpFactory(FollowUpFactory):
    submitter_follow_up_id = factory.Sequence(lambda n: f"FOLLOW_UP_NULL_{str(n).zfill(4)}")
    disease_status_at_followup = None
    method_of_progression_status = None

    @factory.post_generation
    def set_relapse_type_date(self, create, extracted, **kwargs):
        """Override method to keep null values."""
        pass


class AllSynthFollowUpFactory(FollowUpFactory):
    submitter_follow_up_id = factory.Sequence(lambda n: f"FOLLOW_UP_ALL_{str(n).zfill(4)}")

    @factory.post_generation
    def set_relapse_type_date(self, create, extracted, **kwargs):
        """Override method to remove 15% nulls."""
        if self.disease_status_at_followup in ['Distant progression', 'Loco-regional progression',
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