import random

import factory
from django.db.models.signals import post_save

from chord_metadata_service.mohpackets.models import *
from chord_metadata_service.mohpackets.permissible_values import *


class ProgramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Program
        django_get_or_create = ('program_id',)
        
    # default values
    program_id = factory.Sequence(lambda n: 'PROGRAM_%d' % n)

class DonorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Donor
        django_get_or_create = ("submitter_donor_id",)
    
    # default values
    submitter_donor_id = factory.Sequence(lambda n: 'DONOR_%d' % n)
    gender = factory.Faker('random_element', elements=GENDER)
    sex_at_birth = factory.Faker('random_element', elements=SEX_AT_BIRTH)
    is_deceased = factory.Faker('boolean')
    lost_to_followup_reason = None
    lost_to_followup_after_clinical_event_identifier = None
    date_alive_after_lost_to_followup = None
    cause_of_death = factory.Maybe(
        'is_deceased',
        yes_declaration=factory.Faker('random_element', elements=CAUSE_OF_DEATH),
        no_declaration=None,
    )
    date_of_birth = factory.Faker('random_int')
    date_of_death = factory.Maybe(
        'is_deceased',
        yes_declaration=factory.Faker('random_int', min=date_of_birth),
        no_declaration=None,
    )
    primary_site = factory.Faker('random_elements', elements=PRIMARY_SITE, length=random.randint(1, 5), unique=True)

    # set foregin key
    program_id = factory.SubFactory(ProgramFactory)

class PrimaryDiagnosisFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PrimaryDiagnosis
        django_get_or_create = ("submitter_primary_diagnosis_id",)
    
    # Default values
    submitter_primary_diagnosis_id = factory.Sequence(lambda n: 'DIAG_%d' % n)
    date_of_diagnosis = factory.Faker('date', pattern='%Y-%m')
    cancer_type_code = factory.Faker('uuid4')
    basis_of_diagnosis = factory.Faker('random_element', elements=BASIS_OF_DIAGNOSIS)
    laterality = factory.Faker('random_element', elements=PRIMARY_DIAGNOSIS_LATERALITY)
    lymph_nodes_examined_status = factory.Faker('random_element', elements=LYMPH_NODE_STATUS)
    lymph_nodes_examined_method = factory.Faker('random_element', elements=LYMPH_NODE_METHOD)
    number_lymph_nodes_positive = factory.Faker('pyint', min_value=0, max_value=50)
    clinical_tumour_staging_system = factory.Faker('random_element', elements=TUMOUR_STAGING_SYSTEM)
    clinical_t_category = factory.Faker('random_element', elements=T_CATEGORY)
    clinical_n_category = factory.Faker('random_element', elements=N_CATEGORY)
    clinical_m_category = factory.Faker('random_element', elements=M_CATEGORY)
    clinical_stage_group = factory.Faker('random_element', elements=STAGE_GROUP)

    # Set the foreign keys
    program_id = factory.SelfAttribute('submitter_donor_id.program_id')
    submitter_donor_id = factory.SubFactory(DonorFactory)
    
    @factory.post_generation
    def set_clinical_event_identifier(self, create, extracted, **kwargs):
        donor = self.submitter_donor_id
        if not donor.is_deceased:
            donor.lost_to_followup_after_clinical_event_identifier = self.submitter_primary_diagnosis_id
            donor.lost_to_followup_reason = random.choice(LOST_TO_FOLLOWUP_REASON)
            donor.date_alive_after_lost_to_followup = random.randint(1000, 5000)
            donor.save()
            
class SpecimenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Specimen
        django_get_or_create = ("submitter_specimen_id",)

    # default values
    submitter_specimen_id = factory.Sequence(lambda n: 'SPECIMEN_%d' % n)
    pathological_tumour_staging_system = factory.Faker('random_element', elements=TUMOUR_STAGING_SYSTEM)
    pathological_t_category = factory.Faker('random_element', elements=T_CATEGORY)
    pathological_n_category = factory.Faker('random_element', elements=N_CATEGORY)
    pathological_m_category = factory.Faker('random_element', elements=M_CATEGORY)
    pathological_stage_group = factory.Faker('random_element', elements=STAGE_GROUP)
    specimen_collection_date = factory.Faker('random_int')
    specimen_storage = factory.Faker('random_element', elements=STORAGE)
    specimen_processing = factory.Faker('random_element', elements=SPECIMEN_PROCESSING)
    tumour_histological_type = factory.Faker('word')
    specimen_anatomic_location = factory.Faker('word')
    specimen_laterality = factory.Faker('random_element', elements=SPECIMEN_LATERALITY)
    reference_pathology_confirmed_diagnosis = factory.Faker('random_element', elements=CONFIRMED_DIAGNOSIS_TUMOUR)
    reference_pathology_confirmed_tumour_presence = factory.Faker('random_element', elements=CONFIRMED_DIAGNOSIS_TUMOUR)
    tumour_grading_system = factory.Faker('random_element', elements=TUMOUR_GRADING_SYSTEM)
    tumour_grade = factory.Faker('random_element', elements=TUMOUR_GRADE)
    percent_tumour_cells_range = factory.Faker('random_element', elements=PERCENT_CELLS_RANGE)
    percent_tumour_cells_measurement_method = factory.Faker('random_element', elements=CELLS_MEASURE_METHOD)

    # set foregin keys
    program_id = factory.SelfAttribute('submitter_primary_diagnosis_id.program_id')
    submitter_donor_id = factory.SelfAttribute('submitter_primary_diagnosis_id.submitter_donor_id')
    submitter_primary_diagnosis_id = factory.SubFactory(PrimaryDiagnosisFactory)
    
class SampleRegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SampleRegistration
        django_get_or_create = ("submitter_sample_id",)

    # default values
    submitter_sample_id = factory.Sequence(lambda n: 'SAMPLE_%d' % n)
    specimen_tissue_source = factory.Faker('random_element', elements=SPECIMEN_TISSUE_SOURCE)
    tumour_normal_designation = factory.Faker('random_element', elements=["Normal", "Tumour"])
    specimen_type = factory.Faker('random_element', elements=SPECIMEN_TYPE)
    sample_type = factory.Faker('random_element', elements=SAMPLE_TYPE)

    # set foregin keys
    program_id = factory.SelfAttribute('submitter_specimen_id.program_id')
    submitter_donor_id = factory.SelfAttribute('submitter_specimen_id.submitter_donor_id')
    submitter_specimen_id = factory.SubFactory(SpecimenFactory)
    
class TreatmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Treatment
        django_get_or_create = ("submitter_treatment_id",)

    # default values
    submitter_treatment_id = factory.Sequence(lambda n: 'TREATMENT_%d' % n)
    treatment_type = factory.Faker('random_element', elements=SAMPLE_TYPE)
    is_primary_treatment = factory.Faker('random_element', elements=['Yes', 'No'])
    line_of_treatment = factory.Faker('random_int', min=1, max=5)
    treatment_start_date = factory.Faker('random_int')
    treatment_end_date = factory.Faker('random_int')
    treatment_setting = factory.Faker('random_element', elements=TREATMENT_SETTING)
    treatment_intent = factory.Faker('random_element', elements=TREATMENT_INTENT)
    days_per_cycle = factory.Faker('random_int', min=1, max=30)
    number_of_cycles = factory.Faker('random_int', min=1, max=10)
    response_to_treatment_criteria_method = factory.Faker('random_element', elements=TREATMENT_RESPONSE_METHOD)
    response_to_treatment = factory.Faker('random_element', elements=TREATMENT_RESPONSE)
    status_of_treatment = factory.Faker('random_element', elements=TREATMENT_STATUS)

    # set foregin keys
    program_id = factory.SelfAttribute('submitter_primary_diagnosis_id.program_id')
    submitter_donor_id = factory.SelfAttribute('submitter_primary_diagnosis_id.submitter_donor_id')
    submitter_primary_diagnosis_id = factory.SubFactory(SpecimenFactory)

import uuid


class ChemotherapyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Chemotherapy

    # default values
    id = factory.LazyFunction(uuid.uuid4)
    drug_reference_database = factory.Faker('random_element', elements=DRUG_REFERENCE_DB)
    drug_name = factory.Faker('word')
    drug_reference_identifier = factory.Faker('word')
    chemotherapy_drug_dose_units = factory.Faker('random_element', elements=DOSAGE_UNITS)
    prescribed_cumulative_drug_dose = factory.Faker('random_int', min=1, max=100)
    actual_cumulative_drug_dose = factory.Faker('random_int', min=1, max=100)

    # set foregin keys
    program_id = factory.SelfAttribute('submitter_treatment_id.program_id')
    submitter_donor_id = factory.SelfAttribute('submitter_treatment_id.submitter_donor_id')
    submitter_treatment_id = factory.SubFactory(TreatmentFactory)
    
class HormoneTherapyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HormoneTherapy

    # default values
    id = factory.LazyFunction(uuid.uuid4)
    drug_reference_database = factory.Faker('random_element', elements=DRUG_REFERENCE_DB)
    drug_name = factory.Faker('word')
    drug_reference_identifier = factory.Faker('word')
    hormone_drug_dose_units = factory.Faker('random_element', elements=DOSAGE_UNITS)
    prescribed_cumulative_drug_dose = factory.Faker('random_int', min=1, max=100)
    actual_cumulative_drug_dose = factory.Faker('random_int', min=1, max=100)

    # set foreign keys
    program_id = factory.SelfAttribute('submitter_treatment_id.program_id')
    submitter_donor_id = factory.SelfAttribute('submitter_treatment_id.submitter_donor_id')
    submitter_treatment_id = factory.SubFactory(TreatmentFactory)

class RadiationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Radiation

    # default values
    id = factory.LazyFunction(uuid.uuid4)
    radiation_therapy_modality = factory.Faker('random_element', elements=RADIATION_THERAPY_MODALITY)
    radiation_therapy_type = factory.Faker('random_element', elements=["External", "Internal"])
    radiation_therapy_fractions = factory.Faker('random_int', min=1, max=30)
    radiation_therapy_dosage = factory.Faker('random_int', min=1, max=100)
    anatomical_site_irradiated = factory.Faker('random_element', elements=RADIATION_ANATOMICAL_SITE)
    radiation_boost = factory.Faker('pybool')
    reference_radiation_treatment_id = factory.Faker('word')

    # set foreign keys
    program_id = factory.SelfAttribute('submitter_treatment_id.program_id')
    submitter_donor_id = factory.SelfAttribute('submitter_treatment_id.submitter_donor_id')
    submitter_treatment_id = factory.SubFactory(TreatmentFactory)

class ImmunotherapyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Immunotherapy

    # default values
    id = factory.LazyFunction(uuid.uuid4)
    drug_reference_database = factory.Faker('random_element', elements=DRUG_REFERENCE_DB)
    immunotherapy_type = factory.Faker('random_element', elements=IMMUNOTHERAPY_TYPE)
    drug_name = factory.Faker('word')
    drug_reference_identifier = factory.Faker('word')
    immunotherapy_drug_dose_units = factory.Faker('random_element', elements=DOSAGE_UNITS)
    prescribed_cumulative_drug_dose = factory.Faker('random_int', min=1, max=100)
    actual_cumulative_drug_dose = factory.Faker('random_int', min=1, max=100)

    # set foreign keys
    program_id = factory.SelfAttribute('submitter_treatment_id.program_id')
    submitter_donor_id = factory.SelfAttribute('submitter_treatment_id.submitter_donor_id')
    submitter_treatment_id = factory.SubFactory(TreatmentFactory)

class SurgeryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Surgery

    # default values
    id = factory.LazyFunction(uuid.uuid4)
    surgery_type = factory.Faker('random_element', elements=SURGERY_TYPE)
    surgery_site = factory.Faker('word')
    surgery_location = factory.Faker('random_element', elements=SURGERY_LOCATION)
    tumour_length = factory.Faker('random_int', min=1, max=10)
    tumour_width = factory.Faker('random_int', min=1, max=10)
    greatest_dimension_tumour = factory.Faker('random_int', min=1, max=10)
    tumour_focality = factory.Faker('random_element', elements=TUMOUR_FOCALITY)
    residual_tumour_classification = factory.Faker('random_element', elements=TUMOUR_CLASSIFICATION)
    margin_types_involved = factory.Faker('random_elements', elements=MARGIN_TYPES, length=random.randint(1, 5), unique=True)
    margin_types_not_involved = factory.Faker('random_elements', elements=MARGIN_TYPES, length=random.randint(1, 5), unique=True)
    margin_types_not_assessed = factory.Faker('random_elements', elements=MARGIN_TYPES, length=random.randint(1, 5), unique=True)
    lymphovascular_invasion = factory.Faker('random_element', elements=LYMPHOVACULAR_INVASION)
    perineural_invasion = factory.Faker('random_element', elements=PERINEURAL_INVASION)
    submitter_specimen_id = None
    
    # set foreign keys
    program_id = factory.SelfAttribute('submitter_treatment_id.program_id')
    submitter_donor_id = factory.SelfAttribute('submitter_treatment_id.submitter_donor_id')
    submitter_treatment_id = factory.SubFactory(TreatmentFactory)
    
class FollowUpFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FollowUp

    # default values
    submitter_follow_up_id = factory.Sequence(lambda n: 'FOLLOW_UP_%d' % n)
    date_of_followup = factory.Faker('random_int')
    disease_status_at_followup = factory.Faker('random_element', elements=DISEASE_STATUS_FOLLOWUP)
    relapse_type = factory.Faker('random_element', elements=RELAPSE_TYPE)
    date_of_relapse = factory.Faker('random_int')
    method_of_progression_status = factory.Faker('random_element', elements=PROGRESSION_STATUS_METHOD)
    anatomic_site_progression_or_recurrence = factory.Faker('word')
    recurrence_tumour_staging_system = factory.Faker('random_element', elements=TUMOUR_STAGING_SYSTEM)
    recurrence_t_category = factory.Faker('random_element', elements=T_CATEGORY)
    recurrence_n_category = factory.Faker('random_element', elements=N_CATEGORY)
    recurrence_m_category = factory.Faker('random_element', elements=M_CATEGORY)
    recurrence_stage_group = factory.Faker('random_element', elements=STAGE_GROUP)

    # set foreign keys
    program_id = factory.SelfAttribute('submitter_treatment_id.program_id')
    submitter_donor_id = factory.SelfAttribute('submitter_treatment_id.submitter_donor_id')
    submitter_primary_diagnosis_id = factory.SelfAttribute('submitter_treatment_id.submitter_primary_diagnosis_id')
    submitter_treatment_id = factory.SubFactory(TreatmentFactory)

class BiomarkerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Biomarker
    
    # default values
    id = factory.LazyFunction(uuid.uuid4)
    test_interval = factory.Faker('pyint', min_value=0, max_value=100)
    psa_level = factory.Faker('pyint', min_value=0, max_value=100)
    ca125 = factory.Faker('pyint', min_value=0, max_value=100)
    cea = factory.Faker('pyint', min_value=0, max_value=100)
    er_status = factory.Faker('random_element', elements=ER_PR_HPV_STATUS)
    er_percent_positive = factory.Faker('pyfloat', positive=True, left_digits=2, right_digits=2)
    pr_status = factory.Faker('random_element', elements=ER_PR_HPV_STATUS)
    pr_percent_positive = factory.Faker('pyfloat', positive=True, left_digits=2, right_digits=2)
    her2_ihc_status = factory.Faker('random_element', elements=HER2_STATUS)
    her2_ish_status = factory.Faker('random_element', elements=HER2_STATUS)
    hpv_ihc_status = factory.Faker('random_element', elements=ER_PR_HPV_STATUS)
    hpv_pcr_status = factory.Faker('random_element', elements=ER_PR_HPV_STATUS)
    hpv_strain = factory.Faker('random_elements', elements=HPV_STRAIN, length=random.randint(1, 5), unique=True)
    submitter_specimen_id = None
    submitter_primary_diagnosis_id = None
    submitter_treatment_id = None
    submitter_follow_up_id = None
    
    # set foreign keys
    program_id = factory.SelfAttribute('submitter_donor_id.program_id')
    submitter_donor_id = factory.SubFactory(DonorFactory)
 
class ComorbidityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comorbidity
    
    # default values
    id = factory.LazyFunction(uuid.uuid4)
    prior_malignancy = factory.Faker('random_element', elements=UBOOLEAN)
    laterality_of_prior_malignancy = factory.Faker('random_element', elements=MALIGNANCY_LATERALITY)
    age_at_comorbidity_diagnosis = factory.Faker('pyint', min_value=0, max_value=100)
    comorbidity_type_code = factory.Faker('word')
    comorbidity_treatment_status = factory.Faker('random_element', elements=UBOOLEAN)
    comorbidity_treatment = factory.Faker('word')

    # set foreign keys
    program_id = factory.SelfAttribute('submitter_donor_id.program_id')
    submitter_donor_id = factory.SubFactory(DonorFactory)

class ExposureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exposure
    
    # default values
    id = factory.LazyFunction(uuid.uuid4)
    tobacco_smoking_status = factory.Faker('random_element', elements=SMOKING_STATUS)
    tobacco_type = factory.Faker('random_element', elements=TOBACCO_TYPE)
    pack_years_smoked = factory.Faker('random_int')
    
    # set foreign keys
    program_id = factory.SelfAttribute('submitter_donor_id.program_id')
    submitter_donor_id = factory.SubFactory(DonorFactory)