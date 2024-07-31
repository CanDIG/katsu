# Extra-small dataset relationships

The small dataset is composed of:
* 2 Programs
* 12 Donors, Primary Diagnoses, Specimens, Radiations, Surgeries
* 8 Follow Ups
* 6 Comorbidities, Biomarkers, Exposures
* 24 Treatments
* 36 Sample registrations
* 72 Systemic Therapies

Identifiers are numbered sequentially per object.

Diagrams below show example linkage relationships for the different objects.

---

## Sample Registrations, Specimens and Primary Diagnoses to Donors

Each donor has one primary diagnosis, each primary diagnosis has one specimen, each specimen has three samples.

```mermaid
---
title: Samples, Specimens, Diagnoses, Donors, Programs
---
graph LR;  
  SPECIMEN_0001_5 --> DIAG_0001_5 --> DONOR_0001_5 --> SYNTH_01;  
  SPECIMEN_ALL_0001 --> DIAG_ALL_0001 --> DONOR_ALL_0001 --> SYNTH_01;
  SPECIMEN_NULL_0001 --> DIAG_NULL_0001 --> DONOR_NULL_0001 --> SYNTH_01;
  SAMPLE_0001_15--> SPECIMEN_0001_5;
  SAMPLE_0016_30--> SPECIMEN_0006_10;
  SAMPLE_ALL_0001_3--> SPECIMEN_ALL_0001;
  SAMPLE_NULL_0001_3--> SPECIMEN_NULL_0001;
```

Each Specimen has three linked samples, example below with SPECIMEN_0001

```mermaid
graph LR;
  SAMPLE_0001 --> SPECIMEN_0001;
  SAMPLE_0002 --> SPECIMEN_0001;
  SAMPLE_0003 --> SPECIMEN_0001;
  SPECIMEN_0001 --> DIAG_0001 --> DONOR_0001 --> SYNTH_01;
```
---

## Treatments and treatment types

Each diagnosis has two treatments, 

```mermaid
---
title: Treatments, Diagnoses, Donors
---
graph LR;  
  DIAG_0001_5 --> DONOR_0001_5 --> SYNTH_01;  
  DIAG_0006_10 --> DONOR_0006_10 --> SYNTH_02;  
  TREATMENT_0001_10 --> DIAG_0001_5;
  TREATMENT_0011_20 --> DIAG_0006_10;  
  TREATMENT_ALL_0001_2 --> DIAG_ALL_0001 --> DONOR_ALL_0001 --> SYNTH_01;
  TREATMENT_NULL_0001_2 --> DIAG_NULL_0001 --> DONOR_NULL_0001 --> SYNTH_01;
```
Each Diagnosis has two linked treatments, example below with DIAG_0001

```mermaid
graph LR;
  TREATMENT_0001 --> DIAG_0001;
  TREATMENT_0002 --> DIAG_0001;
  DIAG_0001 --> DONOR_0001 --> SYNTH_01;
```

Each treatment has two systemic therapies and either a radiation or surgery.

```mermaid
graph LR;
  SYS_THERAPY_uuid1_20 --> TREATMENT_0001_10;
  SYS_THERAPY_uuid21_40 --> TREATMENT_0011_20;
  SYS_THERAPY_uuid41_44 --> TREATMENT_ALL_0001_2;
  SYS_THERAPY_uuid45_48 --> TREATMENT_NULL_0001_2
```

```mermaid
graph LR;  
  RADIATION_uuid1_10 --> TREATMENT_0002_10_even_numbers;
  RADIATION_uuid11_20 --> TREATMENT_0012_0020_even_numbers; 
  RADIATION_uuid21 --> TREATMENT_ALL_0002;
  RADIATION_uuid22 --> TREATMENT_NULL_0002; 
  SURGERY_uuid1_10 --> TREATMENT_0001_9_odd_numbers;
  SURGERY_uuid11_20 --> TREATMENT_0011_0019_odd_numbers;
  SURGERY_uuid21 --> TREATMENT_ALL_0001;  
  SURGERY_uuid22 --> TREATMENT_NULL_0001;  
```

Radiations are linked to the even numbered treatments while Surgeries are linked to odd numbered treatments. Example with `TREATMENT_0001` below:

```mermaid
graph LR;
  TREATMENT_0001 --> DIAG_0001;
  TREATMENT_0002 --> DIAG_0001;
  DIAG_0001 --> DONOR_0001 --> SYNTH_01;
  SYS_THERAPY_uuid1 --> TREATMENT_0001;
  SYS_THERAPY_uuid2 --> TREATMENT_0001;
  SYS_THERAPY_uuid3 --> TREATMENT_0002;
  SYS_THERAPY_uuid4 --> TREATMENT_0002;
  SURGERY_uuid1 --> TREATMENT_0001;
  RADIATION_uuid1 --> TREATMENT_0002;
```

---

## Follow ups

Follow ups are linked to the first 3 donors of each program. 


```mermaid
graph LR;  
  DIAG_0001 --> DONOR_0001 --> SYNTH_01;
  DIAG_0002 --> DONOR_0002 --> SYNTH_01;
  DIAG_0003 --> DONOR_0003 --> SYNTH_01;
  FOLLOW_UP_0001 --> DONOR_0001;
  FOLLOW_UP_0001 --> DIAG_0001;
  FOLLOW_UP_0002 --> DONOR_0002;
  FOLLOW_UP_0002 --> TREATMENT_0003 --> DIAG_0002;
  FOLLOW_UP_0003 --> DONOR_0003;
  
  DIAG_0006 --> DONOR_0006 --> SYNTH_01;
  DIAG_0007 --> DONOR_0007 --> SYNTH_01;
  DIAG_0008 --> DONOR_0008 --> SYNTH_01;
  FOLLOW_UP_0004 --> DONOR_0006;
  FOLLOW_UP_0004 --> DIAG_0006;
  FOLLOW_UP_0005 --> TREATMENT_0013 --> DIAG_0007;
  FOLLOW_UP_0005 --> DONOR_0007;
  FOLLOW_UP_0006 --> DONOR_0008;
  
  DIAG_NULL_0001 --> DONOR_NULL_0001 --> SYNTH_01;
  DIAG_ALL_0001 --> DONOR_ALL_0001 --> SYNTH_01;
  FOLLOW_UP_NULL_0001 --> DONOR_NULL_0001;
  FOLLOW_UP_NULL_0001 --> DIAG_NULL_0001;
  FOLLOW_UP_ALL_0001 --> DONOR_ALL_0001;
  FOLLOW_UP_ALL_0001 --> DIAG_ALL_0001;
  
  
```

---

## Biomarkers, Comorbidities, Exposures to Donors

Synthetic data is only links Biomarkers to Donors Only. 

The first 3 donors have a linked biomarker objects

The second 3 donors have a linked comorbidity object

Exposures are linked to the 'middle' 3 donors, sometimes linked with comorbidities, sometimes with biomarkers

```mermaid
graph LR;  
  BIOMARKER_uuid1 --> DONOR_0001 --> SYNTH_01;
  BIOMARKER_uuid2 --> DONOR_0002 --> SYNTH_01;
  BIOMARKER_uuid3 --> DONOR_0003 --> SYNTH_01;
  BIOMARKER_uuid4 --> DONOR_0006 --> SYNTH_01;
  BIOMARKER_uuid5 --> DONOR_0007 --> SYNTH_01;
  BIOMARKER_uuid6 --> DONOR_0008 --> SYNTH_01;
  BIOMARKER_uuid7 --> DONOR_NULL_0001 --> SYNTH_01;
  BIOMARKER_uuid8 --> DONOR_ALL_0001 --> SYNTH_01;
  
  COMORBIDITY_uuid1 --> DONOR_0004 --> SYNTH_01;
  COMORBIDITY_uuid2 --> DONOR_0005 --> SYNTH_01;
  COMORBIDITY_uuid4 --> DONOR_0009 --> SYNTH_01;
  COMORBIDITY_uuid5 --> DONOR_0010 --> SYNTH_01;
  COMORBIDITY_uuid6 --> DONOR_ALL_0001 --> SYNTH_01;
  
  EXPOSURE_uuid1 --> DONOR_0003 --> SYNTH_01;
  EXPOSURE_uuid2 --> DONOR_0004 --> SYNTH_01;
  EXPOSURE_uuid3 --> DONOR_0008 --> SYNTH_01;
  EXPOSURE_uuid4 --> DONOR_0009 --> SYNTH_01;
  EXPOSURE_uuid5 --> DONOR_ALL_0001 --> SYNTH_01;
```
---