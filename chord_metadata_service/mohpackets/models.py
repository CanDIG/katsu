from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

"""
    This module contains the MODELS for the Marathon of Hope app.
    --------------------------------
    MOHCCN Clinical Data Model V1: Data Standards Sub-Committee (DSC)
    Model Schema (Excel): https://docs.google.com/spreadsheets/d/1pChl2DQiynU0OdueDHW7saJiLliv31GutgNbW8XSfUk/edit#gid=0 # noqa: E501
    Model Schema (PDF): https://www.marathonofhopecancercentres.ca/docs/default-source/policies-and-guidelines/mohccn-clinical-data-model_v1_endorsed6oct-2022.pdf?Status=Master&sfvrsn=7f6bd159_7 # noqa: E501
    ER Diagram: https://www.marathonofhopecancercentres.ca/docs/default-source/policies-and-guidelines/mohccn_data_standard_er_diagram_endorsed6oct22.pdf?Status=Master&sfvrsn=dd57a75e_5 # noqa: E501
    Schema last updated: September 2022
    --------------------------------
    NOTES:
    - Permissible values are not enforced in the model.
        They are checked in the serializer and ingest process.

    - It is important to have a __str__ method to return just the ID as
        the validator regex relies on this for primary key validation.
"""


class AutoDateTimeField(models.DateTimeField):
    """
    This function provides the timefield when the model is saved.
    Without this, the updated field will be empty and failed on update.
    """

    def pre_save(self, model_instance, add):
        return timezone.now()


class Program(models.Model):
    program_id = models.CharField(max_length=64, primary_key=True)
    created = models.DateTimeField(default=timezone.now)
    updated = AutoDateTimeField(default=timezone.now)

    class Meta:
        ordering = ["program_id"]

    def __str__(self):
        return f"{self.program_id}"


class Donor(models.Model):
    submitter_donor_id = models.CharField(max_length=64, primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    is_deceased = models.BooleanField(null=True)
    cause_of_death = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.CharField(max_length=32, null=True, blank=True)
    date_of_death = models.CharField(max_length=32, null=True, blank=True)
    primary_site = ArrayField(models.CharField(max_length=255, null=True, blank=True))

    class Meta:
        ordering = ["submitter_donor_id"]

    def __str__(self):
        return f"{self.submitter_donor_id}"


class PrimaryDiagnosis(models.Model):
    submitter_primary_diagnosis_id = models.CharField(max_length=64, primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    date_of_diagnosis = models.CharField(max_length=32, null=True, blank=True)
    cancer_type_code = models.CharField(max_length=64, null=True, blank=True)
    basis_of_diagnosis = models.CharField(max_length=128, null=True, blank=True)
    lymph_nodes_examined_status = models.CharField(
        max_length=128, null=True, blank=True
    )
    lymph_nodes_examined_method = models.CharField(max_length=64, null=True, blank=True)
    number_lymph_nodes_positive = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    clinical_tumour_staging_system = models.CharField(
        max_length=128, null=True, blank=True
    )
    clinical_t_category = models.CharField(max_length=64, null=True, blank=True)
    clinical_n_category = models.CharField(max_length=64, null=True, blank=True)
    clinical_m_category = models.CharField(max_length=64, null=True, blank=True)
    clinical_stage_group = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        ordering = ["submitter_primary_diagnosis_id"]

    def __str__(self):
        return f"{self.submitter_primary_diagnosis_id}"


class Specimen(models.Model):
    submitter_specimen_id = models.CharField(max_length=64, primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_primary_diagnosis_id = models.ForeignKey(
        PrimaryDiagnosis, on_delete=models.CASCADE, null=False, blank=False
    )
    pathological_tumour_staging_system = models.CharField(
        max_length=255, null=True, blank=True
    )
    pathological_t_category = models.CharField(max_length=64, null=True, blank=True)
    pathological_n_category = models.CharField(max_length=64, null=True, blank=True)
    pathological_m_category = models.CharField(max_length=64, null=True, blank=True)
    pathological_stage_group = models.CharField(max_length=64, null=True, blank=True)
    specimen_collection_date = models.CharField(max_length=32, null=True, blank=True)
    specimen_storage = models.CharField(max_length=64, null=True, blank=True)
    tumour_histological_type = models.CharField(max_length=128, null=True, blank=True)
    specimen_anatomic_location = models.CharField(max_length=32, null=True, blank=True)
    reference_pathology_confirmed_diagnosis = models.CharField(
        max_length=32, null=True, blank=True
    )
    reference_pathology_confirmed_tumour_presence = models.CharField(
        max_length=32, null=True, blank=True
    )
    tumour_grading_system = models.CharField(max_length=128, null=True, blank=True)
    tumour_grade = models.CharField(max_length=64, null=True, blank=True)
    percent_tumour_cells_range = models.CharField(max_length=64, null=True, blank=True)
    percent_tumour_cells_measurement_method = models.CharField(
        max_length=64, null=True, blank=True
    )

    class Meta:
        ordering = ["submitter_specimen_id"]

    def __str__(self):
        return f"{self.submitter_specimen_id}"


class SampleRegistration(models.Model):
    submitter_sample_id = models.CharField(max_length=64, primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_specimen_id = models.ForeignKey(
        Specimen, on_delete=models.CASCADE, null=False, blank=False
    )
    gender = models.CharField(max_length=32, null=True, blank=True)
    sex_at_birth = models.CharField(max_length=32, null=True, blank=True)
    specimen_tissue_source = models.CharField(max_length=255, null=True, blank=True)
    tumour_normal_designation = models.CharField(max_length=32, null=True, blank=True)
    specimen_type = models.CharField(max_length=255, null=True, blank=True)
    sample_type = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        ordering = ["submitter_sample_id"]

    def __str__(self):
        return f"{self.submitter_sample_id}"


class Treatment(models.Model):
    submitter_treatment_id = models.CharField(max_length=64, primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_primary_diagnosis_id = models.ForeignKey(
        PrimaryDiagnosis, on_delete=models.CASCADE, null=False, blank=False
    )
    treatment_type = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    is_primary_treatment = models.CharField(max_length=32, null=True, blank=True)
    treatment_start_date = models.CharField(max_length=32, null=True, blank=True)
    treatment_end_date = models.CharField(max_length=32, null=True, blank=True)
    treatment_setting = models.CharField(max_length=128, null=True, blank=True)
    treatment_intent = models.CharField(max_length=128, null=True, blank=True)
    days_per_cycle = models.PositiveSmallIntegerField(null=True, blank=True)
    number_of_cycles = models.PositiveSmallIntegerField(null=True, blank=True)
    response_to_treatment_criteria_method = models.CharField(
        max_length=255, null=True, blank=True
    )
    response_to_treatment = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["submitter_treatment_id"]

    def __str__(self):
        return f"{self.submitter_treatment_id}"


class Chemotherapy(models.Model):
    id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_treatment_id = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, null=False, blank=False
    )
    drug_name = models.CharField(max_length=255, null=True, blank=True)
    drug_rxnormcui = models.CharField(max_length=64, null=True, blank=True)
    chemotherapy_dosage_units = models.CharField(max_length=64, null=True, blank=True)
    cumulative_drug_dosage_prescribed = models.PositiveSmallIntegerField(
        blank=True, null=True
    )
    cumulative_drug_dosage_actual = models.PositiveSmallIntegerField(
        blank=True, null=True
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}"


class HormoneTherapy(models.Model):
    id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_treatment_id = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, null=False, blank=False
    )
    drug_name = models.CharField(max_length=255, null=True, blank=True)
    drug_rxnormcui = models.CharField(max_length=64, null=True, blank=True)
    hormone_drug_dosage_units = models.CharField(max_length=64, null=True, blank=True)
    cumulative_drug_dosage_prescribed = models.PositiveSmallIntegerField(
        blank=True, null=True
    )
    cumulative_drug_dosage_actual = models.PositiveSmallIntegerField(
        blank=True, null=True
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}"


class Radiation(models.Model):
    id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_treatment_id = models.OneToOneField(
        Treatment, on_delete=models.CASCADE, null=False, blank=False
    )
    radiation_therapy_modality = models.CharField(max_length=255, null=True, blank=True)
    radiation_therapy_type = models.CharField(max_length=64, null=True, blank=True)
    radiation_therapy_fractions = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    radiation_therapy_dosage = models.PositiveSmallIntegerField(null=True, blank=True)
    anatomical_site_irradiated = models.CharField(max_length=255, null=True, blank=True)
    radiation_boost = models.BooleanField(null=True)
    reference_radiation_treatment_id = models.CharField(
        max_length=64, null=True, blank=True
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}"


class Immunotherapy(models.Model):
    id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_treatment_id = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, null=False, blank=False
    )
    immunotherapy_type = models.CharField(max_length=255, null=True, blank=True)
    drug_name = models.CharField(max_length=255, null=True, blank=True)
    drug_rxnormcui = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}"


class Surgery(models.Model):
    id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_specimen_id = models.OneToOneField(
        Specimen, on_delete=models.CASCADE, null=True, blank=True
    )
    submitter_treatment_id = models.OneToOneField(
        Treatment, on_delete=models.CASCADE, null=False, blank=False
    )
    surgery_type = models.CharField(max_length=255, null=True, blank=True)
    surgery_site = models.CharField(max_length=255, null=True, blank=True)
    surgery_location = models.CharField(max_length=128, null=True, blank=True)
    tumour_length = models.PositiveSmallIntegerField(null=True, blank=True)
    tumour_width = models.PositiveSmallIntegerField(null=True, blank=True)
    greatest_dimension_tumour = models.PositiveSmallIntegerField(null=True, blank=True)
    tumour_focality = models.CharField(max_length=64, null=True, blank=True)
    residual_tumour_classification = models.CharField(
        max_length=64, null=True, blank=True
    )
    margin_types_involved = ArrayField(
        models.CharField(max_length=128, null=True, blank=True)
    )
    margin_types_not_involved = ArrayField(
        models.CharField(max_length=128, null=True, blank=True)
    )
    margin_types_not_assessed = ArrayField(
        models.CharField(max_length=128, null=True, blank=True)
    )
    lymphovascular_invasion = models.CharField(max_length=255, null=True, blank=True)
    perineural_invasion = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}"


class FollowUp(models.Model):
    submitter_follow_up_id = models.CharField(max_length=64, primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_primary_diagnosis_id = models.ForeignKey(
        PrimaryDiagnosis, on_delete=models.SET_NULL, blank=True, null=True
    )
    submitter_treatment_id = models.ForeignKey(
        Treatment, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_of_followup = models.CharField(max_length=32, null=False, blank=False)
    lost_to_followup = models.BooleanField(null=True)
    lost_to_followup_reason = models.CharField(max_length=255, blank=True, default="")
    disease_status_at_followup = models.CharField(
        max_length=255, null=False, blank=False
    )
    relapse_type = models.CharField(max_length=128, blank=True, default="")
    date_of_relapse = models.CharField(max_length=32, blank=True, default="")
    method_of_progression_status = models.CharField(
        max_length=255, blank=True, default=""
    )
    anatomic_site_progression_or_recurrence = models.CharField(
        max_length=255, blank=True, default=""
    )
    recurrence_tumour_staging_system = models.CharField(
        max_length=255, blank=True, default=""
    )
    recurrence_t_category = models.CharField(max_length=32, blank=True, default="")
    recurrence_n_category = models.CharField(max_length=32, blank=True, default="")
    recurrence_m_category = models.CharField(max_length=32, blank=True, default="")
    recurrence_stage_group = models.CharField(max_length=64, blank=True, default="")

    class Meta:
        ordering = ["submitter_follow_up_id"]

    def __str__(self):
        return f"{self.submitter_follow_up_id}"


class Biomarker(models.Model):
    id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_specimen_id = models.ForeignKey(
        Specimen, on_delete=models.SET_NULL, blank=True, null=True
    )
    submitter_primary_diagnosis_id = models.ForeignKey(
        PrimaryDiagnosis, on_delete=models.SET_NULL, blank=True, null=True
    )
    submitter_treatment_id = models.ForeignKey(
        Treatment, on_delete=models.SET_NULL, blank=True, null=True
    )
    submitter_follow_up_id = models.ForeignKey(
        FollowUp, on_delete=models.SET_NULL, blank=True, null=True
    )
    test_interval = models.PositiveSmallIntegerField(null=True, blank=True)
    psa_level = models.PositiveSmallIntegerField(null=True, blank=True)
    ca125 = models.PositiveSmallIntegerField(null=True, blank=True)
    cea = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}"


class Comorbidity(models.Model):
    id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=False, blank=False
    )
    submitter_donor_id = models.ForeignKey(
        Donor, on_delete=models.CASCADE, null=False, blank=False
    )
    prior_malignancy = models.CharField(max_length=32)
    laterality_of_prior_malignancy = models.CharField(
        max_length=64, blank=True, default=""
    )
    age_at_comorbidity_diagnosis = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    comorbidity_type_code = models.CharField(max_length=64, blank=True, default="")
    comorbidity_treatment_status = models.CharField(
        max_length=32, blank=True, default=""
    )
    comorbidity_treatment = models.CharField(max_length=255, blank=True, default="")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}"
