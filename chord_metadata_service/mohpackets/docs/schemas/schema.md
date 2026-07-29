
<h1 id="moh-service-api">MoH Service API v6.0.0</h1>

This is the RESTful API for the MoH Service.

Base URLs:

# Authentication

* API Key (ServiceTokenAuth)
    - Parameter Name: **X-Service-Token**, in: header. 

- HTTP Authentication, scheme: bearer

- HTTP Authentication, scheme: bearer

- HTTP Authentication, scheme: bearer

- HTTP Authentication, scheme: bearer

<h1 id="moh-service-api-default">Default</h1>

## chord_metadata_service_mohpackets_apis_core_service_info

<a id="opIdchord_metadata_service_mohpackets_apis_core_service_info"></a>

`GET /v3/service-info`

*Service Info*

<h1 id="moh-service-api-discovery">discovery</h1>

## chord_metadata_service_mohpackets_apis_discovery_discover_programs

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_discover_programs"></a>

`GET /v3/discovery/programs/`

*Discover Programs*

Return all the programs in the database.

> Example responses

> 200 Response

```json
[
  {
    "program_id": "string",
    "metadata": null
  }
]
```

## chord_metadata_service_mohpackets_apis_discovery_discover_sidebar_list

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_discover_sidebar_list"></a>

`GET /v3/discovery/sidebar_list/`

*Discover Sidebar List*

Retrieve the list of drug names and treatment for frontend usage

> Example responses

> 200 Response

```json
{}
```

<h1 id="moh-service-api-overview">overview</h1>

## chord_metadata_service_mohpackets_apis_discovery_discover_program_count

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_discover_program_count"></a>

`GET /v3/discovery/overview/program_count/`

*Discover Program Count*

Return the number of programs in the database.

> Example responses

> 200 Response

```json
{
  "property1": 0,
  "property2": 0
}
```

## chord_metadata_service_mohpackets_apis_discovery_discover_patients_per_program

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_discover_patients_per_program"></a>

`GET /v3/discovery/overview/patients_per_program/`

*Discover Patients Per Program*

Return the number of patients per program in the database.

> Example responses

> 200 Response

```json
[
  {
    "program_id": "string",
    "patients_count": "string"
  }
]
```

## chord_metadata_service_mohpackets_apis_discovery_discover_individual_count

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_discover_individual_count"></a>

`GET /v3/discovery/overview/individual_count/`

*Discover Individual Count*

Return the number of individuals in the database.

> Example responses

> 200 Response

```json
{
  "property1": "string",
  "property2": "string"
}
```

## chord_metadata_service_mohpackets_apis_discovery_discover_gender_count

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_discover_gender_count"></a>

`GET /v3/discovery/overview/gender_count/`

*Discover Gender Count*

Return the count for every gender in the database.

> Example responses

> 200 Response

```json
[
  {
    "gender": "string",
    "gender_count": "string"
  }
]
```

## chord_metadata_service_mohpackets_apis_discovery_discover_primary_site_count

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_discover_primary_site_count"></a>

`GET /v3/discovery/overview/primary_site_count/`

*Discover Primary Site Count*

Return the count for every cancer type in the database.

> Example responses

> 200 Response

```json
[
  {
    "primary_site_name": "string",
    "primary_site_count": "string"
  }
]
```

## chord_metadata_service_mohpackets_apis_discovery_discover_treatment_type_count

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_discover_treatment_type_count"></a>

`GET /v3/discovery/overview/treatment_type_count/`

*Discover Treatment Type Count*

Return the count for every treatment type in the database.

> Example responses

> 200 Response

```json
[
  {
    "treatment_type_name": "string",
    "treatment_type_count": "string"
  }
]
```

## chord_metadata_service_mohpackets_apis_discovery_discover_diagnosis_age_count

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_discover_diagnosis_age_count"></a>

`GET /v3/discovery/overview/diagnosis_age_count/`

*Discover Diagnosis Age Count*

Return the count for age of diagnosis by calculating the date of birth interval.

> Example responses

> 200 Response

```json
[
  {
    "age_at_diagnosis": "string",
    "age_count": "string"
  }
]
```

<h1 id="moh-service-api-ingest">ingest</h1>

## chord_metadata_service_mohpackets_apis_ingestion_create_programs

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_programs"></a>

`POST /v3/ingest/programs/`

*Create Programs*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_programs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ProgramIngestSchema](#schemaprogramingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_donors

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_donors"></a>

`POST /v3/ingest/donors/`

*Create Donors*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_donors-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DonorIngestSchema](#schemadonoringestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_biomarkers

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_biomarkers"></a>

`POST /v3/ingest/biomarkers/`

*Create Biomarkers*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_biomarkers-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BiomarkerIngestSchema](#schemabiomarkeringestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_systemic_therapies

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_systemic_therapies"></a>

`POST /v3/ingest/systemic_therapies/`

*Create Systemic Therapies*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_systemic_therapies-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SystemicTherapyIngestSchema](#schemasystemictherapyingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_comorbidities

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_comorbidities"></a>

`POST /v3/ingest/comorbidities/`

*Create Comorbidities*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_comorbidities-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ComorbidityIngestSchema](#schemacomorbidityingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_exposures

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_exposures"></a>

`POST /v3/ingest/exposures/`

*Create Exposures*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_exposures-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ExposureIngestSchema](#schemaexposureingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_followups

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_followups"></a>

`POST /v3/ingest/followups/`

*Create Followups*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_followups-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[FollowUpIngestSchema](#schemafollowupingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_primary_diagnoses

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_primary_diagnoses"></a>

`POST /v3/ingest/primary_diagnoses/`

*Create Primary Diagnoses*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_primary_diagnoses-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PrimaryDiagnosisIngestSchema](#schemaprimarydiagnosisingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_radiations

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_radiations"></a>

`POST /v3/ingest/radiations/`

*Create Radiations*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_radiations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RadiationIngestSchema](#schemaradiationingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_radiopharmaceutical_therapies

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_radiopharmaceutical_therapies"></a>

`POST /v3/ingest/radiopharmaceutical_therapies/`

*Create Radiopharmaceutical Therapies*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_radiopharmaceutical_therapies-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RadiopharmaceuticalTherapyIngestSchema](#schemaradiopharmaceuticaltherapyingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_sample_registrations

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_sample_registrations"></a>

`POST /v3/ingest/sample_registrations/`

*Create Sample Registrations*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_sample_registrations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SampleRegistrationIngestSchema](#schemasampleregistrationingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_specimens

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_specimens"></a>

`POST /v3/ingest/specimens/`

*Create Specimens*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_specimens-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SpecimenIngestSchema](#schemaspecimeningestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_surgeries

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_surgeries"></a>

`POST /v3/ingest/surgeries/`

*Create Surgeries*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_surgeries-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SurgeryIngestSchema](#schemasurgeryingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_create_treatments

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_create_treatments"></a>

`POST /v3/ingest/treatments/`

*Create Treatments*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_create_treatments-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TreatmentIngestSchema](#schematreatmentingestschema)|true|none|

## chord_metadata_service_mohpackets_apis_ingestion_delete_program

<a id="opIdchord_metadata_service_mohpackets_apis_ingestion_delete_program"></a>

`DELETE /v3/ingest/program/{program_id}/`

*Delete Program*

<h3 id="chord_metadata_service_mohpackets_apis_ingestion_delete_program-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|path|string|true|none|

> Example responses

> 404 Response

```json
{
  "property1": "string",
  "property2": "string"
}
```

## chord_metadata_service_mohpackets_apis_update_update_program

<a id="opIdchord_metadata_service_mohpackets_apis_update_update_program"></a>

`PATCH /v3/ingest/programs/{program_id}/`

*Update Program*

Partially update a Program's clinical fields.

Only the fields present in the request body are modified; the metadata
field is excluded from ProgramUpdateSchema and is never touched here.

<h3 id="chord_metadata_service_mohpackets_apis_update_update_program-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|path|string|true|none|
|body|body|[ProgramUpdateSchema](#schemaprogramupdateschema)|true|none|

> Example responses

> 200 Response

```json
{
  "property1": "string",
  "property2": "string"
}
```

## chord_metadata_service_mohpackets_apis_update_update_program_metadata

<a id="opIdchord_metadata_service_mohpackets_apis_update_update_program_metadata"></a>

`PATCH /v3/ingest/programs/{program_id}/metadata/`

*Update Program Metadata*

Update a Program's metadata field. Restricted to the ingest service token.

<h3 id="chord_metadata_service_mohpackets_apis_update_update_program_metadata-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|path|string|true|none|
|body|body|[MetadataSchema](#schemametadataschema)|true|none|

> Example responses

> 200 Response

```json
{
  "property1": "string",
  "property2": "string"
}
```

<h1 id="moh-service-api-authorized">authorized</h1>

## chord_metadata_service_mohpackets_apis_authorized_get_donor_with_clinical_data

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_get_donor_with_clinical_data"></a>

`GET /v3/authorized/donor_with_clinical_data/program/{program_id}/donor/{donor_id}`

*Get Donor With Clinical Data*

Retrieves a single donor along with all related clinical data, organized in a nested JSON format.

<h3 id="chord_metadata_service_mohpackets_apis_authorized_get_donor_with_clinical_data-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|path|string|true|none|
|donor_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "submitter_donor_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "is_deceased": "Yes",
  "lost_to_follow_up": "Yes",
  "lost_to_followup_reason": "Completed study",
  "cause_of_death": "Died of cancer",
  "date_of_birth": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death_is_estimated": "Yes",
  "date_resolution": "string",
  "program_id": "string",
  "primary_diagnoses": [
    {
      "submitter_primary_diagnosis_id": "string",
      "primary_site": "Accessory sinuses",
      "date_of_diagnosis": {
        "day_interval": 0,
        "month_interval": 0
      },
      "cancer_type_code": "string",
      "basis_of_diagnosis": "Clinical investigation",
      "laterality": "Bilateral",
      "clinical_tumour_staging_system": "AJCC cancer staging system",
      "clinical_t_category": "T0",
      "clinical_n_category": "N0",
      "clinical_m_category": "M0",
      "clinical_stage_group": "Stage 0",
      "pathological_tumour_staging_system": "AJCC cancer staging system",
      "pathological_t_category": "T0",
      "pathological_n_category": "N0",
      "pathological_m_category": "M0",
      "pathological_stage_group": "Stage 0",
      "specimens": [
        {
          "submitter_specimen_id": "string",
          "submitter_treatment_id": "string",
          "specimen_collection_date": {},
          "specimen_storage": "Cut slide",
          "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
          "tumour_histological_type": "string",
          "specimen_anatomic_location": "string",
          "specimen_laterality": "Left",
          "reference_pathology_confirmed_diagnosis": "Yes",
          "reference_pathology_confirmed_tumour_presence": "Yes",
          "tumour_grading_system": "FNCLCC grading system",
          "tumour_grade": "Low grade",
          "percent_tumour_cells_range": "0-19%",
          "percent_tumour_cells_measurement_method": "Genomics",
          "specimen_tissue_source": "Abdominal fluid",
          "tumour_normal_designation": "Normal",
          "specimen_type": "Cell line - derived from normal",
          "sample_registrations": [
            {
              "submitter_sample_id": "string",
              "sample_type": "Amplified DNA"
            }
          ]
        }
      ],
      "treatments": [
        {
          "submitter_treatment_id": "string",
          "treatment_type": [
            "Bone marrow transplant"
          ],
          "is_primary_treatment": "Yes",
          "treatment_start_date": {
            "day_interval": 0,
            "month_interval": 0
          },
          "treatment_end_date": {
            "day_interval": 0,
            "month_interval": 0
          },
          "treatment_intent": "Curative",
          "treatment_setting": "Adjuvant",
          "response_to_treatment_criteria_method": "RECIST 1.1",
          "response_to_treatment": "Complete response",
          "status_of_treatment": "Treatment completed as prescribed",
          "systemic_therapies": [
            {
              "systemic_therapy_type": "string",
              "days_per_cycle": 0,
              "days_per_cycle_not_available": false,
              "number_of_cycles": 0,
              "number_of_cycles_not_available": false,
              "start_date": {},
              "end_date": {},
              "drug_reference_database": "RxNorm",
              "drug_name": "string",
              "drug_reference_identifier": "string",
              "drug_dose_units": "mg/m2",
              "prescribed_cumulative_drug_dose": 0,
              "prescribed_cumulative_drug_dose_not_available": false,
              "actual_cumulative_drug_dose": 0,
              "actual_cumulative_drug_dose_not_available": false
            }
          ],
          "radiations": [
            {
              "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
              "radiation_therapy_type": "External",
              "radiation_therapy_fractions": 0,
              "radiation_therapy_fractions_not_available": false,
              "radiation_therapy_dosage": 0,
              "radiation_therapy_dosage_not_available": false,
              "anatomical_site_irradiated": "ABDOMEN_WHOLE",
              "radiation_boost": "Yes",
              "reference_radiation_treatment_id": "string"
            }
          ],
          "surgeries": [
            {
              "surgery_type": "string",
              "surgery_site": "string",
              "surgery_location": "Local recurrence",
              "tumour_length": 0,
              "tumour_length_not_available": false,
              "tumour_width": 0,
              "tumour_width_not_available": false,
              "greatest_dimension_tumour": 0,
              "greatest_dimension_tumour_not_available": false,
              "tumour_focality": "Cannot be assessed",
              "residual_tumour_classification": "Not applicable",
              "margins_status": "Margins clear",
              "lymphovascular_invasion": "Absent",
              "perineural_invasion": "Absent",
              "surgery_reference_database": "SNOMED",
              "surgery_reference_identifier": "string"
            }
          ],
          "radiopharmaceutical_therapies": [
            {
              "rxnorm_code": "string",
              "agent_name": "string",
              "radionuclide": "Carbon-14",
              "radionuclide_other": "string",
              "start_date": {},
              "end_date": {},
              "cumulative_drug_dose": 0,
              "cumulative_drug_dose_not_available": false,
              "drug_dose_units": "Bq",
              "mass_value": 0,
              "mass_value_not_available": false,
              "mass_unit_ucum": "ug",
              "number_of_cycles": 0,
              "number_of_cycles_not_available": false
            }
          ],
          "followups": [
            {
              "submitter_follow_up_id": "string",
              "date_of_followup": {
                "day_interval": 0,
                "month_interval": 0
              },
              "disease_status_at_followup": "Complete remission",
              "relapse_type": "Distant recurrence/metastasis",
              "date_of_relapse": {
                "day_interval": 0,
                "month_interval": 0
              },
              "method_of_progression_status": [
                "Imaging (procedure)"
              ],
              "anatomic_site_progression_or_recurrence": [
                "string"
              ]
            }
          ]
        }
      ],
      "followups": [
        {
          "submitter_follow_up_id": "string",
          "date_of_followup": {
            "day_interval": 0,
            "month_interval": 0
          },
          "disease_status_at_followup": "Complete remission",
          "relapse_type": "Distant recurrence/metastasis",
          "date_of_relapse": {
            "day_interval": 0,
            "month_interval": 0
          },
          "method_of_progression_status": [
            "Imaging (procedure)"
          ],
          "anatomic_site_progression_or_recurrence": [
            "string"
          ]
        }
      ]
    }
  ],
  "followups": [
    {
      "submitter_follow_up_id": "string",
      "date_of_followup": {
        "day_interval": 0,
        "month_interval": 0
      },
      "disease_status_at_followup": "Complete remission",
      "relapse_type": "Distant recurrence/metastasis",
      "date_of_relapse": {
        "day_interval": 0,
        "month_interval": 0
      },
      "method_of_progression_status": [
        "Imaging (procedure)"
      ],
      "anatomic_site_progression_or_recurrence": [
        "string"
      ]
    }
  ],
  "biomarkers": [
    {
      "submitter_specimen_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string",
      "submitter_follow_up_id": "string",
      "test_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "psa_level": 0,
      "psa_level_not_available": false,
      "ca125": 0,
      "ca125_not_available": false,
      "cea": 0,
      "cea_not_available": false,
      "ca19_9": 0,
      "ca19_9_not_available": false,
      "er_status": "Cannot be determined",
      "er_percent_positive": 0,
      "er_percent_positive_not_available": false,
      "pr_status": "Cannot be determined",
      "pr_percent_positive": 0,
      "pr_percent_positive_not_available": false,
      "her2_ihc_status": "Cannot be determined",
      "her2_ish_status": "Cannot be determined",
      "hpv_ihc_status": "Cannot be determined",
      "hpv_pcr_status": "Cannot be determined",
      "hpv_strain": [
        "HPV16"
      ]
    }
  ],
  "exposures": [
    {
      "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
      "tobacco_type": [
        "Chewing Tobacco"
      ],
      "pack_years_smoked": 0,
      "pack_years_smoked_not_available": false
    }
  ],
  "comorbidities": [
    {
      "prior_malignancy": "Yes",
      "laterality_of_prior_malignancy": "Bilateral",
      "age_at_comorbidity_diagnosis": 0,
      "age_at_comorbidity_diagnosis_not_available": false,
      "comorbidity_type_code": "string",
      "comorbidity_treatment_status": "Yes",
      "comorbidity_treatment": "string"
    }
  ]
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_programs

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_programs"></a>

`GET /v3/authorized/programs/`

*List Programs*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_programs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "program_id": "string",
      "metadata": {},
      "program_description": "string",
      "program_name": "string",
      "keywords": [
        null
      ],
      "status": "Ongoing",
      "context": "Clinical",
      "participant_criteria": "string",
      "principal_investigators": [
        null
      ],
      "lead_organizations": [
        null
      ],
      "collaborators": [
        null
      ],
      "funding_sources": [
        null
      ],
      "publication_links": [
        null
      ],
      "program_url": "string",
      "pancan_cohort": "Yes",
      "pancan_id": "string",
      "created": "2019-08-24T14:15:22Z",
      "updated": "2019-08-24T14:15:22Z"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_donors

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_donors"></a>

`GET /v3/authorized/donors/`

*List Donors*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_donors-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_donor_id|query|any|false|none|
|program_id|query|any|false|none|
|gender|query|any|false|none|
|sex_at_birth|query|any|false|none|
|is_deceased|query|any|false|none|
|lost_to_follow_up|query|any|false|none|
|lost_to_followup_reason|query|any|false|none|
|cause_of_death|query|any|false|none|
|date_of_death_is_estimated|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "submitter_donor_id": "string",
      "gender": "Man",
      "sex_at_birth": "Male",
      "is_deceased": "Yes",
      "lost_to_follow_up": "Yes",
      "lost_to_followup_reason": "Completed study",
      "cause_of_death": "Died of cancer",
      "date_of_birth": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death_is_estimated": "Yes",
      "date_resolution": "string",
      "program_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_query_donors

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_query_donors"></a>

`GET /v3/authorized/query/`

*Query Donors*

Used by the query service to return donors along with their sample IDs, treatment types, and primary sites.

<h3 id="chord_metadata_service_mohpackets_apis_authorized_query_donors-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|treatment_type|query|array[string]|false|none|
|primary_site|query|array[string]|false|none|
|systemic_therapy_drug_name|query|array[string]|false|none|
|exclude_programs|query|array[string]|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "submitter_donor_id": "string",
      "gender": "Man",
      "sex_at_birth": "Male",
      "is_deceased": "Yes",
      "lost_to_follow_up": "Yes",
      "lost_to_followup_reason": "Completed study",
      "cause_of_death": "Died of cancer",
      "date_of_birth": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death_is_estimated": "Yes",
      "date_resolution": "string",
      "program_id": "string",
      "primary_site": [
        "string"
      ],
      "treatment_type": [
        "string"
      ],
      "submitter_sample_ids": [
        "string"
      ]
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_primary_diagnoses

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_primary_diagnoses"></a>

`GET /v3/authorized/primary_diagnoses/`

*List Primary Diagnoses*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_primary_diagnoses-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|query|any|false|none|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|cancer_type_code|query|any|false|none|
|basis_of_diagnosis|query|any|false|none|
|laterality|query|any|false|none|
|clinical_tumour_staging_system|query|any|false|none|
|clinical_t_category|query|any|false|none|
|clinical_n_category|query|any|false|none|
|clinical_m_category|query|any|false|none|
|clinical_stage_group|query|any|false|none|
|primary_site|query|any|false|none|
|pathological_tumour_staging_system|query|any|false|none|
|pathological_t_category|query|any|false|none|
|pathological_n_category|query|any|false|none|
|pathological_m_category|query|any|false|none|
|pathological_stage_group|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "submitter_primary_diagnosis_id": "string",
      "primary_site": "Accessory sinuses",
      "date_of_diagnosis": {
        "day_interval": 0,
        "month_interval": 0
      },
      "cancer_type_code": "string",
      "basis_of_diagnosis": "Clinical investigation",
      "laterality": "Bilateral",
      "clinical_tumour_staging_system": "AJCC cancer staging system",
      "clinical_t_category": "T0",
      "clinical_n_category": "N0",
      "clinical_m_category": "M0",
      "clinical_stage_group": "Stage 0",
      "pathological_tumour_staging_system": "AJCC cancer staging system",
      "pathological_t_category": "T0",
      "pathological_n_category": "N0",
      "pathological_m_category": "M0",
      "pathological_stage_group": "Stage 0",
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_biomarkers

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_biomarkers"></a>

`GET /v3/authorized/biomarkers/`

*List Biomarkers*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_biomarkers-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|submitter_specimen_id|query|any|false|none|
|submitter_primary_diagnosis_id|query|any|false|none|
|submitter_treatment_id|query|any|false|none|
|submitter_follow_up_id|query|any|false|none|
|psa_level|query|any|false|none|
|ca125|query|any|false|none|
|cea|query|any|false|none|
|ca19_9|query|any|false|none|
|er_status|query|any|false|none|
|er_percent_positive|query|any|false|none|
|pr_status|query|any|false|none|
|pr_percent_positive|query|any|false|none|
|her2_ihc_status|query|any|false|none|
|her2_ish_status|query|any|false|none|
|hpv_ihc_status|query|any|false|none|
|hpv_pcr_status|query|any|false|none|
|hpv_strain|query|array[string]|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "submitter_specimen_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string",
      "submitter_follow_up_id": "string",
      "test_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "psa_level": 0,
      "psa_level_not_available": false,
      "ca125": 0,
      "ca125_not_available": false,
      "cea": 0,
      "cea_not_available": false,
      "ca19_9": 0,
      "ca19_9_not_available": false,
      "er_status": "Cannot be determined",
      "er_percent_positive": 0,
      "er_percent_positive_not_available": false,
      "pr_status": "Cannot be determined",
      "pr_percent_positive": 0,
      "pr_percent_positive_not_available": false,
      "her2_ihc_status": "Cannot be determined",
      "her2_ish_status": "Cannot be determined",
      "hpv_ihc_status": "Cannot be determined",
      "hpv_pcr_status": "Cannot be determined",
      "hpv_strain": [
        "HPV16"
      ],
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_systemic_therapies

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_systemic_therapies"></a>

`GET /v3/authorized/systemic_therapies/`

*List Systemic Therapies*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_systemic_therapies-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|submitter_treatment_id|query|any|false|none|
|drug_reference_database|query|any|false|none|
|drug_name|query|any|false|none|
|drug_reference_identifier|query|any|false|none|
|drug_dose_units|query|any|false|none|
|prescribed_cumulative_drug_dose|query|any|false|none|
|actual_cumulative_drug_dose|query|any|false|none|
|days_per_cycle|query|any|false|none|
|number_of_cycles|query|any|false|none|
|systemic_therapy_type|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "systemic_therapy_type": "string",
      "days_per_cycle": 0,
      "days_per_cycle_not_available": false,
      "number_of_cycles": 0,
      "number_of_cycles_not_available": false,
      "start_date": {},
      "end_date": {},
      "drug_reference_database": "RxNorm",
      "drug_name": "string",
      "drug_reference_identifier": "string",
      "drug_dose_units": "mg/m2",
      "prescribed_cumulative_drug_dose": 0,
      "prescribed_cumulative_drug_dose_not_available": false,
      "actual_cumulative_drug_dose": 0,
      "actual_cumulative_drug_dose_not_available": false,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_comorbidities

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_comorbidities"></a>

`GET /v3/authorized/comorbidities/`

*List Comorbidities*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_comorbidities-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|prior_malignancy|query|any|false|none|
|laterality_of_prior_malignancy|query|any|false|none|
|age_at_comorbidity_diagnosis|query|any|false|none|
|comorbidity_type_code|query|any|false|none|
|comorbidity_treatment_status|query|any|false|none|
|comorbidity_treatment|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "prior_malignancy": "Yes",
      "laterality_of_prior_malignancy": "Bilateral",
      "age_at_comorbidity_diagnosis": 0,
      "age_at_comorbidity_diagnosis_not_available": false,
      "comorbidity_type_code": "string",
      "comorbidity_treatment_status": "Yes",
      "comorbidity_treatment": "string",
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_exposures

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_exposures"></a>

`GET /v3/authorized/exposures/`

*List Exposures*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_exposures-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|tobacco_smoking_status|query|any|false|none|
|tobacco_type|query|array[string]|false|none|
|pack_years_smoked|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
      "tobacco_type": [
        "Chewing Tobacco"
      ],
      "pack_years_smoked": 0,
      "pack_years_smoked_not_available": false,
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_follow_ups

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_follow_ups"></a>

`GET /v3/authorized/follow_ups/`

*List Follow Ups*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_follow_ups-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_follow_up_id|query|any|false|none|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|submitter_primary_diagnosis_id|query|any|false|none|
|submitter_treatment_id|query|any|false|none|
|disease_status_at_followup|query|any|false|none|
|relapse_type|query|any|false|none|
|method_of_progression_status|query|array[string]|false|none|
|anatomic_site_progression_or_recurrence|query|array[string]|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "submitter_follow_up_id": "string",
      "date_of_followup": {
        "day_interval": 0,
        "month_interval": 0
      },
      "disease_status_at_followup": "Complete remission",
      "relapse_type": "Distant recurrence/metastasis",
      "date_of_relapse": {
        "day_interval": 0,
        "month_interval": 0
      },
      "method_of_progression_status": [
        "Imaging (procedure)"
      ],
      "anatomic_site_progression_or_recurrence": [
        "string"
      ],
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_radiations

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_radiations"></a>

`GET /v3/authorized/radiations/`

*List Radiations*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_radiations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|submitter_treatment_id|query|any|false|none|
|radiation_therapy_modality|query|any|false|none|
|radiation_therapy_type|query|any|false|none|
|radiation_therapy_fractions|query|any|false|none|
|radiation_therapy_dosage|query|any|false|none|
|anatomical_site_irradiated|query|any|false|none|
|radiation_boost|query|any|false|none|
|reference_radiation_treatment_id|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
      "radiation_therapy_type": "External",
      "radiation_therapy_fractions": 0,
      "radiation_therapy_fractions_not_available": false,
      "radiation_therapy_dosage": 0,
      "radiation_therapy_dosage_not_available": false,
      "anatomical_site_irradiated": "ABDOMEN_WHOLE",
      "radiation_boost": "Yes",
      "reference_radiation_treatment_id": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_radiopharmaceutical_therapies

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_radiopharmaceutical_therapies"></a>

`GET /v3/authorized/radiopharmaceutical_therapies/`

*List Radiopharmaceutical Therapies*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_radiopharmaceutical_therapies-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|submitter_treatment_id|query|any|false|none|
|rxnorm_code|query|any|false|none|
|agent_name|query|any|false|none|
|radionuclide|query|any|false|none|
|radionuclide_other|query|any|false|none|
|cumulative_drug_dose|query|any|false|none|
|drug_dose_units|query|any|false|none|
|mass_value|query|any|false|none|
|mass_unit_ucum|query|any|false|none|
|number_of_cycles|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "rxnorm_code": "string",
      "agent_name": "string",
      "radionuclide": "Carbon-14",
      "radionuclide_other": "string",
      "start_date": {},
      "end_date": {},
      "cumulative_drug_dose": 0,
      "cumulative_drug_dose_not_available": false,
      "drug_dose_units": "Bq",
      "mass_value": 0,
      "mass_value_not_available": false,
      "mass_unit_ucum": "ug",
      "number_of_cycles": 0,
      "number_of_cycles_not_available": false,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_sample_registrations

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_sample_registrations"></a>

`GET /v3/authorized/sample_registrations/`

*List Sample Registrations*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_sample_registrations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_sample_id|query|any|false|none|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|submitter_specimen_id|query|any|false|none|
|sample_type|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "submitter_sample_id": "string",
      "sample_type": "Amplified DNA",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_specimen_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_specimens

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_specimens"></a>

`GET /v3/authorized/specimens/`

*List Specimens*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_specimens-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_specimen_id|query|any|false|none|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|submitter_primary_diagnosis_id|query|any|false|none|
|submitter_treatment_id|query|any|false|none|
|specimen_storage|query|any|false|none|
|specimen_processing|query|any|false|none|
|tumour_histological_type|query|any|false|none|
|specimen_anatomic_location|query|any|false|none|
|specimen_laterality|query|any|false|none|
|reference_pathology_confirmed_diagnosis|query|any|false|none|
|reference_pathology_confirmed_tumour_presence|query|any|false|none|
|tumour_grading_system|query|any|false|none|
|tumour_grade|query|any|false|none|
|percent_tumour_cells_range|query|any|false|none|
|percent_tumour_cells_measurement_method|query|any|false|none|
|specimen_tissue_source|query|any|false|none|
|tumour_normal_designation|query|any|false|none|
|specimen_type|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "submitter_specimen_id": "string",
      "submitter_treatment_id": "string",
      "specimen_collection_date": {},
      "specimen_storage": "Cut slide",
      "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
      "tumour_histological_type": "string",
      "specimen_anatomic_location": "string",
      "specimen_laterality": "Left",
      "reference_pathology_confirmed_diagnosis": "Yes",
      "reference_pathology_confirmed_tumour_presence": "Yes",
      "tumour_grading_system": "FNCLCC grading system",
      "tumour_grade": "Low grade",
      "percent_tumour_cells_range": "0-19%",
      "percent_tumour_cells_measurement_method": "Genomics",
      "specimen_tissue_source": "Abdominal fluid",
      "tumour_normal_designation": "Normal",
      "specimen_type": "Cell line - derived from normal",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_surgeries

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_surgeries"></a>

`GET /v3/authorized/surgeries/`

*List Surgeries*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_surgeries-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|submitter_treatment_id|query|any|false|none|
|surgery_type|query|any|false|none|
|surgery_site|query|any|false|none|
|surgery_location|query|any|false|none|
|tumour_length|query|any|false|none|
|tumour_width|query|any|false|none|
|greatest_dimension_tumour|query|any|false|none|
|tumour_focality|query|any|false|none|
|residual_tumour_classification|query|any|false|none|
|margins_status|query|any|false|none|
|lymphovascular_invasion|query|any|false|none|
|perineural_invasion|query|any|false|none|
|surgery_reference_database|query|any|false|none|
|surgery_reference_identifier|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "surgery_type": "string",
      "surgery_site": "string",
      "surgery_location": "Local recurrence",
      "tumour_length": 0,
      "tumour_length_not_available": false,
      "tumour_width": 0,
      "tumour_width_not_available": false,
      "greatest_dimension_tumour": 0,
      "greatest_dimension_tumour_not_available": false,
      "tumour_focality": "Cannot be assessed",
      "residual_tumour_classification": "Not applicable",
      "margins_status": "Margins clear",
      "lymphovascular_invasion": "Absent",
      "perineural_invasion": "Absent",
      "surgery_reference_database": "SNOMED",
      "surgery_reference_identifier": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

## chord_metadata_service_mohpackets_apis_authorized_list_treatments

<a id="opIdchord_metadata_service_mohpackets_apis_authorized_list_treatments"></a>

`GET /v3/authorized/treatments/`

*List Treatments*

<h3 id="chord_metadata_service_mohpackets_apis_authorized_list_treatments-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_treatment_id|query|any|false|none|
|program_id|query|any|false|none|
|submitter_donor_id|query|any|false|none|
|submitter_primary_diagnosis_id|query|any|false|none|
|treatment_type|query|any|false|none|
|is_primary_treatment|query|any|false|none|
|treatment_intent|query|any|false|none|
|treatment_setting|query|any|false|none|
|response_to_treatment_criteria_method|query|any|false|none|
|response_to_treatment|query|any|false|none|
|status_of_treatment|query|any|false|none|
|page|query|integer|false|none|
|page_size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "submitter_treatment_id": "string",
      "treatment_type": [
        "Bone marrow transplant"
      ],
      "is_primary_treatment": "Yes",
      "treatment_start_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "treatment_end_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "treatment_intent": "Curative",
      "treatment_setting": "Adjuvant",
      "response_to_treatment_criteria_method": "RECIST 1.1",
      "response_to_treatment": "Complete response",
      "status_of_treatment": "Treatment completed as prescribed",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}
```

<h1 id="moh-service-api-download">download</h1>

## chord_metadata_service_mohpackets_apis_download_search_clinical_data

<a id="opIdchord_metadata_service_mohpackets_apis_download_search_clinical_data"></a>

`POST /v3/download/clinical_data/`

*Search Clinical Data*

Filters clinical data based on criteria provided in the POST request
body. Returns record counts and optionally the detailed data based
on the 'summary_only' flag.

<h3 id="chord_metadata_service_mohpackets_apis_download_search_clinical_data-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DownloadFilterSchema](#schemadownloadfilterschema)|true|none|

> Example responses

> 200 Response

```json
{
  "summary": {
    "message": "string",
    "record_counts": {
      "property1": 0,
      "property2": 0
    }
  },
  "data": {
    "donors": [
      {
        "submitter_donor_id": "string",
        "gender": "Man",
        "sex_at_birth": "Male",
        "is_deceased": "Yes",
        "lost_to_follow_up": "Yes",
        "lost_to_followup_reason": "Completed study",
        "cause_of_death": "Died of cancer",
        "date_of_birth": {
          "day_interval": 0,
          "month_interval": 0
        },
        "date_of_death": {
          "day_interval": 0,
          "month_interval": 0
        },
        "date_of_death_is_estimated": "Yes",
        "date_resolution": "string",
        "program_id": "string"
      }
    ],
    "primary_diagnoses": [
      {
        "submitter_primary_diagnosis_id": "string",
        "primary_site": "Accessory sinuses",
        "date_of_diagnosis": {
          "day_interval": 0,
          "month_interval": 0
        },
        "cancer_type_code": "string",
        "basis_of_diagnosis": "Clinical investigation",
        "laterality": "Bilateral",
        "clinical_tumour_staging_system": "AJCC cancer staging system",
        "clinical_t_category": "T0",
        "clinical_n_category": "N0",
        "clinical_m_category": "M0",
        "clinical_stage_group": "Stage 0",
        "pathological_tumour_staging_system": "AJCC cancer staging system",
        "pathological_t_category": "T0",
        "pathological_n_category": "N0",
        "pathological_m_category": "M0",
        "pathological_stage_group": "Stage 0",
        "program_id": "string",
        "submitter_donor_id": "string"
      }
    ],
    "specimens": [
      {
        "submitter_specimen_id": "string",
        "submitter_treatment_id": "string",
        "specimen_collection_date": {},
        "specimen_storage": "Cut slide",
        "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
        "tumour_histological_type": "string",
        "specimen_anatomic_location": "string",
        "specimen_laterality": "Left",
        "reference_pathology_confirmed_diagnosis": "Yes",
        "reference_pathology_confirmed_tumour_presence": "Yes",
        "tumour_grading_system": "FNCLCC grading system",
        "tumour_grade": "Low grade",
        "percent_tumour_cells_range": "0-19%",
        "percent_tumour_cells_measurement_method": "Genomics",
        "specimen_tissue_source": "Abdominal fluid",
        "tumour_normal_designation": "Normal",
        "specimen_type": "Cell line - derived from normal",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_primary_diagnosis_id": "string"
      }
    ],
    "sample_registrations": [
      {
        "submitter_sample_id": "string",
        "sample_type": "Amplified DNA",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_specimen_id": "string"
      }
    ],
    "treatments": [
      {
        "submitter_treatment_id": "string",
        "treatment_type": [
          "Bone marrow transplant"
        ],
        "is_primary_treatment": "Yes",
        "treatment_start_date": {
          "day_interval": 0,
          "month_interval": 0
        },
        "treatment_end_date": {
          "day_interval": 0,
          "month_interval": 0
        },
        "treatment_intent": "Curative",
        "treatment_setting": "Adjuvant",
        "response_to_treatment_criteria_method": "RECIST 1.1",
        "response_to_treatment": "Complete response",
        "status_of_treatment": "Treatment completed as prescribed",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_primary_diagnosis_id": "string"
      }
    ],
    "systemic_therapies": [
      {
        "systemic_therapy_type": "string",
        "days_per_cycle": 0,
        "days_per_cycle_not_available": false,
        "number_of_cycles": 0,
        "number_of_cycles_not_available": false,
        "start_date": {},
        "end_date": {},
        "drug_reference_database": "RxNorm",
        "drug_name": "string",
        "drug_reference_identifier": "string",
        "drug_dose_units": "mg/m2",
        "prescribed_cumulative_drug_dose": 0,
        "prescribed_cumulative_drug_dose_not_available": false,
        "actual_cumulative_drug_dose": 0,
        "actual_cumulative_drug_dose_not_available": false,
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "radiations": [
      {
        "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
        "radiation_therapy_type": "External",
        "radiation_therapy_fractions": 0,
        "radiation_therapy_fractions_not_available": false,
        "radiation_therapy_dosage": 0,
        "radiation_therapy_dosage_not_available": false,
        "anatomical_site_irradiated": "ABDOMEN_WHOLE",
        "radiation_boost": "Yes",
        "reference_radiation_treatment_id": "string",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "radiopharmaceutical_therapies": [
      {
        "rxnorm_code": "string",
        "agent_name": "string",
        "radionuclide": "Carbon-14",
        "radionuclide_other": "string",
        "start_date": {},
        "end_date": {},
        "cumulative_drug_dose": 0,
        "cumulative_drug_dose_not_available": false,
        "drug_dose_units": "Bq",
        "mass_value": 0,
        "mass_value_not_available": false,
        "mass_unit_ucum": "ug",
        "number_of_cycles": 0,
        "number_of_cycles_not_available": false,
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "surgeries": [
      {
        "surgery_type": "string",
        "surgery_site": "string",
        "surgery_location": "Local recurrence",
        "tumour_length": 0,
        "tumour_length_not_available": false,
        "tumour_width": 0,
        "tumour_width_not_available": false,
        "greatest_dimension_tumour": 0,
        "greatest_dimension_tumour_not_available": false,
        "tumour_focality": "Cannot be assessed",
        "residual_tumour_classification": "Not applicable",
        "margins_status": "Margins clear",
        "lymphovascular_invasion": "Absent",
        "perineural_invasion": "Absent",
        "surgery_reference_database": "SNOMED",
        "surgery_reference_identifier": "string",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "follow_ups": [
      {
        "submitter_follow_up_id": "string",
        "date_of_followup": {
          "day_interval": 0,
          "month_interval": 0
        },
        "disease_status_at_followup": "Complete remission",
        "relapse_type": "Distant recurrence/metastasis",
        "date_of_relapse": {
          "day_interval": 0,
          "month_interval": 0
        },
        "method_of_progression_status": [
          "Imaging (procedure)"
        ],
        "anatomic_site_progression_or_recurrence": [
          "string"
        ],
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_primary_diagnosis_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "biomarkers": [
      {
        "submitter_specimen_id": "string",
        "submitter_primary_diagnosis_id": "string",
        "submitter_treatment_id": "string",
        "submitter_follow_up_id": "string",
        "test_date": {
          "day_interval": 0,
          "month_interval": 0
        },
        "psa_level": 0,
        "psa_level_not_available": false,
        "ca125": 0,
        "ca125_not_available": false,
        "cea": 0,
        "cea_not_available": false,
        "ca19_9": 0,
        "ca19_9_not_available": false,
        "er_status": "Cannot be determined",
        "er_percent_positive": 0,
        "er_percent_positive_not_available": false,
        "pr_status": "Cannot be determined",
        "pr_percent_positive": 0,
        "pr_percent_positive_not_available": false,
        "her2_ihc_status": "Cannot be determined",
        "her2_ish_status": "Cannot be determined",
        "hpv_ihc_status": "Cannot be determined",
        "hpv_pcr_status": "Cannot be determined",
        "hpv_strain": [
          "HPV16"
        ],
        "program_id": "string",
        "submitter_donor_id": "string"
      }
    ],
    "comorbidities": [
      {
        "prior_malignancy": "Yes",
        "laterality_of_prior_malignancy": "Bilateral",
        "age_at_comorbidity_diagnosis": 0,
        "age_at_comorbidity_diagnosis_not_available": false,
        "comorbidity_type_code": "string",
        "comorbidity_treatment_status": "Yes",
        "comorbidity_treatment": "string",
        "program_id": "string",
        "submitter_donor_id": "string"
      }
    ],
    "exposures": [
      {
        "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
        "tobacco_type": [
          "Chewing Tobacco"
        ],
        "pack_years_smoked": 0,
        "pack_years_smoked_not_available": false,
        "program_id": "string",
        "submitter_donor_id": "string"
      }
    ]
  }
}
```

<h1 id="moh-service-api-explorer">explorer</h1>

## chord_metadata_service_mohpackets_apis_discovery_explorer_donor

<a id="opIdchord_metadata_service_mohpackets_apis_discovery_explorer_donor"></a>

`GET /v3/explorer/donors/`

*Explorer Donor*

Returns a list of donors with their sample IDs, treatment types, age, and primary site.
This endpoint is called by the query service and bypasses user authorization.

<h3 id="chord_metadata_service_mohpackets_apis_discovery_explorer_donor-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|treatment_type|query|array[string]|false|none|
|primary_site|query|array[string]|false|none|
|systemic_therapy_drug_name|query|array[string]|false|none|
|exclude_programs|query|array[string]|false|none|

> Example responses

> 200 Response

```json
[
  {
    "program_id": "string",
    "submitter_donor_id": "string",
    "submitter_sample_ids": [
      "string"
    ],
    "primary_site": [
      "string"
    ],
    "treatment_type": [
      "string"
    ],
    "age_at_diagnosis": "string"
  }
]
```

# Schemas

<h2 id="tocS_ProgramDiscoverySchema">ProgramDiscoverySchema</h2>

<a id="schemaprogramdiscoveryschema"></a>
<a id="schema_ProgramDiscoverySchema"></a>
<a id="tocSprogramdiscoveryschema"></a>
<a id="tocsprogramdiscoveryschema"></a>

```json
{
  "program_id": "string",
  "metadata": null
}

```

ProgramDiscoverySchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|metadata|any|true|none|none|

<h2 id="tocS_PatientPerProgramSchema">PatientPerProgramSchema</h2>

<a id="schemapatientperprogramschema"></a>
<a id="schema_PatientPerProgramSchema"></a>
<a id="tocSpatientperprogramschema"></a>
<a id="tocspatientperprogramschema"></a>

```json
{
  "program_id": "string",
  "patients_count": "string"
}

```

PatientPerProgramSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|patients_count|string|true|none|none|

<h2 id="tocS_GenderCountSchema">GenderCountSchema</h2>

<a id="schemagendercountschema"></a>
<a id="schema_GenderCountSchema"></a>
<a id="tocSgendercountschema"></a>
<a id="tocsgendercountschema"></a>

```json
{
  "gender": "string",
  "gender_count": "string"
}

```

GenderCountSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|gender|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|gender_count|string|true|none|none|

<h2 id="tocS_PrimarySiteCountSchema">PrimarySiteCountSchema</h2>

<a id="schemaprimarysitecountschema"></a>
<a id="schema_PrimarySiteCountSchema"></a>
<a id="tocSprimarysitecountschema"></a>
<a id="tocsprimarysitecountschema"></a>

```json
{
  "primary_site_name": "string",
  "primary_site_count": "string"
}

```

PrimarySiteCountSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_site_name|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_site_count|string|true|none|none|

<h2 id="tocS_TreatmentTypeCountSchema">TreatmentTypeCountSchema</h2>

<a id="schematreatmenttypecountschema"></a>
<a id="schema_TreatmentTypeCountSchema"></a>
<a id="tocStreatmenttypecountschema"></a>
<a id="tocstreatmenttypecountschema"></a>

```json
{
  "treatment_type_name": "string",
  "treatment_type_count": "string"
}

```

TreatmentTypeCountSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_type_name|string|true|none|none|
|treatment_type_count|string|true|none|none|

<h2 id="tocS_DiagnosisAgeCountSchema">DiagnosisAgeCountSchema</h2>

<a id="schemadiagnosisagecountschema"></a>
<a id="schema_DiagnosisAgeCountSchema"></a>
<a id="tocSdiagnosisagecountschema"></a>
<a id="tocsdiagnosisagecountschema"></a>

```json
{
  "age_at_diagnosis": "string",
  "age_count": "string"
}

```

DiagnosisAgeCountSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|age_at_diagnosis|string|true|none|none|
|age_count|string|true|none|none|

<h2 id="tocS_ContextEnum">ContextEnum</h2>

<a id="schemacontextenum"></a>
<a id="schema_ContextEnum"></a>
<a id="tocScontextenum"></a>
<a id="tocscontextenum"></a>

```json
"Clinical"

```

ContextEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ContextEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|ContextEnum|Clinical|
|ContextEnum|Research|

<h2 id="tocS_PancanCohortEnum">PancanCohortEnum</h2>

<a id="schemapancancohortenum"></a>
<a id="schema_PancanCohortEnum"></a>
<a id="tocSpancancohortenum"></a>
<a id="tocspancancohortenum"></a>

```json
"Yes"

```

PancanCohortEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|PancanCohortEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|PancanCohortEnum|Yes|
|PancanCohortEnum|No|

<h2 id="tocS_ProgramIngestSchema">ProgramIngestSchema</h2>

<a id="schemaprogramingestschema"></a>
<a id="schema_ProgramIngestSchema"></a>
<a id="tocSprogramingestschema"></a>
<a id="tocsprogramingestschema"></a>

```json
{
  "program_id": "string",
  "metadata": {},
  "program_description": "string",
  "program_name": "string",
  "keywords": [
    null
  ],
  "status": "Ongoing",
  "context": "Clinical",
  "participant_criteria": "string",
  "principal_investigators": [
    null
  ],
  "lead_organizations": [
    null
  ],
  "collaborators": [
    null
  ],
  "funding_sources": [
    null
  ],
  "publication_links": [
    null
  ],
  "program_url": "string",
  "pancan_cohort": "Yes",
  "pancan_id": "string",
  "created": "2019-08-24T14:15:22Z",
  "updated": "2019-08-24T14:15:22Z"
}

```

ProgramIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|metadata|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|keywords|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StatusEnum](#schemastatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|context|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ContextEnum](#schemacontextenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|participant_criteria|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|principal_investigators|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lead_organizations|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|collaborators|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|funding_sources|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publication_links|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_url|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pancan_cohort|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PancanCohortEnum](#schemapancancohortenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pancan_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|created|string(date-time)|false|none|none|
|updated|string(date-time)|false|none|none|

<h2 id="tocS_StatusEnum">StatusEnum</h2>

<a id="schemastatusenum"></a>
<a id="schema_StatusEnum"></a>
<a id="tocSstatusenum"></a>
<a id="tocsstatusenum"></a>

```json
"Ongoing"

```

StatusEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|StatusEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|StatusEnum|Ongoing|
|StatusEnum|Completed|

<h2 id="tocS_CauseOfDeathEnum">CauseOfDeathEnum</h2>

<a id="schemacauseofdeathenum"></a>
<a id="schema_CauseOfDeathEnum"></a>
<a id="tocScauseofdeathenum"></a>
<a id="tocscauseofdeathenum"></a>

```json
"Died of cancer"

```

CauseOfDeathEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|CauseOfDeathEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|CauseOfDeathEnum|Died of cancer|
|CauseOfDeathEnum|Died of other reasons|
|CauseOfDeathEnum|Not available|

<h2 id="tocS_DateInterval">DateInterval</h2>

<a id="schemadateinterval"></a>
<a id="schema_DateInterval"></a>
<a id="tocSdateinterval"></a>
<a id="tocsdateinterval"></a>

```json
{
  "day_interval": 0,
  "month_interval": 0
}

```

DateInterval

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|day_interval|any|false|none|number of days since first diagnosis|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|month_interval|integer|true|none|number of months since first diagnosis|

<h2 id="tocS_DateOfDeathIsEstimatedEnum">DateOfDeathIsEstimatedEnum</h2>

<a id="schemadateofdeathisestimatedenum"></a>
<a id="schema_DateOfDeathIsEstimatedEnum"></a>
<a id="tocSdateofdeathisestimatedenum"></a>
<a id="tocsdateofdeathisestimatedenum"></a>

```json
"Yes"

```

DateOfDeathIsEstimatedEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DateOfDeathIsEstimatedEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|DateOfDeathIsEstimatedEnum|Yes|
|DateOfDeathIsEstimatedEnum|No|
|DateOfDeathIsEstimatedEnum|Not applicable|

<h2 id="tocS_DonorIngestSchema">DonorIngestSchema</h2>

<a id="schemadonoringestschema"></a>
<a id="schema_DonorIngestSchema"></a>
<a id="tocSdonoringestschema"></a>
<a id="tocsdonoringestschema"></a>

```json
{
  "submitter_donor_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "is_deceased": "Yes",
  "lost_to_follow_up": "Yes",
  "lost_to_followup_reason": "Completed study",
  "cause_of_death": "Died of cancer",
  "date_of_birth": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death_is_estimated": "Yes",
  "date_resolution": "string",
  "program_id": "string",
  "uuid": "string"
}

```

DonorIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|string|true|none|none|
|gender|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[GenderEnum](#schemagenderenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sex_at_birth|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SexAtBirthEnum](#schemasexatbirthenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_deceased|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_follow_up|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowUpEnum](#schemalosttofollowupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_followup_reason|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowupReasonEnum](#schemalosttofollowupreasonenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cause_of_death|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CauseOfDeathEnum](#schemacauseofdeathenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_birth|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_death|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_death_is_estimated|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateOfDeathIsEstimatedEnum](#schemadateofdeathisestimatedenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_resolution|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_GenderEnum">GenderEnum</h2>

<a id="schemagenderenum"></a>
<a id="schema_GenderEnum"></a>
<a id="tocSgenderenum"></a>
<a id="tocsgenderenum"></a>

```json
"Man"

```

GenderEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|GenderEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|GenderEnum|Man|
|GenderEnum|Woman|
|GenderEnum|Non-binary|
|GenderEnum|Other|
|GenderEnum|Prefer not to disclose|
|GenderEnum|Not available|

<h2 id="tocS_LostToFollowUpEnum">LostToFollowUpEnum</h2>

<a id="schemalosttofollowupenum"></a>
<a id="schema_LostToFollowUpEnum"></a>
<a id="tocSlosttofollowupenum"></a>
<a id="tocslosttofollowupenum"></a>

```json
"Yes"

```

LostToFollowUpEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|LostToFollowUpEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|LostToFollowUpEnum|Yes|
|LostToFollowUpEnum|No|
|LostToFollowUpEnum|Not applicable|
|LostToFollowUpEnum|Unknown|

<h2 id="tocS_LostToFollowupReasonEnum">LostToFollowupReasonEnum</h2>

<a id="schemalosttofollowupreasonenum"></a>
<a id="schema_LostToFollowupReasonEnum"></a>
<a id="tocSlosttofollowupreasonenum"></a>
<a id="tocslosttofollowupreasonenum"></a>

```json
"Completed study"

```

LostToFollowupReasonEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|LostToFollowupReasonEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|LostToFollowupReasonEnum|Completed study|
|LostToFollowupReasonEnum|Discharged to palliative care|
|LostToFollowupReasonEnum|Lost contact|
|LostToFollowupReasonEnum|Not available|
|LostToFollowupReasonEnum|Withdrew from study|
|LostToFollowupReasonEnum|Discharged from follow-up|

<h2 id="tocS_SexAtBirthEnum">SexAtBirthEnum</h2>

<a id="schemasexatbirthenum"></a>
<a id="schema_SexAtBirthEnum"></a>
<a id="tocSsexatbirthenum"></a>
<a id="tocssexatbirthenum"></a>

```json
"Male"

```

SexAtBirthEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|SexAtBirthEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|SexAtBirthEnum|Male|
|SexAtBirthEnum|Female|
|SexAtBirthEnum|Other|
|SexAtBirthEnum|Not available|

<h2 id="tocS_uBooleanEnum">uBooleanEnum</h2>

<a id="schemaubooleanenum"></a>
<a id="schema_uBooleanEnum"></a>
<a id="tocSubooleanenum"></a>
<a id="tocsubooleanenum"></a>

```json
"Yes"

```

uBooleanEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uBooleanEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|uBooleanEnum|Yes|
|uBooleanEnum|No|
|uBooleanEnum|Not available|

<h2 id="tocS_BiomarkerIngestSchema">BiomarkerIngestSchema</h2>

<a id="schemabiomarkeringestschema"></a>
<a id="schema_BiomarkerIngestSchema"></a>
<a id="tocSbiomarkeringestschema"></a>
<a id="tocsbiomarkeringestschema"></a>

```json
{
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string",
  "test_date": {
    "day_interval": 0,
    "month_interval": 0
  },
  "psa_level": 0,
  "psa_level_not_available": false,
  "ca125": 0,
  "ca125_not_available": false,
  "cea": 0,
  "cea_not_available": false,
  "ca19_9": 0,
  "ca19_9_not_available": false,
  "er_status": "Cannot be determined",
  "er_percent_positive": 0,
  "er_percent_positive_not_available": false,
  "pr_status": "Cannot be determined",
  "pr_percent_positive": 0,
  "pr_percent_positive_not_available": false,
  "her2_ihc_status": "Cannot be determined",
  "her2_ish_status": "Cannot be determined",
  "hpv_ihc_status": "Cannot be determined",
  "hpv_pcr_status": "Cannot be determined",
  "hpv_strain": [
    "HPV16"
  ],
  "program_id": "string",
  "submitter_donor_id": "string",
  "uuid": "string"
}

```

BiomarkerIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|test_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|psa_level|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|psa_level_not_available|boolean|false|none|none|
|ca125|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ca125_not_available|boolean|false|none|none|
|cea|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cea_not_available|boolean|false|none|none|
|ca19_9|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ca19_9_not_available|boolean|false|none|none|
|er_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|er_percent_positive|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|er_percent_positive_not_available|boolean|false|none|none|
|pr_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pr_percent_positive|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pr_percent_positive_not_available|boolean|false|none|none|
|her2_ihc_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[Her2StatusEnum](#schemaher2statusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|her2_ish_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[Her2StatusEnum](#schemaher2statusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_ihc_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_pcr_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_strain|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[HpvStrainEnum](#schemahpvstrainenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ErPrHpvStatusEnum">ErPrHpvStatusEnum</h2>

<a id="schemaerprhpvstatusenum"></a>
<a id="schema_ErPrHpvStatusEnum"></a>
<a id="tocSerprhpvstatusenum"></a>
<a id="tocserprhpvstatusenum"></a>

```json
"Cannot be determined"

```

ErPrHpvStatusEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ErPrHpvStatusEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|ErPrHpvStatusEnum|Cannot be determined|
|ErPrHpvStatusEnum|Negative|
|ErPrHpvStatusEnum|Not applicable|
|ErPrHpvStatusEnum|Positive|
|ErPrHpvStatusEnum|Not available|

<h2 id="tocS_Her2StatusEnum">Her2StatusEnum</h2>

<a id="schemaher2statusenum"></a>
<a id="schema_Her2StatusEnum"></a>
<a id="tocSher2statusenum"></a>
<a id="tocsher2statusenum"></a>

```json
"Cannot be determined"

```

Her2StatusEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Her2StatusEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|Her2StatusEnum|Cannot be determined|
|Her2StatusEnum|Equivocal|
|Her2StatusEnum|Positive|
|Her2StatusEnum|Negative|
|Her2StatusEnum|Not applicable|
|Her2StatusEnum|Not available|

<h2 id="tocS_HpvStrainEnum">HpvStrainEnum</h2>

<a id="schemahpvstrainenum"></a>
<a id="schema_HpvStrainEnum"></a>
<a id="tocShpvstrainenum"></a>
<a id="tocshpvstrainenum"></a>

```json
"HPV16"

```

HpvStrainEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|HpvStrainEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|HpvStrainEnum|HPV16|
|HpvStrainEnum|HPV18|
|HpvStrainEnum|HPV31|
|HpvStrainEnum|HPV33|
|HpvStrainEnum|HPV35|
|HpvStrainEnum|HPV39|
|HpvStrainEnum|HPV45|
|HpvStrainEnum|HPV51|
|HpvStrainEnum|HPV52|
|HpvStrainEnum|HPV56|
|HpvStrainEnum|HPV58|
|HpvStrainEnum|HPV59|
|HpvStrainEnum|HPV66|
|HpvStrainEnum|HPV68|
|HpvStrainEnum|HPV73|

<h2 id="tocS_DosageUnitsEnum">DosageUnitsEnum</h2>

<a id="schemadosageunitsenum"></a>
<a id="schema_DosageUnitsEnum"></a>
<a id="tocSdosageunitsenum"></a>
<a id="tocsdosageunitsenum"></a>

```json
"mg/m2"

```

DosageUnitsEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DosageUnitsEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|DosageUnitsEnum|mg/m2|
|DosageUnitsEnum|IU/m2|
|DosageUnitsEnum|IU/kg|
|DosageUnitsEnum|ug/m2|
|DosageUnitsEnum|g/m2|
|DosageUnitsEnum|mg/kg|
|DosageUnitsEnum|mg|
|DosageUnitsEnum|Not available|

<h2 id="tocS_DrugReferenceDbEnum">DrugReferenceDbEnum</h2>

<a id="schemadrugreferencedbenum"></a>
<a id="schema_DrugReferenceDbEnum"></a>
<a id="tocSdrugreferencedbenum"></a>
<a id="tocsdrugreferencedbenum"></a>

```json
"RxNorm"

```

DrugReferenceDbEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DrugReferenceDbEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|DrugReferenceDbEnum|RxNorm|
|DrugReferenceDbEnum|PubChem|
|DrugReferenceDbEnum|NCI Thesaurus|

<h2 id="tocS_SystemicTherapyIngestSchema">SystemicTherapyIngestSchema</h2>

<a id="schemasystemictherapyingestschema"></a>
<a id="schema_SystemicTherapyIngestSchema"></a>
<a id="tocSsystemictherapyingestschema"></a>
<a id="tocssystemictherapyingestschema"></a>

```json
{
  "systemic_therapy_type": "string",
  "days_per_cycle": 0,
  "days_per_cycle_not_available": false,
  "number_of_cycles": 0,
  "number_of_cycles_not_available": false,
  "start_date": {},
  "end_date": {},
  "drug_reference_database": "RxNorm",
  "drug_name": "string",
  "drug_reference_identifier": "string",
  "drug_dose_units": "mg/m2",
  "prescribed_cumulative_drug_dose": 0,
  "prescribed_cumulative_drug_dose_not_available": false,
  "actual_cumulative_drug_dose": 0,
  "actual_cumulative_drug_dose_not_available": false,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string",
  "uuid": "string"
}

```

SystemicTherapyIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|systemic_therapy_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|days_per_cycle|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|days_per_cycle_not_available|boolean|false|none|none|
|number_of_cycles|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles_not_available|boolean|false|none|none|
|start_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|end_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_reference_database|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DrugReferenceDbEnum](#schemadrugreferencedbenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_reference_identifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_dose_units|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DosageUnitsEnum](#schemadosageunitsenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prescribed_cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prescribed_cumulative_drug_dose_not_available|boolean|false|none|none|
|actual_cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|actual_cumulative_drug_dose_not_available|boolean|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ComorbidityIngestSchema">ComorbidityIngestSchema</h2>

<a id="schemacomorbidityingestschema"></a>
<a id="schema_ComorbidityIngestSchema"></a>
<a id="tocScomorbidityingestschema"></a>
<a id="tocscomorbidityingestschema"></a>

```json
{
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "age_at_comorbidity_diagnosis": 0,
  "age_at_comorbidity_diagnosis_not_available": false,
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "uuid": "string"
}

```

ComorbidityIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prior_malignancy|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|laterality_of_prior_malignancy|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MalignancyLateralityEnum](#schemamalignancylateralityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|age_at_comorbidity_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|age_at_comorbidity_diagnosis_not_available|boolean|false|none|none|
|comorbidity_type_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_MalignancyLateralityEnum">MalignancyLateralityEnum</h2>

<a id="schemamalignancylateralityenum"></a>
<a id="schema_MalignancyLateralityEnum"></a>
<a id="tocSmalignancylateralityenum"></a>
<a id="tocsmalignancylateralityenum"></a>

```json
"Bilateral"

```

MalignancyLateralityEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|MalignancyLateralityEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|MalignancyLateralityEnum|Bilateral|
|MalignancyLateralityEnum|Left|
|MalignancyLateralityEnum|Midline|
|MalignancyLateralityEnum|Not applicable|
|MalignancyLateralityEnum|Right|
|MalignancyLateralityEnum|Unilateral, Side not specified|
|MalignancyLateralityEnum|Not available|

<h2 id="tocS_ExposureIngestSchema">ExposureIngestSchema</h2>

<a id="schemaexposureingestschema"></a>
<a id="schema_ExposureIngestSchema"></a>
<a id="tocSexposureingestschema"></a>
<a id="tocsexposureingestschema"></a>

```json
{
  "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
  "tobacco_type": [
    "Chewing Tobacco"
  ],
  "pack_years_smoked": 0,
  "pack_years_smoked_not_available": false,
  "program_id": "string",
  "submitter_donor_id": "string",
  "uuid": "string"
}

```

ExposureIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tobacco_smoking_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SmokingStatusEnum](#schemasmokingstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tobacco_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[TobaccoTypeEnum](#schematobaccotypeenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pack_years_smoked|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pack_years_smoked_not_available|boolean|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SmokingStatusEnum">SmokingStatusEnum</h2>

<a id="schemasmokingstatusenum"></a>
<a id="schema_SmokingStatusEnum"></a>
<a id="tocSsmokingstatusenum"></a>
<a id="tocssmokingstatusenum"></a>

```json
"Current reformed smoker for <= 15 years"

```

SmokingStatusEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|SmokingStatusEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|SmokingStatusEnum|Current reformed smoker for <= 15 years|
|SmokingStatusEnum|Current reformed smoker for > 15 years|
|SmokingStatusEnum|Current reformed smoker, duration not specified|
|SmokingStatusEnum|Current smoker|
|SmokingStatusEnum|Lifelong non-smoker (<100 cigarettes smoked in lifetime)|
|SmokingStatusEnum|Not applicable|
|SmokingStatusEnum|Not available|

<h2 id="tocS_TobaccoTypeEnum">TobaccoTypeEnum</h2>

<a id="schematobaccotypeenum"></a>
<a id="schema_TobaccoTypeEnum"></a>
<a id="tocStobaccotypeenum"></a>
<a id="tocstobaccotypeenum"></a>

```json
"Chewing Tobacco"

```

TobaccoTypeEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TobaccoTypeEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TobaccoTypeEnum|Chewing Tobacco|
|TobaccoTypeEnum|Cigar|
|TobaccoTypeEnum|Cigarettes|
|TobaccoTypeEnum|Electronic cigarettes|
|TobaccoTypeEnum|Not applicable|
|TobaccoTypeEnum|Pipe|
|TobaccoTypeEnum|Roll-ups|
|TobaccoTypeEnum|Snuff|
|TobaccoTypeEnum|Not available|
|TobaccoTypeEnum|Waterpipe|

<h2 id="tocS_DiseaseStatusFollowupEnum">DiseaseStatusFollowupEnum</h2>

<a id="schemadiseasestatusfollowupenum"></a>
<a id="schema_DiseaseStatusFollowupEnum"></a>
<a id="tocSdiseasestatusfollowupenum"></a>
<a id="tocsdiseasestatusfollowupenum"></a>

```json
"Complete remission"

```

DiseaseStatusFollowupEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DiseaseStatusFollowupEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|DiseaseStatusFollowupEnum|Complete remission|
|DiseaseStatusFollowupEnum|Distant progression|
|DiseaseStatusFollowupEnum|Loco-regional progression|
|DiseaseStatusFollowupEnum|No evidence of disease|
|DiseaseStatusFollowupEnum|Partial remission|
|DiseaseStatusFollowupEnum|Progression not otherwise specified|
|DiseaseStatusFollowupEnum|Relapse or recurrence|
|DiseaseStatusFollowupEnum|Stable|
|DiseaseStatusFollowupEnum|Not available|

<h2 id="tocS_FollowUpIngestSchema">FollowUpIngestSchema</h2>

<a id="schemafollowupingestschema"></a>
<a id="schema_FollowUpIngestSchema"></a>
<a id="tocSfollowupingestschema"></a>
<a id="tocsfollowupingestschema"></a>

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": {
    "day_interval": 0,
    "month_interval": 0
  },
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": {
    "day_interval": 0,
    "month_interval": 0
  },
  "method_of_progression_status": [
    "Imaging (procedure)"
  ],
  "anatomic_site_progression_or_recurrence": [
    "string"
  ],
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "uuid": "string"
}

```

FollowUpIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|string|true|none|none|
|date_of_followup|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|disease_status_at_followup|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DiseaseStatusFollowupEnum](#schemadiseasestatusfollowupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|relapse_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RelapseTypeEnum](#schemarelapsetypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_relapse|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|method_of_progression_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ProgressionStatusMethodEnum](#schemaprogressionstatusmethodenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anatomic_site_progression_or_recurrence|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ProgressionStatusMethodEnum">ProgressionStatusMethodEnum</h2>

<a id="schemaprogressionstatusmethodenum"></a>
<a id="schema_ProgressionStatusMethodEnum"></a>
<a id="tocSprogressionstatusmethodenum"></a>
<a id="tocsprogressionstatusmethodenum"></a>

```json
"Imaging (procedure)"

```

ProgressionStatusMethodEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ProgressionStatusMethodEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|ProgressionStatusMethodEnum|Imaging (procedure)|
|ProgressionStatusMethodEnum|Histopathology test (procedure)|
|ProgressionStatusMethodEnum|Assessment of symptom control (procedure)|
|ProgressionStatusMethodEnum|Physical examination procedure (procedure)|
|ProgressionStatusMethodEnum|Tumor marker measurement (procedure)|
|ProgressionStatusMethodEnum|Laboratory data interpretation (procedure)|

<h2 id="tocS_RelapseTypeEnum">RelapseTypeEnum</h2>

<a id="schemarelapsetypeenum"></a>
<a id="schema_RelapseTypeEnum"></a>
<a id="tocSrelapsetypeenum"></a>
<a id="tocsrelapsetypeenum"></a>

```json
"Distant recurrence/metastasis"

```

RelapseTypeEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|RelapseTypeEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|RelapseTypeEnum|Distant recurrence/metastasis|
|RelapseTypeEnum|Local recurrence|
|RelapseTypeEnum|Local recurrence and distant metastasis|
|RelapseTypeEnum|Progression|
|RelapseTypeEnum|Biochemical progression|
|RelapseTypeEnum|Not available|

<h2 id="tocS_BasisOfDiagnosisEnum">BasisOfDiagnosisEnum</h2>

<a id="schemabasisofdiagnosisenum"></a>
<a id="schema_BasisOfDiagnosisEnum"></a>
<a id="tocSbasisofdiagnosisenum"></a>
<a id="tocsbasisofdiagnosisenum"></a>

```json
"Clinical investigation"

```

BasisOfDiagnosisEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|BasisOfDiagnosisEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|BasisOfDiagnosisEnum|Clinical investigation|
|BasisOfDiagnosisEnum|Clinical|
|BasisOfDiagnosisEnum|Cytology|
|BasisOfDiagnosisEnum|Death certificate only|
|BasisOfDiagnosisEnum|Histology of a metastasis|
|BasisOfDiagnosisEnum|Specific tumour markers|
|BasisOfDiagnosisEnum|Not available|
|BasisOfDiagnosisEnum|Cytogenetic and/or molecular testing|
|BasisOfDiagnosisEnum|Histology at autopsy|
|BasisOfDiagnosisEnum|Histology of the primary tumor|
|BasisOfDiagnosisEnum|Histology|

<h2 id="tocS_MCategoryEnum">MCategoryEnum</h2>

<a id="schemamcategoryenum"></a>
<a id="schema_MCategoryEnum"></a>
<a id="tocSmcategoryenum"></a>
<a id="tocsmcategoryenum"></a>

```json
"M0"

```

MCategoryEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|MCategoryEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|MCategoryEnum|M0|
|MCategoryEnum|M0(i+)|
|MCategoryEnum|M1|
|MCategoryEnum|M1a|
|MCategoryEnum|M1a(0)|
|MCategoryEnum|M1a(1)|
|MCategoryEnum|M1b|
|MCategoryEnum|M1b(0)|
|MCategoryEnum|M1b(1)|
|MCategoryEnum|M1c|
|MCategoryEnum|M1c(0)|
|MCategoryEnum|M1c(1)|
|MCategoryEnum|M1d|
|MCategoryEnum|M1d(0)|
|MCategoryEnum|M1d(1)|
|MCategoryEnum|M1e|
|MCategoryEnum|MX|
|MCategoryEnum|Not applicable|

<h2 id="tocS_NCategoryEnum">NCategoryEnum</h2>

<a id="schemancategoryenum"></a>
<a id="schema_NCategoryEnum"></a>
<a id="tocSncategoryenum"></a>
<a id="tocsncategoryenum"></a>

```json
"N0"

```

NCategoryEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|NCategoryEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|NCategoryEnum|N0|
|NCategoryEnum|N0a|
|NCategoryEnum|N0a (biopsy)|
|NCategoryEnum|N0b|
|NCategoryEnum|N0b (no biopsy)|
|NCategoryEnum|N0(i+)|
|NCategoryEnum|N0(i-)|
|NCategoryEnum|N0(mol+)|
|NCategoryEnum|N0(mol-)|
|NCategoryEnum|N1|
|NCategoryEnum|N1a|
|NCategoryEnum|N1a(sn)|
|NCategoryEnum|N1b|
|NCategoryEnum|N1c|
|NCategoryEnum|N1mi|
|NCategoryEnum|N2|
|NCategoryEnum|N2a|
|NCategoryEnum|N2b|
|NCategoryEnum|N2c|
|NCategoryEnum|N2mi|
|NCategoryEnum|N3|
|NCategoryEnum|N3a|
|NCategoryEnum|N3b|
|NCategoryEnum|N3c|
|NCategoryEnum|N4|
|NCategoryEnum|NX|

<h2 id="tocS_PrimaryDiagnosisIngestSchema">PrimaryDiagnosisIngestSchema</h2>

<a id="schemaprimarydiagnosisingestschema"></a>
<a id="schema_PrimaryDiagnosisIngestSchema"></a>
<a id="tocSprimarydiagnosisingestschema"></a>
<a id="tocsprimarydiagnosisingestschema"></a>

```json
{
  "submitter_primary_diagnosis_id": "string",
  "primary_site": "Accessory sinuses",
  "date_of_diagnosis": {
    "day_interval": 0,
    "month_interval": 0
  },
  "cancer_type_code": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "laterality": "Bilateral",
  "clinical_tumour_staging_system": "AJCC cancer staging system",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Stage 0",
  "pathological_tumour_staging_system": "AJCC cancer staging system",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Stage 0",
  "program_id": "string",
  "submitter_donor_id": "string",
  "uuid": "string"
}

```

PrimaryDiagnosisIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|string|true|none|none|
|primary_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PrimarySiteEnum](#schemaprimarysiteenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cancer_type_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|basis_of_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BasisOfDiagnosisEnum](#schemabasisofdiagnosisenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|laterality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PrimaryDiagnosisLateralityEnum](#schemaprimarydiagnosislateralityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_tumour_staging_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourStagingSystemEnum](#schematumourstagingsystemenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_t_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_n_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_m_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_stage_group|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_tumour_staging_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourStagingSystemEnum](#schematumourstagingsystemenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_t_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_n_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_m_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_stage_group|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PrimaryDiagnosisLateralityEnum">PrimaryDiagnosisLateralityEnum</h2>

<a id="schemaprimarydiagnosislateralityenum"></a>
<a id="schema_PrimaryDiagnosisLateralityEnum"></a>
<a id="tocSprimarydiagnosislateralityenum"></a>
<a id="tocsprimarydiagnosislateralityenum"></a>

```json
"Bilateral"

```

PrimaryDiagnosisLateralityEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|PrimaryDiagnosisLateralityEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|PrimaryDiagnosisLateralityEnum|Bilateral|
|PrimaryDiagnosisLateralityEnum|Left|
|PrimaryDiagnosisLateralityEnum|Midline|
|PrimaryDiagnosisLateralityEnum|Not a paired site|
|PrimaryDiagnosisLateralityEnum|Right|
|PrimaryDiagnosisLateralityEnum|Unilateral, side not specified|
|PrimaryDiagnosisLateralityEnum|Not available|

<h2 id="tocS_PrimarySiteEnum">PrimarySiteEnum</h2>

<a id="schemaprimarysiteenum"></a>
<a id="schema_PrimarySiteEnum"></a>
<a id="tocSprimarysiteenum"></a>
<a id="tocsprimarysiteenum"></a>

```json
"Accessory sinuses"

```

PrimarySiteEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|PrimarySiteEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|PrimarySiteEnum|Accessory sinuses|
|PrimarySiteEnum|Adrenal gland|
|PrimarySiteEnum|Anus and anal canal|
|PrimarySiteEnum|Base of tongue|
|PrimarySiteEnum|Bladder|
|PrimarySiteEnum|Bones, joints and articular cartilage of limbs|
|PrimarySiteEnum|Bones, joints and articular cartilage of other and unspecified sites|
|PrimarySiteEnum|Brain|
|PrimarySiteEnum|Breast|
|PrimarySiteEnum|Bronchus and lung|
|PrimarySiteEnum|Cervix uteri|
|PrimarySiteEnum|Colon|
|PrimarySiteEnum|Connective, subcutaneous and other soft tissues|
|PrimarySiteEnum|Corpus uteri|
|PrimarySiteEnum|Esophagus|
|PrimarySiteEnum|Eye and adnexa|
|PrimarySiteEnum|Floor of mouth|
|PrimarySiteEnum|Gallbladder|
|PrimarySiteEnum|Gum|
|PrimarySiteEnum|Heart, mediastinum, and pleura|
|PrimarySiteEnum|Hematopoietic and reticuloendothelial systems|
|PrimarySiteEnum|Hypopharynx|
|PrimarySiteEnum|Kidney|
|PrimarySiteEnum|Larynx|
|PrimarySiteEnum|Lip|
|PrimarySiteEnum|Liver and intrahepatic bile ducts|
|PrimarySiteEnum|Lymph nodes|
|PrimarySiteEnum|Meninges|
|PrimarySiteEnum|Nasal cavity and middle ear|
|PrimarySiteEnum|Nasopharynx|
|PrimarySiteEnum|Oropharynx|
|PrimarySiteEnum|Other and ill-defined digestive organs|
|PrimarySiteEnum|Other and ill-defined sites|
|PrimarySiteEnum|Other and ill-defined sites in lip, oral cavity and pharynx|
|PrimarySiteEnum|Other and ill-defined sites within respiratory system and intrathoracic organs|
|PrimarySiteEnum|Other and unspecified female genital organs|
|PrimarySiteEnum|Other and unspecified major salivary glands|
|PrimarySiteEnum|Other and unspecified male genital organs|
|PrimarySiteEnum|Other and unspecified parts of biliary tract|
|PrimarySiteEnum|Other and unspecified parts of mouth|
|PrimarySiteEnum|Other and unspecified parts of tongue|
|PrimarySiteEnum|Other and unspecified urinary organs|
|PrimarySiteEnum|Other endocrine glands and related structures|
|PrimarySiteEnum|Ovary|
|PrimarySiteEnum|Palate|
|PrimarySiteEnum|Pancreas|
|PrimarySiteEnum|Parotid gland|
|PrimarySiteEnum|Penis|
|PrimarySiteEnum|Peripheral nerves and autonomic nervous system|
|PrimarySiteEnum|Placenta|
|PrimarySiteEnum|Prostate gland|
|PrimarySiteEnum|Pyriform sinus|
|PrimarySiteEnum|Rectosigmoid junction|
|PrimarySiteEnum|Rectum|
|PrimarySiteEnum|Renal pelvis|
|PrimarySiteEnum|Retroperitoneum and peritoneum|
|PrimarySiteEnum|Skin|
|PrimarySiteEnum|Small intestine|
|PrimarySiteEnum|Spinal cord, cranial nerves, and other parts of central nervous system|
|PrimarySiteEnum|Stomach|
|PrimarySiteEnum|Testis|
|PrimarySiteEnum|Thymus|
|PrimarySiteEnum|Thyroid gland|
|PrimarySiteEnum|Tonsil|
|PrimarySiteEnum|Trachea|
|PrimarySiteEnum|Ureter|
|PrimarySiteEnum|Uterus, NOS|
|PrimarySiteEnum|Vagina|
|PrimarySiteEnum|Vulva|
|PrimarySiteEnum|Unknown primary site|
|PrimarySiteEnum|Not available|

<h2 id="tocS_StageGroupEnum">StageGroupEnum</h2>

<a id="schemastagegroupenum"></a>
<a id="schema_StageGroupEnum"></a>
<a id="tocSstagegroupenum"></a>
<a id="tocsstagegroupenum"></a>

```json
"Stage 0"

```

StageGroupEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|StageGroupEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|StageGroupEnum|Stage 0|
|StageGroupEnum|Stage 0a|
|StageGroupEnum|Stage 0is|
|StageGroupEnum|Stage 1|
|StageGroupEnum|Stage 1A|
|StageGroupEnum|Stage 1B|
|StageGroupEnum|Stage A|
|StageGroupEnum|Stage B|
|StageGroupEnum|Stage C|
|StageGroupEnum|Stage I|
|StageGroupEnum|Stage IA|
|StageGroupEnum|Stage IA1|
|StageGroupEnum|Stage IA2|
|StageGroupEnum|Stage IA3|
|StageGroupEnum|Stage IAB|
|StageGroupEnum|Stage IAE|
|StageGroupEnum|Stage IAES|
|StageGroupEnum|Stage IAS|
|StageGroupEnum|Stage IB|
|StageGroupEnum|Stage IB1|
|StageGroupEnum|Stage IB2|
|StageGroupEnum|Stage IBE|
|StageGroupEnum|Stage IBES|
|StageGroupEnum|Stage IBS|
|StageGroupEnum|Stage IC|
|StageGroupEnum|Stage IE|
|StageGroupEnum|Stage IEA|
|StageGroupEnum|Stage IEB|
|StageGroupEnum|Stage IES|
|StageGroupEnum|Stage II|
|StageGroupEnum|Stage II bulky|
|StageGroupEnum|Stage IIA|
|StageGroupEnum|Stage IIA1|
|StageGroupEnum|Stage IIA2|
|StageGroupEnum|Stage IIAE|
|StageGroupEnum|Stage IIAES|
|StageGroupEnum|Stage IIAS|
|StageGroupEnum|Stage IIB|
|StageGroupEnum|Stage IIBE|
|StageGroupEnum|Stage IIBES|
|StageGroupEnum|Stage IIBS|
|StageGroupEnum|Stage IIC|
|StageGroupEnum|Stage IIE|
|StageGroupEnum|Stage IIEA|
|StageGroupEnum|Stage IIEB|
|StageGroupEnum|Stage IIES|
|StageGroupEnum|Stage III|
|StageGroupEnum|Stage IIIA|
|StageGroupEnum|Stage IIIA1|
|StageGroupEnum|Stage IIIA2|
|StageGroupEnum|Stage IIIAE|
|StageGroupEnum|Stage IIIAES|
|StageGroupEnum|Stage IIIAS|
|StageGroupEnum|Stage IIIB|
|StageGroupEnum|Stage IIIBE|
|StageGroupEnum|Stage IIIBES|
|StageGroupEnum|Stage IIIBS|
|StageGroupEnum|Stage IIIC|
|StageGroupEnum|Stage IIIC1|
|StageGroupEnum|Stage IIIC2|
|StageGroupEnum|Stage IIID|
|StageGroupEnum|Stage IIIE|
|StageGroupEnum|Stage IIIES|
|StageGroupEnum|Stage IIIS|
|StageGroupEnum|Stage IIS|
|StageGroupEnum|Stage IS|
|StageGroupEnum|Stage IV|
|StageGroupEnum|Stage IVA|
|StageGroupEnum|Stage IVA1|
|StageGroupEnum|Stage IVA2|
|StageGroupEnum|Stage IVAE|
|StageGroupEnum|Stage IVAES|
|StageGroupEnum|Stage IVAS|
|StageGroupEnum|Stage IVB|
|StageGroupEnum|Stage IVBE|
|StageGroupEnum|Stage IVBES|
|StageGroupEnum|Stage IVBS|
|StageGroupEnum|Stage IVC|
|StageGroupEnum|Stage IVE|
|StageGroupEnum|Stage IVES|
|StageGroupEnum|Stage IVS|
|StageGroupEnum|In situ|
|StageGroupEnum|Localized|
|StageGroupEnum|Regionalized|
|StageGroupEnum|Distant|
|StageGroupEnum|Stage L1|
|StageGroupEnum|Stage L2|
|StageGroupEnum|Stage M|
|StageGroupEnum|Stage Ms|
|StageGroupEnum|Stage 2A|
|StageGroupEnum|Stage 2B|
|StageGroupEnum|Stage 3|
|StageGroupEnum|Stage 4|
|StageGroupEnum|Stage 4S|
|StageGroupEnum|Occult Carcinoma|
|StageGroupEnum|Not available|
|StageGroupEnum|Stage IC1|
|StageGroupEnum|Stage IC2|
|StageGroupEnum|Stage IC3|

<h2 id="tocS_TCategoryEnum">TCategoryEnum</h2>

<a id="schematcategoryenum"></a>
<a id="schema_TCategoryEnum"></a>
<a id="tocStcategoryenum"></a>
<a id="tocstcategoryenum"></a>

```json
"T0"

```

TCategoryEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TCategoryEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TCategoryEnum|T0|
|TCategoryEnum|T1|
|TCategoryEnum|T1a|
|TCategoryEnum|T1a1|
|TCategoryEnum|T1a2|
|TCategoryEnum|T1a(s)|
|TCategoryEnum|T1a(m)|
|TCategoryEnum|T1b|
|TCategoryEnum|T1b1|
|TCategoryEnum|T1b2|
|TCategoryEnum|T1b(s)|
|TCategoryEnum|T1b(m)|
|TCategoryEnum|T1c|
|TCategoryEnum|T1c1|
|TCategoryEnum|T1c2|
|TCategoryEnum|T1d|
|TCategoryEnum|T1mi|
|TCategoryEnum|T2|
|TCategoryEnum|T2(s)|
|TCategoryEnum|T2(m)|
|TCategoryEnum|T2a|
|TCategoryEnum|T2a1|
|TCategoryEnum|T2a2|
|TCategoryEnum|T2b|
|TCategoryEnum|T2c|
|TCategoryEnum|T2d|
|TCategoryEnum|T3|
|TCategoryEnum|T3(s)|
|TCategoryEnum|T3(m)|
|TCategoryEnum|T3a|
|TCategoryEnum|T3b|
|TCategoryEnum|T3c|
|TCategoryEnum|T3d|
|TCategoryEnum|T3e|
|TCategoryEnum|T4|
|TCategoryEnum|T4a|
|TCategoryEnum|T4a(s)|
|TCategoryEnum|T4a(m)|
|TCategoryEnum|T4b|
|TCategoryEnum|T4b(s)|
|TCategoryEnum|T4b(m)|
|TCategoryEnum|T4c|
|TCategoryEnum|T4d|
|TCategoryEnum|T4e|
|TCategoryEnum|Ta|
|TCategoryEnum|Tis|
|TCategoryEnum|Tis(DCIS)|
|TCategoryEnum|Tis(LAMN)|
|TCategoryEnum|Tis(LCIS)|
|TCategoryEnum|Tis(Paget)|
|TCategoryEnum|Tis(Paget's)|
|TCategoryEnum|Tis pu|
|TCategoryEnum|Tis pd|
|TCategoryEnum|TX|

<h2 id="tocS_TumourStagingSystemEnum">TumourStagingSystemEnum</h2>

<a id="schematumourstagingsystemenum"></a>
<a id="schema_TumourStagingSystemEnum"></a>
<a id="tocStumourstagingsystemenum"></a>
<a id="tocstumourstagingsystemenum"></a>

```json
"AJCC cancer staging system"

```

TumourStagingSystemEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TumourStagingSystemEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TumourStagingSystemEnum|AJCC cancer staging system|
|TumourStagingSystemEnum|Ann Arbor staging system|
|TumourStagingSystemEnum|Binet staging system|
|TumourStagingSystemEnum|Durie-Salmon staging system|
|TumourStagingSystemEnum|FIGO staging system|
|TumourStagingSystemEnum|International Neuroblastoma Risk Group Staging System|
|TumourStagingSystemEnum|International Neuroblastoma Staging System|
|TumourStagingSystemEnum|Lugano staging system|
|TumourStagingSystemEnum|Rai staging system|
|TumourStagingSystemEnum|Revised International staging system (R-ISS)|
|TumourStagingSystemEnum|SEER staging system|
|TumourStagingSystemEnum|St Jude staging system|
|TumourStagingSystemEnum|Not available|

<h2 id="tocS_RadiationAnatomicalSiteEnum">RadiationAnatomicalSiteEnum</h2>

<a id="schemaradiationanatomicalsiteenum"></a>
<a id="schema_RadiationAnatomicalSiteEnum"></a>
<a id="tocSradiationanatomicalsiteenum"></a>
<a id="tocsradiationanatomicalsiteenum"></a>

```json
"ABDOMEN_WHOLE"

```

RadiationAnatomicalSiteEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|RadiationAnatomicalSiteEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|RadiationAnatomicalSiteEnum|ABDOMEN_WHOLE|
|RadiationAnatomicalSiteEnum|ABDOMEN_LEFT|
|RadiationAnatomicalSiteEnum|ABDOMEN_RIGHT|
|RadiationAnatomicalSiteEnum|ABDOMEN_UPPER|
|RadiationAnatomicalSiteEnum|ABDOMEN_LOWER|
|RadiationAnatomicalSiteEnum|ABDOMEN_LEFT_LOWER|
|RadiationAnatomicalSiteEnum|ABDOMEN_LEFT_UPPER|
|RadiationAnatomicalSiteEnum|ABDOMEN_RIGHT_LOWER|
|RadiationAnatomicalSiteEnum|ABDOMEN_RIGHT_UPPER|
|RadiationAnatomicalSiteEnum|ABDOMEN_NOS|
|RadiationAnatomicalSiteEnum|ADRENAL_GLAND_LEFT|
|RadiationAnatomicalSiteEnum|ADRENAL_GLAND_RIGHT|
|RadiationAnatomicalSiteEnum|ADRENAL_GLAND_NOS|
|RadiationAnatomicalSiteEnum|ANKLE_LEFT|
|RadiationAnatomicalSiteEnum|ANKLE_RIGHT|
|RadiationAnatomicalSiteEnum|ANKLE_BILATERAL|
|RadiationAnatomicalSiteEnum|ANKLE_NOS|
|RadiationAnatomicalSiteEnum|ANTRUM_LEFT|
|RadiationAnatomicalSiteEnum|ANTRUM_RIGHT|
|RadiationAnatomicalSiteEnum|ANTRUM_BILATERAL (Bull's eye)|
|RadiationAnatomicalSiteEnum|ANTRUM_NOS|
|RadiationAnatomicalSiteEnum|ANUS|
|RadiationAnatomicalSiteEnum|ARM_LOWER_LEFT|
|RadiationAnatomicalSiteEnum|ARM_UPPER_LEFT|
|RadiationAnatomicalSiteEnum|ARM_LEFT|
|RadiationAnatomicalSiteEnum|ARM_LOWER_RIGHT|
|RadiationAnatomicalSiteEnum|ARM_UPPER_RIGHT|
|RadiationAnatomicalSiteEnum|ARM_RIGHT|
|RadiationAnatomicalSiteEnum|ARM_BILATERAL|
|RadiationAnatomicalSiteEnum|ARM_NOS|
|RadiationAnatomicalSiteEnum|AXILLA_LEFT|
|RadiationAnatomicalSiteEnum|AXILLA_RIGHT|
|RadiationAnatomicalSiteEnum|AXILLA_NOS|
|RadiationAnatomicalSiteEnum|BACK_WHOLE|
|RadiationAnatomicalSiteEnum|BACK_LEFT|
|RadiationAnatomicalSiteEnum|BACK_RIGHT|
|RadiationAnatomicalSiteEnum|BACK_UPPER|
|RadiationAnatomicalSiteEnum|BACK_LOWER|
|RadiationAnatomicalSiteEnum|BACK_LEFT_LOWER|
|RadiationAnatomicalSiteEnum|BACK_LEFT_UPPER|
|RadiationAnatomicalSiteEnum|BACK_RIGHT_LOWER|
|RadiationAnatomicalSiteEnum|BACK_RIGHT_UPPER|
|RadiationAnatomicalSiteEnum|BACK_NOS|
|RadiationAnatomicalSiteEnum|BILE_DUCT_INTRAHEPATIC|
|RadiationAnatomicalSiteEnum|BILE_DUCT_EXTRAHEPATIC|
|RadiationAnatomicalSiteEnum|BILE_DUCT_WHOLE|
|RadiationAnatomicalSiteEnum|BILE_DUCT_NOS|
|RadiationAnatomicalSiteEnum|BLADDER_APEX|
|RadiationAnatomicalSiteEnum|BLADDER_BODY|
|RadiationAnatomicalSiteEnum|BLADDER_FUNDUS|
|RadiationAnatomicalSiteEnum|BLADDER_NECK|
|RadiationAnatomicalSiteEnum|BLADDER_WHOLE|
|RadiationAnatomicalSiteEnum|BLADDER_NOS|
|RadiationAnatomicalSiteEnum|BODY_WHOLE|
|RadiationAnatomicalSiteEnum|BODY_NOS|
|RadiationAnatomicalSiteEnum|BODY_LOWER|
|RadiationAnatomicalSiteEnum|BODY_MIDDLE|
|RadiationAnatomicalSiteEnum|BODY_UPPER|
|RadiationAnatomicalSiteEnum|BOOST_AREA_PREVIOUSLY_TREATED|
|RadiationAnatomicalSiteEnum|BRAIN_NOS|
|RadiationAnatomicalSiteEnum|BRAIN_WHOLE|
|RadiationAnatomicalSiteEnum|BRAIN_CEREBRUM|
|RadiationAnatomicalSiteEnum|BRAIN_CEREBELLUM|
|RadiationAnatomicalSiteEnum|BRAIN_STEM|
|RadiationAnatomicalSiteEnum|BREAST_LEFT|
|RadiationAnatomicalSiteEnum|BREAST_RIGHT|
|RadiationAnatomicalSiteEnum|BREAST_BILATERAL|
|RadiationAnatomicalSiteEnum|BREAST_NOS|
|RadiationAnatomicalSiteEnum|BREAST_BOOST_LEFT|
|RadiationAnatomicalSiteEnum|BREAST_BOOST_RIGHT|
|RadiationAnatomicalSiteEnum|BREAST_BOOST_BILATERAL|
|RadiationAnatomicalSiteEnum|BREAST_BOOST_NOS|
|RadiationAnatomicalSiteEnum|BREAST_WITH_NODES_LEFT|
|RadiationAnatomicalSiteEnum|BREAST_WITH_NODES_RIGHT|
|RadiationAnatomicalSiteEnum|BREAST_WITH_NODES_BILATERAL|
|RadiationAnatomicalSiteEnum|BREAST_WITH_NODES_NOS|
|RadiationAnatomicalSiteEnum|BUTTOCK_LEFT|
|RadiationAnatomicalSiteEnum|BUTTOCK_RIGHT|
|RadiationAnatomicalSiteEnum|BUTTOCK_BILATERAL|
|RadiationAnatomicalSiteEnum|BUTTOCK_NOS|
|RadiationAnatomicalSiteEnum|CANTHUS_INNER|
|RadiationAnatomicalSiteEnum|CANTHUS_OUTER|
|RadiationAnatomicalSiteEnum|CANTHUS_NOS|
|RadiationAnatomicalSiteEnum|CERVIX|
|RadiationAnatomicalSiteEnum|CHEST_WHOLE|
|RadiationAnatomicalSiteEnum|CHEST_LEFT|
|RadiationAnatomicalSiteEnum|CHEST_RIGHT|
|RadiationAnatomicalSiteEnum|CHEST_NOS|
|RadiationAnatomicalSiteEnum|CHEST_THORAX_LEFT|
|RadiationAnatomicalSiteEnum|CHEST_THORAX_RIGHT|
|RadiationAnatomicalSiteEnum|CHEST_THORAX_BILATERAL|
|RadiationAnatomicalSiteEnum|CHEST_THORAX_NOS|
|RadiationAnatomicalSiteEnum|CHEST_WALL_LEFT|
|RadiationAnatomicalSiteEnum|CHEST_WALL_RIGHT|
|RadiationAnatomicalSiteEnum|CHEST_WALL_BILATERAL|
|RadiationAnatomicalSiteEnum|CHEST_WALL_NOS|
|RadiationAnatomicalSiteEnum|CHEST_WALL_BOOST_LEFT|
|RadiationAnatomicalSiteEnum|CHEST_WALL_BOOST_RIGHT|
|RadiationAnatomicalSiteEnum|CHEST_WALL_BOOST_BILATERAL|
|RadiationAnatomicalSiteEnum|CHEST_WALL_BOOST_NOS|
|RadiationAnatomicalSiteEnum|CHEST_WALL_WITH_NODES_LEFT|
|RadiationAnatomicalSiteEnum|CHEST_WALL_WITH_NODES_RIGHT|
|RadiationAnatomicalSiteEnum|CHEST_WALL_WITH_NODES_BILATERAL|
|RadiationAnatomicalSiteEnum|CHEST_WALL_WITH_NODES_NOS|
|RadiationAnatomicalSiteEnum|BILATERAL CHEST LUNG & AREA INVOLVE|
|RadiationAnatomicalSiteEnum|CHIN|
|RadiationAnatomicalSiteEnum|CHEEK_RIGHT|
|RadiationAnatomicalSiteEnum|CHEEK_LEFT|
|RadiationAnatomicalSiteEnum|CLAVICLE_LEFT|
|RadiationAnatomicalSiteEnum|CLAVICLE_RIGHT|
|RadiationAnatomicalSiteEnum|CLAVICLE_BILATERAL|
|RadiationAnatomicalSiteEnum|CLAVICLE_NOS|
|RadiationAnatomicalSiteEnum|COCCYX|
|RadiationAnatomicalSiteEnum|COLON_WHOLE|
|RadiationAnatomicalSiteEnum|COLON_NOS|
|RadiationAnatomicalSiteEnum|COLON_CAECUM|
|RadiationAnatomicalSiteEnum|COLON_ASCENDING|
|RadiationAnatomicalSiteEnum|COLON_TRANSVERSE|
|RadiationAnatomicalSiteEnum|COLON_DESCENDING|
|RadiationAnatomicalSiteEnum|C.N.S._WHOLE (MEDULLA TECHNIQUE)|
|RadiationAnatomicalSiteEnum|CSF SPINE (MEDULL TECH 2 DIFF MACHI|
|RadiationAnatomicalSiteEnum|EAR_LEFT|
|RadiationAnatomicalSiteEnum|EAR_RIGHT|
|RadiationAnatomicalSiteEnum|EAR_BILATERAL|
|RadiationAnatomicalSiteEnum|EAR_NOS|
|RadiationAnatomicalSiteEnum|ESOPHAGUS_LOWER|
|RadiationAnatomicalSiteEnum|ESOPHAGUS_MIDDLE|
|RadiationAnatomicalSiteEnum|ESOPHAGUS_NOS|
|RadiationAnatomicalSiteEnum|ESOPHAGUS_UPPER|
|RadiationAnatomicalSiteEnum|ESOPHAGUS_WHOLE|
|RadiationAnatomicalSiteEnum|EPIGASTRIUM|
|RadiationAnatomicalSiteEnum|ETHMOID_SINUS|
|RadiationAnatomicalSiteEnum|EYE_LEFT|
|RadiationAnatomicalSiteEnum|EYE_RIGHT|
|RadiationAnatomicalSiteEnum|EYE_BILATERAL|
|RadiationAnatomicalSiteEnum|EYE_NOS|
|RadiationAnatomicalSiteEnum|EYELID_LEFT|
|RadiationAnatomicalSiteEnum|EYELID_RIGHT|
|RadiationAnatomicalSiteEnum|EYELID_BILATERAL|
|RadiationAnatomicalSiteEnum|EYELID_NOS|
|RadiationAnatomicalSiteEnum|FACE_LEFT|
|RadiationAnatomicalSiteEnum|FACE_RIGHT|
|RadiationAnatomicalSiteEnum|FACE_BILATERAL|
|RadiationAnatomicalSiteEnum|FACE_NOS|
|RadiationAnatomicalSiteEnum|FALLOPIAN_TUBES_LEFT|
|RadiationAnatomicalSiteEnum|FALLOPIAN_TUBES_RIGHT|
|RadiationAnatomicalSiteEnum|FALLOPIAN_TUBES_NOS|
|RadiationAnatomicalSiteEnum|FEMUR_LEFT|
|RadiationAnatomicalSiteEnum|FEMUR_RIGHT|
|RadiationAnatomicalSiteEnum|FEMUR_BILATERAL|
|RadiationAnatomicalSiteEnum|FEMUR_NOS|
|RadiationAnatomicalSiteEnum|FIBULA_LEFT|
|RadiationAnatomicalSiteEnum|FIBULA_RIGHT|
|RadiationAnatomicalSiteEnum|FIBULA_NOS|
|RadiationAnatomicalSiteEnum|FINGER_RIGHT_HAND|
|RadiationAnatomicalSiteEnum|FINGER_LEFT_HAND|
|RadiationAnatomicalSiteEnum|FINGER_NOS|
|RadiationAnatomicalSiteEnum|FOOT_LEFT|
|RadiationAnatomicalSiteEnum|FOOT_RIGHT|
|RadiationAnatomicalSiteEnum|FOOT_BILATERAL|
|RadiationAnatomicalSiteEnum|FOOT_NOS|
|RadiationAnatomicalSiteEnum|FLOOR_OF_MOUTH|
|RadiationAnatomicalSiteEnum|FLOOR_OF_MOUTH_BOOST|
|RadiationAnatomicalSiteEnum|FOREHEAD|
|RadiationAnatomicalSiteEnum|POSTERIOR_FOSSA|
|RadiationAnatomicalSiteEnum|GALL_BLADDER|
|RadiationAnatomicalSiteEnum|GINGIVA|
|RadiationAnatomicalSiteEnum|HAND_RIGHT|
|RadiationAnatomicalSiteEnum|HAND_LEFT|
|RadiationAnatomicalSiteEnum|HAND_NOS|
|RadiationAnatomicalSiteEnum|HAND_BILATERAL|
|RadiationAnatomicalSiteEnum|HEAD|
|RadiationAnatomicalSiteEnum|HEART|
|RadiationAnatomicalSiteEnum|HEEL_LEFT|
|RadiationAnatomicalSiteEnum|HEEL_RIGHT|
|RadiationAnatomicalSiteEnum|HEEL_BILATERAL|
|RadiationAnatomicalSiteEnum|HEEL_NOS|
|RadiationAnatomicalSiteEnum|HEMIMANTLE_LEFT|
|RadiationAnatomicalSiteEnum|HEMIMANTLE_RIGHT|
|RadiationAnatomicalSiteEnum|HEMIMANTLE_BILATERAL|
|RadiationAnatomicalSiteEnum|HEMIMANTLE_NOS|
|RadiationAnatomicalSiteEnum|HIP_LEFT|
|RadiationAnatomicalSiteEnum|HIP_RIGHT|
|RadiationAnatomicalSiteEnum|HIP_BILATERAL|
|RadiationAnatomicalSiteEnum|HIP_NOS|
|RadiationAnatomicalSiteEnum|HUMERUS_LEFT|
|RadiationAnatomicalSiteEnum|HUMERUS_RIGHT|
|RadiationAnatomicalSiteEnum|HUMERUS_NOS|
|RadiationAnatomicalSiteEnum|HYPOPHARYNX|
|RadiationAnatomicalSiteEnum|INTERNAL_MAMMARY_CHAIN_NOS|
|RadiationAnatomicalSiteEnum|INTERNAL_MAMMARY_CHAIN_LEFT|
|RadiationAnatomicalSiteEnum|INTERNAL_MAMMARY_CHAIN_RIGHT|
|RadiationAnatomicalSiteEnum|INTERNAL_MAMMARY_CHAIN_BILATERAL|
|RadiationAnatomicalSiteEnum|INGUINAL_NODES_LEFT|
|RadiationAnatomicalSiteEnum|INGUINAL_NODES_RIGHT|
|RadiationAnatomicalSiteEnum|INGUINAL_NODES_BILATERAL|
|RadiationAnatomicalSiteEnum|INGUINAL_NODES_NOS|
|RadiationAnatomicalSiteEnum|INVERTED_Y_DOG_LEG_HOCKEY_STICK|
|RadiationAnatomicalSiteEnum|KIDNEY_LEFT|
|RadiationAnatomicalSiteEnum|KIDNEY_RIGHT|
|RadiationAnatomicalSiteEnum|KIDNEY_BILATERAL|
|RadiationAnatomicalSiteEnum|KIDNEY_NOS|
|RadiationAnatomicalSiteEnum|KNEE_LEFT|
|RadiationAnatomicalSiteEnum|KNEE_RIGHT|
|RadiationAnatomicalSiteEnum|KNEE_BILATERAL|
|RadiationAnatomicalSiteEnum|KNEE_NOS|
|RadiationAnatomicalSiteEnum|LACRIMAL_GLAND_LEFT|
|RadiationAnatomicalSiteEnum|LACRIMAL_GLAND_RIGHT|
|RadiationAnatomicalSiteEnum|LACRIMAL_GLAND_BILATERAL|
|RadiationAnatomicalSiteEnum|LACRIMAL_GLAND_NOS|
|RadiationAnatomicalSiteEnum|LARYNGOPHARYNX|
|RadiationAnatomicalSiteEnum|LARYNX|
|RadiationAnatomicalSiteEnum|LEG_BILATERAL_LOWER|
|RadiationAnatomicalSiteEnum|LEG_BILATERAL_NOS|
|RadiationAnatomicalSiteEnum|LEG_BILATERAL_UPPER|
|RadiationAnatomicalSiteEnum|LEG_LEFT_LOWER|
|RadiationAnatomicalSiteEnum|LEG_LEFT_NOS|
|RadiationAnatomicalSiteEnum|LEG_LEFT_UPPER|
|RadiationAnatomicalSiteEnum|LEG_NOS|
|RadiationAnatomicalSiteEnum|LEG_RIGHT_LOWER|
|RadiationAnatomicalSiteEnum|LEG_RIGHT_NOS|
|RadiationAnatomicalSiteEnum|LEG_RIGHT_UPPER|
|RadiationAnatomicalSiteEnum|LEG_LOWER_NOS|
|RadiationAnatomicalSiteEnum|LEG_UPPER_NOS|
|RadiationAnatomicalSiteEnum|LIP_LOWER|
|RadiationAnatomicalSiteEnum|LIP_NOS|
|RadiationAnatomicalSiteEnum|LIP_UPPER|
|RadiationAnatomicalSiteEnum|LIVER_NOS|
|RadiationAnatomicalSiteEnum|LIVER_WHOLE|
|RadiationAnatomicalSiteEnum|LIVER_LOBE_RIGHT|
|RadiationAnatomicalSiteEnum|LIVER_LOBE_LEFT|
|RadiationAnatomicalSiteEnum|LIVER_LOBE_CAUDATE|
|RadiationAnatomicalSiteEnum|LIVER_LOBE_QUADRATE|
|RadiationAnatomicalSiteEnum|LUNG_LEFT_UPPER|
|RadiationAnatomicalSiteEnum|LUNG_LEFT_LOWER|
|RadiationAnatomicalSiteEnum|LUNG_LEFT_WHOLE|
|RadiationAnatomicalSiteEnum|LUNG_LEFT_NOS|
|RadiationAnatomicalSiteEnum|LUNG_RIGHT_UPPER|
|RadiationAnatomicalSiteEnum|LUNG_RIGHT_MIDDLE|
|RadiationAnatomicalSiteEnum|LUNG_RIGHT_LOWER|
|RadiationAnatomicalSiteEnum|LUNG_RIGHT_NOS|
|RadiationAnatomicalSiteEnum|LUNG_BILATERAL|
|RadiationAnatomicalSiteEnum|LUNG_NOS|
|RadiationAnatomicalSiteEnum|MANDIBLE_LEFT|
|RadiationAnatomicalSiteEnum|MANDIBLE_RIGHT|
|RadiationAnatomicalSiteEnum|MANDIBLE_BILATERAL|
|RadiationAnatomicalSiteEnum|MANDIBLE_NOS|
|RadiationAnatomicalSiteEnum|MANTLE|
|RadiationAnatomicalSiteEnum|MAXILLA_LEFT|
|RadiationAnatomicalSiteEnum|MAXILLA_RIGHT|
|RadiationAnatomicalSiteEnum|MAXILLA_BILATERAL|
|RadiationAnatomicalSiteEnum|MAXILLA_NOS|
|RadiationAnatomicalSiteEnum|LYMPH_NODES|
|RadiationAnatomicalSiteEnum|MEDIASTINUM_ANTERIOR|
|RadiationAnatomicalSiteEnum|MEDIASTINUM_MIDDLE|
|RadiationAnatomicalSiteEnum|MEDIASTINUM_POSTERIOR|
|RadiationAnatomicalSiteEnum|MEDIASTINUM_SUPERIOR|
|RadiationAnatomicalSiteEnum|MEDIASTINUM_NOS|
|RadiationAnatomicalSiteEnum|MULTIPLE_SKIN|
|RadiationAnatomicalSiteEnum|NASAL_FOSSA_LEFT|
|RadiationAnatomicalSiteEnum|NASAL_FOSSA_RIGHT|
|RadiationAnatomicalSiteEnum|NASAL_FOSSA_POSTERIOR|
|RadiationAnatomicalSiteEnum|NASAL_FOSSA_BILATERAL|
|RadiationAnatomicalSiteEnum|NASAL_FOSSA_NOS|
|RadiationAnatomicalSiteEnum|NASOPHARYNX|
|RadiationAnatomicalSiteEnum|NECK_NOS|
|RadiationAnatomicalSiteEnum|NECK_SKIN|
|RadiationAnatomicalSiteEnum|NECK_LEFT|
|RadiationAnatomicalSiteEnum|NECK_RIGHT|
|RadiationAnatomicalSiteEnum|NECK_BILATERAL|
|RadiationAnatomicalSiteEnum|NECK_WITH_NODES_LEFT|
|RadiationAnatomicalSiteEnum|NECK_WITH_NODES_RIGHT|
|RadiationAnatomicalSiteEnum|NECK_WITH_NODES_BILATERAL|
|RadiationAnatomicalSiteEnum|NECK_WITH_NODES_NOS|
|RadiationAnatomicalSiteEnum|NOSE|
|RadiationAnatomicalSiteEnum|NOT_AVAILABLE|
|RadiationAnatomicalSiteEnum|ORAL_CAVITY__BUCCAL_MUCOSA_LEFT|
|RadiationAnatomicalSiteEnum|ORAL_CAVITY__BUCCAL_MUCOSA_RIGHT|
|RadiationAnatomicalSiteEnum|ORAL_CAVITY__BUCCAL_MUCOSA_BILATERAL|
|RadiationAnatomicalSiteEnum|ORAL_CAVITY__BUCCAL_MUCOSA_NOS|
|RadiationAnatomicalSiteEnum|ORAL_CAVITY_NOS|
|RadiationAnatomicalSiteEnum|ORAL_CAVITY__HARD PALATE|
|RadiationAnatomicalSiteEnum|ORAL_CAVITY__SOFT PALATE|
|RadiationAnatomicalSiteEnum|ORAL_CAVITY__PALATE_NOS|
|RadiationAnatomicalSiteEnum|ORBIT_LEFT|
|RadiationAnatomicalSiteEnum|ORBIT_RIGHT|
|RadiationAnatomicalSiteEnum|ORBIT_BILATERAL|
|RadiationAnatomicalSiteEnum|ORBIT_NOS|
|RadiationAnatomicalSiteEnum|OROPHARYNX|
|RadiationAnatomicalSiteEnum|OTHER|
|RadiationAnatomicalSiteEnum|OVARY_LEFT|
|RadiationAnatomicalSiteEnum|OVARY_RIGHT|
|RadiationAnatomicalSiteEnum|OVARY_BILATERAL|
|RadiationAnatomicalSiteEnum|OVARY_NOS|
|RadiationAnatomicalSiteEnum|PANCREAS_HEAD|
|RadiationAnatomicalSiteEnum|PANCREAS_BODY|
|RadiationAnatomicalSiteEnum|PANCREAS_TAIL|
|RadiationAnatomicalSiteEnum|PANCREAS_NECK|
|RadiationAnatomicalSiteEnum|PANCREAS_NOS|
|RadiationAnatomicalSiteEnum|PARA_AORTIC_NODES|
|RadiationAnatomicalSiteEnum|PAROTID_GLAND_LEFT|
|RadiationAnatomicalSiteEnum|PAROTID_GLAND_RIGHT|
|RadiationAnatomicalSiteEnum|PAROTID_GLAND_BILATERAL|
|RadiationAnatomicalSiteEnum|PAROTID_GLAND_NOS|
|RadiationAnatomicalSiteEnum|PELVIS|
|RadiationAnatomicalSiteEnum|PELVIS_HEMIPELVIS_LEFT|
|RadiationAnatomicalSiteEnum|PELVIS_HEMIPELVIS_RIGHT|
|RadiationAnatomicalSiteEnum|PELVIS_HEMIPELVIS_BILATERAL|
|RadiationAnatomicalSiteEnum|PELVIS_HEMIPELVIS_NOS|
|RadiationAnatomicalSiteEnum|PENIS|
|RadiationAnatomicalSiteEnum|PERINEUM|
|RadiationAnatomicalSiteEnum|PHARYNX_NOS|
|RadiationAnatomicalSiteEnum|PITUITARY GLAND|
|RadiationAnatomicalSiteEnum|PLEURA_LEFT|
|RadiationAnatomicalSiteEnum|PLEURA_RIGHT|
|RadiationAnatomicalSiteEnum|PLEURA_BILATERAL|
|RadiationAnatomicalSiteEnum|PLEURA_NOS|
|RadiationAnatomicalSiteEnum|PROSTATE|
|RadiationAnatomicalSiteEnum|PUBIS|
|RadiationAnatomicalSiteEnum|LARYNX_PYRIFORM_FOSSA|
|RadiationAnatomicalSiteEnum|RADIUS_LEFT|
|RadiationAnatomicalSiteEnum|RADIUS_RIGHT|
|RadiationAnatomicalSiteEnum|RADIUS_NOS|
|RadiationAnatomicalSiteEnum|RECTUM_INCLUDES_SIGMOID|
|RadiationAnatomicalSiteEnum|RIBS_LEFT|
|RadiationAnatomicalSiteEnum|RIBS_RIGHT|
|RadiationAnatomicalSiteEnum|RIBS_BILATERAL|
|RadiationAnatomicalSiteEnum|RIBS_NOS|
|RadiationAnatomicalSiteEnum|SACRUM|
|RadiationAnatomicalSiteEnum|SALIVARY_GLAND_LEFT|
|RadiationAnatomicalSiteEnum|SALIVARY_GLAND_RIGHT|
|RadiationAnatomicalSiteEnum|SALIVARY_GLAND_BILATERAL|
|RadiationAnatomicalSiteEnum|SALIVARY_GLAND_NOS|
|RadiationAnatomicalSiteEnum|SCALP_LEFT|
|RadiationAnatomicalSiteEnum|SCALP_RIGHT|
|RadiationAnatomicalSiteEnum|SCALP_BILATERAL|
|RadiationAnatomicalSiteEnum|SCALP_NOS|
|RadiationAnatomicalSiteEnum|SCAPULA_LEFT|
|RadiationAnatomicalSiteEnum|SCAPULA_RIGHT|
|RadiationAnatomicalSiteEnum|SCAPULA_BILATERAL|
|RadiationAnatomicalSiteEnum|SCAPULA_NOS|
|RadiationAnatomicalSiteEnum|SCROTUM|
|RadiationAnatomicalSiteEnum|SHOULDER_LEFT|
|RadiationAnatomicalSiteEnum|SHOULDER_RIGHT|
|RadiationAnatomicalSiteEnum|SHOULDER_BILATERAL|
|RadiationAnatomicalSiteEnum|SHOULDER_NOS|
|RadiationAnatomicalSiteEnum|SKIN_WHOLE_BODY|
|RadiationAnatomicalSiteEnum|SKIN_NOS|
|RadiationAnatomicalSiteEnum|SKULL_NOS|
|RadiationAnatomicalSiteEnum|SKULL_PARIETAL|
|RadiationAnatomicalSiteEnum|SKULL_TEMPORAL|
|RadiationAnatomicalSiteEnum|SKULL_OCCIPITAL|
|RadiationAnatomicalSiteEnum|SKULL_ZYGOMATIC|
|RadiationAnatomicalSiteEnum|SKULL_FRONTAL|
|RadiationAnatomicalSiteEnum|SPHENOID_SINUS|
|RadiationAnatomicalSiteEnum|SPINE_CERVICAL|
|RadiationAnatomicalSiteEnum|SPINE_THORACIC|
|RadiationAnatomicalSiteEnum|SPINE_LUMBAR|
|RadiationAnatomicalSiteEnum|SPINE_LUMBO_SACRAL|
|RadiationAnatomicalSiteEnum|SPINE_WHOLE|
|RadiationAnatomicalSiteEnum|SPINE_CERVICAL_AND_THORACIC|
|RadiationAnatomicalSiteEnum|SPINE_LUMBAR_AND_THORACIC|
|RadiationAnatomicalSiteEnum|SPINE_NOS|
|RadiationAnatomicalSiteEnum|SPLEEN|
|RadiationAnatomicalSiteEnum|STERNUM|
|RadiationAnatomicalSiteEnum|STOMACH_CARDIA|
|RadiationAnatomicalSiteEnum|STOMACH_FUNDUS|
|RadiationAnatomicalSiteEnum|STOMACH_BODY|
|RadiationAnatomicalSiteEnum|STOMACH_PYLORUS|
|RadiationAnatomicalSiteEnum|STOMACH_GASTRIC ANTRUM|
|RadiationAnatomicalSiteEnum|STOMACH_LESSER CURVATURE|
|RadiationAnatomicalSiteEnum|STOMACH_GREATER CURVATURE|
|RadiationAnatomicalSiteEnum|STOMACH_NOS|
|RadiationAnatomicalSiteEnum|SUBMANDIBULAR_GLANDS|
|RadiationAnatomicalSiteEnum|SUPRACLAVICULAR_NODES_LEFT|
|RadiationAnatomicalSiteEnum|SUPRACLAVICULAR_NODES_RIGHT|
|RadiationAnatomicalSiteEnum|SUPRACLAVICULAR_NODES_BILATERAL|
|RadiationAnatomicalSiteEnum|SUPRACLAVICULAR_NODES_NOS|
|RadiationAnatomicalSiteEnum|TEMPLE_LEFT|
|RadiationAnatomicalSiteEnum|TEMPLE_RIGHT|
|RadiationAnatomicalSiteEnum|TEMPLE_BILATERAL|
|RadiationAnatomicalSiteEnum|TEMPLE_NOS|
|RadiationAnatomicalSiteEnum|TESTIS_LEFT|
|RadiationAnatomicalSiteEnum|TESTIS_RIGHT|
|RadiationAnatomicalSiteEnum|TESTIS_BILATERAL|
|RadiationAnatomicalSiteEnum|TESTIS_NOS|
|RadiationAnatomicalSiteEnum|THYROID|
|RadiationAnatomicalSiteEnum|TIBIA_LEFT|
|RadiationAnatomicalSiteEnum|TIBIA_RIGHT|
|RadiationAnatomicalSiteEnum|TIBIA_NOS|
|RadiationAnatomicalSiteEnum|TONGUE|
|RadiationAnatomicalSiteEnum|TONSIL|
|RadiationAnatomicalSiteEnum|TOES_LEFT_FOOT|
|RadiationAnatomicalSiteEnum|TOES_RIGHT_FOOT|
|RadiationAnatomicalSiteEnum|TOES_NOS|
|RadiationAnatomicalSiteEnum|TRACHEA|
|RadiationAnatomicalSiteEnum|ULNA_LEFT|
|RadiationAnatomicalSiteEnum|ULNA_RIGHT|
|RadiationAnatomicalSiteEnum|ULNA_NOS|
|RadiationAnatomicalSiteEnum|UPPER_LIMB|
|RadiationAnatomicalSiteEnum|LOWER_LIMB|
|RadiationAnatomicalSiteEnum|URETER_LEFT|
|RadiationAnatomicalSiteEnum|URETER_RIGHT|
|RadiationAnatomicalSiteEnum|URETER_BILATERAL|
|RadiationAnatomicalSiteEnum|URETER_NOS|
|RadiationAnatomicalSiteEnum|URETHRA|
|RadiationAnatomicalSiteEnum|UTERUS|
|RadiationAnatomicalSiteEnum|UVULA|
|RadiationAnatomicalSiteEnum|VAGINA|
|RadiationAnatomicalSiteEnum|VULVA|
|RadiationAnatomicalSiteEnum|WHOLE_CNS|
|RadiationAnatomicalSiteEnum|WHOLE_BODY|
|RadiationAnatomicalSiteEnum|WHOLE_BODY_SKIN|

<h2 id="tocS_RadiationIngestSchema">RadiationIngestSchema</h2>

<a id="schemaradiationingestschema"></a>
<a id="schema_RadiationIngestSchema"></a>
<a id="tocSradiationingestschema"></a>
<a id="tocsradiationingestschema"></a>

```json
{
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "radiation_therapy_fractions": 0,
  "radiation_therapy_fractions_not_available": false,
  "radiation_therapy_dosage": 0,
  "radiation_therapy_dosage_not_available": false,
  "anatomical_site_irradiated": "ABDOMEN_WHOLE",
  "radiation_boost": "Yes",
  "reference_radiation_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string",
  "uuid": "string"
}

```

RadiationIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_modality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RadiationTherapyModalityEnum](#schemaradiationtherapymodalityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TherapyTypeEnum](#schematherapytypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_fractions|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_fractions_not_available|boolean|false|none|none|
|radiation_therapy_dosage|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_dosage_not_available|boolean|false|none|none|
|anatomical_site_irradiated|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RadiationAnatomicalSiteEnum](#schemaradiationanatomicalsiteenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_boost|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_radiation_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_RadiationTherapyModalityEnum">RadiationTherapyModalityEnum</h2>

<a id="schemaradiationtherapymodalityenum"></a>
<a id="schema_RadiationTherapyModalityEnum"></a>
<a id="tocSradiationtherapymodalityenum"></a>
<a id="tocsradiationtherapymodalityenum"></a>

```json
"Megavoltage radiation therapy using photons (procedure)"

```

RadiationTherapyModalityEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|RadiationTherapyModalityEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|RadiationTherapyModalityEnum|Megavoltage radiation therapy using photons (procedure)|
|RadiationTherapyModalityEnum|Radiopharmaceutical|
|RadiationTherapyModalityEnum|Teleradiotherapy using electrons (procedure)|
|RadiationTherapyModalityEnum|Teleradiotherapy protons (procedure)|
|RadiationTherapyModalityEnum|Teleradiotherapy neutrons (procedure)|
|RadiationTherapyModalityEnum|Brachytherapy (procedure)|
|RadiationTherapyModalityEnum|Other|
|RadiationTherapyModalityEnum|Not available|
|RadiationTherapyModalityEnum|Teleradiotherapy using photons|

<h2 id="tocS_TherapyTypeEnum">TherapyTypeEnum</h2>

<a id="schematherapytypeenum"></a>
<a id="schema_TherapyTypeEnum"></a>
<a id="tocStherapytypeenum"></a>
<a id="tocstherapytypeenum"></a>

```json
"External"

```

TherapyTypeEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TherapyTypeEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TherapyTypeEnum|External|
|TherapyTypeEnum|Internal|
|TherapyTypeEnum|Not available|

<h2 id="tocS_DrugDoseUnitsEnum">DrugDoseUnitsEnum</h2>

<a id="schemadrugdoseunitsenum"></a>
<a id="schema_DrugDoseUnitsEnum"></a>
<a id="tocSdrugdoseunitsenum"></a>
<a id="tocsdrugdoseunitsenum"></a>

```json
"Bq"

```

DrugDoseUnitsEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DrugDoseUnitsEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|DrugDoseUnitsEnum|Bq|
|DrugDoseUnitsEnum|kBq|
|DrugDoseUnitsEnum|MBq|
|DrugDoseUnitsEnum|GBq|
|DrugDoseUnitsEnum|Ci|
|DrugDoseUnitsEnum|mCi|

<h2 id="tocS_MassUnitUcumEnum">MassUnitUcumEnum</h2>

<a id="schemamassunitucumenum"></a>
<a id="schema_MassUnitUcumEnum"></a>
<a id="tocSmassunitucumenum"></a>
<a id="tocsmassunitucumenum"></a>

```json
"ug"

```

MassUnitUcumEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|MassUnitUcumEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|MassUnitUcumEnum|ug|
|MassUnitUcumEnum|mg|
|MassUnitUcumEnum|nmol|
|MassUnitUcumEnum|umol|

<h2 id="tocS_RadionuclideEnum">RadionuclideEnum</h2>

<a id="schemaradionuclideenum"></a>
<a id="schema_RadionuclideEnum"></a>
<a id="tocSradionuclideenum"></a>
<a id="tocsradionuclideenum"></a>

```json
"Carbon-14"

```

RadionuclideEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|RadionuclideEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|RadionuclideEnum|Carbon-14|
|RadionuclideEnum|Fluorine-18|
|RadionuclideEnum|Sodium-22|
|RadionuclideEnum|Sodium-24|
|RadionuclideEnum|Phosphorus-32|
|RadionuclideEnum|Potassium-42|
|RadionuclideEnum|Potassium-43|
|RadionuclideEnum|Chromium-51|
|RadionuclideEnum|Cobalt-57|
|RadionuclideEnum|Cobalt-58|
|RadionuclideEnum|Iron-59|
|RadionuclideEnum|Cobalt-60|
|RadionuclideEnum|Copper-64|
|RadionuclideEnum|Copper-67|
|RadionuclideEnum|Gallium-67|
|RadionuclideEnum|Selenium-75|
|RadionuclideEnum|Krypton-81m|
|RadionuclideEnum|Krypton-85|
|RadionuclideEnum|Strontium-85|
|RadionuclideEnum|Strontium-87m|
|RadionuclideEnum|Strontium-89|
|RadionuclideEnum|Yttrium-90|
|RadionuclideEnum|Ruthenium-97|
|RadionuclideEnum|Technetium-99m|
|RadionuclideEnum|Indium-111|
|RadionuclideEnum|Indium-113m|
|RadionuclideEnum|Iodine-123|
|RadionuclideEnum|Iodine-125|
|RadionuclideEnum|Xenon-127|
|RadionuclideEnum|Iodine-131|
|RadionuclideEnum|Barium-133|
|RadionuclideEnum|Xenon-133|
|RadionuclideEnum|Gadolinium-153|
|RadionuclideEnum|Samarium-153|
|RadionuclideEnum|Ytterbium-169|
|RadionuclideEnum|Lutetium-177|
|RadionuclideEnum|Tantalum-178|
|RadionuclideEnum|Rhenium-186|
|RadionuclideEnum|Rhenium-188|
|RadionuclideEnum|Iridium-191m|
|RadionuclideEnum|Gold-198|
|RadionuclideEnum|Gold-199|
|RadionuclideEnum|Thallium-201|
|RadionuclideEnum|Lead-203|
|RadionuclideEnum|Radium-223|

<h2 id="tocS_RadiopharmaceuticalTherapyIngestSchema">RadiopharmaceuticalTherapyIngestSchema</h2>

<a id="schemaradiopharmaceuticaltherapyingestschema"></a>
<a id="schema_RadiopharmaceuticalTherapyIngestSchema"></a>
<a id="tocSradiopharmaceuticaltherapyingestschema"></a>
<a id="tocsradiopharmaceuticaltherapyingestschema"></a>

```json
{
  "rxnorm_code": "string",
  "agent_name": "string",
  "radionuclide": "Carbon-14",
  "radionuclide_other": "string",
  "start_date": {},
  "end_date": {},
  "cumulative_drug_dose": 0,
  "cumulative_drug_dose_not_available": false,
  "drug_dose_units": "Bq",
  "mass_value": 0,
  "mass_value_not_available": false,
  "mass_unit_ucum": "ug",
  "number_of_cycles": 0,
  "number_of_cycles_not_available": false,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string",
  "uuid": "string"
}

```

RadiopharmaceuticalTherapyIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rxnorm_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|agent_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radionuclide|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RadionuclideEnum](#schemaradionuclideenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radionuclide_other|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|start_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|end_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cumulative_drug_dose_not_available|boolean|false|none|none|
|drug_dose_units|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DrugDoseUnitsEnum](#schemadrugdoseunitsenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mass_value|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mass_value_not_available|boolean|false|none|none|
|mass_unit_ucum|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MassUnitUcumEnum](#schemamassunitucumenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles_not_available|boolean|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SampleRegistrationIngestSchema">SampleRegistrationIngestSchema</h2>

<a id="schemasampleregistrationingestschema"></a>
<a id="schema_SampleRegistrationIngestSchema"></a>
<a id="tocSsampleregistrationingestschema"></a>
<a id="tocssampleregistrationingestschema"></a>

```json
{
  "submitter_sample_id": "string",
  "sample_type": "Amplified DNA",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "uuid": "string"
}

```

SampleRegistrationIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_sample_id|string|true|none|none|
|sample_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SampleTypeEnum](#schemasampletypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_specimen_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SampleTypeEnum">SampleTypeEnum</h2>

<a id="schemasampletypeenum"></a>
<a id="schema_SampleTypeEnum"></a>
<a id="tocSsampletypeenum"></a>
<a id="tocssampletypeenum"></a>

```json
"Amplified DNA"

```

SampleTypeEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|SampleTypeEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|SampleTypeEnum|Amplified DNA|
|SampleTypeEnum|ctDNA|
|SampleTypeEnum|Other DNA enrichments|
|SampleTypeEnum|Other RNA fractions|
|SampleTypeEnum|polyA+ RNA|
|SampleTypeEnum|Protein|
|SampleTypeEnum|rRNA-depleted RNA|
|SampleTypeEnum|Total DNA|
|SampleTypeEnum|Total RNA|

<h2 id="tocS_CellsMeasureMethodEnum">CellsMeasureMethodEnum</h2>

<a id="schemacellsmeasuremethodenum"></a>
<a id="schema_CellsMeasureMethodEnum"></a>
<a id="tocScellsmeasuremethodenum"></a>
<a id="tocscellsmeasuremethodenum"></a>

```json
"Genomics"

```

CellsMeasureMethodEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|CellsMeasureMethodEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|CellsMeasureMethodEnum|Genomics|
|CellsMeasureMethodEnum|Image analysis|
|CellsMeasureMethodEnum|Pathology estimate by percent nuclei|
|CellsMeasureMethodEnum|Other|
|CellsMeasureMethodEnum|Not available|

<h2 id="tocS_ConfirmedDiagnosisTumourEnum">ConfirmedDiagnosisTumourEnum</h2>

<a id="schemaconfirmeddiagnosistumourenum"></a>
<a id="schema_ConfirmedDiagnosisTumourEnum"></a>
<a id="tocSconfirmeddiagnosistumourenum"></a>
<a id="tocsconfirmeddiagnosistumourenum"></a>

```json
"Yes"

```

ConfirmedDiagnosisTumourEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ConfirmedDiagnosisTumourEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|ConfirmedDiagnosisTumourEnum|Yes|
|ConfirmedDiagnosisTumourEnum|No|
|ConfirmedDiagnosisTumourEnum|Not done|
|ConfirmedDiagnosisTumourEnum|Not available|

<h2 id="tocS_PercentCellsRangeEnum">PercentCellsRangeEnum</h2>

<a id="schemapercentcellsrangeenum"></a>
<a id="schema_PercentCellsRangeEnum"></a>
<a id="tocSpercentcellsrangeenum"></a>
<a id="tocspercentcellsrangeenum"></a>

```json
"0-19%"

```

PercentCellsRangeEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|PercentCellsRangeEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|PercentCellsRangeEnum|0-19%|
|PercentCellsRangeEnum|20-50%|
|PercentCellsRangeEnum|51-100%|
|PercentCellsRangeEnum|Not available|

<h2 id="tocS_SpecimenIngestSchema">SpecimenIngestSchema</h2>

<a id="schemaspecimeningestschema"></a>
<a id="schema_SpecimenIngestSchema"></a>
<a id="tocSspecimeningestschema"></a>
<a id="tocsspecimeningestschema"></a>

```json
{
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string",
  "specimen_collection_date": {},
  "specimen_storage": "Cut slide",
  "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "specimen_laterality": "Left",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "specimen_tissue_source": "Abdominal fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "uuid": "string"
}

```

SpecimenIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|string|true|none|none|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_collection_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_storage|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StorageEnum](#schemastorageenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_processing|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenProcessingEnum](#schemaspecimenprocessingenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_histological_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_anatomic_location|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_laterality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenLateralityEnum](#schemaspecimenlateralityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ConfirmedDiagnosisTumourEnum](#schemaconfirmeddiagnosistumourenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_tumour_presence|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ConfirmedDiagnosisTumourEnum](#schemaconfirmeddiagnosistumourenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grading_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradingSystemEnum](#schematumourgradingsystemenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grade|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradeEnum](#schematumourgradeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_range|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PercentCellsRangeEnum](#schemapercentcellsrangeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_measurement_method|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CellsMeasureMethodEnum](#schemacellsmeasuremethodenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_tissue_source|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenTissueSourceEnum](#schemaspecimentissuesourceenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_normal_designation|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourDesginationEnum](#schematumourdesginationenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenTypeEnum](#schemaspecimentypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SpecimenLateralityEnum">SpecimenLateralityEnum</h2>

<a id="schemaspecimenlateralityenum"></a>
<a id="schema_SpecimenLateralityEnum"></a>
<a id="tocSspecimenlateralityenum"></a>
<a id="tocsspecimenlateralityenum"></a>

```json
"Left"

```

SpecimenLateralityEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|SpecimenLateralityEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|SpecimenLateralityEnum|Left|
|SpecimenLateralityEnum|Not applicable|
|SpecimenLateralityEnum|Right|
|SpecimenLateralityEnum|Not available|

<h2 id="tocS_SpecimenProcessingEnum">SpecimenProcessingEnum</h2>

<a id="schemaspecimenprocessingenum"></a>
<a id="schema_SpecimenProcessingEnum"></a>
<a id="tocSspecimenprocessingenum"></a>
<a id="tocsspecimenprocessingenum"></a>

```json
"Cryopreservation in liquid nitrogen (dead tissue)"

```

SpecimenProcessingEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|SpecimenProcessingEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|SpecimenProcessingEnum|Cryopreservation in liquid nitrogen (dead tissue)|
|SpecimenProcessingEnum|Cryopreservation in dry ice (dead tissue)|
|SpecimenProcessingEnum|Cryopreservation of live cells in liquid nitrogen|
|SpecimenProcessingEnum|Cryopreservation - other|
|SpecimenProcessingEnum|Formalin fixed & paraffin embedded|
|SpecimenProcessingEnum|Formalin fixed - buffered|
|SpecimenProcessingEnum|Formalin fixed - unbuffered|
|SpecimenProcessingEnum|Fresh|
|SpecimenProcessingEnum|Other|
|SpecimenProcessingEnum|Not available|

<h2 id="tocS_SpecimenTissueSourceEnum">SpecimenTissueSourceEnum</h2>

<a id="schemaspecimentissuesourceenum"></a>
<a id="schema_SpecimenTissueSourceEnum"></a>
<a id="tocSspecimentissuesourceenum"></a>
<a id="tocsspecimentissuesourceenum"></a>

```json
"Abdominal fluid"

```

SpecimenTissueSourceEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|SpecimenTissueSourceEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|SpecimenTissueSourceEnum|Abdominal fluid|
|SpecimenTissueSourceEnum|Amniotic fluid|
|SpecimenTissueSourceEnum|Arterial blood|
|SpecimenTissueSourceEnum|Bile|
|SpecimenTissueSourceEnum|Blood derived - bone marrow|
|SpecimenTissueSourceEnum|Blood derived - peripheral blood|
|SpecimenTissueSourceEnum|Bone marrow fluid|
|SpecimenTissueSourceEnum|Bone marrow derived mononuclear cells|
|SpecimenTissueSourceEnum|Buccal cell|
|SpecimenTissueSourceEnum|Buffy coat|
|SpecimenTissueSourceEnum|Cerebrospinal fluid|
|SpecimenTissueSourceEnum|Cervical mucus|
|SpecimenTissueSourceEnum|Convalescent plasma|
|SpecimenTissueSourceEnum|Cord blood|
|SpecimenTissueSourceEnum|Duodenal fluid|
|SpecimenTissueSourceEnum|Female genital fluid|
|SpecimenTissueSourceEnum|Fetal blood|
|SpecimenTissueSourceEnum|Hydrocele fluid|
|SpecimenTissueSourceEnum|Male genital fluid|
|SpecimenTissueSourceEnum|Other|
|SpecimenTissueSourceEnum|Pancreatic fluid|
|SpecimenTissueSourceEnum|Pericardial effusion|
|SpecimenTissueSourceEnum|Pleural fluid|
|SpecimenTissueSourceEnum|Renal cyst fluid|
|SpecimenTissueSourceEnum|Saliva|
|SpecimenTissueSourceEnum|Seminal fluid|
|SpecimenTissueSourceEnum|Serum|
|SpecimenTissueSourceEnum|Solid tissue|
|SpecimenTissueSourceEnum|Sputum|
|SpecimenTissueSourceEnum|Synovial fluid|
|SpecimenTissueSourceEnum|Urine|
|SpecimenTissueSourceEnum|Venous blood|
|SpecimenTissueSourceEnum|Vitreous fluid|
|SpecimenTissueSourceEnum|Whole blood|
|SpecimenTissueSourceEnum|Wound|

<h2 id="tocS_SpecimenTypeEnum">SpecimenTypeEnum</h2>

<a id="schemaspecimentypeenum"></a>
<a id="schema_SpecimenTypeEnum"></a>
<a id="tocSspecimentypeenum"></a>
<a id="tocsspecimentypeenum"></a>

```json
"Cell line - derived from normal"

```

SpecimenTypeEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|SpecimenTypeEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|SpecimenTypeEnum|Cell line - derived from normal|
|SpecimenTypeEnum|Cell line - derived from primary tumour|
|SpecimenTypeEnum|Cell line - derived from metastatic tumour|
|SpecimenTypeEnum|Cell line - derived from xenograft tumour|
|SpecimenTypeEnum|Metastatic tumour - additional metastatic|
|SpecimenTypeEnum|Metastatic tumour - metastasis local to lymph node|
|SpecimenTypeEnum|Metastatic tumour - metastasis to distant location|
|SpecimenTypeEnum|Metastatic tumour|
|SpecimenTypeEnum|Normal - tissue adjacent to primary tumour|
|SpecimenTypeEnum|Normal|
|SpecimenTypeEnum|Primary tumour - additional new primary|
|SpecimenTypeEnum|Primary tumour - adjacent to normal|
|SpecimenTypeEnum|Primary tumour|
|SpecimenTypeEnum|Tumour - unknown if derived from primary or metastatic tumour|
|SpecimenTypeEnum|Xenograft - derived from primary tumour|
|SpecimenTypeEnum|Xenograft - derived from metastatic tumour|
|SpecimenTypeEnum|Xenograft - derived from tumour cell line|
|SpecimenTypeEnum|Locally recurrent tumour (non-metastatic)|
|SpecimenTypeEnum|Recurrent tumour, NOS|
|SpecimenTypeEnum|Metastatic tumour of uncertain primary|

<h2 id="tocS_StorageEnum">StorageEnum</h2>

<a id="schemastorageenum"></a>
<a id="schema_StorageEnum"></a>
<a id="tocSstorageenum"></a>
<a id="tocsstorageenum"></a>

```json
"Cut slide"

```

StorageEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|StorageEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|StorageEnum|Cut slide|
|StorageEnum|Frozen in -70 freezer|
|StorageEnum|Frozen in liquid nitrogen|
|StorageEnum|Frozen in vapour phase|
|StorageEnum|Not Applicable|
|StorageEnum|OCT embedded|
|StorageEnum|Other|
|StorageEnum|Paraffin block|
|StorageEnum|RNA later frozen|
|StorageEnum|Not available|

<h2 id="tocS_TumourDesginationEnum">TumourDesginationEnum</h2>

<a id="schematumourdesginationenum"></a>
<a id="schema_TumourDesginationEnum"></a>
<a id="tocStumourdesginationenum"></a>
<a id="tocstumourdesginationenum"></a>

```json
"Normal"

```

TumourDesginationEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TumourDesginationEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TumourDesginationEnum|Normal|
|TumourDesginationEnum|Tumour|

<h2 id="tocS_TumourGradeEnum">TumourGradeEnum</h2>

<a id="schematumourgradeenum"></a>
<a id="schema_TumourGradeEnum"></a>
<a id="tocStumourgradeenum"></a>
<a id="tocstumourgradeenum"></a>

```json
"Low grade"

```

TumourGradeEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TumourGradeEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TumourGradeEnum|Low grade|
|TumourGradeEnum|High grade|
|TumourGradeEnum|GX|
|TumourGradeEnum|G1|
|TumourGradeEnum|G2|
|TumourGradeEnum|G3|
|TumourGradeEnum|G4|
|TumourGradeEnum|Low|
|TumourGradeEnum|High|
|TumourGradeEnum|Grade 1|
|TumourGradeEnum|Grade 2|
|TumourGradeEnum|Grade 3|
|TumourGradeEnum|Grade 4|
|TumourGradeEnum|Grade I|
|TumourGradeEnum|Grade II|
|TumourGradeEnum|Grade III|
|TumourGradeEnum|Grade IV|
|TumourGradeEnum|Grade Group 1|
|TumourGradeEnum|Grade Group 2|
|TumourGradeEnum|Grade Group 3|
|TumourGradeEnum|Grade Group 4|
|TumourGradeEnum|Grade Group 5|
|TumourGradeEnum|Not available|

<h2 id="tocS_TumourGradingSystemEnum">TumourGradingSystemEnum</h2>

<a id="schematumourgradingsystemenum"></a>
<a id="schema_TumourGradingSystemEnum"></a>
<a id="tocStumourgradingsystemenum"></a>
<a id="tocstumourgradingsystemenum"></a>

```json
"FNCLCC grading system"

```

TumourGradingSystemEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TumourGradingSystemEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TumourGradingSystemEnum|FNCLCC grading system|
|TumourGradingSystemEnum|Four-tier grading system|
|TumourGradingSystemEnum|Gleason grade group system|
|TumourGradingSystemEnum|Grading system for GISTs|
|TumourGradingSystemEnum|Grading system for GNETs|
|TumourGradingSystemEnum|IASLC grading system|
|TumourGradingSystemEnum|ISUP grading system|
|TumourGradingSystemEnum|Nottingham grading system|
|TumourGradingSystemEnum|Nuclear grading system for DCIS|
|TumourGradingSystemEnum|Scarff-Bloom-Richardson grading system|
|TumourGradingSystemEnum|Three-tier grading system|
|TumourGradingSystemEnum|Two-tier grading system|
|TumourGradingSystemEnum|WHO grading system for CNS tumours|
|TumourGradingSystemEnum|Not available|

<h2 id="tocS_LymphovascularInvasionEnum">LymphovascularInvasionEnum</h2>

<a id="schemalymphovascularinvasionenum"></a>
<a id="schema_LymphovascularInvasionEnum"></a>
<a id="tocSlymphovascularinvasionenum"></a>
<a id="tocslymphovascularinvasionenum"></a>

```json
"Absent"

```

LymphovascularInvasionEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|LymphovascularInvasionEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|LymphovascularInvasionEnum|Absent|
|LymphovascularInvasionEnum|Both lymphatic and small vessel and venous (large vessel) invasion|
|LymphovascularInvasionEnum|Lymphatic and small vessel invasion only|
|LymphovascularInvasionEnum|Not applicable|
|LymphovascularInvasionEnum|Present|
|LymphovascularInvasionEnum|Venous (large vessel) invasion only|
|LymphovascularInvasionEnum|Not available|

<h2 id="tocS_MarginsStatusEnum">MarginsStatusEnum</h2>

<a id="schemamarginsstatusenum"></a>
<a id="schema_MarginsStatusEnum"></a>
<a id="tocSmarginsstatusenum"></a>
<a id="tocsmarginsstatusenum"></a>

```json
"Margins clear"

```

MarginsStatusEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|MarginsStatusEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|MarginsStatusEnum|Margins clear|
|MarginsStatusEnum|Margin(s) involved|
|MarginsStatusEnum|Not applicable|
|MarginsStatusEnum|Not available|
|MarginsStatusEnum|Unknown|

<h2 id="tocS_PerineuralInvasionEnum">PerineuralInvasionEnum</h2>

<a id="schemaperineuralinvasionenum"></a>
<a id="schema_PerineuralInvasionEnum"></a>
<a id="tocSperineuralinvasionenum"></a>
<a id="tocsperineuralinvasionenum"></a>

```json
"Absent"

```

PerineuralInvasionEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|PerineuralInvasionEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|PerineuralInvasionEnum|Absent|
|PerineuralInvasionEnum|Cannot be assessed|
|PerineuralInvasionEnum|Not applicable|
|PerineuralInvasionEnum|Present|
|PerineuralInvasionEnum|Not available|

<h2 id="tocS_SurgeryIngestSchema">SurgeryIngestSchema</h2>

<a id="schemasurgeryingestschema"></a>
<a id="schema_SurgeryIngestSchema"></a>
<a id="tocSsurgeryingestschema"></a>
<a id="tocssurgeryingestschema"></a>

```json
{
  "surgery_type": "string",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_length": 0,
  "tumour_length_not_available": false,
  "tumour_width": 0,
  "tumour_width_not_available": false,
  "greatest_dimension_tumour": 0,
  "greatest_dimension_tumour_not_available": false,
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margins_status": "Margins clear",
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "surgery_reference_database": "SNOMED",
  "surgery_reference_identifier": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string",
  "uuid": "string"
}

```

SurgeryIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_location|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SurgeryLocationEnum](#schemasurgerylocationenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length_not_available|boolean|false|none|none|
|tumour_width|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_width_not_available|boolean|false|none|none|
|greatest_dimension_tumour|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|greatest_dimension_tumour_not_available|boolean|false|none|none|
|tumour_focality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourFocalityEnum](#schematumourfocalityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|residual_tumour_classification|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourClassificationEnum](#schematumourclassificationenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margins_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginsStatusEnum](#schemamarginsstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lymphovascular_invasion|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LymphovascularInvasionEnum](#schemalymphovascularinvasionenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|perineural_invasion|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PerineuralInvasionEnum](#schemaperineuralinvasionenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_reference_database|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SurgeryReferenceDatabaseEnum](#schemasurgeryreferencedatabaseenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_reference_identifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SurgeryLocationEnum">SurgeryLocationEnum</h2>

<a id="schemasurgerylocationenum"></a>
<a id="schema_SurgeryLocationEnum"></a>
<a id="tocSsurgerylocationenum"></a>
<a id="tocssurgerylocationenum"></a>

```json
"Local recurrence"

```

SurgeryLocationEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|SurgeryLocationEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|SurgeryLocationEnum|Local recurrence|
|SurgeryLocationEnum|Metastatic|
|SurgeryLocationEnum|Primary|

<h2 id="tocS_SurgeryReferenceDatabaseEnum">SurgeryReferenceDatabaseEnum</h2>

<a id="schemasurgeryreferencedatabaseenum"></a>
<a id="schema_SurgeryReferenceDatabaseEnum"></a>
<a id="tocSsurgeryreferencedatabaseenum"></a>
<a id="tocssurgeryreferencedatabaseenum"></a>

```json
"SNOMED"

```

SurgeryReferenceDatabaseEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|SurgeryReferenceDatabaseEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|SurgeryReferenceDatabaseEnum|SNOMED|
|SurgeryReferenceDatabaseEnum|NCIt|
|SurgeryReferenceDatabaseEnum|UMLS|
|SurgeryReferenceDatabaseEnum|CCI|

<h2 id="tocS_TumourClassificationEnum">TumourClassificationEnum</h2>

<a id="schematumourclassificationenum"></a>
<a id="schema_TumourClassificationEnum"></a>
<a id="tocStumourclassificationenum"></a>
<a id="tocstumourclassificationenum"></a>

```json
"Not applicable"

```

TumourClassificationEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TumourClassificationEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TumourClassificationEnum|Not applicable|
|TumourClassificationEnum|RX|
|TumourClassificationEnum|R0|
|TumourClassificationEnum|R1|
|TumourClassificationEnum|R2|
|TumourClassificationEnum|Not available|

<h2 id="tocS_TumourFocalityEnum">TumourFocalityEnum</h2>

<a id="schematumourfocalityenum"></a>
<a id="schema_TumourFocalityEnum"></a>
<a id="tocStumourfocalityenum"></a>
<a id="tocstumourfocalityenum"></a>

```json
"Cannot be assessed"

```

TumourFocalityEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TumourFocalityEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TumourFocalityEnum|Cannot be assessed|
|TumourFocalityEnum|Multifocal|
|TumourFocalityEnum|Not applicable|
|TumourFocalityEnum|Unifocal|
|TumourFocalityEnum|Not available|

<h2 id="tocS_TreatmentIngestSchema">TreatmentIngestSchema</h2>

<a id="schematreatmentingestschema"></a>
<a id="schema_TreatmentIngestSchema"></a>
<a id="tocStreatmentingestschema"></a>
<a id="tocstreatmentingestschema"></a>

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Bone marrow transplant"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": {
    "day_interval": 0,
    "month_interval": 0
  },
  "treatment_end_date": {
    "day_interval": 0,
    "month_interval": 0
  },
  "treatment_intent": "Curative",
  "treatment_setting": "Adjuvant",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "status_of_treatment": "Treatment completed as prescribed",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "uuid": "string"
}

```

TreatmentIngestSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|string|true|none|none|
|treatment_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[TreatmentTypeEnum](#schematreatmenttypeenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_primary_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_start_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_end_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_intent|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentIntentEnum](#schematreatmentintentenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_setting|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentSettingEnum](#schematreatmentsettingenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|response_to_treatment_criteria_method|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentResponseMethodEnum](#schematreatmentresponsemethodenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|response_to_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentResponseEnum](#schematreatmentresponseenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status_of_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentStatusEnum](#schematreatmentstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string|true|none|none|
|uuid|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_TreatmentIntentEnum">TreatmentIntentEnum</h2>

<a id="schematreatmentintentenum"></a>
<a id="schema_TreatmentIntentEnum"></a>
<a id="tocStreatmentintentenum"></a>
<a id="tocstreatmentintentenum"></a>

```json
"Curative"

```

TreatmentIntentEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TreatmentIntentEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TreatmentIntentEnum|Curative|
|TreatmentIntentEnum|Palliative|
|TreatmentIntentEnum|Supportive|
|TreatmentIntentEnum|Diagnostic|
|TreatmentIntentEnum|Preventive|
|TreatmentIntentEnum|Guidance|
|TreatmentIntentEnum|Screening|
|TreatmentIntentEnum|Forensic|
|TreatmentIntentEnum|Not available|
|TreatmentIntentEnum|Combined diagnostic and therapeutic intent|
|TreatmentIntentEnum|Life-sustaining intent|

<h2 id="tocS_TreatmentResponseEnum">TreatmentResponseEnum</h2>

<a id="schematreatmentresponseenum"></a>
<a id="schema_TreatmentResponseEnum"></a>
<a id="tocStreatmentresponseenum"></a>
<a id="tocstreatmentresponseenum"></a>

```json
"Complete response"

```

TreatmentResponseEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TreatmentResponseEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TreatmentResponseEnum|Complete response|
|TreatmentResponseEnum|Partial response|
|TreatmentResponseEnum|Progressive disease|
|TreatmentResponseEnum|Stable disease|
|TreatmentResponseEnum|Immune complete response (iCR)|
|TreatmentResponseEnum|Immune partial response (iPR)|
|TreatmentResponseEnum|Immune uncomfirmed progressive disease (iUPD)|
|TreatmentResponseEnum|Immune confirmed progressive disease (iCPD)|
|TreatmentResponseEnum|Immune stable disease (iSD)|
|TreatmentResponseEnum|Complete remission|
|TreatmentResponseEnum|Partial remission|
|TreatmentResponseEnum|Minor response|
|TreatmentResponseEnum|Complete remission without measurable residual disease (CR MRD-)|
|TreatmentResponseEnum|Complete remission with incomplete hematologic recovery (CRi)|
|TreatmentResponseEnum|Morphologic leukemia-free state|
|TreatmentResponseEnum|Primary refractory disease|
|TreatmentResponseEnum|Hematologic relapse (after CR MRD-, CR, CRi)|
|TreatmentResponseEnum|Molecular relapse (after CR MRD-)|
|TreatmentResponseEnum|Physician assessed complete response|
|TreatmentResponseEnum|Physician assessed partial response|
|TreatmentResponseEnum|Physician assessed stable disease|
|TreatmentResponseEnum|No evidence of disease (NED)|
|TreatmentResponseEnum|Major response|
|TreatmentResponseEnum|Not available|

<h2 id="tocS_TreatmentResponseMethodEnum">TreatmentResponseMethodEnum</h2>

<a id="schematreatmentresponsemethodenum"></a>
<a id="schema_TreatmentResponseMethodEnum"></a>
<a id="tocStreatmentresponsemethodenum"></a>
<a id="tocstreatmentresponsemethodenum"></a>

```json
"RECIST 1.1"

```

TreatmentResponseMethodEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TreatmentResponseMethodEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TreatmentResponseMethodEnum|RECIST 1.1|
|TreatmentResponseMethodEnum|iRECIST|
|TreatmentResponseMethodEnum|Cheson CLL 2012 Oncology Response Criteria|
|TreatmentResponseMethodEnum|Response Assessment in Neuro-Oncology (RANO)|
|TreatmentResponseMethodEnum|AML Response Criteria|
|TreatmentResponseMethodEnum|Physician Assessed Response Criteria|
|TreatmentResponseMethodEnum|Blazer score|
|TreatmentResponseMethodEnum|Not available|

<h2 id="tocS_TreatmentSettingEnum">TreatmentSettingEnum</h2>

<a id="schematreatmentsettingenum"></a>
<a id="schema_TreatmentSettingEnum"></a>
<a id="tocStreatmentsettingenum"></a>
<a id="tocstreatmentsettingenum"></a>

```json
"Adjuvant"

```

TreatmentSettingEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TreatmentSettingEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TreatmentSettingEnum|Adjuvant|
|TreatmentSettingEnum|Neoadjuvant|
|TreatmentSettingEnum|Not available|

<h2 id="tocS_TreatmentStatusEnum">TreatmentStatusEnum</h2>

<a id="schematreatmentstatusenum"></a>
<a id="schema_TreatmentStatusEnum"></a>
<a id="tocStreatmentstatusenum"></a>
<a id="tocstreatmentstatusenum"></a>

```json
"Treatment completed as prescribed"

```

TreatmentStatusEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TreatmentStatusEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TreatmentStatusEnum|Treatment completed as prescribed|
|TreatmentStatusEnum|Treatment incomplete due to technical or organizational problems|
|TreatmentStatusEnum|Treatment incomplete because patient died|
|TreatmentStatusEnum|Patient choice (stopped or interrupted treatment)|
|TreatmentStatusEnum|Physician decision (stopped or interrupted treatment)|
|TreatmentStatusEnum|Treatment stopped due to lack of efficacy (disease progression)|
|TreatmentStatusEnum|Treatment stopped due to acute toxicity|
|TreatmentStatusEnum|Treatment ongoing|
|TreatmentStatusEnum|Other|
|TreatmentStatusEnum|Not available|

<h2 id="tocS_TreatmentTypeEnum">TreatmentTypeEnum</h2>

<a id="schematreatmenttypeenum"></a>
<a id="schema_TreatmentTypeEnum"></a>
<a id="tocStreatmenttypeenum"></a>
<a id="tocstreatmenttypeenum"></a>

```json
"Bone marrow transplant"

```

TreatmentTypeEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TreatmentTypeEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|TreatmentTypeEnum|Bone marrow transplant|
|TreatmentTypeEnum|Systemic therapy|
|TreatmentTypeEnum|No treatment|
|TreatmentTypeEnum|Targeted molecular therapy|
|TreatmentTypeEnum|Photodynamic therapy|
|TreatmentTypeEnum|Radiation therapy|
|TreatmentTypeEnum|Stem cell transplant|
|TreatmentTypeEnum|Surgery|
|TreatmentTypeEnum|Other|
|TreatmentTypeEnum|Unknown whether patient received treatment|
|TreatmentTypeEnum|Patient referred for treatment at other center, details unknown|
|TreatmentTypeEnum|Radiopharmaceutical Therapy|

<h2 id="tocS_ProgramUpdateSchema">ProgramUpdateSchema</h2>

<a id="schemaprogramupdateschema"></a>
<a id="schema_ProgramUpdateSchema"></a>
<a id="tocSprogramupdateschema"></a>
<a id="tocsprogramupdateschema"></a>

```json
{
  "program_description": "string",
  "program_name": "string",
  "keywords": [
    null
  ],
  "status": "Ongoing",
  "context": "Clinical",
  "participant_criteria": "string",
  "principal_investigators": [
    null
  ],
  "lead_organizations": [
    null
  ],
  "collaborators": [
    null
  ],
  "funding_sources": [
    null
  ],
  "publication_links": [
    null
  ],
  "program_url": "string",
  "pancan_cohort": "Yes",
  "pancan_id": "string"
}

```

ProgramUpdateSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|keywords|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StatusEnum](#schemastatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|context|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ContextEnum](#schemacontextenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|participant_criteria|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|principal_investigators|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lead_organizations|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|collaborators|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|funding_sources|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publication_links|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_url|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pancan_cohort|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PancanCohortEnum](#schemapancancohortenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pancan_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_MetadataSchema">MetadataSchema</h2>

<a id="schemametadataschema"></a>
<a id="schema_MetadataSchema"></a>
<a id="tocSmetadataschema"></a>
<a id="tocsmetadataschema"></a>

```json
{
  "metadata": {}
}

```

MetadataSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|metadata|object|true|none|none|

<h2 id="tocS_DonorWithClinicalDataSchema">DonorWithClinicalDataSchema</h2>

<a id="schemadonorwithclinicaldataschema"></a>
<a id="schema_DonorWithClinicalDataSchema"></a>
<a id="tocSdonorwithclinicaldataschema"></a>
<a id="tocsdonorwithclinicaldataschema"></a>

```json
{
  "submitter_donor_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "is_deceased": "Yes",
  "lost_to_follow_up": "Yes",
  "lost_to_followup_reason": "Completed study",
  "cause_of_death": "Died of cancer",
  "date_of_birth": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death_is_estimated": "Yes",
  "date_resolution": "string",
  "program_id": "string",
  "primary_diagnoses": [
    {
      "submitter_primary_diagnosis_id": "string",
      "primary_site": "Accessory sinuses",
      "date_of_diagnosis": {
        "day_interval": 0,
        "month_interval": 0
      },
      "cancer_type_code": "string",
      "basis_of_diagnosis": "Clinical investigation",
      "laterality": "Bilateral",
      "clinical_tumour_staging_system": "AJCC cancer staging system",
      "clinical_t_category": "T0",
      "clinical_n_category": "N0",
      "clinical_m_category": "M0",
      "clinical_stage_group": "Stage 0",
      "pathological_tumour_staging_system": "AJCC cancer staging system",
      "pathological_t_category": "T0",
      "pathological_n_category": "N0",
      "pathological_m_category": "M0",
      "pathological_stage_group": "Stage 0",
      "specimens": [
        {
          "submitter_specimen_id": "string",
          "submitter_treatment_id": "string",
          "specimen_collection_date": {},
          "specimen_storage": "Cut slide",
          "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
          "tumour_histological_type": "string",
          "specimen_anatomic_location": "string",
          "specimen_laterality": "Left",
          "reference_pathology_confirmed_diagnosis": "Yes",
          "reference_pathology_confirmed_tumour_presence": "Yes",
          "tumour_grading_system": "FNCLCC grading system",
          "tumour_grade": "Low grade",
          "percent_tumour_cells_range": "0-19%",
          "percent_tumour_cells_measurement_method": "Genomics",
          "specimen_tissue_source": "Abdominal fluid",
          "tumour_normal_designation": "Normal",
          "specimen_type": "Cell line - derived from normal",
          "sample_registrations": [
            {
              "submitter_sample_id": "string",
              "sample_type": "Amplified DNA"
            }
          ]
        }
      ],
      "treatments": [
        {
          "submitter_treatment_id": "string",
          "treatment_type": [
            "Bone marrow transplant"
          ],
          "is_primary_treatment": "Yes",
          "treatment_start_date": {
            "day_interval": 0,
            "month_interval": 0
          },
          "treatment_end_date": {
            "day_interval": 0,
            "month_interval": 0
          },
          "treatment_intent": "Curative",
          "treatment_setting": "Adjuvant",
          "response_to_treatment_criteria_method": "RECIST 1.1",
          "response_to_treatment": "Complete response",
          "status_of_treatment": "Treatment completed as prescribed",
          "systemic_therapies": [
            {
              "systemic_therapy_type": "string",
              "days_per_cycle": 0,
              "days_per_cycle_not_available": false,
              "number_of_cycles": 0,
              "number_of_cycles_not_available": false,
              "start_date": {},
              "end_date": {},
              "drug_reference_database": "RxNorm",
              "drug_name": "string",
              "drug_reference_identifier": "string",
              "drug_dose_units": "mg/m2",
              "prescribed_cumulative_drug_dose": 0,
              "prescribed_cumulative_drug_dose_not_available": false,
              "actual_cumulative_drug_dose": 0,
              "actual_cumulative_drug_dose_not_available": false
            }
          ],
          "radiations": [
            {
              "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
              "radiation_therapy_type": "External",
              "radiation_therapy_fractions": 0,
              "radiation_therapy_fractions_not_available": false,
              "radiation_therapy_dosage": 0,
              "radiation_therapy_dosage_not_available": false,
              "anatomical_site_irradiated": "ABDOMEN_WHOLE",
              "radiation_boost": "Yes",
              "reference_radiation_treatment_id": "string"
            }
          ],
          "surgeries": [
            {
              "surgery_type": "string",
              "surgery_site": "string",
              "surgery_location": "Local recurrence",
              "tumour_length": 0,
              "tumour_length_not_available": false,
              "tumour_width": 0,
              "tumour_width_not_available": false,
              "greatest_dimension_tumour": 0,
              "greatest_dimension_tumour_not_available": false,
              "tumour_focality": "Cannot be assessed",
              "residual_tumour_classification": "Not applicable",
              "margins_status": "Margins clear",
              "lymphovascular_invasion": "Absent",
              "perineural_invasion": "Absent",
              "surgery_reference_database": "SNOMED",
              "surgery_reference_identifier": "string"
            }
          ],
          "radiopharmaceutical_therapies": [
            {
              "rxnorm_code": "string",
              "agent_name": "string",
              "radionuclide": "Carbon-14",
              "radionuclide_other": "string",
              "start_date": {},
              "end_date": {},
              "cumulative_drug_dose": 0,
              "cumulative_drug_dose_not_available": false,
              "drug_dose_units": "Bq",
              "mass_value": 0,
              "mass_value_not_available": false,
              "mass_unit_ucum": "ug",
              "number_of_cycles": 0,
              "number_of_cycles_not_available": false
            }
          ],
          "followups": [
            {
              "submitter_follow_up_id": "string",
              "date_of_followup": {
                "day_interval": 0,
                "month_interval": 0
              },
              "disease_status_at_followup": "Complete remission",
              "relapse_type": "Distant recurrence/metastasis",
              "date_of_relapse": {
                "day_interval": 0,
                "month_interval": 0
              },
              "method_of_progression_status": [
                "Imaging (procedure)"
              ],
              "anatomic_site_progression_or_recurrence": [
                "string"
              ]
            }
          ]
        }
      ],
      "followups": [
        {
          "submitter_follow_up_id": "string",
          "date_of_followup": {
            "day_interval": 0,
            "month_interval": 0
          },
          "disease_status_at_followup": "Complete remission",
          "relapse_type": "Distant recurrence/metastasis",
          "date_of_relapse": {
            "day_interval": 0,
            "month_interval": 0
          },
          "method_of_progression_status": [
            "Imaging (procedure)"
          ],
          "anatomic_site_progression_or_recurrence": [
            "string"
          ]
        }
      ]
    }
  ],
  "followups": [
    {
      "submitter_follow_up_id": "string",
      "date_of_followup": {
        "day_interval": 0,
        "month_interval": 0
      },
      "disease_status_at_followup": "Complete remission",
      "relapse_type": "Distant recurrence/metastasis",
      "date_of_relapse": {
        "day_interval": 0,
        "month_interval": 0
      },
      "method_of_progression_status": [
        "Imaging (procedure)"
      ],
      "anatomic_site_progression_or_recurrence": [
        "string"
      ]
    }
  ],
  "biomarkers": [
    {
      "submitter_specimen_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string",
      "submitter_follow_up_id": "string",
      "test_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "psa_level": 0,
      "psa_level_not_available": false,
      "ca125": 0,
      "ca125_not_available": false,
      "cea": 0,
      "cea_not_available": false,
      "ca19_9": 0,
      "ca19_9_not_available": false,
      "er_status": "Cannot be determined",
      "er_percent_positive": 0,
      "er_percent_positive_not_available": false,
      "pr_status": "Cannot be determined",
      "pr_percent_positive": 0,
      "pr_percent_positive_not_available": false,
      "her2_ihc_status": "Cannot be determined",
      "her2_ish_status": "Cannot be determined",
      "hpv_ihc_status": "Cannot be determined",
      "hpv_pcr_status": "Cannot be determined",
      "hpv_strain": [
        "HPV16"
      ]
    }
  ],
  "exposures": [
    {
      "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
      "tobacco_type": [
        "Chewing Tobacco"
      ],
      "pack_years_smoked": 0,
      "pack_years_smoked_not_available": false
    }
  ],
  "comorbidities": [
    {
      "prior_malignancy": "Yes",
      "laterality_of_prior_malignancy": "Bilateral",
      "age_at_comorbidity_diagnosis": 0,
      "age_at_comorbidity_diagnosis_not_available": false,
      "comorbidity_type_code": "string",
      "comorbidity_treatment_status": "Yes",
      "comorbidity_treatment": "string"
    }
  ]
}

```

DonorWithClinicalDataSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|string|true|none|none|
|gender|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[GenderEnum](#schemagenderenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sex_at_birth|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SexAtBirthEnum](#schemasexatbirthenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_deceased|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_follow_up|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowUpEnum](#schemalosttofollowupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_followup_reason|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowupReasonEnum](#schemalosttofollowupreasonenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cause_of_death|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CauseOfDeathEnum](#schemacauseofdeathenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_birth|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_death|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_death_is_estimated|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateOfDeathIsEstimatedEnum](#schemadateofdeathisestimatedenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_resolution|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|primary_diagnoses|[[NestedPrimaryDiagnosisSchema](#schemanestedprimarydiagnosisschema)]|false|none|none|
|followups|[[NestedFollowUpSchema](#schemanestedfollowupschema)]|false|none|none|
|biomarkers|[[NestedBiomarkerSchema](#schemanestedbiomarkerschema)]|false|none|none|
|exposures|[[NestedExposureSchema](#schemanestedexposureschema)]|false|none|none|
|comorbidities|[[NestedComorbiditySchema](#schemanestedcomorbidityschema)]|false|none|none|

<h2 id="tocS_NestedBiomarkerSchema">NestedBiomarkerSchema</h2>

<a id="schemanestedbiomarkerschema"></a>
<a id="schema_NestedBiomarkerSchema"></a>
<a id="tocSnestedbiomarkerschema"></a>
<a id="tocsnestedbiomarkerschema"></a>

```json
{
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string",
  "test_date": {
    "day_interval": 0,
    "month_interval": 0
  },
  "psa_level": 0,
  "psa_level_not_available": false,
  "ca125": 0,
  "ca125_not_available": false,
  "cea": 0,
  "cea_not_available": false,
  "ca19_9": 0,
  "ca19_9_not_available": false,
  "er_status": "Cannot be determined",
  "er_percent_positive": 0,
  "er_percent_positive_not_available": false,
  "pr_status": "Cannot be determined",
  "pr_percent_positive": 0,
  "pr_percent_positive_not_available": false,
  "her2_ihc_status": "Cannot be determined",
  "her2_ish_status": "Cannot be determined",
  "hpv_ihc_status": "Cannot be determined",
  "hpv_pcr_status": "Cannot be determined",
  "hpv_strain": [
    "HPV16"
  ]
}

```

NestedBiomarkerSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|test_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|psa_level|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|psa_level_not_available|boolean|false|none|none|
|ca125|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ca125_not_available|boolean|false|none|none|
|cea|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cea_not_available|boolean|false|none|none|
|ca19_9|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ca19_9_not_available|boolean|false|none|none|
|er_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|er_percent_positive|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|er_percent_positive_not_available|boolean|false|none|none|
|pr_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pr_percent_positive|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pr_percent_positive_not_available|boolean|false|none|none|
|her2_ihc_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[Her2StatusEnum](#schemaher2statusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|her2_ish_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[Her2StatusEnum](#schemaher2statusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_ihc_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_pcr_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_strain|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[HpvStrainEnum](#schemahpvstrainenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_NestedComorbiditySchema">NestedComorbiditySchema</h2>

<a id="schemanestedcomorbidityschema"></a>
<a id="schema_NestedComorbiditySchema"></a>
<a id="tocSnestedcomorbidityschema"></a>
<a id="tocsnestedcomorbidityschema"></a>

```json
{
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "age_at_comorbidity_diagnosis": 0,
  "age_at_comorbidity_diagnosis_not_available": false,
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string"
}

```

NestedComorbiditySchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prior_malignancy|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|laterality_of_prior_malignancy|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MalignancyLateralityEnum](#schemamalignancylateralityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|age_at_comorbidity_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|age_at_comorbidity_diagnosis_not_available|boolean|false|none|none|
|comorbidity_type_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_NestedExposureSchema">NestedExposureSchema</h2>

<a id="schemanestedexposureschema"></a>
<a id="schema_NestedExposureSchema"></a>
<a id="tocSnestedexposureschema"></a>
<a id="tocsnestedexposureschema"></a>

```json
{
  "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
  "tobacco_type": [
    "Chewing Tobacco"
  ],
  "pack_years_smoked": 0,
  "pack_years_smoked_not_available": false
}

```

NestedExposureSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tobacco_smoking_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SmokingStatusEnum](#schemasmokingstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tobacco_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[TobaccoTypeEnum](#schematobaccotypeenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pack_years_smoked|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pack_years_smoked_not_available|boolean|false|none|none|

<h2 id="tocS_NestedFollowUpSchema">NestedFollowUpSchema</h2>

<a id="schemanestedfollowupschema"></a>
<a id="schema_NestedFollowUpSchema"></a>
<a id="tocSnestedfollowupschema"></a>
<a id="tocsnestedfollowupschema"></a>

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": {
    "day_interval": 0,
    "month_interval": 0
  },
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": {
    "day_interval": 0,
    "month_interval": 0
  },
  "method_of_progression_status": [
    "Imaging (procedure)"
  ],
  "anatomic_site_progression_or_recurrence": [
    "string"
  ]
}

```

NestedFollowUpSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|string|true|none|none|
|date_of_followup|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|disease_status_at_followup|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DiseaseStatusFollowupEnum](#schemadiseasestatusfollowupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|relapse_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RelapseTypeEnum](#schemarelapsetypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_relapse|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|method_of_progression_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ProgressionStatusMethodEnum](#schemaprogressionstatusmethodenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anatomic_site_progression_or_recurrence|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_NestedPrimaryDiagnosisSchema">NestedPrimaryDiagnosisSchema</h2>

<a id="schemanestedprimarydiagnosisschema"></a>
<a id="schema_NestedPrimaryDiagnosisSchema"></a>
<a id="tocSnestedprimarydiagnosisschema"></a>
<a id="tocsnestedprimarydiagnosisschema"></a>

```json
{
  "submitter_primary_diagnosis_id": "string",
  "primary_site": "Accessory sinuses",
  "date_of_diagnosis": {
    "day_interval": 0,
    "month_interval": 0
  },
  "cancer_type_code": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "laterality": "Bilateral",
  "clinical_tumour_staging_system": "AJCC cancer staging system",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Stage 0",
  "pathological_tumour_staging_system": "AJCC cancer staging system",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Stage 0",
  "specimens": [
    {
      "submitter_specimen_id": "string",
      "submitter_treatment_id": "string",
      "specimen_collection_date": {},
      "specimen_storage": "Cut slide",
      "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
      "tumour_histological_type": "string",
      "specimen_anatomic_location": "string",
      "specimen_laterality": "Left",
      "reference_pathology_confirmed_diagnosis": "Yes",
      "reference_pathology_confirmed_tumour_presence": "Yes",
      "tumour_grading_system": "FNCLCC grading system",
      "tumour_grade": "Low grade",
      "percent_tumour_cells_range": "0-19%",
      "percent_tumour_cells_measurement_method": "Genomics",
      "specimen_tissue_source": "Abdominal fluid",
      "tumour_normal_designation": "Normal",
      "specimen_type": "Cell line - derived from normal",
      "sample_registrations": [
        {
          "submitter_sample_id": "string",
          "sample_type": "Amplified DNA"
        }
      ]
    }
  ],
  "treatments": [
    {
      "submitter_treatment_id": "string",
      "treatment_type": [
        "Bone marrow transplant"
      ],
      "is_primary_treatment": "Yes",
      "treatment_start_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "treatment_end_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "treatment_intent": "Curative",
      "treatment_setting": "Adjuvant",
      "response_to_treatment_criteria_method": "RECIST 1.1",
      "response_to_treatment": "Complete response",
      "status_of_treatment": "Treatment completed as prescribed",
      "systemic_therapies": [
        {
          "systemic_therapy_type": "string",
          "days_per_cycle": 0,
          "days_per_cycle_not_available": false,
          "number_of_cycles": 0,
          "number_of_cycles_not_available": false,
          "start_date": {},
          "end_date": {},
          "drug_reference_database": "RxNorm",
          "drug_name": "string",
          "drug_reference_identifier": "string",
          "drug_dose_units": "mg/m2",
          "prescribed_cumulative_drug_dose": 0,
          "prescribed_cumulative_drug_dose_not_available": false,
          "actual_cumulative_drug_dose": 0,
          "actual_cumulative_drug_dose_not_available": false
        }
      ],
      "radiations": [
        {
          "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
          "radiation_therapy_type": "External",
          "radiation_therapy_fractions": 0,
          "radiation_therapy_fractions_not_available": false,
          "radiation_therapy_dosage": 0,
          "radiation_therapy_dosage_not_available": false,
          "anatomical_site_irradiated": "ABDOMEN_WHOLE",
          "radiation_boost": "Yes",
          "reference_radiation_treatment_id": "string"
        }
      ],
      "surgeries": [
        {
          "surgery_type": "string",
          "surgery_site": "string",
          "surgery_location": "Local recurrence",
          "tumour_length": 0,
          "tumour_length_not_available": false,
          "tumour_width": 0,
          "tumour_width_not_available": false,
          "greatest_dimension_tumour": 0,
          "greatest_dimension_tumour_not_available": false,
          "tumour_focality": "Cannot be assessed",
          "residual_tumour_classification": "Not applicable",
          "margins_status": "Margins clear",
          "lymphovascular_invasion": "Absent",
          "perineural_invasion": "Absent",
          "surgery_reference_database": "SNOMED",
          "surgery_reference_identifier": "string"
        }
      ],
      "radiopharmaceutical_therapies": [
        {
          "rxnorm_code": "string",
          "agent_name": "string",
          "radionuclide": "Carbon-14",
          "radionuclide_other": "string",
          "start_date": {},
          "end_date": {},
          "cumulative_drug_dose": 0,
          "cumulative_drug_dose_not_available": false,
          "drug_dose_units": "Bq",
          "mass_value": 0,
          "mass_value_not_available": false,
          "mass_unit_ucum": "ug",
          "number_of_cycles": 0,
          "number_of_cycles_not_available": false
        }
      ],
      "followups": [
        {
          "submitter_follow_up_id": "string",
          "date_of_followup": {
            "day_interval": 0,
            "month_interval": 0
          },
          "disease_status_at_followup": "Complete remission",
          "relapse_type": "Distant recurrence/metastasis",
          "date_of_relapse": {
            "day_interval": 0,
            "month_interval": 0
          },
          "method_of_progression_status": [
            "Imaging (procedure)"
          ],
          "anatomic_site_progression_or_recurrence": [
            "string"
          ]
        }
      ]
    }
  ],
  "followups": [
    {
      "submitter_follow_up_id": "string",
      "date_of_followup": {
        "day_interval": 0,
        "month_interval": 0
      },
      "disease_status_at_followup": "Complete remission",
      "relapse_type": "Distant recurrence/metastasis",
      "date_of_relapse": {
        "day_interval": 0,
        "month_interval": 0
      },
      "method_of_progression_status": [
        "Imaging (procedure)"
      ],
      "anatomic_site_progression_or_recurrence": [
        "string"
      ]
    }
  ]
}

```

NestedPrimaryDiagnosisSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|string|true|none|none|
|primary_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PrimarySiteEnum](#schemaprimarysiteenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cancer_type_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|basis_of_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BasisOfDiagnosisEnum](#schemabasisofdiagnosisenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|laterality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PrimaryDiagnosisLateralityEnum](#schemaprimarydiagnosislateralityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_tumour_staging_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourStagingSystemEnum](#schematumourstagingsystemenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_t_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_n_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_m_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_stage_group|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_tumour_staging_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourStagingSystemEnum](#schematumourstagingsystemenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_t_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_n_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_m_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_stage_group|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimens|[[NestedSpecimenSchema](#schemanestedspecimenschema)]|false|none|none|
|treatments|[[NestedTreatmentSchema](#schemanestedtreatmentschema)]|false|none|none|
|followups|[[NestedFollowUpSchema](#schemanestedfollowupschema)]|false|none|none|

<h2 id="tocS_NestedRadiationSchema">NestedRadiationSchema</h2>

<a id="schemanestedradiationschema"></a>
<a id="schema_NestedRadiationSchema"></a>
<a id="tocSnestedradiationschema"></a>
<a id="tocsnestedradiationschema"></a>

```json
{
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "radiation_therapy_fractions": 0,
  "radiation_therapy_fractions_not_available": false,
  "radiation_therapy_dosage": 0,
  "radiation_therapy_dosage_not_available": false,
  "anatomical_site_irradiated": "ABDOMEN_WHOLE",
  "radiation_boost": "Yes",
  "reference_radiation_treatment_id": "string"
}

```

NestedRadiationSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_modality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RadiationTherapyModalityEnum](#schemaradiationtherapymodalityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TherapyTypeEnum](#schematherapytypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_fractions|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_fractions_not_available|boolean|false|none|none|
|radiation_therapy_dosage|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_dosage_not_available|boolean|false|none|none|
|anatomical_site_irradiated|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RadiationAnatomicalSiteEnum](#schemaradiationanatomicalsiteenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_boost|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_radiation_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_NestedRadiopharmaceuticalTherapySchema">NestedRadiopharmaceuticalTherapySchema</h2>

<a id="schemanestedradiopharmaceuticaltherapyschema"></a>
<a id="schema_NestedRadiopharmaceuticalTherapySchema"></a>
<a id="tocSnestedradiopharmaceuticaltherapyschema"></a>
<a id="tocsnestedradiopharmaceuticaltherapyschema"></a>

```json
{
  "rxnorm_code": "string",
  "agent_name": "string",
  "radionuclide": "Carbon-14",
  "radionuclide_other": "string",
  "start_date": {},
  "end_date": {},
  "cumulative_drug_dose": 0,
  "cumulative_drug_dose_not_available": false,
  "drug_dose_units": "Bq",
  "mass_value": 0,
  "mass_value_not_available": false,
  "mass_unit_ucum": "ug",
  "number_of_cycles": 0,
  "number_of_cycles_not_available": false
}

```

NestedRadiopharmaceuticalTherapySchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rxnorm_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|agent_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radionuclide|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RadionuclideEnum](#schemaradionuclideenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radionuclide_other|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|start_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|end_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cumulative_drug_dose_not_available|boolean|false|none|none|
|drug_dose_units|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DrugDoseUnitsEnum](#schemadrugdoseunitsenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mass_value|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mass_value_not_available|boolean|false|none|none|
|mass_unit_ucum|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MassUnitUcumEnum](#schemamassunitucumenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles_not_available|boolean|false|none|none|

<h2 id="tocS_NestedSampleRegistrationSchema">NestedSampleRegistrationSchema</h2>

<a id="schemanestedsampleregistrationschema"></a>
<a id="schema_NestedSampleRegistrationSchema"></a>
<a id="tocSnestedsampleregistrationschema"></a>
<a id="tocsnestedsampleregistrationschema"></a>

```json
{
  "submitter_sample_id": "string",
  "sample_type": "Amplified DNA"
}

```

NestedSampleRegistrationSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_sample_id|string|true|none|none|
|sample_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SampleTypeEnum](#schemasampletypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_NestedSpecimenSchema">NestedSpecimenSchema</h2>

<a id="schemanestedspecimenschema"></a>
<a id="schema_NestedSpecimenSchema"></a>
<a id="tocSnestedspecimenschema"></a>
<a id="tocsnestedspecimenschema"></a>

```json
{
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string",
  "specimen_collection_date": {},
  "specimen_storage": "Cut slide",
  "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "specimen_laterality": "Left",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "specimen_tissue_source": "Abdominal fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "sample_registrations": [
    {
      "submitter_sample_id": "string",
      "sample_type": "Amplified DNA"
    }
  ]
}

```

NestedSpecimenSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|string|true|none|none|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_collection_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_storage|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StorageEnum](#schemastorageenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_processing|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenProcessingEnum](#schemaspecimenprocessingenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_histological_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_anatomic_location|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_laterality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenLateralityEnum](#schemaspecimenlateralityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ConfirmedDiagnosisTumourEnum](#schemaconfirmeddiagnosistumourenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_tumour_presence|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ConfirmedDiagnosisTumourEnum](#schemaconfirmeddiagnosistumourenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grading_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradingSystemEnum](#schematumourgradingsystemenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grade|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradeEnum](#schematumourgradeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_range|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PercentCellsRangeEnum](#schemapercentcellsrangeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_measurement_method|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CellsMeasureMethodEnum](#schemacellsmeasuremethodenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_tissue_source|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenTissueSourceEnum](#schemaspecimentissuesourceenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_normal_designation|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourDesginationEnum](#schematumourdesginationenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenTypeEnum](#schemaspecimentypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sample_registrations|[[NestedSampleRegistrationSchema](#schemanestedsampleregistrationschema)]|false|none|none|

<h2 id="tocS_NestedSurgerySchema">NestedSurgerySchema</h2>

<a id="schemanestedsurgeryschema"></a>
<a id="schema_NestedSurgerySchema"></a>
<a id="tocSnestedsurgeryschema"></a>
<a id="tocsnestedsurgeryschema"></a>

```json
{
  "surgery_type": "string",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_length": 0,
  "tumour_length_not_available": false,
  "tumour_width": 0,
  "tumour_width_not_available": false,
  "greatest_dimension_tumour": 0,
  "greatest_dimension_tumour_not_available": false,
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margins_status": "Margins clear",
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "surgery_reference_database": "SNOMED",
  "surgery_reference_identifier": "string"
}

```

NestedSurgerySchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_location|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SurgeryLocationEnum](#schemasurgerylocationenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length_not_available|boolean|false|none|none|
|tumour_width|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_width_not_available|boolean|false|none|none|
|greatest_dimension_tumour|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|greatest_dimension_tumour_not_available|boolean|false|none|none|
|tumour_focality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourFocalityEnum](#schematumourfocalityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|residual_tumour_classification|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourClassificationEnum](#schematumourclassificationenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margins_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginsStatusEnum](#schemamarginsstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lymphovascular_invasion|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LymphovascularInvasionEnum](#schemalymphovascularinvasionenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|perineural_invasion|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PerineuralInvasionEnum](#schemaperineuralinvasionenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_reference_database|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SurgeryReferenceDatabaseEnum](#schemasurgeryreferencedatabaseenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_reference_identifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_NestedSystemicTherapySchema">NestedSystemicTherapySchema</h2>

<a id="schemanestedsystemictherapyschema"></a>
<a id="schema_NestedSystemicTherapySchema"></a>
<a id="tocSnestedsystemictherapyschema"></a>
<a id="tocsnestedsystemictherapyschema"></a>

```json
{
  "systemic_therapy_type": "string",
  "days_per_cycle": 0,
  "days_per_cycle_not_available": false,
  "number_of_cycles": 0,
  "number_of_cycles_not_available": false,
  "start_date": {},
  "end_date": {},
  "drug_reference_database": "RxNorm",
  "drug_name": "string",
  "drug_reference_identifier": "string",
  "drug_dose_units": "mg/m2",
  "prescribed_cumulative_drug_dose": 0,
  "prescribed_cumulative_drug_dose_not_available": false,
  "actual_cumulative_drug_dose": 0,
  "actual_cumulative_drug_dose_not_available": false
}

```

NestedSystemicTherapySchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|systemic_therapy_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|days_per_cycle|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|days_per_cycle_not_available|boolean|false|none|none|
|number_of_cycles|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles_not_available|boolean|false|none|none|
|start_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|end_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_reference_database|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DrugReferenceDbEnum](#schemadrugreferencedbenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_reference_identifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_dose_units|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DosageUnitsEnum](#schemadosageunitsenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prescribed_cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prescribed_cumulative_drug_dose_not_available|boolean|false|none|none|
|actual_cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|actual_cumulative_drug_dose_not_available|boolean|false|none|none|

<h2 id="tocS_NestedTreatmentSchema">NestedTreatmentSchema</h2>

<a id="schemanestedtreatmentschema"></a>
<a id="schema_NestedTreatmentSchema"></a>
<a id="tocSnestedtreatmentschema"></a>
<a id="tocsnestedtreatmentschema"></a>

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Bone marrow transplant"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": {
    "day_interval": 0,
    "month_interval": 0
  },
  "treatment_end_date": {
    "day_interval": 0,
    "month_interval": 0
  },
  "treatment_intent": "Curative",
  "treatment_setting": "Adjuvant",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "status_of_treatment": "Treatment completed as prescribed",
  "systemic_therapies": [
    {
      "systemic_therapy_type": "string",
      "days_per_cycle": 0,
      "days_per_cycle_not_available": false,
      "number_of_cycles": 0,
      "number_of_cycles_not_available": false,
      "start_date": {},
      "end_date": {},
      "drug_reference_database": "RxNorm",
      "drug_name": "string",
      "drug_reference_identifier": "string",
      "drug_dose_units": "mg/m2",
      "prescribed_cumulative_drug_dose": 0,
      "prescribed_cumulative_drug_dose_not_available": false,
      "actual_cumulative_drug_dose": 0,
      "actual_cumulative_drug_dose_not_available": false
    }
  ],
  "radiations": [
    {
      "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
      "radiation_therapy_type": "External",
      "radiation_therapy_fractions": 0,
      "radiation_therapy_fractions_not_available": false,
      "radiation_therapy_dosage": 0,
      "radiation_therapy_dosage_not_available": false,
      "anatomical_site_irradiated": "ABDOMEN_WHOLE",
      "radiation_boost": "Yes",
      "reference_radiation_treatment_id": "string"
    }
  ],
  "surgeries": [
    {
      "surgery_type": "string",
      "surgery_site": "string",
      "surgery_location": "Local recurrence",
      "tumour_length": 0,
      "tumour_length_not_available": false,
      "tumour_width": 0,
      "tumour_width_not_available": false,
      "greatest_dimension_tumour": 0,
      "greatest_dimension_tumour_not_available": false,
      "tumour_focality": "Cannot be assessed",
      "residual_tumour_classification": "Not applicable",
      "margins_status": "Margins clear",
      "lymphovascular_invasion": "Absent",
      "perineural_invasion": "Absent",
      "surgery_reference_database": "SNOMED",
      "surgery_reference_identifier": "string"
    }
  ],
  "radiopharmaceutical_therapies": [
    {
      "rxnorm_code": "string",
      "agent_name": "string",
      "radionuclide": "Carbon-14",
      "radionuclide_other": "string",
      "start_date": {},
      "end_date": {},
      "cumulative_drug_dose": 0,
      "cumulative_drug_dose_not_available": false,
      "drug_dose_units": "Bq",
      "mass_value": 0,
      "mass_value_not_available": false,
      "mass_unit_ucum": "ug",
      "number_of_cycles": 0,
      "number_of_cycles_not_available": false
    }
  ],
  "followups": [
    {
      "submitter_follow_up_id": "string",
      "date_of_followup": {
        "day_interval": 0,
        "month_interval": 0
      },
      "disease_status_at_followup": "Complete remission",
      "relapse_type": "Distant recurrence/metastasis",
      "date_of_relapse": {
        "day_interval": 0,
        "month_interval": 0
      },
      "method_of_progression_status": [
        "Imaging (procedure)"
      ],
      "anatomic_site_progression_or_recurrence": [
        "string"
      ]
    }
  ]
}

```

NestedTreatmentSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|string|true|none|none|
|treatment_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[TreatmentTypeEnum](#schematreatmenttypeenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_primary_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_start_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_end_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_intent|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentIntentEnum](#schematreatmentintentenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_setting|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentSettingEnum](#schematreatmentsettingenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|response_to_treatment_criteria_method|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentResponseMethodEnum](#schematreatmentresponsemethodenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|response_to_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentResponseEnum](#schematreatmentresponseenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status_of_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentStatusEnum](#schematreatmentstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|systemic_therapies|[[NestedSystemicTherapySchema](#schemanestedsystemictherapyschema)]|false|none|none|
|radiations|[[NestedRadiationSchema](#schemanestedradiationschema)]|false|none|none|
|surgeries|[[NestedSurgerySchema](#schemanestedsurgeryschema)]|false|none|none|
|radiopharmaceutical_therapies|[[NestedRadiopharmaceuticalTherapySchema](#schemanestedradiopharmaceuticaltherapyschema)]|false|none|none|
|followups|[[NestedFollowUpSchema](#schemanestedfollowupschema)]|false|none|none|

<h2 id="tocS_Input">Input</h2>

<a id="schemainput"></a>
<a id="schema_Input"></a>
<a id="tocSinput"></a>
<a id="tocsinput"></a>

```json
{
  "page": 1,
  "page_size": 1
}

```

Input

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|page|integer|false|none|none|
|page_size|integer|false|none|none|

<h2 id="tocS_ProgramFilterSchema">ProgramFilterSchema</h2>

<a id="schemaprogramfilterschema"></a>
<a id="schema_ProgramFilterSchema"></a>
<a id="tocSprogramfilterschema"></a>
<a id="tocsprogramfilterschema"></a>

```json
{
  "program_id": "string"
}

```

ProgramFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedProgramModelSchema">PagedProgramModelSchema</h2>

<a id="schemapagedprogrammodelschema"></a>
<a id="schema_PagedProgramModelSchema"></a>
<a id="tocSpagedprogrammodelschema"></a>
<a id="tocspagedprogrammodelschema"></a>

```json
{
  "items": [
    {
      "program_id": "string",
      "metadata": {},
      "program_description": "string",
      "program_name": "string",
      "keywords": [
        null
      ],
      "status": "Ongoing",
      "context": "Clinical",
      "participant_criteria": "string",
      "principal_investigators": [
        null
      ],
      "lead_organizations": [
        null
      ],
      "collaborators": [
        null
      ],
      "funding_sources": [
        null
      ],
      "publication_links": [
        null
      ],
      "program_url": "string",
      "pancan_cohort": "Yes",
      "pancan_id": "string",
      "created": "2019-08-24T14:15:22Z",
      "updated": "2019-08-24T14:15:22Z"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedProgramModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[ProgramModelSchema](#schemaprogrammodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ProgramModelSchema">ProgramModelSchema</h2>

<a id="schemaprogrammodelschema"></a>
<a id="schema_ProgramModelSchema"></a>
<a id="tocSprogrammodelschema"></a>
<a id="tocsprogrammodelschema"></a>

```json
{
  "program_id": "string",
  "metadata": {},
  "program_description": "string",
  "program_name": "string",
  "keywords": [
    null
  ],
  "status": "Ongoing",
  "context": "Clinical",
  "participant_criteria": "string",
  "principal_investigators": [
    null
  ],
  "lead_organizations": [
    null
  ],
  "collaborators": [
    null
  ],
  "funding_sources": [
    null
  ],
  "publication_links": [
    null
  ],
  "program_url": "string",
  "pancan_cohort": "Yes",
  "pancan_id": "string",
  "created": "2019-08-24T14:15:22Z",
  "updated": "2019-08-24T14:15:22Z"
}

```

ProgramModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|metadata|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|keywords|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StatusEnum](#schemastatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|context|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ContextEnum](#schemacontextenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|participant_criteria|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|principal_investigators|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lead_organizations|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|collaborators|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|funding_sources|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publication_links|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_url|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pancan_cohort|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PancanCohortEnum](#schemapancancohortenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pancan_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|created|string(date-time)|false|none|none|
|updated|string(date-time)|false|none|none|

<h2 id="tocS_DonorFilterSchema">DonorFilterSchema</h2>

<a id="schemadonorfilterschema"></a>
<a id="schema_DonorFilterSchema"></a>
<a id="tocSdonorfilterschema"></a>
<a id="tocsdonorfilterschema"></a>

```json
{
  "submitter_donor_id": "string",
  "program_id": "string",
  "gender": "string",
  "sex_at_birth": "string",
  "is_deceased": "string",
  "lost_to_follow_up": "string",
  "lost_to_followup_reason": "string",
  "cause_of_death": "string",
  "date_of_death_is_estimated": "string"
}

```

DonorFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|gender|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sex_at_birth|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_deceased|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_follow_up|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_followup_reason|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cause_of_death|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_death_is_estimated|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DonorModelSchema">DonorModelSchema</h2>

<a id="schemadonormodelschema"></a>
<a id="schema_DonorModelSchema"></a>
<a id="tocSdonormodelschema"></a>
<a id="tocsdonormodelschema"></a>

```json
{
  "submitter_donor_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "is_deceased": "Yes",
  "lost_to_follow_up": "Yes",
  "lost_to_followup_reason": "Completed study",
  "cause_of_death": "Died of cancer",
  "date_of_birth": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death_is_estimated": "Yes",
  "date_resolution": "string",
  "program_id": "string"
}

```

DonorModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|string|true|none|none|
|gender|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[GenderEnum](#schemagenderenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sex_at_birth|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SexAtBirthEnum](#schemasexatbirthenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_deceased|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_follow_up|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowUpEnum](#schemalosttofollowupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_followup_reason|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowupReasonEnum](#schemalosttofollowupreasonenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cause_of_death|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CauseOfDeathEnum](#schemacauseofdeathenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_birth|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_death|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_death_is_estimated|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateOfDeathIsEstimatedEnum](#schemadateofdeathisestimatedenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_resolution|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|

<h2 id="tocS_PagedDonorModelSchema">PagedDonorModelSchema</h2>

<a id="schemapageddonormodelschema"></a>
<a id="schema_PagedDonorModelSchema"></a>
<a id="tocSpageddonormodelschema"></a>
<a id="tocspageddonormodelschema"></a>

```json
{
  "items": [
    {
      "submitter_donor_id": "string",
      "gender": "Man",
      "sex_at_birth": "Male",
      "is_deceased": "Yes",
      "lost_to_follow_up": "Yes",
      "lost_to_followup_reason": "Completed study",
      "cause_of_death": "Died of cancer",
      "date_of_birth": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death_is_estimated": "Yes",
      "date_resolution": "string",
      "program_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedDonorModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[DonorModelSchema](#schemadonormodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DonorExplorerFilterSchema">DonorExplorerFilterSchema</h2>

<a id="schemadonorexplorerfilterschema"></a>
<a id="schema_DonorExplorerFilterSchema"></a>
<a id="tocSdonorexplorerfilterschema"></a>
<a id="tocsdonorexplorerfilterschema"></a>

```json
{
  "treatment_type": [
    "string"
  ],
  "primary_site": [
    "string"
  ],
  "systemic_therapy_drug_name": [
    "string"
  ],
  "exclude_programs": [
    "string"
  ]
}

```

DonorExplorerFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_type|[string]|false|none|none|
|primary_site|[string]|false|none|none|
|systemic_therapy_drug_name|[string]|false|none|none|
|exclude_programs|[string]|false|none|none|

<h2 id="tocS_PagedQueryDonorSchema">PagedQueryDonorSchema</h2>

<a id="schemapagedquerydonorschema"></a>
<a id="schema_PagedQueryDonorSchema"></a>
<a id="tocSpagedquerydonorschema"></a>
<a id="tocspagedquerydonorschema"></a>

```json
{
  "items": [
    {
      "submitter_donor_id": "string",
      "gender": "Man",
      "sex_at_birth": "Male",
      "is_deceased": "Yes",
      "lost_to_follow_up": "Yes",
      "lost_to_followup_reason": "Completed study",
      "cause_of_death": "Died of cancer",
      "date_of_birth": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death_is_estimated": "Yes",
      "date_resolution": "string",
      "program_id": "string",
      "primary_site": [
        "string"
      ],
      "treatment_type": [
        "string"
      ],
      "submitter_sample_ids": [
        "string"
      ]
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedQueryDonorSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[QueryDonorSchema](#schemaquerydonorschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_QueryDonorSchema">QueryDonorSchema</h2>

<a id="schemaquerydonorschema"></a>
<a id="schema_QueryDonorSchema"></a>
<a id="tocSquerydonorschema"></a>
<a id="tocsquerydonorschema"></a>

```json
{
  "submitter_donor_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "is_deceased": "Yes",
  "lost_to_follow_up": "Yes",
  "lost_to_followup_reason": "Completed study",
  "cause_of_death": "Died of cancer",
  "date_of_birth": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death": {
    "day_interval": 0,
    "month_interval": 0
  },
  "date_of_death_is_estimated": "Yes",
  "date_resolution": "string",
  "program_id": "string",
  "primary_site": [
    "string"
  ],
  "treatment_type": [
    "string"
  ],
  "submitter_sample_ids": [
    "string"
  ]
}

```

QueryDonorSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|string|true|none|none|
|gender|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[GenderEnum](#schemagenderenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sex_at_birth|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SexAtBirthEnum](#schemasexatbirthenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_deceased|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_follow_up|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowUpEnum](#schemalosttofollowupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_followup_reason|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowupReasonEnum](#schemalosttofollowupreasonenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cause_of_death|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CauseOfDeathEnum](#schemacauseofdeathenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_birth|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_death|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_death_is_estimated|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateOfDeathIsEstimatedEnum](#schemadateofdeathisestimatedenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_resolution|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|primary_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_sample_ids|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PrimaryDiagnosisFilterSchema">PrimaryDiagnosisFilterSchema</h2>

<a id="schemaprimarydiagnosisfilterschema"></a>
<a id="schema_PrimaryDiagnosisFilterSchema"></a>
<a id="tocSprimarydiagnosisfilterschema"></a>
<a id="tocsprimarydiagnosisfilterschema"></a>

```json
{
  "submitter_primary_diagnosis_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "cancer_type_code": "string",
  "basis_of_diagnosis": "string",
  "laterality": "string",
  "clinical_tumour_staging_system": "string",
  "clinical_t_category": "string",
  "clinical_n_category": "string",
  "clinical_m_category": "string",
  "clinical_stage_group": "string",
  "primary_site": "string",
  "pathological_tumour_staging_system": "string",
  "pathological_t_category": "string",
  "pathological_n_category": "string",
  "pathological_m_category": "string",
  "pathological_stage_group": "string"
}

```

PrimaryDiagnosisFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cancer_type_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|basis_of_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|laterality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_tumour_staging_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_t_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_n_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_m_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_stage_group|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_tumour_staging_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_t_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_n_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_m_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_stage_group|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedPrimaryDiagnosisModelSchema">PagedPrimaryDiagnosisModelSchema</h2>

<a id="schemapagedprimarydiagnosismodelschema"></a>
<a id="schema_PagedPrimaryDiagnosisModelSchema"></a>
<a id="tocSpagedprimarydiagnosismodelschema"></a>
<a id="tocspagedprimarydiagnosismodelschema"></a>

```json
{
  "items": [
    {
      "submitter_primary_diagnosis_id": "string",
      "primary_site": "Accessory sinuses",
      "date_of_diagnosis": {
        "day_interval": 0,
        "month_interval": 0
      },
      "cancer_type_code": "string",
      "basis_of_diagnosis": "Clinical investigation",
      "laterality": "Bilateral",
      "clinical_tumour_staging_system": "AJCC cancer staging system",
      "clinical_t_category": "T0",
      "clinical_n_category": "N0",
      "clinical_m_category": "M0",
      "clinical_stage_group": "Stage 0",
      "pathological_tumour_staging_system": "AJCC cancer staging system",
      "pathological_t_category": "T0",
      "pathological_n_category": "N0",
      "pathological_m_category": "M0",
      "pathological_stage_group": "Stage 0",
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedPrimaryDiagnosisModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[PrimaryDiagnosisModelSchema](#schemaprimarydiagnosismodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PrimaryDiagnosisModelSchema">PrimaryDiagnosisModelSchema</h2>

<a id="schemaprimarydiagnosismodelschema"></a>
<a id="schema_PrimaryDiagnosisModelSchema"></a>
<a id="tocSprimarydiagnosismodelschema"></a>
<a id="tocsprimarydiagnosismodelschema"></a>

```json
{
  "submitter_primary_diagnosis_id": "string",
  "primary_site": "Accessory sinuses",
  "date_of_diagnosis": {
    "day_interval": 0,
    "month_interval": 0
  },
  "cancer_type_code": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "laterality": "Bilateral",
  "clinical_tumour_staging_system": "AJCC cancer staging system",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Stage 0",
  "pathological_tumour_staging_system": "AJCC cancer staging system",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Stage 0",
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

PrimaryDiagnosisModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|string|true|none|none|
|primary_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PrimarySiteEnum](#schemaprimarysiteenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cancer_type_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|basis_of_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BasisOfDiagnosisEnum](#schemabasisofdiagnosisenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|laterality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PrimaryDiagnosisLateralityEnum](#schemaprimarydiagnosislateralityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_tumour_staging_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourStagingSystemEnum](#schematumourstagingsystemenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_t_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_n_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_m_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_stage_group|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_tumour_staging_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourStagingSystemEnum](#schematumourstagingsystemenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_t_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_n_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_m_category|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_stage_group|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|

<h2 id="tocS_BiomarkerFilterSchema">BiomarkerFilterSchema</h2>

<a id="schemabiomarkerfilterschema"></a>
<a id="schema_BiomarkerFilterSchema"></a>
<a id="tocSbiomarkerfilterschema"></a>
<a id="tocsbiomarkerfilterschema"></a>

```json
{
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string",
  "psa_level": 0,
  "ca125": 0,
  "cea": 0,
  "ca19_9": 0,
  "er_status": "string",
  "er_percent_positive": 0,
  "pr_status": "string",
  "pr_percent_positive": 0,
  "her2_ihc_status": "string",
  "her2_ish_status": "string",
  "hpv_ihc_status": "string",
  "hpv_pcr_status": "string",
  "hpv_strain": [
    "string"
  ]
}

```

BiomarkerFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|psa_level|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ca125|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cea|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ca19_9|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|er_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|er_percent_positive|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pr_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pr_percent_positive|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|her2_ihc_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|her2_ish_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_ihc_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_pcr_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_strain|[string]|false|none|none|

<h2 id="tocS_BiomarkerModelSchema">BiomarkerModelSchema</h2>

<a id="schemabiomarkermodelschema"></a>
<a id="schema_BiomarkerModelSchema"></a>
<a id="tocSbiomarkermodelschema"></a>
<a id="tocsbiomarkermodelschema"></a>

```json
{
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string",
  "test_date": {
    "day_interval": 0,
    "month_interval": 0
  },
  "psa_level": 0,
  "psa_level_not_available": false,
  "ca125": 0,
  "ca125_not_available": false,
  "cea": 0,
  "cea_not_available": false,
  "ca19_9": 0,
  "ca19_9_not_available": false,
  "er_status": "Cannot be determined",
  "er_percent_positive": 0,
  "er_percent_positive_not_available": false,
  "pr_status": "Cannot be determined",
  "pr_percent_positive": 0,
  "pr_percent_positive_not_available": false,
  "her2_ihc_status": "Cannot be determined",
  "her2_ish_status": "Cannot be determined",
  "hpv_ihc_status": "Cannot be determined",
  "hpv_pcr_status": "Cannot be determined",
  "hpv_strain": [
    "HPV16"
  ],
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

BiomarkerModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|test_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|psa_level|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|psa_level_not_available|boolean|false|none|none|
|ca125|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ca125_not_available|boolean|false|none|none|
|cea|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cea_not_available|boolean|false|none|none|
|ca19_9|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ca19_9_not_available|boolean|false|none|none|
|er_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|er_percent_positive|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|er_percent_positive_not_available|boolean|false|none|none|
|pr_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pr_percent_positive|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pr_percent_positive_not_available|boolean|false|none|none|
|her2_ihc_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[Her2StatusEnum](#schemaher2statusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|her2_ish_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[Her2StatusEnum](#schemaher2statusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_ihc_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_pcr_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErPrHpvStatusEnum](#schemaerprhpvstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hpv_strain|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[HpvStrainEnum](#schemahpvstrainenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|

<h2 id="tocS_PagedBiomarkerModelSchema">PagedBiomarkerModelSchema</h2>

<a id="schemapagedbiomarkermodelschema"></a>
<a id="schema_PagedBiomarkerModelSchema"></a>
<a id="tocSpagedbiomarkermodelschema"></a>
<a id="tocspagedbiomarkermodelschema"></a>

```json
{
  "items": [
    {
      "submitter_specimen_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string",
      "submitter_follow_up_id": "string",
      "test_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "psa_level": 0,
      "psa_level_not_available": false,
      "ca125": 0,
      "ca125_not_available": false,
      "cea": 0,
      "cea_not_available": false,
      "ca19_9": 0,
      "ca19_9_not_available": false,
      "er_status": "Cannot be determined",
      "er_percent_positive": 0,
      "er_percent_positive_not_available": false,
      "pr_status": "Cannot be determined",
      "pr_percent_positive": 0,
      "pr_percent_positive_not_available": false,
      "her2_ihc_status": "Cannot be determined",
      "her2_ish_status": "Cannot be determined",
      "hpv_ihc_status": "Cannot be determined",
      "hpv_pcr_status": "Cannot be determined",
      "hpv_strain": [
        "HPV16"
      ],
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedBiomarkerModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[BiomarkerModelSchema](#schemabiomarkermodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SystemicTherapyFilterSchema">SystemicTherapyFilterSchema</h2>

<a id="schemasystemictherapyfilterschema"></a>
<a id="schema_SystemicTherapyFilterSchema"></a>
<a id="tocSsystemictherapyfilterschema"></a>
<a id="tocssystemictherapyfilterschema"></a>

```json
{
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string",
  "drug_reference_database": "string",
  "drug_name": "string",
  "drug_reference_identifier": "string",
  "drug_dose_units": "string",
  "prescribed_cumulative_drug_dose": 0,
  "actual_cumulative_drug_dose": 0,
  "days_per_cycle": 0,
  "number_of_cycles": 0,
  "systemic_therapy_type": "string"
}

```

SystemicTherapyFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_reference_database|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_reference_identifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_dose_units|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prescribed_cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|actual_cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|days_per_cycle|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|systemic_therapy_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedSystemicTherapyModelSchema">PagedSystemicTherapyModelSchema</h2>

<a id="schemapagedsystemictherapymodelschema"></a>
<a id="schema_PagedSystemicTherapyModelSchema"></a>
<a id="tocSpagedsystemictherapymodelschema"></a>
<a id="tocspagedsystemictherapymodelschema"></a>

```json
{
  "items": [
    {
      "systemic_therapy_type": "string",
      "days_per_cycle": 0,
      "days_per_cycle_not_available": false,
      "number_of_cycles": 0,
      "number_of_cycles_not_available": false,
      "start_date": {},
      "end_date": {},
      "drug_reference_database": "RxNorm",
      "drug_name": "string",
      "drug_reference_identifier": "string",
      "drug_dose_units": "mg/m2",
      "prescribed_cumulative_drug_dose": 0,
      "prescribed_cumulative_drug_dose_not_available": false,
      "actual_cumulative_drug_dose": 0,
      "actual_cumulative_drug_dose_not_available": false,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedSystemicTherapyModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[SystemicTherapyModelSchema](#schemasystemictherapymodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SystemicTherapyModelSchema">SystemicTherapyModelSchema</h2>

<a id="schemasystemictherapymodelschema"></a>
<a id="schema_SystemicTherapyModelSchema"></a>
<a id="tocSsystemictherapymodelschema"></a>
<a id="tocssystemictherapymodelschema"></a>

```json
{
  "systemic_therapy_type": "string",
  "days_per_cycle": 0,
  "days_per_cycle_not_available": false,
  "number_of_cycles": 0,
  "number_of_cycles_not_available": false,
  "start_date": {},
  "end_date": {},
  "drug_reference_database": "RxNorm",
  "drug_name": "string",
  "drug_reference_identifier": "string",
  "drug_dose_units": "mg/m2",
  "prescribed_cumulative_drug_dose": 0,
  "prescribed_cumulative_drug_dose_not_available": false,
  "actual_cumulative_drug_dose": 0,
  "actual_cumulative_drug_dose_not_available": false,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

SystemicTherapyModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|systemic_therapy_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|days_per_cycle|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|days_per_cycle_not_available|boolean|false|none|none|
|number_of_cycles|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles_not_available|boolean|false|none|none|
|start_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|end_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_reference_database|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DrugReferenceDbEnum](#schemadrugreferencedbenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_reference_identifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_dose_units|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DosageUnitsEnum](#schemadosageunitsenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prescribed_cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prescribed_cumulative_drug_dose_not_available|boolean|false|none|none|
|actual_cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|actual_cumulative_drug_dose_not_available|boolean|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_ComorbidityFilterSchema">ComorbidityFilterSchema</h2>

<a id="schemacomorbidityfilterschema"></a>
<a id="schema_ComorbidityFilterSchema"></a>
<a id="tocScomorbidityfilterschema"></a>
<a id="tocscomorbidityfilterschema"></a>

```json
{
  "program_id": "string",
  "submitter_donor_id": "string",
  "prior_malignancy": "string",
  "laterality_of_prior_malignancy": "string",
  "age_at_comorbidity_diagnosis": 0,
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "string",
  "comorbidity_treatment": "string"
}

```

ComorbidityFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prior_malignancy|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|laterality_of_prior_malignancy|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|age_at_comorbidity_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_type_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ComorbidityModelSchema">ComorbidityModelSchema</h2>

<a id="schemacomorbiditymodelschema"></a>
<a id="schema_ComorbidityModelSchema"></a>
<a id="tocScomorbiditymodelschema"></a>
<a id="tocscomorbiditymodelschema"></a>

```json
{
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "age_at_comorbidity_diagnosis": 0,
  "age_at_comorbidity_diagnosis_not_available": false,
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string",
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

ComorbidityModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prior_malignancy|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|laterality_of_prior_malignancy|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MalignancyLateralityEnum](#schemamalignancylateralityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|age_at_comorbidity_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|age_at_comorbidity_diagnosis_not_available|boolean|false|none|none|
|comorbidity_type_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|

<h2 id="tocS_PagedComorbidityModelSchema">PagedComorbidityModelSchema</h2>

<a id="schemapagedcomorbiditymodelschema"></a>
<a id="schema_PagedComorbidityModelSchema"></a>
<a id="tocSpagedcomorbiditymodelschema"></a>
<a id="tocspagedcomorbiditymodelschema"></a>

```json
{
  "items": [
    {
      "prior_malignancy": "Yes",
      "laterality_of_prior_malignancy": "Bilateral",
      "age_at_comorbidity_diagnosis": 0,
      "age_at_comorbidity_diagnosis_not_available": false,
      "comorbidity_type_code": "string",
      "comorbidity_treatment_status": "Yes",
      "comorbidity_treatment": "string",
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedComorbidityModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[ComorbidityModelSchema](#schemacomorbiditymodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ExposureFilterSchema">ExposureFilterSchema</h2>

<a id="schemaexposurefilterschema"></a>
<a id="schema_ExposureFilterSchema"></a>
<a id="tocSexposurefilterschema"></a>
<a id="tocsexposurefilterschema"></a>

```json
{
  "program_id": "string",
  "submitter_donor_id": "string",
  "tobacco_smoking_status": "string",
  "tobacco_type": [
    "string"
  ],
  "pack_years_smoked": 0
}

```

ExposureFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tobacco_smoking_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tobacco_type|[string]|false|none|none|
|pack_years_smoked|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ExposureModelSchema">ExposureModelSchema</h2>

<a id="schemaexposuremodelschema"></a>
<a id="schema_ExposureModelSchema"></a>
<a id="tocSexposuremodelschema"></a>
<a id="tocsexposuremodelschema"></a>

```json
{
  "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
  "tobacco_type": [
    "Chewing Tobacco"
  ],
  "pack_years_smoked": 0,
  "pack_years_smoked_not_available": false,
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

ExposureModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tobacco_smoking_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SmokingStatusEnum](#schemasmokingstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tobacco_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[TobaccoTypeEnum](#schematobaccotypeenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pack_years_smoked|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pack_years_smoked_not_available|boolean|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|

<h2 id="tocS_PagedExposureModelSchema">PagedExposureModelSchema</h2>

<a id="schemapagedexposuremodelschema"></a>
<a id="schema_PagedExposureModelSchema"></a>
<a id="tocSpagedexposuremodelschema"></a>
<a id="tocspagedexposuremodelschema"></a>

```json
{
  "items": [
    {
      "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
      "tobacco_type": [
        "Chewing Tobacco"
      ],
      "pack_years_smoked": 0,
      "pack_years_smoked_not_available": false,
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedExposureModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[ExposureModelSchema](#schemaexposuremodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_FollowUpFilterSchema">FollowUpFilterSchema</h2>

<a id="schemafollowupfilterschema"></a>
<a id="schema_FollowUpFilterSchema"></a>
<a id="tocSfollowupfilterschema"></a>
<a id="tocsfollowupfilterschema"></a>

```json
{
  "submitter_follow_up_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "disease_status_at_followup": "string",
  "relapse_type": "string",
  "method_of_progression_status": [
    "string"
  ],
  "anatomic_site_progression_or_recurrence": [
    "string"
  ]
}

```

FollowUpFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|disease_status_at_followup|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|relapse_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|method_of_progression_status|[string]|false|none|none|
|anatomic_site_progression_or_recurrence|[string]|false|none|none|

<h2 id="tocS_FollowUpModelSchema">FollowUpModelSchema</h2>

<a id="schemafollowupmodelschema"></a>
<a id="schema_FollowUpModelSchema"></a>
<a id="tocSfollowupmodelschema"></a>
<a id="tocsfollowupmodelschema"></a>

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": {
    "day_interval": 0,
    "month_interval": 0
  },
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": {
    "day_interval": 0,
    "month_interval": 0
  },
  "method_of_progression_status": [
    "Imaging (procedure)"
  ],
  "anatomic_site_progression_or_recurrence": [
    "string"
  ],
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string"
}

```

FollowUpModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|string|true|none|none|
|date_of_followup|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|disease_status_at_followup|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DiseaseStatusFollowupEnum](#schemadiseasestatusfollowupenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|relapse_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RelapseTypeEnum](#schemarelapsetypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_relapse|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|method_of_progression_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ProgressionStatusMethodEnum](#schemaprogressionstatusmethodenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anatomic_site_progression_or_recurrence|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedFollowUpModelSchema">PagedFollowUpModelSchema</h2>

<a id="schemapagedfollowupmodelschema"></a>
<a id="schema_PagedFollowUpModelSchema"></a>
<a id="tocSpagedfollowupmodelschema"></a>
<a id="tocspagedfollowupmodelschema"></a>

```json
{
  "items": [
    {
      "submitter_follow_up_id": "string",
      "date_of_followup": {
        "day_interval": 0,
        "month_interval": 0
      },
      "disease_status_at_followup": "Complete remission",
      "relapse_type": "Distant recurrence/metastasis",
      "date_of_relapse": {
        "day_interval": 0,
        "month_interval": 0
      },
      "method_of_progression_status": [
        "Imaging (procedure)"
      ],
      "anatomic_site_progression_or_recurrence": [
        "string"
      ],
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedFollowUpModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[FollowUpModelSchema](#schemafollowupmodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_RadiationFilterSchema">RadiationFilterSchema</h2>

<a id="schemaradiationfilterschema"></a>
<a id="schema_RadiationFilterSchema"></a>
<a id="tocSradiationfilterschema"></a>
<a id="tocsradiationfilterschema"></a>

```json
{
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string",
  "radiation_therapy_modality": "string",
  "radiation_therapy_type": "string",
  "radiation_therapy_fractions": 0,
  "radiation_therapy_dosage": 0,
  "anatomical_site_irradiated": "string",
  "radiation_boost": "string",
  "reference_radiation_treatment_id": "string"
}

```

RadiationFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_modality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_fractions|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_dosage|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anatomical_site_irradiated|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_boost|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_radiation_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedRadiationModelSchema">PagedRadiationModelSchema</h2>

<a id="schemapagedradiationmodelschema"></a>
<a id="schema_PagedRadiationModelSchema"></a>
<a id="tocSpagedradiationmodelschema"></a>
<a id="tocspagedradiationmodelschema"></a>

```json
{
  "items": [
    {
      "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
      "radiation_therapy_type": "External",
      "radiation_therapy_fractions": 0,
      "radiation_therapy_fractions_not_available": false,
      "radiation_therapy_dosage": 0,
      "radiation_therapy_dosage_not_available": false,
      "anatomical_site_irradiated": "ABDOMEN_WHOLE",
      "radiation_boost": "Yes",
      "reference_radiation_treatment_id": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedRadiationModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[RadiationModelSchema](#schemaradiationmodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_RadiationModelSchema">RadiationModelSchema</h2>

<a id="schemaradiationmodelschema"></a>
<a id="schema_RadiationModelSchema"></a>
<a id="tocSradiationmodelschema"></a>
<a id="tocsradiationmodelschema"></a>

```json
{
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "radiation_therapy_fractions": 0,
  "radiation_therapy_fractions_not_available": false,
  "radiation_therapy_dosage": 0,
  "radiation_therapy_dosage_not_available": false,
  "anatomical_site_irradiated": "ABDOMEN_WHOLE",
  "radiation_boost": "Yes",
  "reference_radiation_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

RadiationModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_modality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RadiationTherapyModalityEnum](#schemaradiationtherapymodalityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TherapyTypeEnum](#schematherapytypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_fractions|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_fractions_not_available|boolean|false|none|none|
|radiation_therapy_dosage|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_dosage_not_available|boolean|false|none|none|
|anatomical_site_irradiated|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RadiationAnatomicalSiteEnum](#schemaradiationanatomicalsiteenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_boost|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_radiation_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_RadiopharmaceuticalTherapyFilterSchema">RadiopharmaceuticalTherapyFilterSchema</h2>

<a id="schemaradiopharmaceuticaltherapyfilterschema"></a>
<a id="schema_RadiopharmaceuticalTherapyFilterSchema"></a>
<a id="tocSradiopharmaceuticaltherapyfilterschema"></a>
<a id="tocsradiopharmaceuticaltherapyfilterschema"></a>

```json
{
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string",
  "rxnorm_code": "string",
  "agent_name": "string",
  "radionuclide": "string",
  "radionuclide_other": "string",
  "cumulative_drug_dose": 0,
  "drug_dose_units": "string",
  "mass_value": 0,
  "mass_unit_ucum": "string",
  "number_of_cycles": 0
}

```

RadiopharmaceuticalTherapyFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rxnorm_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|agent_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radionuclide|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radionuclide_other|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|drug_dose_units|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mass_value|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mass_unit_ucum|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedRadiopharmaceuticalTherapyModelSchema">PagedRadiopharmaceuticalTherapyModelSchema</h2>

<a id="schemapagedradiopharmaceuticaltherapymodelschema"></a>
<a id="schema_PagedRadiopharmaceuticalTherapyModelSchema"></a>
<a id="tocSpagedradiopharmaceuticaltherapymodelschema"></a>
<a id="tocspagedradiopharmaceuticaltherapymodelschema"></a>

```json
{
  "items": [
    {
      "rxnorm_code": "string",
      "agent_name": "string",
      "radionuclide": "Carbon-14",
      "radionuclide_other": "string",
      "start_date": {},
      "end_date": {},
      "cumulative_drug_dose": 0,
      "cumulative_drug_dose_not_available": false,
      "drug_dose_units": "Bq",
      "mass_value": 0,
      "mass_value_not_available": false,
      "mass_unit_ucum": "ug",
      "number_of_cycles": 0,
      "number_of_cycles_not_available": false,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedRadiopharmaceuticalTherapyModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[RadiopharmaceuticalTherapyModelSchema](#schemaradiopharmaceuticaltherapymodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_RadiopharmaceuticalTherapyModelSchema">RadiopharmaceuticalTherapyModelSchema</h2>

<a id="schemaradiopharmaceuticaltherapymodelschema"></a>
<a id="schema_RadiopharmaceuticalTherapyModelSchema"></a>
<a id="tocSradiopharmaceuticaltherapymodelschema"></a>
<a id="tocsradiopharmaceuticaltherapymodelschema"></a>

```json
{
  "rxnorm_code": "string",
  "agent_name": "string",
  "radionuclide": "Carbon-14",
  "radionuclide_other": "string",
  "start_date": {},
  "end_date": {},
  "cumulative_drug_dose": 0,
  "cumulative_drug_dose_not_available": false,
  "drug_dose_units": "Bq",
  "mass_value": 0,
  "mass_value_not_available": false,
  "mass_unit_ucum": "ug",
  "number_of_cycles": 0,
  "number_of_cycles_not_available": false,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

RadiopharmaceuticalTherapyModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rxnorm_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|agent_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radionuclide|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RadionuclideEnum](#schemaradionuclideenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radionuclide_other|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|start_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|end_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cumulative_drug_dose|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cumulative_drug_dose_not_available|boolean|false|none|none|
|drug_dose_units|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DrugDoseUnitsEnum](#schemadrugdoseunitsenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mass_value|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mass_value_not_available|boolean|false|none|none|
|mass_unit_ucum|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MassUnitUcumEnum](#schemamassunitucumenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number_of_cycles_not_available|boolean|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_SampleRegistrationFilterSchema">SampleRegistrationFilterSchema</h2>

<a id="schemasampleregistrationfilterschema"></a>
<a id="schema_SampleRegistrationFilterSchema"></a>
<a id="tocSsampleregistrationfilterschema"></a>
<a id="tocssampleregistrationfilterschema"></a>

```json
{
  "submitter_sample_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "sample_type": "string"
}

```

SampleRegistrationFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_sample_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sample_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedSampleRegistrationModelSchema">PagedSampleRegistrationModelSchema</h2>

<a id="schemapagedsampleregistrationmodelschema"></a>
<a id="schema_PagedSampleRegistrationModelSchema"></a>
<a id="tocSpagedsampleregistrationmodelschema"></a>
<a id="tocspagedsampleregistrationmodelschema"></a>

```json
{
  "items": [
    {
      "submitter_sample_id": "string",
      "sample_type": "Amplified DNA",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_specimen_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedSampleRegistrationModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[SampleRegistrationModelSchema](#schemasampleregistrationmodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SampleRegistrationModelSchema">SampleRegistrationModelSchema</h2>

<a id="schemasampleregistrationmodelschema"></a>
<a id="schema_SampleRegistrationModelSchema"></a>
<a id="tocSsampleregistrationmodelschema"></a>
<a id="tocssampleregistrationmodelschema"></a>

```json
{
  "submitter_sample_id": "string",
  "sample_type": "Amplified DNA",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string"
}

```

SampleRegistrationModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_sample_id|string|true|none|none|
|sample_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SampleTypeEnum](#schemasampletypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_specimen_id|string|true|none|none|

<h2 id="tocS_SpecimenFilterSchema">SpecimenFilterSchema</h2>

<a id="schemaspecimenfilterschema"></a>
<a id="schema_SpecimenFilterSchema"></a>
<a id="tocSspecimenfilterschema"></a>
<a id="tocsspecimenfilterschema"></a>

```json
{
  "submitter_specimen_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "specimen_storage": "string",
  "specimen_processing": "string",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "specimen_laterality": "string",
  "reference_pathology_confirmed_diagnosis": "string",
  "reference_pathology_confirmed_tumour_presence": "string",
  "tumour_grading_system": "string",
  "tumour_grade": "string",
  "percent_tumour_cells_range": "string",
  "percent_tumour_cells_measurement_method": "string",
  "specimen_tissue_source": "string",
  "tumour_normal_designation": "string",
  "specimen_type": "string"
}

```

SpecimenFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_storage|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_processing|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_histological_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_anatomic_location|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_laterality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_tumour_presence|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grading_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grade|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_range|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_measurement_method|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_tissue_source|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_normal_designation|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedSpecimenModelSchema">PagedSpecimenModelSchema</h2>

<a id="schemapagedspecimenmodelschema"></a>
<a id="schema_PagedSpecimenModelSchema"></a>
<a id="tocSpagedspecimenmodelschema"></a>
<a id="tocspagedspecimenmodelschema"></a>

```json
{
  "items": [
    {
      "submitter_specimen_id": "string",
      "submitter_treatment_id": "string",
      "specimen_collection_date": {},
      "specimen_storage": "Cut slide",
      "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
      "tumour_histological_type": "string",
      "specimen_anatomic_location": "string",
      "specimen_laterality": "Left",
      "reference_pathology_confirmed_diagnosis": "Yes",
      "reference_pathology_confirmed_tumour_presence": "Yes",
      "tumour_grading_system": "FNCLCC grading system",
      "tumour_grade": "Low grade",
      "percent_tumour_cells_range": "0-19%",
      "percent_tumour_cells_measurement_method": "Genomics",
      "specimen_tissue_source": "Abdominal fluid",
      "tumour_normal_designation": "Normal",
      "specimen_type": "Cell line - derived from normal",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedSpecimenModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[SpecimenModelSchema](#schemaspecimenmodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SpecimenModelSchema">SpecimenModelSchema</h2>

<a id="schemaspecimenmodelschema"></a>
<a id="schema_SpecimenModelSchema"></a>
<a id="tocSspecimenmodelschema"></a>
<a id="tocsspecimenmodelschema"></a>

```json
{
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string",
  "specimen_collection_date": {},
  "specimen_storage": "Cut slide",
  "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "specimen_laterality": "Left",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "specimen_tissue_source": "Abdominal fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}

```

SpecimenModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|string|true|none|none|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_collection_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_storage|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StorageEnum](#schemastorageenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_processing|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenProcessingEnum](#schemaspecimenprocessingenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_histological_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_anatomic_location|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_laterality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenLateralityEnum](#schemaspecimenlateralityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ConfirmedDiagnosisTumourEnum](#schemaconfirmeddiagnosistumourenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_tumour_presence|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ConfirmedDiagnosisTumourEnum](#schemaconfirmeddiagnosistumourenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grading_system|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradingSystemEnum](#schematumourgradingsystemenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grade|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradeEnum](#schematumourgradeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_range|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PercentCellsRangeEnum](#schemapercentcellsrangeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_measurement_method|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CellsMeasureMethodEnum](#schemacellsmeasuremethodenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_tissue_source|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenTissueSourceEnum](#schemaspecimentissuesourceenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_normal_designation|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourDesginationEnum](#schematumourdesginationenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SpecimenTypeEnum](#schemaspecimentypeenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string|true|none|none|

<h2 id="tocS_SurgeryFilterSchema">SurgeryFilterSchema</h2>

<a id="schemasurgeryfilterschema"></a>
<a id="schema_SurgeryFilterSchema"></a>
<a id="tocSsurgeryfilterschema"></a>
<a id="tocssurgeryfilterschema"></a>

```json
{
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string",
  "surgery_type": "string",
  "surgery_site": "string",
  "surgery_location": "string",
  "tumour_length": 0,
  "tumour_width": 0,
  "greatest_dimension_tumour": 0,
  "tumour_focality": "string",
  "residual_tumour_classification": "string",
  "margins_status": "string",
  "lymphovascular_invasion": "string",
  "perineural_invasion": "string",
  "surgery_reference_database": "string",
  "surgery_reference_identifier": "string"
}

```

SurgeryFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_location|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_width|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|greatest_dimension_tumour|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_focality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|residual_tumour_classification|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margins_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lymphovascular_invasion|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|perineural_invasion|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_reference_database|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_reference_identifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedSurgeryModelSchema">PagedSurgeryModelSchema</h2>

<a id="schemapagedsurgerymodelschema"></a>
<a id="schema_PagedSurgeryModelSchema"></a>
<a id="tocSpagedsurgerymodelschema"></a>
<a id="tocspagedsurgerymodelschema"></a>

```json
{
  "items": [
    {
      "surgery_type": "string",
      "surgery_site": "string",
      "surgery_location": "Local recurrence",
      "tumour_length": 0,
      "tumour_length_not_available": false,
      "tumour_width": 0,
      "tumour_width_not_available": false,
      "greatest_dimension_tumour": 0,
      "greatest_dimension_tumour_not_available": false,
      "tumour_focality": "Cannot be assessed",
      "residual_tumour_classification": "Not applicable",
      "margins_status": "Margins clear",
      "lymphovascular_invasion": "Absent",
      "perineural_invasion": "Absent",
      "surgery_reference_database": "SNOMED",
      "surgery_reference_identifier": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedSurgeryModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[SurgeryModelSchema](#schemasurgerymodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SurgeryModelSchema">SurgeryModelSchema</h2>

<a id="schemasurgerymodelschema"></a>
<a id="schema_SurgeryModelSchema"></a>
<a id="tocSsurgerymodelschema"></a>
<a id="tocssurgerymodelschema"></a>

```json
{
  "surgery_type": "string",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_length": 0,
  "tumour_length_not_available": false,
  "tumour_width": 0,
  "tumour_width_not_available": false,
  "greatest_dimension_tumour": 0,
  "greatest_dimension_tumour_not_available": false,
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margins_status": "Margins clear",
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "surgery_reference_database": "SNOMED",
  "surgery_reference_identifier": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

SurgeryModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_location|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SurgeryLocationEnum](#schemasurgerylocationenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length_not_available|boolean|false|none|none|
|tumour_width|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_width_not_available|boolean|false|none|none|
|greatest_dimension_tumour|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|greatest_dimension_tumour_not_available|boolean|false|none|none|
|tumour_focality|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourFocalityEnum](#schematumourfocalityenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|residual_tumour_classification|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourClassificationEnum](#schematumourclassificationenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margins_status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginsStatusEnum](#schemamarginsstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lymphovascular_invasion|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LymphovascularInvasionEnum](#schemalymphovascularinvasionenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|perineural_invasion|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PerineuralInvasionEnum](#schemaperineuralinvasionenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_reference_database|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SurgeryReferenceDatabaseEnum](#schemasurgeryreferencedatabaseenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_reference_identifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_TreatmentFilterSchema">TreatmentFilterSchema</h2>

<a id="schematreatmentfilterschema"></a>
<a id="schema_TreatmentFilterSchema"></a>
<a id="tocStreatmentfilterschema"></a>
<a id="tocstreatmentfilterschema"></a>

```json
{
  "submitter_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "treatment_type": "string",
  "is_primary_treatment": "string",
  "treatment_intent": "string",
  "treatment_setting": "string",
  "response_to_treatment_criteria_method": "string",
  "response_to_treatment": "string",
  "status_of_treatment": "string"
}

```

TreatmentFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_primary_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_intent|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_setting|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|response_to_treatment_criteria_method|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|response_to_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status_of_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PagedTreatmentModelSchema">PagedTreatmentModelSchema</h2>

<a id="schemapagedtreatmentmodelschema"></a>
<a id="schema_PagedTreatmentModelSchema"></a>
<a id="tocSpagedtreatmentmodelschema"></a>
<a id="tocspagedtreatmentmodelschema"></a>

```json
{
  "items": [
    {
      "submitter_treatment_id": "string",
      "treatment_type": [
        "Bone marrow transplant"
      ],
      "is_primary_treatment": "Yes",
      "treatment_start_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "treatment_end_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "treatment_intent": "Curative",
      "treatment_setting": "Adjuvant",
      "response_to_treatment_criteria_method": "RECIST 1.1",
      "response_to_treatment": "Complete response",
      "status_of_treatment": "Treatment completed as prescribed",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ],
  "count": 0,
  "next_page": 0,
  "previous_page": 0
}

```

PagedTreatmentModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[TreatmentModelSchema](#schematreatmentmodelschema)]|true|none|none|
|count|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|previous_page|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_TreatmentModelSchema">TreatmentModelSchema</h2>

<a id="schematreatmentmodelschema"></a>
<a id="schema_TreatmentModelSchema"></a>
<a id="tocStreatmentmodelschema"></a>
<a id="tocstreatmentmodelschema"></a>

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Bone marrow transplant"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": {
    "day_interval": 0,
    "month_interval": 0
  },
  "treatment_end_date": {
    "day_interval": 0,
    "month_interval": 0
  },
  "treatment_intent": "Curative",
  "treatment_setting": "Adjuvant",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "status_of_treatment": "Treatment completed as prescribed",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}

```

TreatmentModelSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|string|true|none|none|
|treatment_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[TreatmentTypeEnum](#schematreatmenttypeenum)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_primary_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_start_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_end_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[DateInterval](#schemadateinterval)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_intent|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentIntentEnum](#schematreatmentintentenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_setting|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentSettingEnum](#schematreatmentsettingenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|response_to_treatment_criteria_method|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentResponseMethodEnum](#schematreatmentresponsemethodenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|response_to_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentResponseEnum](#schematreatmentresponseenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status_of_treatment|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TreatmentStatusEnum](#schematreatmentstatusenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string|true|none|none|

<h2 id="tocS_AllModelsSchema">AllModelsSchema</h2>

<a id="schemaallmodelsschema"></a>
<a id="schema_AllModelsSchema"></a>
<a id="tocSallmodelsschema"></a>
<a id="tocsallmodelsschema"></a>

```json
{
  "donors": [
    {
      "submitter_donor_id": "string",
      "gender": "Man",
      "sex_at_birth": "Male",
      "is_deceased": "Yes",
      "lost_to_follow_up": "Yes",
      "lost_to_followup_reason": "Completed study",
      "cause_of_death": "Died of cancer",
      "date_of_birth": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death": {
        "day_interval": 0,
        "month_interval": 0
      },
      "date_of_death_is_estimated": "Yes",
      "date_resolution": "string",
      "program_id": "string"
    }
  ],
  "primary_diagnoses": [
    {
      "submitter_primary_diagnosis_id": "string",
      "primary_site": "Accessory sinuses",
      "date_of_diagnosis": {
        "day_interval": 0,
        "month_interval": 0
      },
      "cancer_type_code": "string",
      "basis_of_diagnosis": "Clinical investigation",
      "laterality": "Bilateral",
      "clinical_tumour_staging_system": "AJCC cancer staging system",
      "clinical_t_category": "T0",
      "clinical_n_category": "N0",
      "clinical_m_category": "M0",
      "clinical_stage_group": "Stage 0",
      "pathological_tumour_staging_system": "AJCC cancer staging system",
      "pathological_t_category": "T0",
      "pathological_n_category": "N0",
      "pathological_m_category": "M0",
      "pathological_stage_group": "Stage 0",
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "specimens": [
    {
      "submitter_specimen_id": "string",
      "submitter_treatment_id": "string",
      "specimen_collection_date": {},
      "specimen_storage": "Cut slide",
      "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
      "tumour_histological_type": "string",
      "specimen_anatomic_location": "string",
      "specimen_laterality": "Left",
      "reference_pathology_confirmed_diagnosis": "Yes",
      "reference_pathology_confirmed_tumour_presence": "Yes",
      "tumour_grading_system": "FNCLCC grading system",
      "tumour_grade": "Low grade",
      "percent_tumour_cells_range": "0-19%",
      "percent_tumour_cells_measurement_method": "Genomics",
      "specimen_tissue_source": "Abdominal fluid",
      "tumour_normal_designation": "Normal",
      "specimen_type": "Cell line - derived from normal",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ],
  "sample_registrations": [
    {
      "submitter_sample_id": "string",
      "sample_type": "Amplified DNA",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_specimen_id": "string"
    }
  ],
  "treatments": [
    {
      "submitter_treatment_id": "string",
      "treatment_type": [
        "Bone marrow transplant"
      ],
      "is_primary_treatment": "Yes",
      "treatment_start_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "treatment_end_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "treatment_intent": "Curative",
      "treatment_setting": "Adjuvant",
      "response_to_treatment_criteria_method": "RECIST 1.1",
      "response_to_treatment": "Complete response",
      "status_of_treatment": "Treatment completed as prescribed",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ],
  "systemic_therapies": [
    {
      "systemic_therapy_type": "string",
      "days_per_cycle": 0,
      "days_per_cycle_not_available": false,
      "number_of_cycles": 0,
      "number_of_cycles_not_available": false,
      "start_date": {},
      "end_date": {},
      "drug_reference_database": "RxNorm",
      "drug_name": "string",
      "drug_reference_identifier": "string",
      "drug_dose_units": "mg/m2",
      "prescribed_cumulative_drug_dose": 0,
      "prescribed_cumulative_drug_dose_not_available": false,
      "actual_cumulative_drug_dose": 0,
      "actual_cumulative_drug_dose_not_available": false,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "radiations": [
    {
      "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
      "radiation_therapy_type": "External",
      "radiation_therapy_fractions": 0,
      "radiation_therapy_fractions_not_available": false,
      "radiation_therapy_dosage": 0,
      "radiation_therapy_dosage_not_available": false,
      "anatomical_site_irradiated": "ABDOMEN_WHOLE",
      "radiation_boost": "Yes",
      "reference_radiation_treatment_id": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "radiopharmaceutical_therapies": [
    {
      "rxnorm_code": "string",
      "agent_name": "string",
      "radionuclide": "Carbon-14",
      "radionuclide_other": "string",
      "start_date": {},
      "end_date": {},
      "cumulative_drug_dose": 0,
      "cumulative_drug_dose_not_available": false,
      "drug_dose_units": "Bq",
      "mass_value": 0,
      "mass_value_not_available": false,
      "mass_unit_ucum": "ug",
      "number_of_cycles": 0,
      "number_of_cycles_not_available": false,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "surgeries": [
    {
      "surgery_type": "string",
      "surgery_site": "string",
      "surgery_location": "Local recurrence",
      "tumour_length": 0,
      "tumour_length_not_available": false,
      "tumour_width": 0,
      "tumour_width_not_available": false,
      "greatest_dimension_tumour": 0,
      "greatest_dimension_tumour_not_available": false,
      "tumour_focality": "Cannot be assessed",
      "residual_tumour_classification": "Not applicable",
      "margins_status": "Margins clear",
      "lymphovascular_invasion": "Absent",
      "perineural_invasion": "Absent",
      "surgery_reference_database": "SNOMED",
      "surgery_reference_identifier": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "follow_ups": [
    {
      "submitter_follow_up_id": "string",
      "date_of_followup": {
        "day_interval": 0,
        "month_interval": 0
      },
      "disease_status_at_followup": "Complete remission",
      "relapse_type": "Distant recurrence/metastasis",
      "date_of_relapse": {
        "day_interval": 0,
        "month_interval": 0
      },
      "method_of_progression_status": [
        "Imaging (procedure)"
      ],
      "anatomic_site_progression_or_recurrence": [
        "string"
      ],
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string"
    }
  ],
  "biomarkers": [
    {
      "submitter_specimen_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string",
      "submitter_follow_up_id": "string",
      "test_date": {
        "day_interval": 0,
        "month_interval": 0
      },
      "psa_level": 0,
      "psa_level_not_available": false,
      "ca125": 0,
      "ca125_not_available": false,
      "cea": 0,
      "cea_not_available": false,
      "ca19_9": 0,
      "ca19_9_not_available": false,
      "er_status": "Cannot be determined",
      "er_percent_positive": 0,
      "er_percent_positive_not_available": false,
      "pr_status": "Cannot be determined",
      "pr_percent_positive": 0,
      "pr_percent_positive_not_available": false,
      "her2_ihc_status": "Cannot be determined",
      "her2_ish_status": "Cannot be determined",
      "hpv_ihc_status": "Cannot be determined",
      "hpv_pcr_status": "Cannot be determined",
      "hpv_strain": [
        "HPV16"
      ],
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "comorbidities": [
    {
      "prior_malignancy": "Yes",
      "laterality_of_prior_malignancy": "Bilateral",
      "age_at_comorbidity_diagnosis": 0,
      "age_at_comorbidity_diagnosis_not_available": false,
      "comorbidity_type_code": "string",
      "comorbidity_treatment_status": "Yes",
      "comorbidity_treatment": "string",
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ],
  "exposures": [
    {
      "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
      "tobacco_type": [
        "Chewing Tobacco"
      ],
      "pack_years_smoked": 0,
      "pack_years_smoked_not_available": false,
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ]
}

```

AllModelsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|donors|[[DonorModelSchema](#schemadonormodelschema)]|true|none|none|
|primary_diagnoses|[[PrimaryDiagnosisModelSchema](#schemaprimarydiagnosismodelschema)]|true|none|none|
|specimens|[[SpecimenModelSchema](#schemaspecimenmodelschema)]|true|none|none|
|sample_registrations|[[SampleRegistrationModelSchema](#schemasampleregistrationmodelschema)]|true|none|none|
|treatments|[[TreatmentModelSchema](#schematreatmentmodelschema)]|true|none|none|
|systemic_therapies|[[SystemicTherapyModelSchema](#schemasystemictherapymodelschema)]|true|none|none|
|radiations|[[RadiationModelSchema](#schemaradiationmodelschema)]|true|none|none|
|radiopharmaceutical_therapies|[[RadiopharmaceuticalTherapyModelSchema](#schemaradiopharmaceuticaltherapymodelschema)]|true|none|none|
|surgeries|[[SurgeryModelSchema](#schemasurgerymodelschema)]|true|none|none|
|follow_ups|[[FollowUpModelSchema](#schemafollowupmodelschema)]|true|none|none|
|biomarkers|[[BiomarkerModelSchema](#schemabiomarkermodelschema)]|true|none|none|
|comorbidities|[[ComorbidityModelSchema](#schemacomorbiditymodelschema)]|true|none|none|
|exposures|[[ExposureModelSchema](#schemaexposuremodelschema)]|true|none|none|

<h2 id="tocS_DownloadResponseSchema">DownloadResponseSchema</h2>

<a id="schemadownloadresponseschema"></a>
<a id="schema_DownloadResponseSchema"></a>
<a id="tocSdownloadresponseschema"></a>
<a id="tocsdownloadresponseschema"></a>

```json
{
  "summary": {
    "message": "string",
    "record_counts": {
      "property1": 0,
      "property2": 0
    }
  },
  "data": {
    "donors": [
      {
        "submitter_donor_id": "string",
        "gender": "Man",
        "sex_at_birth": "Male",
        "is_deceased": "Yes",
        "lost_to_follow_up": "Yes",
        "lost_to_followup_reason": "Completed study",
        "cause_of_death": "Died of cancer",
        "date_of_birth": {
          "day_interval": 0,
          "month_interval": 0
        },
        "date_of_death": {
          "day_interval": 0,
          "month_interval": 0
        },
        "date_of_death_is_estimated": "Yes",
        "date_resolution": "string",
        "program_id": "string"
      }
    ],
    "primary_diagnoses": [
      {
        "submitter_primary_diagnosis_id": "string",
        "primary_site": "Accessory sinuses",
        "date_of_diagnosis": {
          "day_interval": 0,
          "month_interval": 0
        },
        "cancer_type_code": "string",
        "basis_of_diagnosis": "Clinical investigation",
        "laterality": "Bilateral",
        "clinical_tumour_staging_system": "AJCC cancer staging system",
        "clinical_t_category": "T0",
        "clinical_n_category": "N0",
        "clinical_m_category": "M0",
        "clinical_stage_group": "Stage 0",
        "pathological_tumour_staging_system": "AJCC cancer staging system",
        "pathological_t_category": "T0",
        "pathological_n_category": "N0",
        "pathological_m_category": "M0",
        "pathological_stage_group": "Stage 0",
        "program_id": "string",
        "submitter_donor_id": "string"
      }
    ],
    "specimens": [
      {
        "submitter_specimen_id": "string",
        "submitter_treatment_id": "string",
        "specimen_collection_date": {},
        "specimen_storage": "Cut slide",
        "specimen_processing": "Cryopreservation in liquid nitrogen (dead tissue)",
        "tumour_histological_type": "string",
        "specimen_anatomic_location": "string",
        "specimen_laterality": "Left",
        "reference_pathology_confirmed_diagnosis": "Yes",
        "reference_pathology_confirmed_tumour_presence": "Yes",
        "tumour_grading_system": "FNCLCC grading system",
        "tumour_grade": "Low grade",
        "percent_tumour_cells_range": "0-19%",
        "percent_tumour_cells_measurement_method": "Genomics",
        "specimen_tissue_source": "Abdominal fluid",
        "tumour_normal_designation": "Normal",
        "specimen_type": "Cell line - derived from normal",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_primary_diagnosis_id": "string"
      }
    ],
    "sample_registrations": [
      {
        "submitter_sample_id": "string",
        "sample_type": "Amplified DNA",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_specimen_id": "string"
      }
    ],
    "treatments": [
      {
        "submitter_treatment_id": "string",
        "treatment_type": [
          "Bone marrow transplant"
        ],
        "is_primary_treatment": "Yes",
        "treatment_start_date": {
          "day_interval": 0,
          "month_interval": 0
        },
        "treatment_end_date": {
          "day_interval": 0,
          "month_interval": 0
        },
        "treatment_intent": "Curative",
        "treatment_setting": "Adjuvant",
        "response_to_treatment_criteria_method": "RECIST 1.1",
        "response_to_treatment": "Complete response",
        "status_of_treatment": "Treatment completed as prescribed",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_primary_diagnosis_id": "string"
      }
    ],
    "systemic_therapies": [
      {
        "systemic_therapy_type": "string",
        "days_per_cycle": 0,
        "days_per_cycle_not_available": false,
        "number_of_cycles": 0,
        "number_of_cycles_not_available": false,
        "start_date": {},
        "end_date": {},
        "drug_reference_database": "RxNorm",
        "drug_name": "string",
        "drug_reference_identifier": "string",
        "drug_dose_units": "mg/m2",
        "prescribed_cumulative_drug_dose": 0,
        "prescribed_cumulative_drug_dose_not_available": false,
        "actual_cumulative_drug_dose": 0,
        "actual_cumulative_drug_dose_not_available": false,
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "radiations": [
      {
        "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
        "radiation_therapy_type": "External",
        "radiation_therapy_fractions": 0,
        "radiation_therapy_fractions_not_available": false,
        "radiation_therapy_dosage": 0,
        "radiation_therapy_dosage_not_available": false,
        "anatomical_site_irradiated": "ABDOMEN_WHOLE",
        "radiation_boost": "Yes",
        "reference_radiation_treatment_id": "string",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "radiopharmaceutical_therapies": [
      {
        "rxnorm_code": "string",
        "agent_name": "string",
        "radionuclide": "Carbon-14",
        "radionuclide_other": "string",
        "start_date": {},
        "end_date": {},
        "cumulative_drug_dose": 0,
        "cumulative_drug_dose_not_available": false,
        "drug_dose_units": "Bq",
        "mass_value": 0,
        "mass_value_not_available": false,
        "mass_unit_ucum": "ug",
        "number_of_cycles": 0,
        "number_of_cycles_not_available": false,
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "surgeries": [
      {
        "surgery_type": "string",
        "surgery_site": "string",
        "surgery_location": "Local recurrence",
        "tumour_length": 0,
        "tumour_length_not_available": false,
        "tumour_width": 0,
        "tumour_width_not_available": false,
        "greatest_dimension_tumour": 0,
        "greatest_dimension_tumour_not_available": false,
        "tumour_focality": "Cannot be assessed",
        "residual_tumour_classification": "Not applicable",
        "margins_status": "Margins clear",
        "lymphovascular_invasion": "Absent",
        "perineural_invasion": "Absent",
        "surgery_reference_database": "SNOMED",
        "surgery_reference_identifier": "string",
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "follow_ups": [
      {
        "submitter_follow_up_id": "string",
        "date_of_followup": {
          "day_interval": 0,
          "month_interval": 0
        },
        "disease_status_at_followup": "Complete remission",
        "relapse_type": "Distant recurrence/metastasis",
        "date_of_relapse": {
          "day_interval": 0,
          "month_interval": 0
        },
        "method_of_progression_status": [
          "Imaging (procedure)"
        ],
        "anatomic_site_progression_or_recurrence": [
          "string"
        ],
        "program_id": "string",
        "submitter_donor_id": "string",
        "submitter_primary_diagnosis_id": "string",
        "submitter_treatment_id": "string"
      }
    ],
    "biomarkers": [
      {
        "submitter_specimen_id": "string",
        "submitter_primary_diagnosis_id": "string",
        "submitter_treatment_id": "string",
        "submitter_follow_up_id": "string",
        "test_date": {
          "day_interval": 0,
          "month_interval": 0
        },
        "psa_level": 0,
        "psa_level_not_available": false,
        "ca125": 0,
        "ca125_not_available": false,
        "cea": 0,
        "cea_not_available": false,
        "ca19_9": 0,
        "ca19_9_not_available": false,
        "er_status": "Cannot be determined",
        "er_percent_positive": 0,
        "er_percent_positive_not_available": false,
        "pr_status": "Cannot be determined",
        "pr_percent_positive": 0,
        "pr_percent_positive_not_available": false,
        "her2_ihc_status": "Cannot be determined",
        "her2_ish_status": "Cannot be determined",
        "hpv_ihc_status": "Cannot be determined",
        "hpv_pcr_status": "Cannot be determined",
        "hpv_strain": [
          "HPV16"
        ],
        "program_id": "string",
        "submitter_donor_id": "string"
      }
    ],
    "comorbidities": [
      {
        "prior_malignancy": "Yes",
        "laterality_of_prior_malignancy": "Bilateral",
        "age_at_comorbidity_diagnosis": 0,
        "age_at_comorbidity_diagnosis_not_available": false,
        "comorbidity_type_code": "string",
        "comorbidity_treatment_status": "Yes",
        "comorbidity_treatment": "string",
        "program_id": "string",
        "submitter_donor_id": "string"
      }
    ],
    "exposures": [
      {
        "tobacco_smoking_status": "Current reformed smoker for <= 15 years",
        "tobacco_type": [
          "Chewing Tobacco"
        ],
        "pack_years_smoked": 0,
        "pack_years_smoked_not_available": false,
        "program_id": "string",
        "submitter_donor_id": "string"
      }
    ]
  }
}

```

DownloadResponseSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|summary|[SummaryMessageSchema](#schemasummarymessageschema)|true|none|none|
|data|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[AllModelsSchema](#schemaallmodelsschema)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_SummaryMessageSchema">SummaryMessageSchema</h2>

<a id="schemasummarymessageschema"></a>
<a id="schema_SummaryMessageSchema"></a>
<a id="tocSsummarymessageschema"></a>
<a id="tocssummarymessageschema"></a>

```json
{
  "message": "string",
  "record_counts": {
    "property1": 0,
    "property2": 0
  }
}

```

SummaryMessageSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|true|none|none|
|record_counts|object|true|none|none|
|» **additionalProperties**|integer|false|none|none|

<h2 id="tocS_DownloadFilterSchema">DownloadFilterSchema</h2>

<a id="schemadownloadfilterschema"></a>
<a id="schema_DownloadFilterSchema"></a>
<a id="tocSdownloadfilterschema"></a>
<a id="tocsdownloadfilterschema"></a>

```json
{
  "treatment_type": [
    "string"
  ],
  "primary_site": [
    "string"
  ],
  "systemic_therapy_drug_name": [
    "string"
  ],
  "program_id": [
    "string"
  ],
  "biosample_id": [
    "string"
  ],
  "summary_only": false
}

```

DownloadFilterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_type|[string]|false|none|none|
|primary_site|[string]|false|none|none|
|systemic_therapy_drug_name|[string]|false|none|none|
|program_id|[string]|false|none|none|
|biosample_id|[string]|false|none|none|
|summary_only|boolean|false|none|If true, only summary data will be returned. If false, detailed data will be returned.|

<h2 id="tocS_DonorExplorerSchema">DonorExplorerSchema</h2>

<a id="schemadonorexplorerschema"></a>
<a id="schema_DonorExplorerSchema"></a>
<a id="tocSdonorexplorerschema"></a>
<a id="tocsdonorexplorerschema"></a>

```json
{
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_sample_ids": [
    "string"
  ],
  "primary_site": [
    "string"
  ],
  "treatment_type": [
    "string"
  ],
  "age_at_diagnosis": "string"
}

```

DonorExplorerSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_sample_ids|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_site|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|treatment_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|age_at_diagnosis|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

