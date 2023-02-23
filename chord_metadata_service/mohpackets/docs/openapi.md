
<h1 id="moh-service-api">MoH Service API v1.0.0</h1>

This is the RESTful API for the MoH Service.

# Authentication

- HTTP Authentication, scheme: basic

* API Key (cookieAuth)
    - Parameter Name: **sessionid**, in: cookie. 

* API Key (tokenAuth)
    - Parameter Name: **Authorization**, in: header. Token-based authentication with required prefix "Token"

<h1 id="moh-service-api-discovery">discovery</h1>

## discovery_biomarkers_list

<a id="opIddiscovery_biomarkers_list"></a>

`GET /moh/v1/discovery/biomarkers/`

<h3 id="discovery_biomarkers_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_specimen_id|query|string|false|none|
|submitter_primary_diagnosis_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|submitter_follow_up_id|query|string|false|none|
|test_interval|query|integer|false|none|
|psa_level|query|integer|false|none|
|ca125|query|integer|false|none|
|cea|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_chemotherapies_list

<a id="opIddiscovery_chemotherapies_list"></a>

`GET /moh/v1/discovery/chemotherapies/`

<h3 id="discovery_chemotherapies_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|drug_name|query|string|false|none|
|drug_rxnormcui|query|string|false|none|
|chemotherapy_dosage_units|query|string|false|none|
|cumulative_drug_dosage_prescribed|query|integer|false|none|
|cumulative_drug_dosage_actual|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_comorbidities_list

<a id="opIddiscovery_comorbidities_list"></a>

`GET /moh/v1/discovery/comorbidities/`

<h3 id="discovery_comorbidities_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|prior_malignancy|query|string|false|none|
|laterality_of_prior_malignancy|query|string|false|none|
|age_at_comorbidity_diagnosis|query|integer|false|none|
|comorbidity_type_code|query|string|false|none|
|comorbidity_treatment_status|query|string|false|none|
|comorbidity_treatment|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_donors_list

<a id="opIddiscovery_donors_list"></a>

`GET /moh/v1/discovery/donors/`

<h3 id="discovery_donors_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_donor_id|query|string|false|none|
|program_id|query|string|false|none|
|is_deceased|query|boolean|false|none|
|cause_of_death|query|string|false|none|
|date_of_birth|query|string|false|none|
|date_of_death|query|string|false|none|
|primary_site|query|string|false|none|
|age|query|number|false|none|
|max_age|query|number|false|none|
|min_age|query|number|false|none|
|donors|query|string|false|none|
|primary_diagnosis|query|string|false|none|
|speciman|query|string|false|none|
|sample_registration|query|string|false|none|
|treatment|query|string|false|none|
|chemotherapy|query|string|false|none|
|hormone_therapy|query|string|false|none|
|radiation|query|string|false|none|
|immunotherapy|query|string|false|none|
|surgery|query|string|false|none|
|follow_up|query|string|false|none|
|biomarker|query|string|false|none|
|comorbidity|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_follow_ups_list

<a id="opIddiscovery_follow_ups_list"></a>

`GET /moh/v1/discovery/follow_ups/`

<h3 id="discovery_follow_ups_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_follow_up_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_primary_diagnosis_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|date_of_followup|query|string|false|none|
|lost_to_followup|query|boolean|false|none|
|lost_to_followup_reason|query|string|false|none|
|disease_status_at_followup|query|string|false|none|
|relapse_type|query|string|false|none|
|date_of_relapse|query|string|false|none|
|method_of_progression_status|query|string|false|none|
|anatomic_site_progression_or_recurrence|query|string|false|none|
|recurrence_tumour_staging_system|query|string|false|none|
|recurrence_t_category|query|string|false|none|
|recurrence_n_category|query|string|false|none|
|recurrence_m_category|query|string|false|none|
|recurrence_stage_group|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_hormone_therapies_list

<a id="opIddiscovery_hormone_therapies_list"></a>

`GET /moh/v1/discovery/hormone_therapies/`

<h3 id="discovery_hormone_therapies_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|drug_name|query|string|false|none|
|drug_rxnormcui|query|string|false|none|
|hormone_drug_dosage_units|query|string|false|none|
|cumulative_drug_dosage_prescribed|query|integer|false|none|
|cumulative_drug_dosage_actual|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_immunotherapies_list

<a id="opIddiscovery_immunotherapies_list"></a>

`GET /moh/v1/discovery/immunotherapies/`

<h3 id="discovery_immunotherapies_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|immunotherapy_type|query|string|false|none|
|drug_name|query|string|false|none|
|drug_rxnormcui|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_overview_retrieve

<a id="opIddiscovery_overview_retrieve"></a>

`GET /moh/v1/discovery/overview`

MoH Overview schema

> Example responses

> 200 Response

```json
{
  "cohort_count": 0,
  "individual_count": 0
}
```

## discovery_primary_diagnoses_list

<a id="opIddiscovery_primary_diagnoses_list"></a>

`GET /moh/v1/discovery/primary_diagnoses/`

<h3 id="discovery_primary_diagnoses_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|date_of_diagnosis|query|string|false|none|
|cancer_type_code|query|string|false|none|
|basis_of_diagnosis|query|string|false|none|
|lymph_nodes_examined_status|query|string|false|none|
|lymph_nodes_examined_method|query|string|false|none|
|number_lymph_nodes_positive|query|integer|false|none|
|clinical_tumour_staging_system|query|string|false|none|
|clinical_t_category|query|string|false|none|
|clinical_n_category|query|string|false|none|
|clinical_m_category|query|string|false|none|
|clinical_stage_group|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_radiations_list

<a id="opIddiscovery_radiations_list"></a>

`GET /moh/v1/discovery/radiations/`

<h3 id="discovery_radiations_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|radiation_therapy_modality|query|string|false|none|
|radiation_therapy_type|query|string|false|none|
|radiation_therapy_fractions|query|integer|false|none|
|radiation_therapy_dosage|query|integer|false|none|
|anatomical_site_irradiated|query|string|false|none|
|radiation_boost|query|boolean|false|none|
|reference_radiation_treatment_id|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_sample_registrations_list

<a id="opIddiscovery_sample_registrations_list"></a>

`GET /moh/v1/discovery/sample_registrations/`

<h3 id="discovery_sample_registrations_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_sample_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_specimen_id|query|string|false|none|
|gender|query|string|false|none|
|sex_at_birth|query|string|false|none|
|specimen_tissue_source|query|string|false|none|
|tumour_normal_designation|query|string|false|none|
|specimen_type|query|string|false|none|
|sample_type|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_specimens_list

<a id="opIddiscovery_specimens_list"></a>

`GET /moh/v1/discovery/specimens/`

<h3 id="discovery_specimens_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_specimen_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_primary_diagnosis_id|query|string|false|none|
|pathological_tumour_staging_system|query|string|false|none|
|pathological_t_category|query|string|false|none|
|pathological_n_category|query|string|false|none|
|pathological_m_category|query|string|false|none|
|pathological_stage_group|query|string|false|none|
|specimen_collection_date|query|string|false|none|
|specimen_storage|query|string|false|none|
|tumour_histological_type|query|string|false|none|
|specimen_anatomic_location|query|string|false|none|
|reference_pathology_confirmed_diagnosis|query|string|false|none|
|reference_pathology_confirmed_tumour_presence|query|string|false|none|
|tumour_grading_system|query|string|false|none|
|tumour_grade|query|string|false|none|
|percent_tumour_cells_range|query|string|false|none|
|percent_tumour_cells_measurement_method|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_surgeries_list

<a id="opIddiscovery_surgeries_list"></a>

`GET /moh/v1/discovery/surgeries/`

<h3 id="discovery_surgeries_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_specimen_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|surgery_type|query|string|false|none|
|surgery_site|query|string|false|none|
|surgery_location|query|string|false|none|
|tumour_length|query|integer|false|none|
|tumour_width|query|integer|false|none|
|greatest_dimension_tumour|query|integer|false|none|
|tumour_focality|query|string|false|none|
|residual_tumour_classification|query|string|false|none|
|margin_types_involved|query|string|false|none|
|margin_types_not_involved|query|string|false|none|
|margin_types_not_assessed|query|string|false|none|
|lymphovascular_invasion|query|string|false|none|
|perineural_invasion|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

## discovery_treatments_list

<a id="opIddiscovery_treatments_list"></a>

`GET /moh/v1/discovery/treatments/`

<h3 id="discovery_treatments_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_treatment_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_primary_diagnosis_id|query|string|false|none|
|treatment_type|query|string|false|none|
|is_primary_treatment|query|string|false|none|
|treatment_start_date|query|string|false|none|
|treatment_end_date|query|string|false|none|
|treatment_setting|query|string|false|none|
|treatment_intent|query|string|false|none|
|days_per_cycle|query|integer|false|none|
|number_of_cycles|query|integer|false|none|
|response_to_treatment_criteria_method|query|string|false|none|
|response_to_treatment|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "discovery_count": 0
}
```

<h1 id="moh-service-api-model">model</h1>

## model_biomarkers_list

<a id="opIdmodel_biomarkers_list"></a>

`GET /moh/v1/model/biomarkers/`

<h3 id="model_biomarkers_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_specimen_id|query|string|false|none|
|submitter_primary_diagnosis_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|submitter_follow_up_id|query|string|false|none|
|test_interval|query|integer|false|none|
|psa_level|query|integer|false|none|
|ca125|query|integer|false|none|
|cea|query|integer|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "test_interval": 32767,
      "psa_level": 32767,
      "ca125": 32767,
      "cea": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_specimen_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string",
      "submitter_follow_up_id": "string"
    }
  ]
}
```

## model_biomarkers_create

<a id="opIdmodel_biomarkers_create"></a>

`POST /moh/v1/model/biomarkers/`

<h3 id="model_biomarkers_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BiomarkerRequest](#schemabiomarkerrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "test_interval": 32767,
  "psa_level": 32767,
  "ca125": 32767,
  "cea": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string"
}
```

## model_biomarkers_retrieve

<a id="opIdmodel_biomarkers_retrieve"></a>

`GET /moh/v1/model/biomarkers/{id}/`

<h3 id="model_biomarkers_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this biomarker.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "test_interval": 32767,
  "psa_level": 32767,
  "ca125": 32767,
  "cea": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string"
}
```

## model_biomarkers_update

<a id="opIdmodel_biomarkers_update"></a>

`PUT /moh/v1/model/biomarkers/{id}/`

<h3 id="model_biomarkers_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this biomarker.|
|body|body|[BiomarkerRequest](#schemabiomarkerrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "test_interval": 32767,
  "psa_level": 32767,
  "ca125": 32767,
  "cea": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string"
}
```

## model_biomarkers_partial_update

<a id="opIdmodel_biomarkers_partial_update"></a>

`PATCH /moh/v1/model/biomarkers/{id}/`

<h3 id="model_biomarkers_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this biomarker.|
|body|body|[PatchedBiomarkerRequest](#schemapatchedbiomarkerrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "test_interval": 32767,
  "psa_level": 32767,
  "ca125": 32767,
  "cea": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string"
}
```

## model_biomarkers_destroy

<a id="opIdmodel_biomarkers_destroy"></a>

`DELETE /moh/v1/model/biomarkers/{id}/`

<h3 id="model_biomarkers_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this biomarker.|

## model_chemotherapies_list

<a id="opIdmodel_chemotherapies_list"></a>

`GET /moh/v1/model/chemotherapies/`

<h3 id="model_chemotherapies_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|drug_name|query|string|false|none|
|drug_rxnormcui|query|string|false|none|
|chemotherapy_dosage_units|query|string|false|none|
|cumulative_drug_dosage_prescribed|query|integer|false|none|
|cumulative_drug_dosage_actual|query|integer|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "chemotherapy_dosage_units": "mg/m2",
      "drug_name": "string",
      "drug_rxnormcui": "string",
      "cumulative_drug_dosage_prescribed": 32767,
      "cumulative_drug_dosage_actual": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}
```

## model_chemotherapies_create

<a id="opIdmodel_chemotherapies_create"></a>

`POST /moh/v1/model/chemotherapies/`

<h3 id="model_chemotherapies_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ChemotherapyRequest](#schemachemotherapyrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "chemotherapy_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_chemotherapies_retrieve

<a id="opIdmodel_chemotherapies_retrieve"></a>

`GET /moh/v1/model/chemotherapies/{id}/`

<h3 id="model_chemotherapies_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this chemotherapy.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "chemotherapy_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_chemotherapies_update

<a id="opIdmodel_chemotherapies_update"></a>

`PUT /moh/v1/model/chemotherapies/{id}/`

<h3 id="model_chemotherapies_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this chemotherapy.|
|body|body|[ChemotherapyRequest](#schemachemotherapyrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "chemotherapy_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_chemotherapies_partial_update

<a id="opIdmodel_chemotherapies_partial_update"></a>

`PATCH /moh/v1/model/chemotherapies/{id}/`

<h3 id="model_chemotherapies_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this chemotherapy.|
|body|body|[PatchedChemotherapyRequest](#schemapatchedchemotherapyrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "chemotherapy_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_chemotherapies_destroy

<a id="opIdmodel_chemotherapies_destroy"></a>

`DELETE /moh/v1/model/chemotherapies/{id}/`

<h3 id="model_chemotherapies_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this chemotherapy.|

## model_comorbidities_list

<a id="opIdmodel_comorbidities_list"></a>

`GET /moh/v1/model/comorbidities/`

<h3 id="model_comorbidities_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|prior_malignancy|query|string|false|none|
|laterality_of_prior_malignancy|query|string|false|none|
|age_at_comorbidity_diagnosis|query|integer|false|none|
|comorbidity_type_code|query|string|false|none|
|comorbidity_treatment_status|query|string|false|none|
|comorbidity_treatment|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "prior_malignancy": "Yes",
      "laterality_of_prior_malignancy": "Bilateral",
      "comorbidity_type_code": "string",
      "comorbidity_treatment_status": "Yes",
      "comorbidity_treatment": "string",
      "age_at_comorbidity_diagnosis": 32767,
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ]
}
```

## model_comorbidities_create

<a id="opIdmodel_comorbidities_create"></a>

`POST /moh/v1/model/comorbidities/`

<h3 id="model_comorbidities_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ComorbidityRequest](#schemacomorbidityrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string",
  "age_at_comorbidity_diagnosis": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}
```

## model_comorbidities_retrieve

<a id="opIdmodel_comorbidities_retrieve"></a>

`GET /moh/v1/model/comorbidities/{id}/`

<h3 id="model_comorbidities_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this comorbidity.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string",
  "age_at_comorbidity_diagnosis": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}
```

## model_comorbidities_update

<a id="opIdmodel_comorbidities_update"></a>

`PUT /moh/v1/model/comorbidities/{id}/`

<h3 id="model_comorbidities_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this comorbidity.|
|body|body|[ComorbidityRequest](#schemacomorbidityrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string",
  "age_at_comorbidity_diagnosis": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}
```

## model_comorbidities_partial_update

<a id="opIdmodel_comorbidities_partial_update"></a>

`PATCH /moh/v1/model/comorbidities/{id}/`

<h3 id="model_comorbidities_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this comorbidity.|
|body|body|[PatchedComorbidityRequest](#schemapatchedcomorbidityrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string",
  "age_at_comorbidity_diagnosis": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}
```

## model_comorbidities_destroy

<a id="opIdmodel_comorbidities_destroy"></a>

`DELETE /moh/v1/model/comorbidities/{id}/`

<h3 id="model_comorbidities_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this comorbidity.|

## model_donors_list

<a id="opIdmodel_donors_list"></a>

`GET /moh/v1/model/donors/`

<h3 id="model_donors_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_donor_id|query|string|false|none|
|program_id|query|string|false|none|
|is_deceased|query|boolean|false|none|
|cause_of_death|query|string|false|none|
|date_of_birth|query|string|false|none|
|date_of_death|query|string|false|none|
|primary_site|query|string|false|none|
|age|query|number|false|none|
|max_age|query|number|false|none|
|min_age|query|number|false|none|
|donors|query|string|false|none|
|primary_diagnosis|query|string|false|none|
|speciman|query|string|false|none|
|sample_registration|query|string|false|none|
|treatment|query|string|false|none|
|chemotherapy|query|string|false|none|
|hormone_therapy|query|string|false|none|
|radiation|query|string|false|none|
|immunotherapy|query|string|false|none|
|surgery|query|string|false|none|
|follow_up|query|string|false|none|
|biomarker|query|string|false|none|
|comorbidity|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_donor_id": "string",
      "cause_of_death": "Died of cancer",
      "date_of_birth": "string",
      "date_of_death": "string",
      "primary_site": [
        "Accessory sinuses"
      ],
      "is_deceased": true,
      "program_id": "string"
    }
  ]
}
```

## model_donors_create

<a id="opIdmodel_donors_create"></a>

`POST /moh/v1/model/donors/`

<h3 id="model_donors_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DonorRequest](#schemadonorrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "submitter_donor_id": "string",
  "cause_of_death": "Died of cancer",
  "date_of_birth": "string",
  "date_of_death": "string",
  "primary_site": [
    "Accessory sinuses"
  ],
  "is_deceased": true,
  "program_id": "string"
}
```

## model_donors_retrieve

<a id="opIdmodel_donors_retrieve"></a>

`GET /moh/v1/model/donors/{submitter_donor_id}/`

<h3 id="model_donors_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_donor_id|path|string|true|A unique value identifying this donor.|

> Example responses

> 200 Response

```json
{
  "submitter_donor_id": "string",
  "cause_of_death": "Died of cancer",
  "date_of_birth": "string",
  "date_of_death": "string",
  "primary_site": [
    "Accessory sinuses"
  ],
  "is_deceased": true,
  "program_id": "string"
}
```

## model_donors_update

<a id="opIdmodel_donors_update"></a>

`PUT /moh/v1/model/donors/{submitter_donor_id}/`

<h3 id="model_donors_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_donor_id|path|string|true|A unique value identifying this donor.|
|body|body|[DonorRequest](#schemadonorrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "submitter_donor_id": "string",
  "cause_of_death": "Died of cancer",
  "date_of_birth": "string",
  "date_of_death": "string",
  "primary_site": [
    "Accessory sinuses"
  ],
  "is_deceased": true,
  "program_id": "string"
}
```

## model_donors_partial_update

<a id="opIdmodel_donors_partial_update"></a>

`PATCH /moh/v1/model/donors/{submitter_donor_id}/`

<h3 id="model_donors_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_donor_id|path|string|true|A unique value identifying this donor.|
|body|body|[PatchedDonorRequest](#schemapatcheddonorrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "submitter_donor_id": "string",
  "cause_of_death": "Died of cancer",
  "date_of_birth": "string",
  "date_of_death": "string",
  "primary_site": [
    "Accessory sinuses"
  ],
  "is_deceased": true,
  "program_id": "string"
}
```

## model_donors_destroy

<a id="opIdmodel_donors_destroy"></a>

`DELETE /moh/v1/model/donors/{submitter_donor_id}/`

<h3 id="model_donors_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_donor_id|path|string|true|A unique value identifying this donor.|

## model_follow_ups_list

<a id="opIdmodel_follow_ups_list"></a>

`GET /moh/v1/model/follow_ups/`

<h3 id="model_follow_ups_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_follow_up_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_primary_diagnosis_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|date_of_followup|query|string|false|none|
|lost_to_followup|query|boolean|false|none|
|lost_to_followup_reason|query|string|false|none|
|disease_status_at_followup|query|string|false|none|
|relapse_type|query|string|false|none|
|date_of_relapse|query|string|false|none|
|method_of_progression_status|query|string|false|none|
|anatomic_site_progression_or_recurrence|query|string|false|none|
|recurrence_tumour_staging_system|query|string|false|none|
|recurrence_t_category|query|string|false|none|
|recurrence_n_category|query|string|false|none|
|recurrence_m_category|query|string|false|none|
|recurrence_stage_group|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_follow_up_id": "string",
      "date_of_followup": "string",
      "lost_to_followup_reason": "Completed study",
      "disease_status_at_followup": "Complete remission",
      "relapse_type": "Distant recurrence/metastasis",
      "date_of_relapse": "string",
      "method_of_progression_status": "Imaging (procedure)",
      "anatomic_site_progression_or_recurrence": "string",
      "recurrence_tumour_staging_system": "AJCC 8th edition",
      "recurrence_t_category": "T0",
      "recurrence_n_category": "N0",
      "recurrence_m_category": "M0",
      "recurrence_stage_group": "Occult Carcinoma",
      "lost_to_followup": true,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}
```

## model_follow_ups_create

<a id="opIdmodel_follow_ups_create"></a>

`POST /moh/v1/model/follow_ups/`

<h3 id="model_follow_ups_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[FollowUpRequest](#schemafollowuprequest)|true|none|

> Example responses

> 201 Response

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": "string",
  "lost_to_followup_reason": "Completed study",
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": "string",
  "method_of_progression_status": "Imaging (procedure)",
  "anatomic_site_progression_or_recurrence": "string",
  "recurrence_tumour_staging_system": "AJCC 8th edition",
  "recurrence_t_category": "T0",
  "recurrence_n_category": "N0",
  "recurrence_m_category": "M0",
  "recurrence_stage_group": "Occult Carcinoma",
  "lost_to_followup": true,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_follow_ups_retrieve

<a id="opIdmodel_follow_ups_retrieve"></a>

`GET /moh/v1/model/follow_ups/{submitter_follow_up_id}/`

<h3 id="model_follow_ups_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_follow_up_id|path|string|true|A unique value identifying this follow up.|

> Example responses

> 200 Response

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": "string",
  "lost_to_followup_reason": "Completed study",
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": "string",
  "method_of_progression_status": "Imaging (procedure)",
  "anatomic_site_progression_or_recurrence": "string",
  "recurrence_tumour_staging_system": "AJCC 8th edition",
  "recurrence_t_category": "T0",
  "recurrence_n_category": "N0",
  "recurrence_m_category": "M0",
  "recurrence_stage_group": "Occult Carcinoma",
  "lost_to_followup": true,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_follow_ups_update

<a id="opIdmodel_follow_ups_update"></a>

`PUT /moh/v1/model/follow_ups/{submitter_follow_up_id}/`

<h3 id="model_follow_ups_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_follow_up_id|path|string|true|A unique value identifying this follow up.|
|body|body|[FollowUpRequest](#schemafollowuprequest)|true|none|

> Example responses

> 200 Response

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": "string",
  "lost_to_followup_reason": "Completed study",
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": "string",
  "method_of_progression_status": "Imaging (procedure)",
  "anatomic_site_progression_or_recurrence": "string",
  "recurrence_tumour_staging_system": "AJCC 8th edition",
  "recurrence_t_category": "T0",
  "recurrence_n_category": "N0",
  "recurrence_m_category": "M0",
  "recurrence_stage_group": "Occult Carcinoma",
  "lost_to_followup": true,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_follow_ups_partial_update

<a id="opIdmodel_follow_ups_partial_update"></a>

`PATCH /moh/v1/model/follow_ups/{submitter_follow_up_id}/`

<h3 id="model_follow_ups_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_follow_up_id|path|string|true|A unique value identifying this follow up.|
|body|body|[PatchedFollowUpRequest](#schemapatchedfollowuprequest)|false|none|

> Example responses

> 200 Response

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": "string",
  "lost_to_followup_reason": "Completed study",
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": "string",
  "method_of_progression_status": "Imaging (procedure)",
  "anatomic_site_progression_or_recurrence": "string",
  "recurrence_tumour_staging_system": "AJCC 8th edition",
  "recurrence_t_category": "T0",
  "recurrence_n_category": "N0",
  "recurrence_m_category": "M0",
  "recurrence_stage_group": "Occult Carcinoma",
  "lost_to_followup": true,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_follow_ups_destroy

<a id="opIdmodel_follow_ups_destroy"></a>

`DELETE /moh/v1/model/follow_ups/{submitter_follow_up_id}/`

<h3 id="model_follow_ups_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_follow_up_id|path|string|true|A unique value identifying this follow up.|

## model_hormone_therapies_list

<a id="opIdmodel_hormone_therapies_list"></a>

`GET /moh/v1/model/hormone_therapies/`

<h3 id="model_hormone_therapies_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|drug_name|query|string|false|none|
|drug_rxnormcui|query|string|false|none|
|hormone_drug_dosage_units|query|string|false|none|
|cumulative_drug_dosage_prescribed|query|integer|false|none|
|cumulative_drug_dosage_actual|query|integer|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "hormone_drug_dosage_units": "mg/m2",
      "drug_name": "string",
      "drug_rxnormcui": "string",
      "cumulative_drug_dosage_prescribed": 32767,
      "cumulative_drug_dosage_actual": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}
```

## model_hormone_therapies_create

<a id="opIdmodel_hormone_therapies_create"></a>

`POST /moh/v1/model/hormone_therapies/`

<h3 id="model_hormone_therapies_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[HormoneTherapyRequest](#schemahormonetherapyrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "hormone_drug_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_hormone_therapies_retrieve

<a id="opIdmodel_hormone_therapies_retrieve"></a>

`GET /moh/v1/model/hormone_therapies/{id}/`

<h3 id="model_hormone_therapies_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this hormone therapy.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "hormone_drug_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_hormone_therapies_update

<a id="opIdmodel_hormone_therapies_update"></a>

`PUT /moh/v1/model/hormone_therapies/{id}/`

<h3 id="model_hormone_therapies_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this hormone therapy.|
|body|body|[HormoneTherapyRequest](#schemahormonetherapyrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "hormone_drug_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_hormone_therapies_partial_update

<a id="opIdmodel_hormone_therapies_partial_update"></a>

`PATCH /moh/v1/model/hormone_therapies/{id}/`

<h3 id="model_hormone_therapies_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this hormone therapy.|
|body|body|[PatchedHormoneTherapyRequest](#schemapatchedhormonetherapyrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "hormone_drug_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_hormone_therapies_destroy

<a id="opIdmodel_hormone_therapies_destroy"></a>

`DELETE /moh/v1/model/hormone_therapies/{id}/`

<h3 id="model_hormone_therapies_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this hormone therapy.|

## model_immunotherapies_list

<a id="opIdmodel_immunotherapies_list"></a>

`GET /moh/v1/model/immunotherapies/`

<h3 id="model_immunotherapies_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|immunotherapy_type|query|string|false|none|
|drug_name|query|string|false|none|
|drug_rxnormcui|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "immunotherapy_type": "Cell-based",
      "drug_name": "string",
      "drug_rxnormcui": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}
```

## model_immunotherapies_create

<a id="opIdmodel_immunotherapies_create"></a>

`POST /moh/v1/model/immunotherapies/`

<h3 id="model_immunotherapies_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ImmunotherapyRequest](#schemaimmunotherapyrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "immunotherapy_type": "Cell-based",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_immunotherapies_retrieve

<a id="opIdmodel_immunotherapies_retrieve"></a>

`GET /moh/v1/model/immunotherapies/{id}/`

<h3 id="model_immunotherapies_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this immunotherapy.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "immunotherapy_type": "Cell-based",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_immunotherapies_update

<a id="opIdmodel_immunotherapies_update"></a>

`PUT /moh/v1/model/immunotherapies/{id}/`

<h3 id="model_immunotherapies_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this immunotherapy.|
|body|body|[ImmunotherapyRequest](#schemaimmunotherapyrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "immunotherapy_type": "Cell-based",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_immunotherapies_partial_update

<a id="opIdmodel_immunotherapies_partial_update"></a>

`PATCH /moh/v1/model/immunotherapies/{id}/`

<h3 id="model_immunotherapies_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this immunotherapy.|
|body|body|[PatchedImmunotherapyRequest](#schemapatchedimmunotherapyrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "immunotherapy_type": "Cell-based",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_immunotherapies_destroy

<a id="opIdmodel_immunotherapies_destroy"></a>

`DELETE /moh/v1/model/immunotherapies/{id}/`

<h3 id="model_immunotherapies_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this immunotherapy.|

## model_primary_diagnoses_list

<a id="opIdmodel_primary_diagnoses_list"></a>

`GET /moh/v1/model/primary_diagnoses/`

<h3 id="model_primary_diagnoses_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|date_of_diagnosis|query|string|false|none|
|cancer_type_code|query|string|false|none|
|basis_of_diagnosis|query|string|false|none|
|lymph_nodes_examined_status|query|string|false|none|
|lymph_nodes_examined_method|query|string|false|none|
|number_lymph_nodes_positive|query|integer|false|none|
|clinical_tumour_staging_system|query|string|false|none|
|clinical_t_category|query|string|false|none|
|clinical_n_category|query|string|false|none|
|clinical_m_category|query|string|false|none|
|clinical_stage_group|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_primary_diagnosis_id": "string",
      "date_of_diagnosis": "string",
      "basis_of_diagnosis": "Clinical investigation",
      "lymph_nodes_examined_status": "Cannot be determined",
      "lymph_nodes_examined_method": "Imaging",
      "clinical_tumour_staging_system": "AJCC 8th edition",
      "clinical_t_category": "T0",
      "clinical_n_category": "N0",
      "clinical_m_category": "M0",
      "clinical_stage_group": "Occult Carcinoma",
      "cancer_type_code": "string",
      "number_lymph_nodes_positive": 32767,
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ]
}
```

## model_primary_diagnoses_create

<a id="opIdmodel_primary_diagnoses_create"></a>

`POST /moh/v1/model/primary_diagnoses/`

<h3 id="model_primary_diagnoses_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PrimaryDiagnosisRequest](#schemaprimarydiagnosisrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "submitter_primary_diagnosis_id": "string",
  "date_of_diagnosis": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "lymph_nodes_examined_status": "Cannot be determined",
  "lymph_nodes_examined_method": "Imaging",
  "clinical_tumour_staging_system": "AJCC 8th edition",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Occult Carcinoma",
  "cancer_type_code": "string",
  "number_lymph_nodes_positive": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}
```

## model_primary_diagnoses_retrieve

<a id="opIdmodel_primary_diagnoses_retrieve"></a>

`GET /moh/v1/model/primary_diagnoses/{submitter_primary_diagnosis_id}/`

<h3 id="model_primary_diagnoses_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|path|string|true|A unique value identifying this primary diagnosis.|

> Example responses

> 200 Response

```json
{
  "submitter_primary_diagnosis_id": "string",
  "date_of_diagnosis": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "lymph_nodes_examined_status": "Cannot be determined",
  "lymph_nodes_examined_method": "Imaging",
  "clinical_tumour_staging_system": "AJCC 8th edition",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Occult Carcinoma",
  "cancer_type_code": "string",
  "number_lymph_nodes_positive": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}
```

## model_primary_diagnoses_update

<a id="opIdmodel_primary_diagnoses_update"></a>

`PUT /moh/v1/model/primary_diagnoses/{submitter_primary_diagnosis_id}/`

<h3 id="model_primary_diagnoses_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|path|string|true|A unique value identifying this primary diagnosis.|
|body|body|[PrimaryDiagnosisRequest](#schemaprimarydiagnosisrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "submitter_primary_diagnosis_id": "string",
  "date_of_diagnosis": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "lymph_nodes_examined_status": "Cannot be determined",
  "lymph_nodes_examined_method": "Imaging",
  "clinical_tumour_staging_system": "AJCC 8th edition",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Occult Carcinoma",
  "cancer_type_code": "string",
  "number_lymph_nodes_positive": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}
```

## model_primary_diagnoses_partial_update

<a id="opIdmodel_primary_diagnoses_partial_update"></a>

`PATCH /moh/v1/model/primary_diagnoses/{submitter_primary_diagnosis_id}/`

<h3 id="model_primary_diagnoses_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|path|string|true|A unique value identifying this primary diagnosis.|
|body|body|[PatchedPrimaryDiagnosisRequest](#schemapatchedprimarydiagnosisrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "submitter_primary_diagnosis_id": "string",
  "date_of_diagnosis": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "lymph_nodes_examined_status": "Cannot be determined",
  "lymph_nodes_examined_method": "Imaging",
  "clinical_tumour_staging_system": "AJCC 8th edition",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Occult Carcinoma",
  "cancer_type_code": "string",
  "number_lymph_nodes_positive": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}
```

## model_primary_diagnoses_destroy

<a id="opIdmodel_primary_diagnoses_destroy"></a>

`DELETE /moh/v1/model/primary_diagnoses/{submitter_primary_diagnosis_id}/`

<h3 id="model_primary_diagnoses_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|path|string|true|A unique value identifying this primary diagnosis.|

## model_programs_list

<a id="opIdmodel_programs_list"></a>

`GET /moh/v1/model/programs/`

<h3 id="model_programs_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|name|query|string|false|none|
|created|query|string(date-time)|false|none|
|updated|query|string(date-time)|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "program_id": "string",
      "name": "string",
      "created": "2019-08-24T14:15:22Z",
      "updated": "2019-08-24T14:15:22Z"
    }
  ]
}
```

## model_programs_create

<a id="opIdmodel_programs_create"></a>

`POST /moh/v1/model/programs/`

<h3 id="model_programs_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ProgramRequest](#schemaprogramrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "program_id": "string",
  "name": "string",
  "created": "2019-08-24T14:15:22Z",
  "updated": "2019-08-24T14:15:22Z"
}
```

## model_programs_retrieve

<a id="opIdmodel_programs_retrieve"></a>

`GET /moh/v1/model/programs/{program_id}/`

<h3 id="model_programs_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|path|string|true|A unique value identifying this program.|

> Example responses

> 200 Response

```json
{
  "program_id": "string",
  "name": "string",
  "created": "2019-08-24T14:15:22Z",
  "updated": "2019-08-24T14:15:22Z"
}
```

## model_programs_update

<a id="opIdmodel_programs_update"></a>

`PUT /moh/v1/model/programs/{program_id}/`

<h3 id="model_programs_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|path|string|true|A unique value identifying this program.|
|body|body|[ProgramRequest](#schemaprogramrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "program_id": "string",
  "name": "string",
  "created": "2019-08-24T14:15:22Z",
  "updated": "2019-08-24T14:15:22Z"
}
```

## model_programs_partial_update

<a id="opIdmodel_programs_partial_update"></a>

`PATCH /moh/v1/model/programs/{program_id}/`

<h3 id="model_programs_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|path|string|true|A unique value identifying this program.|
|body|body|[PatchedProgramRequest](#schemapatchedprogramrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "program_id": "string",
  "name": "string",
  "created": "2019-08-24T14:15:22Z",
  "updated": "2019-08-24T14:15:22Z"
}
```

## model_programs_destroy

<a id="opIdmodel_programs_destroy"></a>

`DELETE /moh/v1/model/programs/{program_id}/`

<h3 id="model_programs_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|path|string|true|A unique value identifying this program.|

## model_radiations_list

<a id="opIdmodel_radiations_list"></a>

`GET /moh/v1/model/radiations/`

<h3 id="model_radiations_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|radiation_therapy_modality|query|string|false|none|
|radiation_therapy_type|query|string|false|none|
|radiation_therapy_fractions|query|integer|false|none|
|radiation_therapy_dosage|query|integer|false|none|
|anatomical_site_irradiated|query|string|false|none|
|radiation_boost|query|boolean|false|none|
|reference_radiation_treatment_id|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
      "radiation_therapy_type": "External",
      "anatomical_site_irradiated": "Cervical lymph node group",
      "radiation_therapy_fractions": 32767,
      "radiation_therapy_dosage": 32767,
      "radiation_boost": true,
      "reference_radiation_treatment_id": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}
```

## model_radiations_create

<a id="opIdmodel_radiations_create"></a>

`POST /moh/v1/model/radiations/`

<h3 id="model_radiations_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RadiationRequest](#schemaradiationrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "anatomical_site_irradiated": "Cervical lymph node group",
  "radiation_therapy_fractions": 32767,
  "radiation_therapy_dosage": 32767,
  "radiation_boost": true,
  "reference_radiation_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_radiations_retrieve

<a id="opIdmodel_radiations_retrieve"></a>

`GET /moh/v1/model/radiations/{id}/`

<h3 id="model_radiations_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this radiation.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "anatomical_site_irradiated": "Cervical lymph node group",
  "radiation_therapy_fractions": 32767,
  "radiation_therapy_dosage": 32767,
  "radiation_boost": true,
  "reference_radiation_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_radiations_update

<a id="opIdmodel_radiations_update"></a>

`PUT /moh/v1/model/radiations/{id}/`

<h3 id="model_radiations_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this radiation.|
|body|body|[RadiationRequest](#schemaradiationrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "anatomical_site_irradiated": "Cervical lymph node group",
  "radiation_therapy_fractions": 32767,
  "radiation_therapy_dosage": 32767,
  "radiation_boost": true,
  "reference_radiation_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_radiations_partial_update

<a id="opIdmodel_radiations_partial_update"></a>

`PATCH /moh/v1/model/radiations/{id}/`

<h3 id="model_radiations_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this radiation.|
|body|body|[PatchedRadiationRequest](#schemapatchedradiationrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "anatomical_site_irradiated": "Cervical lymph node group",
  "radiation_therapy_fractions": 32767,
  "radiation_therapy_dosage": 32767,
  "radiation_boost": true,
  "reference_radiation_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_radiations_destroy

<a id="opIdmodel_radiations_destroy"></a>

`DELETE /moh/v1/model/radiations/{id}/`

<h3 id="model_radiations_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this radiation.|

## model_sample_registrations_list

<a id="opIdmodel_sample_registrations_list"></a>

`GET /moh/v1/model/sample_registrations/`

<h3 id="model_sample_registrations_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_sample_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_specimen_id|query|string|false|none|
|gender|query|string|false|none|
|sex_at_birth|query|string|false|none|
|specimen_tissue_source|query|string|false|none|
|tumour_normal_designation|query|string|false|none|
|specimen_type|query|string|false|none|
|sample_type|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_sample_id": "string",
      "gender": "Man",
      "sex_at_birth": "Male",
      "specimen_tissue_source": "Amniotic fluid",
      "tumour_normal_designation": "Normal",
      "specimen_type": "Cell line - derived from normal",
      "sample_type": "Amplified DNA",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_specimen_id": "string"
    }
  ]
}
```

## model_sample_registrations_create

<a id="opIdmodel_sample_registrations_create"></a>

`POST /moh/v1/model/sample_registrations/`

<h3 id="model_sample_registrations_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SampleRegistrationRequest](#schemasampleregistrationrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "submitter_sample_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "specimen_tissue_source": "Amniotic fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "sample_type": "Amplified DNA",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string"
}
```

## model_sample_registrations_retrieve

<a id="opIdmodel_sample_registrations_retrieve"></a>

`GET /moh/v1/model/sample_registrations/{submitter_sample_id}/`

<h3 id="model_sample_registrations_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_sample_id|path|string|true|A unique value identifying this sample registration.|

> Example responses

> 200 Response

```json
{
  "submitter_sample_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "specimen_tissue_source": "Amniotic fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "sample_type": "Amplified DNA",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string"
}
```

## model_sample_registrations_update

<a id="opIdmodel_sample_registrations_update"></a>

`PUT /moh/v1/model/sample_registrations/{submitter_sample_id}/`

<h3 id="model_sample_registrations_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_sample_id|path|string|true|A unique value identifying this sample registration.|
|body|body|[SampleRegistrationRequest](#schemasampleregistrationrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "submitter_sample_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "specimen_tissue_source": "Amniotic fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "sample_type": "Amplified DNA",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string"
}
```

## model_sample_registrations_partial_update

<a id="opIdmodel_sample_registrations_partial_update"></a>

`PATCH /moh/v1/model/sample_registrations/{submitter_sample_id}/`

<h3 id="model_sample_registrations_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_sample_id|path|string|true|A unique value identifying this sample registration.|
|body|body|[PatchedSampleRegistrationRequest](#schemapatchedsampleregistrationrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "submitter_sample_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "specimen_tissue_source": "Amniotic fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "sample_type": "Amplified DNA",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string"
}
```

## model_sample_registrations_destroy

<a id="opIdmodel_sample_registrations_destroy"></a>

`DELETE /moh/v1/model/sample_registrations/{submitter_sample_id}/`

<h3 id="model_sample_registrations_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_sample_id|path|string|true|A unique value identifying this sample registration.|

## model_specimens_list

<a id="opIdmodel_specimens_list"></a>

`GET /moh/v1/model/specimens/`

<h3 id="model_specimens_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_specimen_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_primary_diagnosis_id|query|string|false|none|
|pathological_tumour_staging_system|query|string|false|none|
|pathological_t_category|query|string|false|none|
|pathological_n_category|query|string|false|none|
|pathological_m_category|query|string|false|none|
|pathological_stage_group|query|string|false|none|
|specimen_collection_date|query|string|false|none|
|specimen_storage|query|string|false|none|
|tumour_histological_type|query|string|false|none|
|specimen_anatomic_location|query|string|false|none|
|reference_pathology_confirmed_diagnosis|query|string|false|none|
|reference_pathology_confirmed_tumour_presence|query|string|false|none|
|tumour_grading_system|query|string|false|none|
|tumour_grade|query|string|false|none|
|percent_tumour_cells_range|query|string|false|none|
|percent_tumour_cells_measurement_method|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_specimen_id": "string",
      "pathological_tumour_staging_system": "AJCC 8th edition",
      "pathological_t_category": "T0",
      "pathological_n_category": "N0",
      "pathological_m_category": "M0",
      "pathological_stage_group": "Occult Carcinoma",
      "specimen_collection_date": "string",
      "specimen_storage": "Cut slide",
      "tumour_histological_type": "string",
      "specimen_anatomic_location": "string",
      "reference_pathology_confirmed_diagnosis": "Yes",
      "reference_pathology_confirmed_tumour_presence": "Yes",
      "tumour_grading_system": "FNCLCC grading system",
      "tumour_grade": "Low grade",
      "percent_tumour_cells_range": "0-19%",
      "percent_tumour_cells_measurement_method": "Genomics",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ]
}
```

## model_specimens_create

<a id="opIdmodel_specimens_create"></a>

`POST /moh/v1/model/specimens/`

<h3 id="model_specimens_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SpecimenRequest](#schemaspecimenrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "submitter_specimen_id": "string",
  "pathological_tumour_staging_system": "AJCC 8th edition",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Occult Carcinoma",
  "specimen_collection_date": "string",
  "specimen_storage": "Cut slide",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}
```

## model_specimens_retrieve

<a id="opIdmodel_specimens_retrieve"></a>

`GET /moh/v1/model/specimens/{submitter_specimen_id}/`

<h3 id="model_specimens_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_specimen_id|path|string|true|A unique value identifying this specimen.|

> Example responses

> 200 Response

```json
{
  "submitter_specimen_id": "string",
  "pathological_tumour_staging_system": "AJCC 8th edition",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Occult Carcinoma",
  "specimen_collection_date": "string",
  "specimen_storage": "Cut slide",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}
```

## model_specimens_update

<a id="opIdmodel_specimens_update"></a>

`PUT /moh/v1/model/specimens/{submitter_specimen_id}/`

<h3 id="model_specimens_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_specimen_id|path|string|true|A unique value identifying this specimen.|
|body|body|[SpecimenRequest](#schemaspecimenrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "submitter_specimen_id": "string",
  "pathological_tumour_staging_system": "AJCC 8th edition",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Occult Carcinoma",
  "specimen_collection_date": "string",
  "specimen_storage": "Cut slide",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}
```

## model_specimens_partial_update

<a id="opIdmodel_specimens_partial_update"></a>

`PATCH /moh/v1/model/specimens/{submitter_specimen_id}/`

<h3 id="model_specimens_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_specimen_id|path|string|true|A unique value identifying this specimen.|
|body|body|[PatchedSpecimenRequest](#schemapatchedspecimenrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "submitter_specimen_id": "string",
  "pathological_tumour_staging_system": "AJCC 8th edition",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Occult Carcinoma",
  "specimen_collection_date": "string",
  "specimen_storage": "Cut slide",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}
```

## model_specimens_destroy

<a id="opIdmodel_specimens_destroy"></a>

`DELETE /moh/v1/model/specimens/{submitter_specimen_id}/`

<h3 id="model_specimens_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_specimen_id|path|string|true|A unique value identifying this specimen.|

## model_surgeries_list

<a id="opIdmodel_surgeries_list"></a>

`GET /moh/v1/model/surgeries/`

<h3 id="model_surgeries_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_specimen_id|query|string|false|none|
|submitter_treatment_id|query|string|false|none|
|surgery_type|query|string|false|none|
|surgery_site|query|string|false|none|
|surgery_location|query|string|false|none|
|tumour_length|query|integer|false|none|
|tumour_width|query|integer|false|none|
|greatest_dimension_tumour|query|integer|false|none|
|tumour_focality|query|string|false|none|
|residual_tumour_classification|query|string|false|none|
|margin_types_involved|query|string|false|none|
|margin_types_not_involved|query|string|false|none|
|margin_types_not_assessed|query|string|false|none|
|lymphovascular_invasion|query|string|false|none|
|perineural_invasion|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "surgery_type": "Axillary Clearance",
      "surgery_site": "string",
      "surgery_location": "Local recurrence",
      "tumour_focality": "Cannot be assessed",
      "residual_tumour_classification": "Not applicable",
      "margin_types_involved": [
        "Circumferential resection margin"
      ],
      "margin_types_not_involved": [
        "Circumferential resection margin"
      ],
      "margin_types_not_assessed": [
        "Circumferential resection margin"
      ],
      "lymphovascular_invasion": "Absent",
      "perineural_invasion": "Absent",
      "tumour_length": 32767,
      "tumour_width": 32767,
      "greatest_dimension_tumour": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_specimen_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}
```

## model_surgeries_create

<a id="opIdmodel_surgeries_create"></a>

`POST /moh/v1/model/surgeries/`

<h3 id="model_surgeries_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SurgeryRequest](#schemasurgeryrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "surgery_type": "Axillary Clearance",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margin_types_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_assessed": [
    "Circumferential resection margin"
  ],
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "tumour_length": 32767,
  "tumour_width": 32767,
  "greatest_dimension_tumour": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_surgeries_retrieve

<a id="opIdmodel_surgeries_retrieve"></a>

`GET /moh/v1/model/surgeries/{id}/`

<h3 id="model_surgeries_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this surgery.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "surgery_type": "Axillary Clearance",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margin_types_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_assessed": [
    "Circumferential resection margin"
  ],
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "tumour_length": 32767,
  "tumour_width": 32767,
  "greatest_dimension_tumour": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_surgeries_update

<a id="opIdmodel_surgeries_update"></a>

`PUT /moh/v1/model/surgeries/{id}/`

<h3 id="model_surgeries_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this surgery.|
|body|body|[SurgeryRequest](#schemasurgeryrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "surgery_type": "Axillary Clearance",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margin_types_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_assessed": [
    "Circumferential resection margin"
  ],
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "tumour_length": 32767,
  "tumour_width": 32767,
  "greatest_dimension_tumour": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_surgeries_partial_update

<a id="opIdmodel_surgeries_partial_update"></a>

`PATCH /moh/v1/model/surgeries/{id}/`

<h3 id="model_surgeries_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this surgery.|
|body|body|[PatchedSurgeryRequest](#schemapatchedsurgeryrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "surgery_type": "Axillary Clearance",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margin_types_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_assessed": [
    "Circumferential resection margin"
  ],
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "tumour_length": 32767,
  "tumour_width": 32767,
  "greatest_dimension_tumour": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string"
}
```

## model_surgeries_destroy

<a id="opIdmodel_surgeries_destroy"></a>

`DELETE /moh/v1/model/surgeries/{id}/`

<h3 id="model_surgeries_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this surgery.|

## model_treatments_list

<a id="opIdmodel_treatments_list"></a>

`GET /moh/v1/model/treatments/`

<h3 id="model_treatments_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_treatment_id|query|string|false|none|
|program_id|query|string|false|none|
|submitter_donor_id|query|string|false|none|
|submitter_primary_diagnosis_id|query|string|false|none|
|treatment_type|query|string|false|none|
|is_primary_treatment|query|string|false|none|
|treatment_start_date|query|string|false|none|
|treatment_end_date|query|string|false|none|
|treatment_setting|query|string|false|none|
|treatment_intent|query|string|false|none|
|days_per_cycle|query|integer|false|none|
|number_of_cycles|query|integer|false|none|
|response_to_treatment_criteria_method|query|string|false|none|
|response_to_treatment|query|string|false|none|
|page|query|integer|false|A page number within the paginated result set.|
|page_size|query|integer|false|Number of results to return per page.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_treatment_id": "string",
      "treatment_type": [
        "Ablation"
      ],
      "is_primary_treatment": "Yes",
      "treatment_start_date": "string",
      "treatment_end_date": "string",
      "treatment_setting": "Adjuvant",
      "treatment_intent": "Curative",
      "response_to_treatment_criteria_method": "RECIST 1.1",
      "response_to_treatment": "Complete response",
      "days_per_cycle": 32767,
      "number_of_cycles": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ]
}
```

## model_treatments_create

<a id="opIdmodel_treatments_create"></a>

`POST /moh/v1/model/treatments/`

<h3 id="model_treatments_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TreatmentRequest](#schematreatmentrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Ablation"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": "string",
  "treatment_end_date": "string",
  "treatment_setting": "Adjuvant",
  "treatment_intent": "Curative",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "days_per_cycle": 32767,
  "number_of_cycles": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}
```

## model_treatments_retrieve

<a id="opIdmodel_treatments_retrieve"></a>

`GET /moh/v1/model/treatments/{submitter_treatment_id}/`

<h3 id="model_treatments_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_treatment_id|path|string|true|A unique value identifying this treatment.|

> Example responses

> 200 Response

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Ablation"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": "string",
  "treatment_end_date": "string",
  "treatment_setting": "Adjuvant",
  "treatment_intent": "Curative",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "days_per_cycle": 32767,
  "number_of_cycles": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}
```

## model_treatments_update

<a id="opIdmodel_treatments_update"></a>

`PUT /moh/v1/model/treatments/{submitter_treatment_id}/`

<h3 id="model_treatments_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_treatment_id|path|string|true|A unique value identifying this treatment.|
|body|body|[TreatmentRequest](#schematreatmentrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Ablation"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": "string",
  "treatment_end_date": "string",
  "treatment_setting": "Adjuvant",
  "treatment_intent": "Curative",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "days_per_cycle": 32767,
  "number_of_cycles": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}
```

## model_treatments_partial_update

<a id="opIdmodel_treatments_partial_update"></a>

`PATCH /moh/v1/model/treatments/{submitter_treatment_id}/`

<h3 id="model_treatments_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_treatment_id|path|string|true|A unique value identifying this treatment.|
|body|body|[PatchedTreatmentRequest](#schemapatchedtreatmentrequest)|false|none|

> Example responses

> 200 Response

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Ablation"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": "string",
  "treatment_end_date": "string",
  "treatment_setting": "Adjuvant",
  "treatment_intent": "Curative",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "days_per_cycle": 32767,
  "number_of_cycles": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}
```

## model_treatments_destroy

<a id="opIdmodel_treatments_destroy"></a>

`DELETE /moh/v1/model/treatments/{submitter_treatment_id}/`

<h3 id="model_treatments_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|submitter_treatment_id|path|string|true|A unique value identifying this treatment.|

# Schemas

<h2 id="tocS_AnatomicalSiteIrradiatedEnum">AnatomicalSiteIrradiatedEnum</h2>

<a id="schemaanatomicalsiteirradiatedenum"></a>
<a id="schema_AnatomicalSiteIrradiatedEnum"></a>
<a id="tocSanatomicalsiteirradiatedenum"></a>
<a id="tocsanatomicalsiteirradiatedenum"></a>

```json
"Cervical lymph node group"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Cervical lymph node group|
|*anonymous*|Entire lymph node of thorax|
|*anonymous*|Axillary lymph node group|
|*anonymous*|Supraclavicular lymph node group|
|*anonymous*|Internal mammary lymph node group|
|*anonymous*|Abdominal lymph node group|
|*anonymous*|Pelvic lymph node group|
|*anonymous*|Structure of lymph node|
|*anonymous*|Entire eye|
|*anonymous*|Pituitary structure|
|*anonymous*|Brain structure|
|*anonymous*|Brain part|
|*anonymous*|Spinal cord structure|
|*anonymous*|Nasopharyngeal structure|
|*anonymous*|Oral cavity structure|
|*anonymous*|Oropharyngeal structure|
|*anonymous*|Laryngeal structure|
|*anonymous*|Hypopharyngeal structure|
|*anonymous*|Nasal sinus structure|
|*anonymous*|Salivary gland structure|
|*anonymous*|Thyroid structure|
|*anonymous*|Entire head and neck|
|*anonymous*|Entire lung|
|*anonymous*|Mesothelium structure|
|*anonymous*|Entire thorax|
|*anonymous*|Entire breast|
|*anonymous*|Breast part|
|*anonymous*|Chest wall structure|
|*anonymous*|Entire esophagus|
|*anonymous*|Stomach structure|
|*anonymous*|Small intestinal structure|
|*anonymous*|Colon structure|
|*anonymous*|Rectum structure|
|*anonymous*|Anal structure|
|*anonymous*|Liver structure|
|*anonymous*|Biliary tract structure|
|*anonymous*|Gallbladder structure|
|*anonymous*|Pancreatic structure|
|*anonymous*|Abdominal structure|
|*anonymous*|Entire urinary bladder|
|*anonymous*|Bladder part|
|*anonymous*|Kidney structure|
|*anonymous*|Ureteric structure|
|*anonymous*|Entire prostate|
|*anonymous*|Prostate part|
|*anonymous*|Urethral structure|
|*anonymous*|Penile structure|
|*anonymous*|Testis structure|
|*anonymous*|Scrotal structure|
|*anonymous*|Ovarian structure|
|*anonymous*|Fallopian tube structure|
|*anonymous*|Uterine structure|
|*anonymous*|Cervix uteri structure|
|*anonymous*|Vaginal structure|
|*anonymous*|Vulval structure|
|*anonymous*|Bone structure of cranium|
|*anonymous*|Entire vertebral column|
|*anonymous*|Shoulder region structure|
|*anonymous*|Bone structure of rib|
|*anonymous*|Hip region structure|
|*anonymous*|Entire bony pelvis|
|*anonymous*|Pelvic structure|
|*anonymous*|Bone structure of extremity|
|*anonymous*|Skin structure|
|*anonymous*|Soft tissues|
|*anonymous*|Entire body as a whole|

<h2 id="tocS_BasisOfDiagnosisEnum">BasisOfDiagnosisEnum</h2>

<a id="schemabasisofdiagnosisenum"></a>
<a id="schema_BasisOfDiagnosisEnum"></a>
<a id="tocSbasisofdiagnosisenum"></a>
<a id="tocsbasisofdiagnosisenum"></a>

```json
"Clinical investigation"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Clinical investigation|
|*anonymous*|Clinical|
|*anonymous*|Cytology|
|*anonymous*|Death certificate only|
|*anonymous*|Histology of a metastasis|
|*anonymous*|Histology of a primary tumour|
|*anonymous*|Specific tumour markers|
|*anonymous*|Unknown|

<h2 id="tocS_Biomarker">Biomarker</h2>

<a id="schemabiomarker"></a>
<a id="schema_Biomarker"></a>
<a id="tocSbiomarker"></a>
<a id="tocsbiomarker"></a>

```json
{
  "id": 0,
  "test_interval": 32767,
  "psa_level": 32767,
  "ca125": 32767,
  "cea": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|test_interval|integer¦null|false|none|none|
|psa_level|integer¦null|false|none|none|
|ca125|integer¦null|false|none|none|
|cea|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_specimen_id|string¦null|false|none|none|
|submitter_primary_diagnosis_id|string¦null|false|none|none|
|submitter_treatment_id|string¦null|false|none|none|
|submitter_follow_up_id|string¦null|false|none|none|

<h2 id="tocS_BiomarkerRequest">BiomarkerRequest</h2>

<a id="schemabiomarkerrequest"></a>
<a id="schema_BiomarkerRequest"></a>
<a id="tocSbiomarkerrequest"></a>
<a id="tocsbiomarkerrequest"></a>

```json
{
  "test_interval": 32767,
  "psa_level": 32767,
  "ca125": 32767,
  "cea": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|test_interval|integer¦null|false|none|none|
|psa_level|integer¦null|false|none|none|
|ca125|integer¦null|false|none|none|
|cea|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_specimen_id|string¦null|false|none|none|
|submitter_primary_diagnosis_id|string¦null|false|none|none|
|submitter_treatment_id|string¦null|false|none|none|
|submitter_follow_up_id|string¦null|false|none|none|

<h2 id="tocS_BlankEnum">BlankEnum</h2>

<a id="schemablankenum"></a>
<a id="schema_BlankEnum"></a>
<a id="tocSblankenum"></a>
<a id="tocsblankenum"></a>

```json
""

```

### Properties

*None*

<h2 id="tocS_CauseOfDeathEnum">CauseOfDeathEnum</h2>

<a id="schemacauseofdeathenum"></a>
<a id="schema_CauseOfDeathEnum"></a>
<a id="tocScauseofdeathenum"></a>
<a id="tocscauseofdeathenum"></a>

```json
"Died of cancer"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Died of cancer|
|*anonymous*|Died of other reasons|
|*anonymous*|Unknown|

<h2 id="tocS_Chemotherapy">Chemotherapy</h2>

<a id="schemachemotherapy"></a>
<a id="schema_Chemotherapy"></a>
<a id="tocSchemotherapy"></a>
<a id="tocschemotherapy"></a>

```json
{
  "id": 0,
  "chemotherapy_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|chemotherapy_dosage_units|[DosageUnitsEnum](#schemadosageunitsenum)|true|none|none|
|drug_name|string|true|none|none|
|drug_rxnormcui|string|true|none|none|
|cumulative_drug_dosage_prescribed|integer¦null|false|none|none|
|cumulative_drug_dosage_actual|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_ChemotherapyRequest">ChemotherapyRequest</h2>

<a id="schemachemotherapyrequest"></a>
<a id="schema_ChemotherapyRequest"></a>
<a id="tocSchemotherapyrequest"></a>
<a id="tocschemotherapyrequest"></a>

```json
{
  "chemotherapy_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|chemotherapy_dosage_units|[DosageUnitsEnum](#schemadosageunitsenum)|true|none|none|
|drug_name|string|true|none|none|
|drug_rxnormcui|string|true|none|none|
|cumulative_drug_dosage_prescribed|integer¦null|false|none|none|
|cumulative_drug_dosage_actual|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_Comorbidity">Comorbidity</h2>

<a id="schemacomorbidity"></a>
<a id="schema_Comorbidity"></a>
<a id="tocScomorbidity"></a>
<a id="tocscomorbidity"></a>

```json
{
  "id": 0,
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string",
  "age_at_comorbidity_diagnosis": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|prior_malignancy|[uBooleanEnum](#schemaubooleanenum)|true|none|none|
|laterality_of_prior_malignancy|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LateralityOfPriorMalignancyEnum](#schemalateralityofpriormalignancyenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_type_code|string|true|none|none|
|comorbidity_treatment_status|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment|string|true|none|none|
|age_at_comorbidity_diagnosis|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|

<h2 id="tocS_ComorbidityRequest">ComorbidityRequest</h2>

<a id="schemacomorbidityrequest"></a>
<a id="schema_ComorbidityRequest"></a>
<a id="tocScomorbidityrequest"></a>
<a id="tocscomorbidityrequest"></a>

```json
{
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string",
  "age_at_comorbidity_diagnosis": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prior_malignancy|[uBooleanEnum](#schemaubooleanenum)|true|none|none|
|laterality_of_prior_malignancy|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LateralityOfPriorMalignancyEnum](#schemalateralityofpriormalignancyenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_type_code|string|true|none|none|
|comorbidity_treatment_status|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment|string|true|none|none|
|age_at_comorbidity_diagnosis|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|

<h2 id="tocS_Discovery">Discovery</h2>

<a id="schemadiscovery"></a>
<a id="schema_Discovery"></a>
<a id="tocSdiscovery"></a>
<a id="tocsdiscovery"></a>

```json
{
  "discovery_count": 0
}

```

This serializer is used to return the discovery_count.
It also override the list serializer to a single object

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|discovery_count|integer|true|none|none|

<h2 id="tocS_DiseaseStatusAtFollowupEnum">DiseaseStatusAtFollowupEnum</h2>

<a id="schemadiseasestatusatfollowupenum"></a>
<a id="schema_DiseaseStatusAtFollowupEnum"></a>
<a id="tocSdiseasestatusatfollowupenum"></a>
<a id="tocsdiseasestatusatfollowupenum"></a>

```json
"Complete remission"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Complete remission|
|*anonymous*|Distant progression|
|*anonymous*|Loco-regional progression|
|*anonymous*|No evidence of disease|
|*anonymous*|Partial remission|
|*anonymous*|Progression NOS|
|*anonymous*|Relapse or recurrence|
|*anonymous*|Stable|

<h2 id="tocS_Donor">Donor</h2>

<a id="schemadonor"></a>
<a id="schema_Donor"></a>
<a id="tocSdonor"></a>
<a id="tocsdonor"></a>

```json
{
  "submitter_donor_id": "string",
  "cause_of_death": "Died of cancer",
  "date_of_birth": "string",
  "date_of_death": "string",
  "primary_site": [
    "Accessory sinuses"
  ],
  "is_deceased": true,
  "program_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|string|true|none|none|
|cause_of_death|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CauseOfDeathEnum](#schemacauseofdeathenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_birth|string|true|none|none|
|date_of_death|string|true|none|none|
|primary_site|[[PrimarySiteEnum](#schemaprimarysiteenum)]|true|none|none|
|is_deceased|boolean|true|none|none|
|program_id|string|true|none|none|

<h2 id="tocS_DonorRequest">DonorRequest</h2>

<a id="schemadonorrequest"></a>
<a id="schema_DonorRequest"></a>
<a id="tocSdonorrequest"></a>
<a id="tocsdonorrequest"></a>

```json
{
  "submitter_donor_id": "string",
  "cause_of_death": "Died of cancer",
  "date_of_birth": "string",
  "date_of_death": "string",
  "primary_site": [
    "Accessory sinuses"
  ],
  "is_deceased": true,
  "program_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|string|true|none|none|
|cause_of_death|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CauseOfDeathEnum](#schemacauseofdeathenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_birth|string|true|none|none|
|date_of_death|string|true|none|none|
|primary_site|[[PrimarySiteEnum](#schemaprimarysiteenum)]|true|none|none|
|is_deceased|boolean|true|none|none|
|program_id|string|true|none|none|

<h2 id="tocS_DosageUnitsEnum">DosageUnitsEnum</h2>

<a id="schemadosageunitsenum"></a>
<a id="schema_DosageUnitsEnum"></a>
<a id="tocSdosageunitsenum"></a>
<a id="tocsdosageunitsenum"></a>

```json
"mg/m2"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|mg/m2|
|*anonymous*|IU/m2|
|*anonymous*|ug/m2|
|*anonymous*|g/m2|
|*anonymous*|mg/kg|

<h2 id="tocS_FollowUp">FollowUp</h2>

<a id="schemafollowup"></a>
<a id="schema_FollowUp"></a>
<a id="tocSfollowup"></a>
<a id="tocsfollowup"></a>

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": "string",
  "lost_to_followup_reason": "Completed study",
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": "string",
  "method_of_progression_status": "Imaging (procedure)",
  "anatomic_site_progression_or_recurrence": "string",
  "recurrence_tumour_staging_system": "AJCC 8th edition",
  "recurrence_t_category": "T0",
  "recurrence_n_category": "N0",
  "recurrence_m_category": "M0",
  "recurrence_stage_group": "Occult Carcinoma",
  "lost_to_followup": true,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|string|true|none|none|
|date_of_followup|string|true|none|none|
|lost_to_followup_reason|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowupReasonEnum](#schemalosttofollowupreasonenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|disease_status_at_followup|[DiseaseStatusAtFollowupEnum](#schemadiseasestatusatfollowupenum)|true|none|none|
|relapse_type|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RelapseTypeEnum](#schemarelapsetypeenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_relapse|string|true|none|none|
|method_of_progression_status|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MethodOfProgressionStatusEnum](#schemamethodofprogressionstatusenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anatomic_site_progression_or_recurrence|string|true|none|none|
|recurrence_tumour_staging_system|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StagingSystemEnum](#schemastagingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_t_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_n_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_m_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_stage_group|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_followup|boolean¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string¦null|false|none|none|
|submitter_treatment_id|string¦null|false|none|none|

<h2 id="tocS_FollowUpRequest">FollowUpRequest</h2>

<a id="schemafollowuprequest"></a>
<a id="schema_FollowUpRequest"></a>
<a id="tocSfollowuprequest"></a>
<a id="tocsfollowuprequest"></a>

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": "string",
  "lost_to_followup_reason": "Completed study",
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": "string",
  "method_of_progression_status": "Imaging (procedure)",
  "anatomic_site_progression_or_recurrence": "string",
  "recurrence_tumour_staging_system": "AJCC 8th edition",
  "recurrence_t_category": "T0",
  "recurrence_n_category": "N0",
  "recurrence_m_category": "M0",
  "recurrence_stage_group": "Occult Carcinoma",
  "lost_to_followup": true,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|string|true|none|none|
|date_of_followup|string|true|none|none|
|lost_to_followup_reason|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowupReasonEnum](#schemalosttofollowupreasonenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|disease_status_at_followup|[DiseaseStatusAtFollowupEnum](#schemadiseasestatusatfollowupenum)|true|none|none|
|relapse_type|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RelapseTypeEnum](#schemarelapsetypeenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_relapse|string|true|none|none|
|method_of_progression_status|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MethodOfProgressionStatusEnum](#schemamethodofprogressionstatusenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anatomic_site_progression_or_recurrence|string|true|none|none|
|recurrence_tumour_staging_system|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StagingSystemEnum](#schemastagingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_t_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_n_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_m_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_stage_group|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_followup|boolean¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string¦null|false|none|none|
|submitter_treatment_id|string¦null|false|none|none|

<h2 id="tocS_GenderEnum">GenderEnum</h2>

<a id="schemagenderenum"></a>
<a id="schema_GenderEnum"></a>
<a id="tocSgenderenum"></a>
<a id="tocsgenderenum"></a>

```json
"Man"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Man|
|*anonymous*|Woman|
|*anonymous*|Non-binary|

<h2 id="tocS_HormoneTherapy">HormoneTherapy</h2>

<a id="schemahormonetherapy"></a>
<a id="schema_HormoneTherapy"></a>
<a id="tocShormonetherapy"></a>
<a id="tocshormonetherapy"></a>

```json
{
  "id": 0,
  "hormone_drug_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|hormone_drug_dosage_units|[DosageUnitsEnum](#schemadosageunitsenum)|true|none|none|
|drug_name|string|true|none|none|
|drug_rxnormcui|string|true|none|none|
|cumulative_drug_dosage_prescribed|integer¦null|false|none|none|
|cumulative_drug_dosage_actual|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_HormoneTherapyRequest">HormoneTherapyRequest</h2>

<a id="schemahormonetherapyrequest"></a>
<a id="schema_HormoneTherapyRequest"></a>
<a id="tocShormonetherapyrequest"></a>
<a id="tocshormonetherapyrequest"></a>

```json
{
  "hormone_drug_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hormone_drug_dosage_units|[DosageUnitsEnum](#schemadosageunitsenum)|true|none|none|
|drug_name|string|true|none|none|
|drug_rxnormcui|string|true|none|none|
|cumulative_drug_dosage_prescribed|integer¦null|false|none|none|
|cumulative_drug_dosage_actual|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_Immunotherapy">Immunotherapy</h2>

<a id="schemaimmunotherapy"></a>
<a id="schema_Immunotherapy"></a>
<a id="tocSimmunotherapy"></a>
<a id="tocsimmunotherapy"></a>

```json
{
  "id": 0,
  "immunotherapy_type": "Cell-based",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|immunotherapy_type|[ImmunotherapyTypeEnum](#schemaimmunotherapytypeenum)|true|none|none|
|drug_name|string|true|none|none|
|drug_rxnormcui|string|true|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_ImmunotherapyRequest">ImmunotherapyRequest</h2>

<a id="schemaimmunotherapyrequest"></a>
<a id="schema_ImmunotherapyRequest"></a>
<a id="tocSimmunotherapyrequest"></a>
<a id="tocsimmunotherapyrequest"></a>

```json
{
  "immunotherapy_type": "Cell-based",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|immunotherapy_type|[ImmunotherapyTypeEnum](#schemaimmunotherapytypeenum)|true|none|none|
|drug_name|string|true|none|none|
|drug_rxnormcui|string|true|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_ImmunotherapyTypeEnum">ImmunotherapyTypeEnum</h2>

<a id="schemaimmunotherapytypeenum"></a>
<a id="schema_ImmunotherapyTypeEnum"></a>
<a id="tocSimmunotherapytypeenum"></a>
<a id="tocsimmunotherapytypeenum"></a>

```json
"Cell-based"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Cell-based|
|*anonymous*|Immune checkpoint inhibitors|
|*anonymous*|Monoclonal antibodies other than immune checkpoint inhibitors|
|*anonymous*|Other immunomodulatory substances|

<h2 id="tocS_LateralityOfPriorMalignancyEnum">LateralityOfPriorMalignancyEnum</h2>

<a id="schemalateralityofpriormalignancyenum"></a>
<a id="schema_LateralityOfPriorMalignancyEnum"></a>
<a id="tocSlateralityofpriormalignancyenum"></a>
<a id="tocslateralityofpriormalignancyenum"></a>

```json
"Bilateral"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Bilateral|
|*anonymous*|Left|
|*anonymous*|Midline|
|*anonymous*|Not applicable|
|*anonymous*|Right|
|*anonymous*|Unilateral, Side not specified|
|*anonymous*|Unknown|

<h2 id="tocS_LostToFollowupReasonEnum">LostToFollowupReasonEnum</h2>

<a id="schemalosttofollowupreasonenum"></a>
<a id="schema_LostToFollowupReasonEnum"></a>
<a id="tocSlosttofollowupreasonenum"></a>
<a id="tocslosttofollowupreasonenum"></a>

```json
"Completed study"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Completed study|
|*anonymous*|Discharged to palliative care|
|*anonymous*|Lost contact|
|*anonymous*|Not applicable|
|*anonymous*|Unknown|
|*anonymous*|Withdrew from study|

<h2 id="tocS_LymphNodesExaminedMethodEnum">LymphNodesExaminedMethodEnum</h2>

<a id="schemalymphnodesexaminedmethodenum"></a>
<a id="schema_LymphNodesExaminedMethodEnum"></a>
<a id="tocSlymphnodesexaminedmethodenum"></a>
<a id="tocslymphnodesexaminedmethodenum"></a>

```json
"Imaging"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Imaging|
|*anonymous*|Lymph node dissection/pathological exam|
|*anonymous*|Physical palpation of patient|

<h2 id="tocS_LymphNodesExaminedStatusEnum">LymphNodesExaminedStatusEnum</h2>

<a id="schemalymphnodesexaminedstatusenum"></a>
<a id="schema_LymphNodesExaminedStatusEnum"></a>
<a id="tocSlymphnodesexaminedstatusenum"></a>
<a id="tocslymphnodesexaminedstatusenum"></a>

```json
"Cannot be determined"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Cannot be determined|
|*anonymous*|No|
|*anonymous*|No lymph nodes found in resected specimen|
|*anonymous*|Not applicable|
|*anonymous*|Yes|

<h2 id="tocS_LymphovascularInvasionEnum">LymphovascularInvasionEnum</h2>

<a id="schemalymphovascularinvasionenum"></a>
<a id="schema_LymphovascularInvasionEnum"></a>
<a id="tocSlymphovascularinvasionenum"></a>
<a id="tocslymphovascularinvasionenum"></a>

```json
"Absent"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Absent|
|*anonymous*|Both lymphatic and small vessel and venous (large vessel) invasion|
|*anonymous*|Lymphatic and small vessel invasion only|
|*anonymous*|Not applicable|
|*anonymous*|Present|
|*anonymous*|Venous (large vessel) invasion only|
|*anonymous*|Unknown|

<h2 id="tocS_MCategoryEnum">MCategoryEnum</h2>

<a id="schemamcategoryenum"></a>
<a id="schema_MCategoryEnum"></a>
<a id="tocSmcategoryenum"></a>
<a id="tocsmcategoryenum"></a>

```json
"M0"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|M0|
|*anonymous*|M0(i+)|
|*anonymous*|M1|
|*anonymous*|M1a|
|*anonymous*|M1a(0)|
|*anonymous*|M1a(1)|
|*anonymous*|M1b|
|*anonymous*|M1b(0)|
|*anonymous*|M1b(1)|
|*anonymous*|M1c|
|*anonymous*|M1c(0)|
|*anonymous*|M1c(1)|
|*anonymous*|M1d|
|*anonymous*|M1d(0)|
|*anonymous*|M1d(1)|
|*anonymous*|M1e|
|*anonymous*|MX|

<h2 id="tocS_MarginTypesEnum">MarginTypesEnum</h2>

<a id="schemamargintypesenum"></a>
<a id="schema_MarginTypesEnum"></a>
<a id="tocSmargintypesenum"></a>
<a id="tocsmargintypesenum"></a>

```json
"Circumferential resection margin"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Circumferential resection margin|
|*anonymous*|Common bile duct margin|
|*anonymous*|Distal margin|
|*anonymous*|Not applicable|
|*anonymous*|Proximal margin|
|*anonymous*|Unknown|

<h2 id="tocS_MethodOfProgressionStatusEnum">MethodOfProgressionStatusEnum</h2>

<a id="schemamethodofprogressionstatusenum"></a>
<a id="schema_MethodOfProgressionStatusEnum"></a>
<a id="tocSmethodofprogressionstatusenum"></a>
<a id="tocsmethodofprogressionstatusenum"></a>

```json
"Imaging (procedure)"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Imaging (procedure)|
|*anonymous*|Histopathology test (procedure)|
|*anonymous*|Assessment of symptom control (procedure)|
|*anonymous*|Physical examination procedure (procedure)|
|*anonymous*|Tumor marker measurement (procedure)|
|*anonymous*|Laboratory data interpretation (procedure)|

<h2 id="tocS_NCategoryEnum">NCategoryEnum</h2>

<a id="schemancategoryenum"></a>
<a id="schema_NCategoryEnum"></a>
<a id="tocSncategoryenum"></a>
<a id="tocsncategoryenum"></a>

```json
"N0"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|N0|
|*anonymous*|N0a|
|*anonymous*|N0a (biopsy)|
|*anonymous*|N0b|
|*anonymous*|N0b (no biopsy)|
|*anonymous*|N0(i+)|
|*anonymous*|N0(i-)|
|*anonymous*|N0(mol+)|
|*anonymous*|N0(mol-)|
|*anonymous*|N1|
|*anonymous*|N1a|
|*anonymous*|N1a(sn)|
|*anonymous*|N1b|
|*anonymous*|N1c|
|*anonymous*|N1mi|
|*anonymous*|N2|
|*anonymous*|N2a|
|*anonymous*|N2b|
|*anonymous*|N2c|
|*anonymous*|N2mi|
|*anonymous*|N3|
|*anonymous*|N3a|
|*anonymous*|N3b|
|*anonymous*|N3c|
|*anonymous*|N4|
|*anonymous*|NX|

<h2 id="tocS_PaginatedBiomarkerList">PaginatedBiomarkerList</h2>

<a id="schemapaginatedbiomarkerlist"></a>
<a id="schema_PaginatedBiomarkerList"></a>
<a id="tocSpaginatedbiomarkerlist"></a>
<a id="tocspaginatedbiomarkerlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "test_interval": 32767,
      "psa_level": 32767,
      "ca125": 32767,
      "cea": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_specimen_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string",
      "submitter_follow_up_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Biomarker](#schemabiomarker)]|false|none|none|

<h2 id="tocS_PaginatedChemotherapyList">PaginatedChemotherapyList</h2>

<a id="schemapaginatedchemotherapylist"></a>
<a id="schema_PaginatedChemotherapyList"></a>
<a id="tocSpaginatedchemotherapylist"></a>
<a id="tocspaginatedchemotherapylist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "chemotherapy_dosage_units": "mg/m2",
      "drug_name": "string",
      "drug_rxnormcui": "string",
      "cumulative_drug_dosage_prescribed": 32767,
      "cumulative_drug_dosage_actual": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Chemotherapy](#schemachemotherapy)]|false|none|none|

<h2 id="tocS_PaginatedComorbidityList">PaginatedComorbidityList</h2>

<a id="schemapaginatedcomorbiditylist"></a>
<a id="schema_PaginatedComorbidityList"></a>
<a id="tocSpaginatedcomorbiditylist"></a>
<a id="tocspaginatedcomorbiditylist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "prior_malignancy": "Yes",
      "laterality_of_prior_malignancy": "Bilateral",
      "comorbidity_type_code": "string",
      "comorbidity_treatment_status": "Yes",
      "comorbidity_treatment": "string",
      "age_at_comorbidity_diagnosis": 32767,
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Comorbidity](#schemacomorbidity)]|false|none|none|

<h2 id="tocS_PaginatedDonorList">PaginatedDonorList</h2>

<a id="schemapaginateddonorlist"></a>
<a id="schema_PaginatedDonorList"></a>
<a id="tocSpaginateddonorlist"></a>
<a id="tocspaginateddonorlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_donor_id": "string",
      "cause_of_death": "Died of cancer",
      "date_of_birth": "string",
      "date_of_death": "string",
      "primary_site": [
        "Accessory sinuses"
      ],
      "is_deceased": true,
      "program_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Donor](#schemadonor)]|false|none|none|

<h2 id="tocS_PaginatedFollowUpList">PaginatedFollowUpList</h2>

<a id="schemapaginatedfollowuplist"></a>
<a id="schema_PaginatedFollowUpList"></a>
<a id="tocSpaginatedfollowuplist"></a>
<a id="tocspaginatedfollowuplist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_follow_up_id": "string",
      "date_of_followup": "string",
      "lost_to_followup_reason": "Completed study",
      "disease_status_at_followup": "Complete remission",
      "relapse_type": "Distant recurrence/metastasis",
      "date_of_relapse": "string",
      "method_of_progression_status": "Imaging (procedure)",
      "anatomic_site_progression_or_recurrence": "string",
      "recurrence_tumour_staging_system": "AJCC 8th edition",
      "recurrence_t_category": "T0",
      "recurrence_n_category": "N0",
      "recurrence_m_category": "M0",
      "recurrence_stage_group": "Occult Carcinoma",
      "lost_to_followup": true,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[FollowUp](#schemafollowup)]|false|none|none|

<h2 id="tocS_PaginatedHormoneTherapyList">PaginatedHormoneTherapyList</h2>

<a id="schemapaginatedhormonetherapylist"></a>
<a id="schema_PaginatedHormoneTherapyList"></a>
<a id="tocSpaginatedhormonetherapylist"></a>
<a id="tocspaginatedhormonetherapylist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "hormone_drug_dosage_units": "mg/m2",
      "drug_name": "string",
      "drug_rxnormcui": "string",
      "cumulative_drug_dosage_prescribed": 32767,
      "cumulative_drug_dosage_actual": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[HormoneTherapy](#schemahormonetherapy)]|false|none|none|

<h2 id="tocS_PaginatedImmunotherapyList">PaginatedImmunotherapyList</h2>

<a id="schemapaginatedimmunotherapylist"></a>
<a id="schema_PaginatedImmunotherapyList"></a>
<a id="tocSpaginatedimmunotherapylist"></a>
<a id="tocspaginatedimmunotherapylist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "immunotherapy_type": "Cell-based",
      "drug_name": "string",
      "drug_rxnormcui": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Immunotherapy](#schemaimmunotherapy)]|false|none|none|

<h2 id="tocS_PaginatedPrimaryDiagnosisList">PaginatedPrimaryDiagnosisList</h2>

<a id="schemapaginatedprimarydiagnosislist"></a>
<a id="schema_PaginatedPrimaryDiagnosisList"></a>
<a id="tocSpaginatedprimarydiagnosislist"></a>
<a id="tocspaginatedprimarydiagnosislist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_primary_diagnosis_id": "string",
      "date_of_diagnosis": "string",
      "basis_of_diagnosis": "Clinical investigation",
      "lymph_nodes_examined_status": "Cannot be determined",
      "lymph_nodes_examined_method": "Imaging",
      "clinical_tumour_staging_system": "AJCC 8th edition",
      "clinical_t_category": "T0",
      "clinical_n_category": "N0",
      "clinical_m_category": "M0",
      "clinical_stage_group": "Occult Carcinoma",
      "cancer_type_code": "string",
      "number_lymph_nodes_positive": 32767,
      "program_id": "string",
      "submitter_donor_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[PrimaryDiagnosis](#schemaprimarydiagnosis)]|false|none|none|

<h2 id="tocS_PaginatedProgramList">PaginatedProgramList</h2>

<a id="schemapaginatedprogramlist"></a>
<a id="schema_PaginatedProgramList"></a>
<a id="tocSpaginatedprogramlist"></a>
<a id="tocspaginatedprogramlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "program_id": "string",
      "name": "string",
      "created": "2019-08-24T14:15:22Z",
      "updated": "2019-08-24T14:15:22Z"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Program](#schemaprogram)]|false|none|none|

<h2 id="tocS_PaginatedRadiationList">PaginatedRadiationList</h2>

<a id="schemapaginatedradiationlist"></a>
<a id="schema_PaginatedRadiationList"></a>
<a id="tocSpaginatedradiationlist"></a>
<a id="tocspaginatedradiationlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
      "radiation_therapy_type": "External",
      "anatomical_site_irradiated": "Cervical lymph node group",
      "radiation_therapy_fractions": 32767,
      "radiation_therapy_dosage": 32767,
      "radiation_boost": true,
      "reference_radiation_treatment_id": "string",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Radiation](#schemaradiation)]|false|none|none|

<h2 id="tocS_PaginatedSampleRegistrationList">PaginatedSampleRegistrationList</h2>

<a id="schemapaginatedsampleregistrationlist"></a>
<a id="schema_PaginatedSampleRegistrationList"></a>
<a id="tocSpaginatedsampleregistrationlist"></a>
<a id="tocspaginatedsampleregistrationlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_sample_id": "string",
      "gender": "Man",
      "sex_at_birth": "Male",
      "specimen_tissue_source": "Amniotic fluid",
      "tumour_normal_designation": "Normal",
      "specimen_type": "Cell line - derived from normal",
      "sample_type": "Amplified DNA",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_specimen_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[SampleRegistration](#schemasampleregistration)]|false|none|none|

<h2 id="tocS_PaginatedSpecimenList">PaginatedSpecimenList</h2>

<a id="schemapaginatedspecimenlist"></a>
<a id="schema_PaginatedSpecimenList"></a>
<a id="tocSpaginatedspecimenlist"></a>
<a id="tocspaginatedspecimenlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_specimen_id": "string",
      "pathological_tumour_staging_system": "AJCC 8th edition",
      "pathological_t_category": "T0",
      "pathological_n_category": "N0",
      "pathological_m_category": "M0",
      "pathological_stage_group": "Occult Carcinoma",
      "specimen_collection_date": "string",
      "specimen_storage": "Cut slide",
      "tumour_histological_type": "string",
      "specimen_anatomic_location": "string",
      "reference_pathology_confirmed_diagnosis": "Yes",
      "reference_pathology_confirmed_tumour_presence": "Yes",
      "tumour_grading_system": "FNCLCC grading system",
      "tumour_grade": "Low grade",
      "percent_tumour_cells_range": "0-19%",
      "percent_tumour_cells_measurement_method": "Genomics",
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Specimen](#schemaspecimen)]|false|none|none|

<h2 id="tocS_PaginatedSurgeryList">PaginatedSurgeryList</h2>

<a id="schemapaginatedsurgerylist"></a>
<a id="schema_PaginatedSurgeryList"></a>
<a id="tocSpaginatedsurgerylist"></a>
<a id="tocspaginatedsurgerylist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "surgery_type": "Axillary Clearance",
      "surgery_site": "string",
      "surgery_location": "Local recurrence",
      "tumour_focality": "Cannot be assessed",
      "residual_tumour_classification": "Not applicable",
      "margin_types_involved": [
        "Circumferential resection margin"
      ],
      "margin_types_not_involved": [
        "Circumferential resection margin"
      ],
      "margin_types_not_assessed": [
        "Circumferential resection margin"
      ],
      "lymphovascular_invasion": "Absent",
      "perineural_invasion": "Absent",
      "tumour_length": 32767,
      "tumour_width": 32767,
      "greatest_dimension_tumour": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_specimen_id": "string",
      "submitter_treatment_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Surgery](#schemasurgery)]|false|none|none|

<h2 id="tocS_PaginatedTreatmentList">PaginatedTreatmentList</h2>

<a id="schemapaginatedtreatmentlist"></a>
<a id="schema_PaginatedTreatmentList"></a>
<a id="tocSpaginatedtreatmentlist"></a>
<a id="tocspaginatedtreatmentlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "submitter_treatment_id": "string",
      "treatment_type": [
        "Ablation"
      ],
      "is_primary_treatment": "Yes",
      "treatment_start_date": "string",
      "treatment_end_date": "string",
      "treatment_setting": "Adjuvant",
      "treatment_intent": "Curative",
      "response_to_treatment_criteria_method": "RECIST 1.1",
      "response_to_treatment": "Complete response",
      "days_per_cycle": 32767,
      "number_of_cycles": 32767,
      "program_id": "string",
      "submitter_donor_id": "string",
      "submitter_primary_diagnosis_id": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Treatment](#schematreatment)]|false|none|none|

<h2 id="tocS_PatchedBiomarkerRequest">PatchedBiomarkerRequest</h2>

<a id="schemapatchedbiomarkerrequest"></a>
<a id="schema_PatchedBiomarkerRequest"></a>
<a id="tocSpatchedbiomarkerrequest"></a>
<a id="tocspatchedbiomarkerrequest"></a>

```json
{
  "test_interval": 32767,
  "psa_level": 32767,
  "ca125": 32767,
  "cea": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string",
  "submitter_follow_up_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|test_interval|integer¦null|false|none|none|
|psa_level|integer¦null|false|none|none|
|ca125|integer¦null|false|none|none|
|cea|integer¦null|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_specimen_id|string¦null|false|none|none|
|submitter_primary_diagnosis_id|string¦null|false|none|none|
|submitter_treatment_id|string¦null|false|none|none|
|submitter_follow_up_id|string¦null|false|none|none|

<h2 id="tocS_PatchedChemotherapyRequest">PatchedChemotherapyRequest</h2>

<a id="schemapatchedchemotherapyrequest"></a>
<a id="schema_PatchedChemotherapyRequest"></a>
<a id="tocSpatchedchemotherapyrequest"></a>
<a id="tocspatchedchemotherapyrequest"></a>

```json
{
  "chemotherapy_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|chemotherapy_dosage_units|[DosageUnitsEnum](#schemadosageunitsenum)|false|none|none|
|drug_name|string|false|none|none|
|drug_rxnormcui|string|false|none|none|
|cumulative_drug_dosage_prescribed|integer¦null|false|none|none|
|cumulative_drug_dosage_actual|integer¦null|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_treatment_id|string|false|none|none|

<h2 id="tocS_PatchedComorbidityRequest">PatchedComorbidityRequest</h2>

<a id="schemapatchedcomorbidityrequest"></a>
<a id="schema_PatchedComorbidityRequest"></a>
<a id="tocSpatchedcomorbidityrequest"></a>
<a id="tocspatchedcomorbidityrequest"></a>

```json
{
  "prior_malignancy": "Yes",
  "laterality_of_prior_malignancy": "Bilateral",
  "comorbidity_type_code": "string",
  "comorbidity_treatment_status": "Yes",
  "comorbidity_treatment": "string",
  "age_at_comorbidity_diagnosis": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prior_malignancy|[uBooleanEnum](#schemaubooleanenum)|false|none|none|
|laterality_of_prior_malignancy|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LateralityOfPriorMalignancyEnum](#schemalateralityofpriormalignancyenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_type_code|string|false|none|none|
|comorbidity_treatment_status|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[uBooleanEnum](#schemaubooleanenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comorbidity_treatment|string|false|none|none|
|age_at_comorbidity_diagnosis|integer¦null|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|

<h2 id="tocS_PatchedDonorRequest">PatchedDonorRequest</h2>

<a id="schemapatcheddonorrequest"></a>
<a id="schema_PatchedDonorRequest"></a>
<a id="tocSpatcheddonorrequest"></a>
<a id="tocspatcheddonorrequest"></a>

```json
{
  "submitter_donor_id": "string",
  "cause_of_death": "Died of cancer",
  "date_of_birth": "string",
  "date_of_death": "string",
  "primary_site": [
    "Accessory sinuses"
  ],
  "is_deceased": true,
  "program_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_donor_id|string|false|none|none|
|cause_of_death|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CauseOfDeathEnum](#schemacauseofdeathenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_birth|string|false|none|none|
|date_of_death|string|false|none|none|
|primary_site|[[PrimarySiteEnum](#schemaprimarysiteenum)]|false|none|none|
|is_deceased|boolean|false|none|none|
|program_id|string|false|none|none|

<h2 id="tocS_PatchedFollowUpRequest">PatchedFollowUpRequest</h2>

<a id="schemapatchedfollowuprequest"></a>
<a id="schema_PatchedFollowUpRequest"></a>
<a id="tocSpatchedfollowuprequest"></a>
<a id="tocspatchedfollowuprequest"></a>

```json
{
  "submitter_follow_up_id": "string",
  "date_of_followup": "string",
  "lost_to_followup_reason": "Completed study",
  "disease_status_at_followup": "Complete remission",
  "relapse_type": "Distant recurrence/metastasis",
  "date_of_relapse": "string",
  "method_of_progression_status": "Imaging (procedure)",
  "anatomic_site_progression_or_recurrence": "string",
  "recurrence_tumour_staging_system": "AJCC 8th edition",
  "recurrence_t_category": "T0",
  "recurrence_n_category": "N0",
  "recurrence_m_category": "M0",
  "recurrence_stage_group": "Occult Carcinoma",
  "lost_to_followup": true,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_follow_up_id|string|false|none|none|
|date_of_followup|string|false|none|none|
|lost_to_followup_reason|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LostToFollowupReasonEnum](#schemalosttofollowupreasonenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|disease_status_at_followup|[DiseaseStatusAtFollowupEnum](#schemadiseasestatusatfollowupenum)|false|none|none|
|relapse_type|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[RelapseTypeEnum](#schemarelapsetypeenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_of_relapse|string|false|none|none|
|method_of_progression_status|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MethodOfProgressionStatusEnum](#schemamethodofprogressionstatusenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anatomic_site_progression_or_recurrence|string|false|none|none|
|recurrence_tumour_staging_system|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StagingSystemEnum](#schemastagingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_t_category|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_n_category|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_m_category|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recurrence_stage_group|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lost_to_followup|boolean¦null|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_primary_diagnosis_id|string¦null|false|none|none|
|submitter_treatment_id|string¦null|false|none|none|

<h2 id="tocS_PatchedHormoneTherapyRequest">PatchedHormoneTherapyRequest</h2>

<a id="schemapatchedhormonetherapyrequest"></a>
<a id="schema_PatchedHormoneTherapyRequest"></a>
<a id="tocSpatchedhormonetherapyrequest"></a>
<a id="tocspatchedhormonetherapyrequest"></a>

```json
{
  "hormone_drug_dosage_units": "mg/m2",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "cumulative_drug_dosage_prescribed": 32767,
  "cumulative_drug_dosage_actual": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hormone_drug_dosage_units|[DosageUnitsEnum](#schemadosageunitsenum)|false|none|none|
|drug_name|string|false|none|none|
|drug_rxnormcui|string|false|none|none|
|cumulative_drug_dosage_prescribed|integer¦null|false|none|none|
|cumulative_drug_dosage_actual|integer¦null|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_treatment_id|string|false|none|none|

<h2 id="tocS_PatchedImmunotherapyRequest">PatchedImmunotherapyRequest</h2>

<a id="schemapatchedimmunotherapyrequest"></a>
<a id="schema_PatchedImmunotherapyRequest"></a>
<a id="tocSpatchedimmunotherapyrequest"></a>
<a id="tocspatchedimmunotherapyrequest"></a>

```json
{
  "immunotherapy_type": "Cell-based",
  "drug_name": "string",
  "drug_rxnormcui": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|immunotherapy_type|[ImmunotherapyTypeEnum](#schemaimmunotherapytypeenum)|false|none|none|
|drug_name|string|false|none|none|
|drug_rxnormcui|string|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_treatment_id|string|false|none|none|

<h2 id="tocS_PatchedPrimaryDiagnosisRequest">PatchedPrimaryDiagnosisRequest</h2>

<a id="schemapatchedprimarydiagnosisrequest"></a>
<a id="schema_PatchedPrimaryDiagnosisRequest"></a>
<a id="tocSpatchedprimarydiagnosisrequest"></a>
<a id="tocspatchedprimarydiagnosisrequest"></a>

```json
{
  "submitter_primary_diagnosis_id": "string",
  "date_of_diagnosis": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "lymph_nodes_examined_status": "Cannot be determined",
  "lymph_nodes_examined_method": "Imaging",
  "clinical_tumour_staging_system": "AJCC 8th edition",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Occult Carcinoma",
  "cancer_type_code": "string",
  "number_lymph_nodes_positive": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|string|false|none|none|
|date_of_diagnosis|string|false|none|none|
|basis_of_diagnosis|[BasisOfDiagnosisEnum](#schemabasisofdiagnosisenum)|false|none|none|
|lymph_nodes_examined_status|[LymphNodesExaminedStatusEnum](#schemalymphnodesexaminedstatusenum)|false|none|none|
|lymph_nodes_examined_method|[LymphNodesExaminedMethodEnum](#schemalymphnodesexaminedmethodenum)|false|none|none|
|clinical_tumour_staging_system|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StagingSystemEnum](#schemastagingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_t_category|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_n_category|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_m_category|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_stage_group|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cancer_type_code|string|false|none|none|
|number_lymph_nodes_positive|integer¦null|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|

<h2 id="tocS_PatchedProgramRequest">PatchedProgramRequest</h2>

<a id="schemapatchedprogramrequest"></a>
<a id="schema_PatchedProgramRequest"></a>
<a id="tocSpatchedprogramrequest"></a>
<a id="tocspatchedprogramrequest"></a>

```json
{
  "program_id": "string",
  "name": "string",
  "created": "2019-08-24T14:15:22Z",
  "updated": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|false|none|none|
|name|string|false|none|none|
|created|string(date-time)|false|none|none|
|updated|string(date-time)|false|none|none|

<h2 id="tocS_PatchedRadiationRequest">PatchedRadiationRequest</h2>

<a id="schemapatchedradiationrequest"></a>
<a id="schema_PatchedRadiationRequest"></a>
<a id="tocSpatchedradiationrequest"></a>
<a id="tocspatchedradiationrequest"></a>

```json
{
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "anatomical_site_irradiated": "Cervical lymph node group",
  "radiation_therapy_fractions": 32767,
  "radiation_therapy_dosage": 32767,
  "radiation_boost": true,
  "reference_radiation_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_modality|[RadiationTherapyModalityEnum](#schemaradiationtherapymodalityenum)|false|none|none|
|radiation_therapy_type|[RadiationTherapyTypeEnum](#schemaradiationtherapytypeenum)|false|none|none|
|anatomical_site_irradiated|[AnatomicalSiteIrradiatedEnum](#schemaanatomicalsiteirradiatedenum)|false|none|none|
|radiation_therapy_fractions|integer|false|none|none|
|radiation_therapy_dosage|integer|false|none|none|
|radiation_boost|boolean¦null|false|none|none|
|reference_radiation_treatment_id|string|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_treatment_id|string|false|none|none|

<h2 id="tocS_PatchedSampleRegistrationRequest">PatchedSampleRegistrationRequest</h2>

<a id="schemapatchedsampleregistrationrequest"></a>
<a id="schema_PatchedSampleRegistrationRequest"></a>
<a id="tocSpatchedsampleregistrationrequest"></a>
<a id="tocspatchedsampleregistrationrequest"></a>

```json
{
  "submitter_sample_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "specimen_tissue_source": "Amniotic fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "sample_type": "Amplified DNA",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_sample_id|string|false|none|none|
|gender|[GenderEnum](#schemagenderenum)|false|none|none|
|sex_at_birth|[SexAtBirthEnum](#schemasexatbirthenum)|false|none|none|
|specimen_tissue_source|[SpecimenTissueSourceEnum](#schemaspecimentissuesourceenum)|false|none|none|
|tumour_normal_designation|[TumourNormalDesignationEnum](#schematumournormaldesignationenum)|false|none|none|
|specimen_type|[SpecimenTypeEnum](#schemaspecimentypeenum)|false|none|none|
|sample_type|[SampleTypeEnum](#schemasampletypeenum)|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_specimen_id|string|false|none|none|

<h2 id="tocS_PatchedSpecimenRequest">PatchedSpecimenRequest</h2>

<a id="schemapatchedspecimenrequest"></a>
<a id="schema_PatchedSpecimenRequest"></a>
<a id="tocSpatchedspecimenrequest"></a>
<a id="tocspatchedspecimenrequest"></a>

```json
{
  "submitter_specimen_id": "string",
  "pathological_tumour_staging_system": "AJCC 8th edition",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Occult Carcinoma",
  "specimen_collection_date": "string",
  "specimen_storage": "Cut slide",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|string|false|none|none|
|pathological_tumour_staging_system|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StagingSystemEnum](#schemastagingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_t_category|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_n_category|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_m_category|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_stage_group|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_collection_date|string|false|none|none|
|specimen_storage|[SpecimenStorageEnum](#schemaspecimenstorageenum)|false|none|none|
|tumour_histological_type|string|false|none|none|
|specimen_anatomic_location|string|false|none|none|
|reference_pathology_confirmed_diagnosis|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ReferencePathologyEnum](#schemareferencepathologyenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_tumour_presence|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ReferencePathologyEnum](#schemareferencepathologyenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grading_system|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradingSystemEnum](#schematumourgradingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grade|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradeEnum](#schematumourgradeenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_range|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PercentTumourCellsRangeEnum](#schemapercenttumourcellsrangeenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_measurement_method|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PercentTumourCellsMeasurementMethodEnum](#schemapercenttumourcellsmeasurementmethodenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_primary_diagnosis_id|string|false|none|none|

<h2 id="tocS_PatchedSurgeryRequest">PatchedSurgeryRequest</h2>

<a id="schemapatchedsurgeryrequest"></a>
<a id="schema_PatchedSurgeryRequest"></a>
<a id="tocSpatchedsurgeryrequest"></a>
<a id="tocspatchedsurgeryrequest"></a>

```json
{
  "surgery_type": "Axillary Clearance",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margin_types_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_assessed": [
    "Circumferential resection margin"
  ],
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "tumour_length": 32767,
  "tumour_width": 32767,
  "greatest_dimension_tumour": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_type|[SurgeryTypeEnum](#schemasurgerytypeenum)|false|none|none|
|surgery_site|string|false|none|none|
|surgery_location|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SurgeryLocationEnum](#schemasurgerylocationenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_focality|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourFocalityEnum](#schematumourfocalityenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|residual_tumour_classification|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ResidualTumourClassificationEnum](#schemaresidualtumourclassificationenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_types_involved|[oneOf]|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginTypesEnum](#schemamargintypesenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_types_not_involved|[oneOf]|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginTypesEnum](#schemamargintypesenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_types_not_assessed|[oneOf]|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginTypesEnum](#schemamargintypesenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lymphovascular_invasion|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LymphovascularInvasionEnum](#schemalymphovascularinvasionenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|perineural_invasion|any|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PerineuralInvasionEnum](#schemaperineuralinvasionenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length|integer¦null|false|none|none|
|tumour_width|integer¦null|false|none|none|
|greatest_dimension_tumour|integer¦null|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_specimen_id|string¦null|false|none|none|
|submitter_treatment_id|string|false|none|none|

<h2 id="tocS_PatchedTreatmentRequest">PatchedTreatmentRequest</h2>

<a id="schemapatchedtreatmentrequest"></a>
<a id="schema_PatchedTreatmentRequest"></a>
<a id="tocSpatchedtreatmentrequest"></a>
<a id="tocspatchedtreatmentrequest"></a>

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Ablation"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": "string",
  "treatment_end_date": "string",
  "treatment_setting": "Adjuvant",
  "treatment_intent": "Curative",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "days_per_cycle": 32767,
  "number_of_cycles": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|string|false|none|none|
|treatment_type|[[TreatmentTypeEnum](#schematreatmenttypeenum)]|false|none|none|
|is_primary_treatment|[uBooleanEnum](#schemaubooleanenum)|false|none|none|
|treatment_start_date|string|false|none|none|
|treatment_end_date|string|false|none|none|
|treatment_setting|[TreatmentSettingEnum](#schematreatmentsettingenum)|false|none|none|
|treatment_intent|[TreatmentIntentEnum](#schematreatmentintentenum)|false|none|none|
|response_to_treatment_criteria_method|[ResponseToTreatmentCriteriaMethodEnum](#schemaresponsetotreatmentcriteriamethodenum)|false|none|none|
|response_to_treatment|[ResponseToTreatmentEnum](#schemaresponsetotreatmentenum)|false|none|none|
|days_per_cycle|integer¦null|false|none|none|
|number_of_cycles|integer¦null|false|none|none|
|program_id|string|false|none|none|
|submitter_donor_id|string|false|none|none|
|submitter_primary_diagnosis_id|string|false|none|none|

<h2 id="tocS_PercentTumourCellsMeasurementMethodEnum">PercentTumourCellsMeasurementMethodEnum</h2>

<a id="schemapercenttumourcellsmeasurementmethodenum"></a>
<a id="schema_PercentTumourCellsMeasurementMethodEnum"></a>
<a id="tocSpercenttumourcellsmeasurementmethodenum"></a>
<a id="tocspercenttumourcellsmeasurementmethodenum"></a>

```json
"Genomics"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Genomics|
|*anonymous*|Image analysis|
|*anonymous*|Pathology estimate by percent nuclei|
|*anonymous*|Unknown|

<h2 id="tocS_PercentTumourCellsRangeEnum">PercentTumourCellsRangeEnum</h2>

<a id="schemapercenttumourcellsrangeenum"></a>
<a id="schema_PercentTumourCellsRangeEnum"></a>
<a id="tocSpercenttumourcellsrangeenum"></a>
<a id="tocspercenttumourcellsrangeenum"></a>

```json
"0-19%"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|0-19%|
|*anonymous*|20-50%|
|*anonymous*|51-100%|

<h2 id="tocS_PerineuralInvasionEnum">PerineuralInvasionEnum</h2>

<a id="schemaperineuralinvasionenum"></a>
<a id="schema_PerineuralInvasionEnum"></a>
<a id="tocSperineuralinvasionenum"></a>
<a id="tocsperineuralinvasionenum"></a>

```json
"Absent"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Absent|
|*anonymous*|Cannot be assessed|
|*anonymous*|Not applicable|
|*anonymous*|Present|
|*anonymous*|Unknown|

<h2 id="tocS_PrimaryDiagnosis">PrimaryDiagnosis</h2>

<a id="schemaprimarydiagnosis"></a>
<a id="schema_PrimaryDiagnosis"></a>
<a id="tocSprimarydiagnosis"></a>
<a id="tocsprimarydiagnosis"></a>

```json
{
  "submitter_primary_diagnosis_id": "string",
  "date_of_diagnosis": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "lymph_nodes_examined_status": "Cannot be determined",
  "lymph_nodes_examined_method": "Imaging",
  "clinical_tumour_staging_system": "AJCC 8th edition",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Occult Carcinoma",
  "cancer_type_code": "string",
  "number_lymph_nodes_positive": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|string|true|none|none|
|date_of_diagnosis|string|true|none|none|
|basis_of_diagnosis|[BasisOfDiagnosisEnum](#schemabasisofdiagnosisenum)|true|none|none|
|lymph_nodes_examined_status|[LymphNodesExaminedStatusEnum](#schemalymphnodesexaminedstatusenum)|true|none|none|
|lymph_nodes_examined_method|[LymphNodesExaminedMethodEnum](#schemalymphnodesexaminedmethodenum)|true|none|none|
|clinical_tumour_staging_system|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StagingSystemEnum](#schemastagingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_t_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_n_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_m_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_stage_group|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cancer_type_code|string|true|none|none|
|number_lymph_nodes_positive|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|

<h2 id="tocS_PrimaryDiagnosisRequest">PrimaryDiagnosisRequest</h2>

<a id="schemaprimarydiagnosisrequest"></a>
<a id="schema_PrimaryDiagnosisRequest"></a>
<a id="tocSprimarydiagnosisrequest"></a>
<a id="tocsprimarydiagnosisrequest"></a>

```json
{
  "submitter_primary_diagnosis_id": "string",
  "date_of_diagnosis": "string",
  "basis_of_diagnosis": "Clinical investigation",
  "lymph_nodes_examined_status": "Cannot be determined",
  "lymph_nodes_examined_method": "Imaging",
  "clinical_tumour_staging_system": "AJCC 8th edition",
  "clinical_t_category": "T0",
  "clinical_n_category": "N0",
  "clinical_m_category": "M0",
  "clinical_stage_group": "Occult Carcinoma",
  "cancer_type_code": "string",
  "number_lymph_nodes_positive": 32767,
  "program_id": "string",
  "submitter_donor_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_primary_diagnosis_id|string|true|none|none|
|date_of_diagnosis|string|true|none|none|
|basis_of_diagnosis|[BasisOfDiagnosisEnum](#schemabasisofdiagnosisenum)|true|none|none|
|lymph_nodes_examined_status|[LymphNodesExaminedStatusEnum](#schemalymphnodesexaminedstatusenum)|true|none|none|
|lymph_nodes_examined_method|[LymphNodesExaminedMethodEnum](#schemalymphnodesexaminedmethodenum)|true|none|none|
|clinical_tumour_staging_system|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StagingSystemEnum](#schemastagingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_t_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_n_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_m_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clinical_stage_group|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cancer_type_code|string|true|none|none|
|number_lymph_nodes_positive|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|

<h2 id="tocS_PrimarySiteEnum">PrimarySiteEnum</h2>

<a id="schemaprimarysiteenum"></a>
<a id="schema_PrimarySiteEnum"></a>
<a id="tocSprimarysiteenum"></a>
<a id="tocsprimarysiteenum"></a>

```json
"Accessory sinuses"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Accessory sinuses|
|*anonymous*|Adrenal gland|
|*anonymous*|Anus and anal canal|
|*anonymous*|Base of tongue|
|*anonymous*|Bladder|
|*anonymous*|Bones, joints and articular cartilage of limbs|
|*anonymous*|Bones, joints and articular cartilage of other and unspecified sites|
|*anonymous*|Brain|
|*anonymous*|Breast|
|*anonymous*|Bronchus and lung|
|*anonymous*|Cervix uteri|
|*anonymous*|Colon|
|*anonymous*|Connective, subcutaneous and other soft tissues|
|*anonymous*|Corpus uteri|
|*anonymous*|Esophagus|
|*anonymous*|Eye and adnexa|
|*anonymous*|Floor of mouth|
|*anonymous*|Gallbladder|
|*anonymous*|Gum|
|*anonymous*|Heart, mediastinum, and pleura|
|*anonymous*|Hematopoietic and reticuloendothelial systems|
|*anonymous*|Hypopharynx|
|*anonymous*|Kidney|
|*anonymous*|Larynx|
|*anonymous*|Lip|
|*anonymous*|Liver and intrahepatic bile ducts|
|*anonymous*|Lymph nodes|
|*anonymous*|Meninges|
|*anonymous*|Nasal cavity and middle ear|
|*anonymous*|Nasopharynx|
|*anonymous*|Oropharynx|
|*anonymous*|Other and ill-defined digestive organs|
|*anonymous*|Other and ill-defined sites|
|*anonymous*|Other and ill-defined sites in lip, oral cavity and pharynx|
|*anonymous*|Other and ill-defined sites within respiratory system and intrathoracic organs|
|*anonymous*|Other and unspecified female genital organs|
|*anonymous*|Other and unspecified major salivary glands|
|*anonymous*|Other and unspecified male genital organs|
|*anonymous*|Other and unspecified parts of biliary tract|
|*anonymous*|Other and unspecified parts of mouth|
|*anonymous*|Other and unspecified parts of tongue|
|*anonymous*|Other and unspecified urinary organs|
|*anonymous*|Other endocrine glands and related structures|
|*anonymous*|Ovary|
|*anonymous*|Palate|
|*anonymous*|Pancreas|
|*anonymous*|Parotid gland|
|*anonymous*|Penis|
|*anonymous*|Peripheral nerves and autonomic nervous system|
|*anonymous*|Placenta|
|*anonymous*|Prostate gland|
|*anonymous*|Pyriform sinus|
|*anonymous*|Rectosigmoid junction|
|*anonymous*|Rectum|
|*anonymous*|Renal pelvis|
|*anonymous*|Retroperitoneum and peritoneum|
|*anonymous*|Skin|
|*anonymous*|Small intestine|
|*anonymous*|Spinal cord, cranial nerves, and other parts of central nervous system|
|*anonymous*|Stomach|
|*anonymous*|Testis|
|*anonymous*|Thymus|
|*anonymous*|Thyroid gland|
|*anonymous*|Tonsil|
|*anonymous*|Trachea|
|*anonymous*|Unknown primary site|
|*anonymous*|Ureter|
|*anonymous*|Uterus, NOS|
|*anonymous*|Vagina|
|*anonymous*|Vulva|

<h2 id="tocS_Program">Program</h2>

<a id="schemaprogram"></a>
<a id="schema_Program"></a>
<a id="tocSprogram"></a>
<a id="tocsprogram"></a>

```json
{
  "program_id": "string",
  "name": "string",
  "created": "2019-08-24T14:15:22Z",
  "updated": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|name|string|true|none|none|
|created|string(date-time)|false|none|none|
|updated|string(date-time)|false|none|none|

<h2 id="tocS_ProgramRequest">ProgramRequest</h2>

<a id="schemaprogramrequest"></a>
<a id="schema_ProgramRequest"></a>
<a id="tocSprogramrequest"></a>
<a id="tocsprogramrequest"></a>

```json
{
  "program_id": "string",
  "name": "string",
  "created": "2019-08-24T14:15:22Z",
  "updated": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|name|string|true|none|none|
|created|string(date-time)|false|none|none|
|updated|string(date-time)|false|none|none|

<h2 id="tocS_Radiation">Radiation</h2>

<a id="schemaradiation"></a>
<a id="schema_Radiation"></a>
<a id="tocSradiation"></a>
<a id="tocsradiation"></a>

```json
{
  "id": 0,
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "anatomical_site_irradiated": "Cervical lymph node group",
  "radiation_therapy_fractions": 32767,
  "radiation_therapy_dosage": 32767,
  "radiation_boost": true,
  "reference_radiation_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|radiation_therapy_modality|[RadiationTherapyModalityEnum](#schemaradiationtherapymodalityenum)|true|none|none|
|radiation_therapy_type|[RadiationTherapyTypeEnum](#schemaradiationtherapytypeenum)|true|none|none|
|anatomical_site_irradiated|[AnatomicalSiteIrradiatedEnum](#schemaanatomicalsiteirradiatedenum)|true|none|none|
|radiation_therapy_fractions|integer|true|none|none|
|radiation_therapy_dosage|integer|true|none|none|
|radiation_boost|boolean¦null|false|none|none|
|reference_radiation_treatment_id|string|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_RadiationRequest">RadiationRequest</h2>

<a id="schemaradiationrequest"></a>
<a id="schema_RadiationRequest"></a>
<a id="tocSradiationrequest"></a>
<a id="tocsradiationrequest"></a>

```json
{
  "radiation_therapy_modality": "Megavoltage radiation therapy using photons (procedure)",
  "radiation_therapy_type": "External",
  "anatomical_site_irradiated": "Cervical lymph node group",
  "radiation_therapy_fractions": 32767,
  "radiation_therapy_dosage": 32767,
  "radiation_boost": true,
  "reference_radiation_treatment_id": "string",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|radiation_therapy_modality|[RadiationTherapyModalityEnum](#schemaradiationtherapymodalityenum)|true|none|none|
|radiation_therapy_type|[RadiationTherapyTypeEnum](#schemaradiationtherapytypeenum)|true|none|none|
|anatomical_site_irradiated|[AnatomicalSiteIrradiatedEnum](#schemaanatomicalsiteirradiatedenum)|true|none|none|
|radiation_therapy_fractions|integer|true|none|none|
|radiation_therapy_dosage|integer|true|none|none|
|radiation_boost|boolean¦null|false|none|none|
|reference_radiation_treatment_id|string|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_RadiationTherapyModalityEnum">RadiationTherapyModalityEnum</h2>

<a id="schemaradiationtherapymodalityenum"></a>
<a id="schema_RadiationTherapyModalityEnum"></a>
<a id="tocSradiationtherapymodalityenum"></a>
<a id="tocsradiationtherapymodalityenum"></a>

```json
"Megavoltage radiation therapy using photons (procedure)"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Megavoltage radiation therapy using photons (procedure)|
|*anonymous*|Teleradiotherapy using electrons (procedure)|
|*anonymous*|Teleradiotherapy protons (procedure)|
|*anonymous*|Teleradiotherapy neutrons (procedure)|
|*anonymous*|Brachytherapy (procedure)|
|*anonymous*|Other|

<h2 id="tocS_RadiationTherapyTypeEnum">RadiationTherapyTypeEnum</h2>

<a id="schemaradiationtherapytypeenum"></a>
<a id="schema_RadiationTherapyTypeEnum"></a>
<a id="tocSradiationtherapytypeenum"></a>
<a id="tocsradiationtherapytypeenum"></a>

```json
"External"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|External|
|*anonymous*|Internal|

<h2 id="tocS_ReferencePathologyEnum">ReferencePathologyEnum</h2>

<a id="schemareferencepathologyenum"></a>
<a id="schema_ReferencePathologyEnum"></a>
<a id="tocSreferencepathologyenum"></a>
<a id="tocsreferencepathologyenum"></a>

```json
"Yes"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Yes|
|*anonymous*|No|
|*anonymous*|Not done|
|*anonymous*|Unknown|

<h2 id="tocS_RelapseTypeEnum">RelapseTypeEnum</h2>

<a id="schemarelapsetypeenum"></a>
<a id="schema_RelapseTypeEnum"></a>
<a id="tocSrelapsetypeenum"></a>
<a id="tocsrelapsetypeenum"></a>

```json
"Distant recurrence/metastasis"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Distant recurrence/metastasis|
|*anonymous*|Local recurrence|
|*anonymous*|Local recurrence and distant metastasis|
|*anonymous*|Progression (liquid tumours)|
|*anonymous*|Biochemical progression|

<h2 id="tocS_ResidualTumourClassificationEnum">ResidualTumourClassificationEnum</h2>

<a id="schemaresidualtumourclassificationenum"></a>
<a id="schema_ResidualTumourClassificationEnum"></a>
<a id="tocSresidualtumourclassificationenum"></a>
<a id="tocsresidualtumourclassificationenum"></a>

```json
"Not applicable"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Not applicable|
|*anonymous*|RX|
|*anonymous*|R0|
|*anonymous*|R1|
|*anonymous*|R2|
|*anonymous*|Unknown|

<h2 id="tocS_ResponseToTreatmentCriteriaMethodEnum">ResponseToTreatmentCriteriaMethodEnum</h2>

<a id="schemaresponsetotreatmentcriteriamethodenum"></a>
<a id="schema_ResponseToTreatmentCriteriaMethodEnum"></a>
<a id="tocSresponsetotreatmentcriteriamethodenum"></a>
<a id="tocsresponsetotreatmentcriteriamethodenum"></a>

```json
"RECIST 1.1"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|RECIST 1.1|
|*anonymous*|iRECIST|
|*anonymous*|Cheson CLL 2012 Oncology Response Criteria|
|*anonymous*|Response Assessment in Neuro-Oncology (RANO)|
|*anonymous*|AML Response Criteria|
|*anonymous*|Physician Assessed Response Criteria|

<h2 id="tocS_ResponseToTreatmentEnum">ResponseToTreatmentEnum</h2>

<a id="schemaresponsetotreatmentenum"></a>
<a id="schema_ResponseToTreatmentEnum"></a>
<a id="tocSresponsetotreatmentenum"></a>
<a id="tocsresponsetotreatmentenum"></a>

```json
"Complete response"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Complete response|
|*anonymous*|Partial response|
|*anonymous*|Progressive disease|
|*anonymous*|Stable disease|
|*anonymous*|Immune complete response (iCR)|
|*anonymous*|Immune partial response (iPR)|
|*anonymous*|Immune uncomfirmed progressive disease (iUPD)|
|*anonymous*|Immune confirmed progressive disease (iCPD)|
|*anonymous*|Immune stable disease (iSD)|
|*anonymous*|Complete remission|
|*anonymous*|Partial remission|
|*anonymous*|Minor response|
|*anonymous*|Complete remission without measurable residual disease (CR MRD-)|
|*anonymous*|Complete remission with incomplete hematologic recovery (CRi)|
|*anonymous*|Morphologic leukemia-free state|
|*anonymous*|Primary refractory disease|
|*anonymous*|Hematologic relapse (after CR MRD-, CR, CRi)|
|*anonymous*|Molecular relapse (after CR MRD-)|
|*anonymous*|Physician assessed complete response|
|*anonymous*|Physician assessed partial response|
|*anonymous*|Physician assessed stable disease|
|*anonymous*|No evidence of disease (NED)|

<h2 id="tocS_SampleRegistration">SampleRegistration</h2>

<a id="schemasampleregistration"></a>
<a id="schema_SampleRegistration"></a>
<a id="tocSsampleregistration"></a>
<a id="tocssampleregistration"></a>

```json
{
  "submitter_sample_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "specimen_tissue_source": "Amniotic fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "sample_type": "Amplified DNA",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_sample_id|string|true|none|none|
|gender|[GenderEnum](#schemagenderenum)|true|none|none|
|sex_at_birth|[SexAtBirthEnum](#schemasexatbirthenum)|true|none|none|
|specimen_tissue_source|[SpecimenTissueSourceEnum](#schemaspecimentissuesourceenum)|true|none|none|
|tumour_normal_designation|[TumourNormalDesignationEnum](#schematumournormaldesignationenum)|true|none|none|
|specimen_type|[SpecimenTypeEnum](#schemaspecimentypeenum)|true|none|none|
|sample_type|[SampleTypeEnum](#schemasampletypeenum)|true|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_specimen_id|string|true|none|none|

<h2 id="tocS_SampleRegistrationRequest">SampleRegistrationRequest</h2>

<a id="schemasampleregistrationrequest"></a>
<a id="schema_SampleRegistrationRequest"></a>
<a id="tocSsampleregistrationrequest"></a>
<a id="tocssampleregistrationrequest"></a>

```json
{
  "submitter_sample_id": "string",
  "gender": "Man",
  "sex_at_birth": "Male",
  "specimen_tissue_source": "Amniotic fluid",
  "tumour_normal_designation": "Normal",
  "specimen_type": "Cell line - derived from normal",
  "sample_type": "Amplified DNA",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_sample_id|string|true|none|none|
|gender|[GenderEnum](#schemagenderenum)|true|none|none|
|sex_at_birth|[SexAtBirthEnum](#schemasexatbirthenum)|true|none|none|
|specimen_tissue_source|[SpecimenTissueSourceEnum](#schemaspecimentissuesourceenum)|true|none|none|
|tumour_normal_designation|[TumourNormalDesignationEnum](#schematumournormaldesignationenum)|true|none|none|
|specimen_type|[SpecimenTypeEnum](#schemaspecimentypeenum)|true|none|none|
|sample_type|[SampleTypeEnum](#schemasampletypeenum)|true|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_specimen_id|string|true|none|none|

<h2 id="tocS_SampleTypeEnum">SampleTypeEnum</h2>

<a id="schemasampletypeenum"></a>
<a id="schema_SampleTypeEnum"></a>
<a id="tocSsampletypeenum"></a>
<a id="tocssampletypeenum"></a>

```json
"Amplified DNA"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Amplified DNA|
|*anonymous*|ctDNA|
|*anonymous*|Other DNA enrichments|
|*anonymous*|Other RNA fractions|
|*anonymous*|polyA+ RNA|
|*anonymous*|Protein|
|*anonymous*|rRNA-depleted RNA|
|*anonymous*|Total DNA|
|*anonymous*|Total RNA|

<h2 id="tocS_SexAtBirthEnum">SexAtBirthEnum</h2>

<a id="schemasexatbirthenum"></a>
<a id="schema_SexAtBirthEnum"></a>
<a id="tocSsexatbirthenum"></a>
<a id="tocssexatbirthenum"></a>

```json
"Male"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Male|
|*anonymous*|Female|
|*anonymous*|Other|
|*anonymous*|Unknown|

<h2 id="tocS_Specimen">Specimen</h2>

<a id="schemaspecimen"></a>
<a id="schema_Specimen"></a>
<a id="tocSspecimen"></a>
<a id="tocsspecimen"></a>

```json
{
  "submitter_specimen_id": "string",
  "pathological_tumour_staging_system": "AJCC 8th edition",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Occult Carcinoma",
  "specimen_collection_date": "string",
  "specimen_storage": "Cut slide",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|string|true|none|none|
|pathological_tumour_staging_system|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StagingSystemEnum](#schemastagingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_t_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_n_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_m_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_stage_group|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_collection_date|string|true|none|none|
|specimen_storage|[SpecimenStorageEnum](#schemaspecimenstorageenum)|true|none|none|
|tumour_histological_type|string|true|none|none|
|specimen_anatomic_location|string|true|none|none|
|reference_pathology_confirmed_diagnosis|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ReferencePathologyEnum](#schemareferencepathologyenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_tumour_presence|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ReferencePathologyEnum](#schemareferencepathologyenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grading_system|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradingSystemEnum](#schematumourgradingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grade|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradeEnum](#schematumourgradeenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_range|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PercentTumourCellsRangeEnum](#schemapercenttumourcellsrangeenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_measurement_method|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PercentTumourCellsMeasurementMethodEnum](#schemapercenttumourcellsmeasurementmethodenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string|true|none|none|

<h2 id="tocS_SpecimenRequest">SpecimenRequest</h2>

<a id="schemaspecimenrequest"></a>
<a id="schema_SpecimenRequest"></a>
<a id="tocSspecimenrequest"></a>
<a id="tocsspecimenrequest"></a>

```json
{
  "submitter_specimen_id": "string",
  "pathological_tumour_staging_system": "AJCC 8th edition",
  "pathological_t_category": "T0",
  "pathological_n_category": "N0",
  "pathological_m_category": "M0",
  "pathological_stage_group": "Occult Carcinoma",
  "specimen_collection_date": "string",
  "specimen_storage": "Cut slide",
  "tumour_histological_type": "string",
  "specimen_anatomic_location": "string",
  "reference_pathology_confirmed_diagnosis": "Yes",
  "reference_pathology_confirmed_tumour_presence": "Yes",
  "tumour_grading_system": "FNCLCC grading system",
  "tumour_grade": "Low grade",
  "percent_tumour_cells_range": "0-19%",
  "percent_tumour_cells_measurement_method": "Genomics",
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_specimen_id|string|true|none|none|
|pathological_tumour_staging_system|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StagingSystemEnum](#schemastagingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_t_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TCategoryEnum](#schematcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_n_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[NCategoryEnum](#schemancategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_m_category|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MCategoryEnum](#schemamcategoryenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pathological_stage_group|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[StageGroupEnum](#schemastagegroupenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specimen_collection_date|string|true|none|none|
|specimen_storage|[SpecimenStorageEnum](#schemaspecimenstorageenum)|true|none|none|
|tumour_histological_type|string|true|none|none|
|specimen_anatomic_location|string|true|none|none|
|reference_pathology_confirmed_diagnosis|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ReferencePathologyEnum](#schemareferencepathologyenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reference_pathology_confirmed_tumour_presence|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ReferencePathologyEnum](#schemareferencepathologyenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grading_system|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradingSystemEnum](#schematumourgradingsystemenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_grade|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourGradeEnum](#schematumourgradeenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_range|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PercentTumourCellsRangeEnum](#schemapercenttumourcellsrangeenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|percent_tumour_cells_measurement_method|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PercentTumourCellsMeasurementMethodEnum](#schemapercenttumourcellsmeasurementmethodenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string|true|none|none|

<h2 id="tocS_SpecimenStorageEnum">SpecimenStorageEnum</h2>

<a id="schemaspecimenstorageenum"></a>
<a id="schema_SpecimenStorageEnum"></a>
<a id="tocSspecimenstorageenum"></a>
<a id="tocsspecimenstorageenum"></a>

```json
"Cut slide"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Cut slide|
|*anonymous*|Frozen in -70 freezer|
|*anonymous*|Frozen in liquid nitrogen|
|*anonymous*|Frozen in vapour phase|
|*anonymous*|Not Applicable|
|*anonymous*|Other|
|*anonymous*|Paraffin block|
|*anonymous*|RNA later frozen|
|*anonymous*|Unknown|

<h2 id="tocS_SpecimenTissueSourceEnum">SpecimenTissueSourceEnum</h2>

<a id="schemaspecimentissuesourceenum"></a>
<a id="schema_SpecimenTissueSourceEnum"></a>
<a id="tocSspecimentissuesourceenum"></a>
<a id="tocsspecimentissuesourceenum"></a>

```json
"Amniotic fluid"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Amniotic fluid|
|*anonymous*|Bile Fluid|
|*anonymous*|Whole blood|
|*anonymous*|Blood arterial|
|*anonymous*|Cord blood|
|*anonymous*|Blood venous|
|*anonymous*|Bone|
|*anonymous*|Serum, Convalescent|
|*anonymous*|Cerebral spinal fluid|
|*anonymous*|Cervical Mucus|
|*anonymous*|Duodenal fluid|
|*anonymous*|Blood, Fetal|
|*anonymous*|Fluid, Abdomen|
|*anonymous*|Genital vaginal|
|*anonymous*|Fluid, Hydrocele|
|*anonymous*|Fluid, Joint|
|*anonymous*|Fluid, Kidney|
|*anonymous*|Fluid, Lumbar Sac|
|*anonymous*|Marrow|
|*anonymous*|Pancreatic fluid|
|*anonymous*|Fluid, Pericardial|
|*anonymous*|Placenta|
|*anonymous*|Pleural fluid (thoracentesis fluid)|
|*anonymous*|Saliva|
|*anonymous*|Skin|
|*anonymous*|Seminal fluid|
|*anonymous*|Fluid, synovial (Joint fluid)|
|*anonymous*|Sputum|
|*anonymous*|Tissue|
|*anonymous*|Vitreous Fluid|
|*anonymous*|Wound|

<h2 id="tocS_SpecimenTypeEnum">SpecimenTypeEnum</h2>

<a id="schemaspecimentypeenum"></a>
<a id="schema_SpecimenTypeEnum"></a>
<a id="tocSspecimentypeenum"></a>
<a id="tocsspecimentypeenum"></a>

```json
"Cell line - derived from normal"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Cell line - derived from normal|
|*anonymous*|Cell line - derived from metastatic tumour|
|*anonymous*|Cell line - derived from primary tumour|
|*anonymous*|Cell line - derived from xenograft tumour|
|*anonymous*|Metastatic tumour - additional metastatic|
|*anonymous*|Metastatic tumour - metastasis local to lymph node|
|*anonymous*|Metastatic tumour - metastasis to distant location|
|*anonymous*|Metastatic tumour|
|*anonymous*|Normal - tissue adjacent to primary tumour|
|*anonymous*|Normal|
|*anonymous*|Primary tumour - additional new primary|
|*anonymous*|Primary tumour - adjacent to normal|
|*anonymous*|Primary tumour|
|*anonymous*|Recurrent tumour|
|*anonymous*|Xenograft - derived from primary tumour|
|*anonymous*|Xenograft - derived from metastatic tumour|
|*anonymous*|Xenograft - derived from tumour cell line|

<h2 id="tocS_StageGroupEnum">StageGroupEnum</h2>

<a id="schemastagegroupenum"></a>
<a id="schema_StageGroupEnum"></a>
<a id="tocSstagegroupenum"></a>
<a id="tocsstagegroupenum"></a>

```json
"Occult Carcinoma"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Occult Carcinoma|
|*anonymous*|Stage 0|
|*anonymous*|Stage 0a|
|*anonymous*|Stage 0is|
|*anonymous*|Stage 1|
|*anonymous*|Stage 1A|
|*anonymous*|Stage 1B|
|*anonymous*|Stage A|
|*anonymous*|Stage B|
|*anonymous*|Stage C|
|*anonymous*|Stage I|
|*anonymous*|Stage IA|
|*anonymous*|Stage IA1|
|*anonymous*|Stage IA2|
|*anonymous*|Stage IA3|
|*anonymous*|Stage IAB|
|*anonymous*|Stage IAE|
|*anonymous*|Stage IAES|
|*anonymous*|Stage IAS|
|*anonymous*|Stage IB|
|*anonymous*|Stage IB1|
|*anonymous*|Stage IB2|
|*anonymous*|Stage IBE|
|*anonymous*|Stage IBES|
|*anonymous*|Stage IBS|
|*anonymous*|Stage IC|
|*anonymous*|Stage IE|
|*anonymous*|Stage IEA|
|*anonymous*|Stage IEB|
|*anonymous*|Stage IES|
|*anonymous*|Stage II|
|*anonymous*|Stage II bulky|
|*anonymous*|Stage IIA|
|*anonymous*|Stage IIA1|
|*anonymous*|Stage IIA2|
|*anonymous*|Stage IIAE|
|*anonymous*|Stage IIAES|
|*anonymous*|Stage IIAS|
|*anonymous*|Stage IIB|
|*anonymous*|Stage IIBE|
|*anonymous*|Stage IIBES|
|*anonymous*|Stage IIBS|
|*anonymous*|Stage IIC|
|*anonymous*|Stage IIE|
|*anonymous*|Stage IIEA|
|*anonymous*|Stage IIEB|
|*anonymous*|Stage IIES|
|*anonymous*|Stage III|
|*anonymous*|Stage IIIA|
|*anonymous*|Stage IIIA1|
|*anonymous*|Stage IIIA2|
|*anonymous*|Stage IIIAE|
|*anonymous*|Stage IIIAES|
|*anonymous*|Stage IIIAS|
|*anonymous*|Stage IIIB|
|*anonymous*|Stage IIIBE|
|*anonymous*|Stage IIIBES|
|*anonymous*|Stage IIIBS|
|*anonymous*|Stage IIIC|
|*anonymous*|Stage IIIC1|
|*anonymous*|Stage IIIC2|
|*anonymous*|Stage IIID|
|*anonymous*|Stage IIIE|
|*anonymous*|Stage IIIES|
|*anonymous*|Stage IIIS|
|*anonymous*|Stage IIS|
|*anonymous*|Stage IS|
|*anonymous*|Stage IV|
|*anonymous*|Stage IVA|
|*anonymous*|Stage IVA1|
|*anonymous*|Stage IVA2|
|*anonymous*|Stage IVAE|
|*anonymous*|Stage IVAES|
|*anonymous*|Stage IVAS|
|*anonymous*|Stage IVB|
|*anonymous*|Stage IVBE|
|*anonymous*|Stage IVBES|
|*anonymous*|Stage IVBS|
|*anonymous*|Stage IVC|
|*anonymous*|Stage IVE|
|*anonymous*|Stage IVES|
|*anonymous*|Stage IVS|
|*anonymous*|In situ|
|*anonymous*|Localized|
|*anonymous*|Regionalized|
|*anonymous*|Distant|

<h2 id="tocS_StagingSystemEnum">StagingSystemEnum</h2>

<a id="schemastagingsystemenum"></a>
<a id="schema_StagingSystemEnum"></a>
<a id="tocSstagingsystemenum"></a>
<a id="tocsstagingsystemenum"></a>

```json
"AJCC 8th edition"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|AJCC 8th edition|
|*anonymous*|AJCC 7th edition|
|*anonymous*|AJCC 6th edition|
|*anonymous*|Ann Arbor staging system|
|*anonymous*|Binet staging system|
|*anonymous*|Durie-Salmon staging system|
|*anonymous*|FIGO staging system|
|*anonymous*|Lugano staging system|
|*anonymous*|Rai staging system|
|*anonymous*|Revised International staging system (RISS)|
|*anonymous*|SEER staging system|
|*anonymous*|St Jude staging system|

<h2 id="tocS_Surgery">Surgery</h2>

<a id="schemasurgery"></a>
<a id="schema_Surgery"></a>
<a id="tocSsurgery"></a>
<a id="tocssurgery"></a>

```json
{
  "id": 0,
  "surgery_type": "Axillary Clearance",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margin_types_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_assessed": [
    "Circumferential resection margin"
  ],
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "tumour_length": 32767,
  "tumour_width": 32767,
  "greatest_dimension_tumour": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|surgery_type|[SurgeryTypeEnum](#schemasurgerytypeenum)|true|none|none|
|surgery_site|string|true|none|none|
|surgery_location|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SurgeryLocationEnum](#schemasurgerylocationenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_focality|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourFocalityEnum](#schematumourfocalityenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|residual_tumour_classification|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ResidualTumourClassificationEnum](#schemaresidualtumourclassificationenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_types_involved|[oneOf]|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginTypesEnum](#schemamargintypesenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_types_not_involved|[oneOf]|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginTypesEnum](#schemamargintypesenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_types_not_assessed|[oneOf]|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginTypesEnum](#schemamargintypesenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lymphovascular_invasion|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LymphovascularInvasionEnum](#schemalymphovascularinvasionenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|perineural_invasion|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PerineuralInvasionEnum](#schemaperineuralinvasionenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length|integer¦null|false|none|none|
|tumour_width|integer¦null|false|none|none|
|greatest_dimension_tumour|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_specimen_id|string¦null|false|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_SurgeryLocationEnum">SurgeryLocationEnum</h2>

<a id="schemasurgerylocationenum"></a>
<a id="schema_SurgeryLocationEnum"></a>
<a id="tocSsurgerylocationenum"></a>
<a id="tocssurgerylocationenum"></a>

```json
"Local recurrence"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Local recurrence|
|*anonymous*|Metastatic|
|*anonymous*|Primary|

<h2 id="tocS_SurgeryRequest">SurgeryRequest</h2>

<a id="schemasurgeryrequest"></a>
<a id="schema_SurgeryRequest"></a>
<a id="tocSsurgeryrequest"></a>
<a id="tocssurgeryrequest"></a>

```json
{
  "surgery_type": "Axillary Clearance",
  "surgery_site": "string",
  "surgery_location": "Local recurrence",
  "tumour_focality": "Cannot be assessed",
  "residual_tumour_classification": "Not applicable",
  "margin_types_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_involved": [
    "Circumferential resection margin"
  ],
  "margin_types_not_assessed": [
    "Circumferential resection margin"
  ],
  "lymphovascular_invasion": "Absent",
  "perineural_invasion": "Absent",
  "tumour_length": 32767,
  "tumour_width": 32767,
  "greatest_dimension_tumour": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_specimen_id": "string",
  "submitter_treatment_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|surgery_type|[SurgeryTypeEnum](#schemasurgerytypeenum)|true|none|none|
|surgery_site|string|true|none|none|
|surgery_location|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SurgeryLocationEnum](#schemasurgerylocationenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_focality|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[TumourFocalityEnum](#schematumourfocalityenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|residual_tumour_classification|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ResidualTumourClassificationEnum](#schemaresidualtumourclassificationenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_types_involved|[oneOf]|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginTypesEnum](#schemamargintypesenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_types_not_involved|[oneOf]|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginTypesEnum](#schemamargintypesenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_types_not_assessed|[oneOf]|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MarginTypesEnum](#schemamargintypesenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lymphovascular_invasion|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LymphovascularInvasionEnum](#schemalymphovascularinvasionenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|perineural_invasion|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PerineuralInvasionEnum](#schemaperineuralinvasionenum)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BlankEnum](#schemablankenum)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tumour_length|integer¦null|false|none|none|
|tumour_width|integer¦null|false|none|none|
|greatest_dimension_tumour|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_specimen_id|string¦null|false|none|none|
|submitter_treatment_id|string|true|none|none|

<h2 id="tocS_SurgeryTypeEnum">SurgeryTypeEnum</h2>

<a id="schemasurgerytypeenum"></a>
<a id="schema_SurgeryTypeEnum"></a>
<a id="tocSsurgerytypeenum"></a>
<a id="tocssurgerytypeenum"></a>

```json
"Axillary Clearance"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Axillary Clearance|
|*anonymous*|Axillary lymph nodes sampling|
|*anonymous*|Biopsy|
|*anonymous*|Bypass Gastrojejunostomy|
|*anonymous*|Cholecystectomy|
|*anonymous*|Cholecystojejunostomy|
|*anonymous*|Completion gastrectomy|
|*anonymous*|Debridement of pancreatic and peripancreatic necrosis|
|*anonymous*|Debulking|
|*anonymous*|Distal subtotal pancreatectomy|
|*anonymous*|Drainage of abscess|
|*anonymous*|Duodenal preserving pancreatic head resection|
|*anonymous*|Endoscopic biopsy|
|*anonymous*|Endoscopic brushings of GIT|
|*anonymous*|Enucleation|
|*anonymous*|Esophageal bypass surgery/jejunostomy only|
|*anonymous*|Exploratory laparotomy|
|*anonymous*|Fine needle aspiration biopsy|
|*anonymous*|Gastric Antrectomy|
|*anonymous*|Hepaticojejunostomy|
|*anonymous*|Ivor Lewis subtotal esophagectomy|
|*anonymous*|Laparotomy (Open and Shut)|
|*anonymous*|Left thoracoabdominal incision|
|*anonymous*|Lobectomy|
|*anonymous*|Mammoplasty|
|*anonymous*|Mastectomy|
|*anonymous*|McKeown esophagectomy|
|*anonymous*|Merendino procedure|
|*anonymous*|Minimally invasive esophagectomy|
|*anonymous*|Pancreaticoduodenectomy|
|*anonymous*|Pancreaticojejunostomy, side-to-side anastomosis|
|*anonymous*|Pneumonectomy|
|*anonymous*|Proximal subtotal gastrectomy|
|*anonymous*|Pylorus-sparing Whipple operation|
|*anonymous*|Radical pancreaticoduodenectomy|
|*anonymous*|Reexcision|
|*anonymous*|Segmentectomy|
|*anonymous*|Sentinal Lymph Node Biopsy|
|*anonymous*|Spleen preserving distal pancreatectomy|
|*anonymous*|Splenectomy|
|*anonymous*|Subtotal pancreatectomy|
|*anonymous*|Thoracotomy (Open & Shut)|
|*anonymous*|Total gastrectomy|
|*anonymous*|Total gastrectomy with extended lymphadenectomy|
|*anonymous*|Total pancreatectomy|
|*anonymous*|Transhiatal esophagectomy|
|*anonymous*|Triple bypass of pancreas|
|*anonymous*|Wedge/localised gastric resection|
|*anonymous*|Wide Local Excision|

<h2 id="tocS_TCategoryEnum">TCategoryEnum</h2>

<a id="schematcategoryenum"></a>
<a id="schema_TCategoryEnum"></a>
<a id="tocStcategoryenum"></a>
<a id="tocstcategoryenum"></a>

```json
"T0"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|T0|
|*anonymous*|T1|
|*anonymous*|T1a|
|*anonymous*|T1a1|
|*anonymous*|T1a2|
|*anonymous*|T1a(s)|
|*anonymous*|T1a(m)|
|*anonymous*|T1b|
|*anonymous*|T1b1|
|*anonymous*|T1b2|
|*anonymous*|T1b(s)|
|*anonymous*|T1b(m)|
|*anonymous*|T1c|
|*anonymous*|T1d|
|*anonymous*|T1mi|
|*anonymous*|T2|
|*anonymous*|T2(s)|
|*anonymous*|T2(m)|
|*anonymous*|T2a|
|*anonymous*|T2a1|
|*anonymous*|T2a2|
|*anonymous*|T2b|
|*anonymous*|T2c|
|*anonymous*|T2d|
|*anonymous*|T3|
|*anonymous*|T3(s)|
|*anonymous*|T3(m)|
|*anonymous*|T3a|
|*anonymous*|T3b|
|*anonymous*|T3c|
|*anonymous*|T3d|
|*anonymous*|T3e|
|*anonymous*|T4|
|*anonymous*|T4a|
|*anonymous*|T4a(s)|
|*anonymous*|T4a(m)|
|*anonymous*|T4b|
|*anonymous*|T4b(s)|
|*anonymous*|T4b(m)|
|*anonymous*|T4c|
|*anonymous*|T4d|
|*anonymous*|T4e|
|*anonymous*|Ta|
|*anonymous*|Tis|
|*anonymous*|Tis(DCIS)|
|*anonymous*|Tis(LAMN)|
|*anonymous*|Tis(LCIS)|
|*anonymous*|Tis(Paget)|
|*anonymous*|Tis(Paget’s)|
|*anonymous*|Tis pu|
|*anonymous*|Tis pd|
|*anonymous*|TX|

<h2 id="tocS_Treatment">Treatment</h2>

<a id="schematreatment"></a>
<a id="schema_Treatment"></a>
<a id="tocStreatment"></a>
<a id="tocstreatment"></a>

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Ablation"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": "string",
  "treatment_end_date": "string",
  "treatment_setting": "Adjuvant",
  "treatment_intent": "Curative",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "days_per_cycle": 32767,
  "number_of_cycles": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|string|true|none|none|
|treatment_type|[[TreatmentTypeEnum](#schematreatmenttypeenum)]|true|none|none|
|is_primary_treatment|[uBooleanEnum](#schemaubooleanenum)|true|none|none|
|treatment_start_date|string|true|none|none|
|treatment_end_date|string|true|none|none|
|treatment_setting|[TreatmentSettingEnum](#schematreatmentsettingenum)|true|none|none|
|treatment_intent|[TreatmentIntentEnum](#schematreatmentintentenum)|true|none|none|
|response_to_treatment_criteria_method|[ResponseToTreatmentCriteriaMethodEnum](#schemaresponsetotreatmentcriteriamethodenum)|true|none|none|
|response_to_treatment|[ResponseToTreatmentEnum](#schemaresponsetotreatmentenum)|true|none|none|
|days_per_cycle|integer¦null|false|none|none|
|number_of_cycles|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string|true|none|none|

<h2 id="tocS_TreatmentIntentEnum">TreatmentIntentEnum</h2>

<a id="schematreatmentintentenum"></a>
<a id="schema_TreatmentIntentEnum"></a>
<a id="tocStreatmentintentenum"></a>
<a id="tocstreatmentintentenum"></a>

```json
"Curative"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Curative|
|*anonymous*|Palliative|

<h2 id="tocS_TreatmentRequest">TreatmentRequest</h2>

<a id="schematreatmentrequest"></a>
<a id="schema_TreatmentRequest"></a>
<a id="tocStreatmentrequest"></a>
<a id="tocstreatmentrequest"></a>

```json
{
  "submitter_treatment_id": "string",
  "treatment_type": [
    "Ablation"
  ],
  "is_primary_treatment": "Yes",
  "treatment_start_date": "string",
  "treatment_end_date": "string",
  "treatment_setting": "Adjuvant",
  "treatment_intent": "Curative",
  "response_to_treatment_criteria_method": "RECIST 1.1",
  "response_to_treatment": "Complete response",
  "days_per_cycle": 32767,
  "number_of_cycles": 32767,
  "program_id": "string",
  "submitter_donor_id": "string",
  "submitter_primary_diagnosis_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|submitter_treatment_id|string|true|none|none|
|treatment_type|[[TreatmentTypeEnum](#schematreatmenttypeenum)]|true|none|none|
|is_primary_treatment|[uBooleanEnum](#schemaubooleanenum)|true|none|none|
|treatment_start_date|string|true|none|none|
|treatment_end_date|string|true|none|none|
|treatment_setting|[TreatmentSettingEnum](#schematreatmentsettingenum)|true|none|none|
|treatment_intent|[TreatmentIntentEnum](#schematreatmentintentenum)|true|none|none|
|response_to_treatment_criteria_method|[ResponseToTreatmentCriteriaMethodEnum](#schemaresponsetotreatmentcriteriamethodenum)|true|none|none|
|response_to_treatment|[ResponseToTreatmentEnum](#schemaresponsetotreatmentenum)|true|none|none|
|days_per_cycle|integer¦null|false|none|none|
|number_of_cycles|integer¦null|false|none|none|
|program_id|string|true|none|none|
|submitter_donor_id|string|true|none|none|
|submitter_primary_diagnosis_id|string|true|none|none|

<h2 id="tocS_TreatmentSettingEnum">TreatmentSettingEnum</h2>

<a id="schematreatmentsettingenum"></a>
<a id="schema_TreatmentSettingEnum"></a>
<a id="tocStreatmentsettingenum"></a>
<a id="tocstreatmentsettingenum"></a>

```json
"Adjuvant"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Adjuvant|
|*anonymous*|Advanced/Metastatic|
|*anonymous*|Neoadjuvant|
|*anonymous*|Not applicable|

<h2 id="tocS_TreatmentTypeEnum">TreatmentTypeEnum</h2>

<a id="schematreatmenttypeenum"></a>
<a id="schema_TreatmentTypeEnum"></a>
<a id="tocStreatmenttypeenum"></a>
<a id="tocstreatmenttypeenum"></a>

```json
"Ablation"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Ablation|
|*anonymous*|Bone marrow transplant|
|*anonymous*|Chemotherapy|
|*anonymous*|Endoscopic therapy|
|*anonymous*|Hormonal therapy|
|*anonymous*|Immunotherapy|
|*anonymous*|No treatment|
|*anonymous*|Other targeting molecular therapy|
|*anonymous*|Photodynamic therapy|
|*anonymous*|Radiation therapy|
|*anonymous*|Stem cell transplant|
|*anonymous*|Surgery|

<h2 id="tocS_TumourFocalityEnum">TumourFocalityEnum</h2>

<a id="schematumourfocalityenum"></a>
<a id="schema_TumourFocalityEnum"></a>
<a id="tocStumourfocalityenum"></a>
<a id="tocstumourfocalityenum"></a>

```json
"Cannot be assessed"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Cannot be assessed|
|*anonymous*|Multifocal|
|*anonymous*|Not applicable|
|*anonymous*|Unifocal|
|*anonymous*|Unknown|

<h2 id="tocS_TumourGradeEnum">TumourGradeEnum</h2>

<a id="schematumourgradeenum"></a>
<a id="schema_TumourGradeEnum"></a>
<a id="tocStumourgradeenum"></a>
<a id="tocstumourgradeenum"></a>

```json
"Low grade"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Low grade|
|*anonymous*|High grade|
|*anonymous*|GX|
|*anonymous*|G1|
|*anonymous*|G2|
|*anonymous*|G3|
|*anonymous*|G4|
|*anonymous*|Low|
|*anonymous*|High|
|*anonymous*|Grade I|
|*anonymous*|Grade II|
|*anonymous*|Grade III|
|*anonymous*|Grade IV|
|*anonymous*|Grade Group 1|
|*anonymous*|Grade Group 2|
|*anonymous*|Grade Group 3|
|*anonymous*|Grade Group 4|
|*anonymous*|Grade Group 5|

<h2 id="tocS_TumourGradingSystemEnum">TumourGradingSystemEnum</h2>

<a id="schematumourgradingsystemenum"></a>
<a id="schema_TumourGradingSystemEnum"></a>
<a id="tocStumourgradingsystemenum"></a>
<a id="tocstumourgradingsystemenum"></a>

```json
"FNCLCC grading system"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|FNCLCC grading system|
|*anonymous*|Four-tier grading system|
|*anonymous*|Gleason grade group system|
|*anonymous*|Grading system for GISTs|
|*anonymous*|Grading system for GNETs|
|*anonymous*|ISUP grading system|
|*anonymous*|Nuclear grading system for DCIS|
|*anonymous*|Scarff-Bloom-Richardson grading system|
|*anonymous*|Three-tier grading system|
|*anonymous*|Two-tier grading system|
|*anonymous*|WHO grading system for CNS tumours|

<h2 id="tocS_TumourNormalDesignationEnum">TumourNormalDesignationEnum</h2>

<a id="schematumournormaldesignationenum"></a>
<a id="schema_TumourNormalDesignationEnum"></a>
<a id="tocStumournormaldesignationenum"></a>
<a id="tocstumournormaldesignationenum"></a>

```json
"Normal"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Normal|
|*anonymous*|Tumour|

<h2 id="tocS_moh_overview_schema_response">moh_overview_schema_response</h2>

<a id="schemamoh_overview_schema_response"></a>
<a id="schema_moh_overview_schema_response"></a>
<a id="tocSmoh_overview_schema_response"></a>
<a id="tocsmoh_overview_schema_response"></a>

```json
{
  "cohort_count": 0,
  "individual_count": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cohort_count|integer|true|none|none|
|individual_count|integer|true|none|none|

<h2 id="tocS_uBooleanEnum">uBooleanEnum</h2>

<a id="schemaubooleanenum"></a>
<a id="schema_uBooleanEnum"></a>
<a id="tocSubooleanenum"></a>
<a id="tocsubooleanenum"></a>

```json
"Yes"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Yes|
|*anonymous*|No|
|*anonymous*|Unknown|

