# Small dataset relationships

The small dataset is composed of:
* 4 Programs
* 20 Follow Ups
* 40 Comorbidities, Biomarkers, Exposures
* 80 Donors, Primary Diagnoses, Specimens, Radiations, Surgeries
* 160 Treatments
* 240 Sample registrations
* 320 Systemic Therapies

Sub-objects are iterated over and assigned evenly to a parent object until all objects are exhausted. Identifiers show the pattern in the diagrams below.

Diagrams below show example linkage relationships for the different objects.

---

## Sample Registrations, Specimens and Primary Diagnoses to Donors

Each donor has one primary diagnosis, each primary diagnosis has one specimen, each specimen has three samples.

```mermaid
---
title: Samples, Specimens, Diagnoses, Donors, Programs
---
graph LR;  
  SPECIMEN_0001 --> DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  SPECIMEN_0005 --> DIAG_0005 --> DONOR_0005 --> PROGRAM_01;  
  SPECIMEN_0002 --> DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  SPECIMEN_0003 --> DIAG_0003 --> DONOR_0003 --> PROGRAM_03;  
  SPECIMEN_0004 --> DIAG_0004 --> DONOR_0004 --> PROGRAM_04;
  SPECIMEN_0008 --> DIAG_0008 --> DONOR_0008 --> PROGRAM_04;
  SAMPLE_0001--> SPECIMEN_0001; 
  SAMPLE_0081--> SPECIMEN_0001;  
  SAMPLE_0161--> SPECIMEN_0001;  
  SAMPLE_0005--> SPECIMEN_0005;  
  SAMPLE_0085--> SPECIMEN_0005;  
  SAMPLE_0165--> SPECIMEN_0005;  
  SAMPLE_0002--> SPECIMEN_0002;  
  SAMPLE_0082--> SPECIMEN_0002;  
  SAMPLE_0162--> SPECIMEN_0002;  
  SAMPLE_0003--> SPECIMEN_0003;  
  SAMPLE_0083--> SPECIMEN_0003;  
  SAMPLE_0163--> SPECIMEN_0003;  
  SAMPLE_0004--> SPECIMEN_0004;
  SAMPLE_0084--> SPECIMEN_0004;
  SAMPLE_0164--> SPECIMEN_0004;
  SAMPLE_0008--> SPECIMEN_0008;
  SAMPLE_0088--> SPECIMEN_0008;
  SAMPLE_0168--> SPECIMEN_0008;
```

---

## Treatments and treatment types

Each diagnosis has two treatments, each treatment has two systemic therapies and either a radiation or surgery.

```mermaid
---
title: Surgeries, Radiations, Systemic therapies, Treatments, Diagnoses, Donors
---
graph LR;  
  DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  DIAG_0003 --> DONOR_0003 --> PROGRAM_03;  
  DIAG_0004 --> DONOR_0004 --> PROGRAM_04;
  TREATMENT_0001 --> DIAG_0001;
  TREATMENT_0081 --> DIAG_0001;  
  TREATMENT_0002 --> DIAG_0002; 
  TREATMENT_0082 --> DIAG_0002;  
  TREATMENT_0003 --> DIAG_0003; 
  TREATMENT_0083 --> DIAG_0003; 
  TREATMENT_0004 --> DIAG_0004; 
  TREATMENT_0084 --> DIAG_0004; 
  SYS_THERAPY_uuid1a --> TREATMENT_0001;
  SYS_THERAPY_uuid1b --> TREATMENT_0001;
  SYS_THERAPY_uuid2a --> TREATMENT_0081;
  SYS_THERAPY_uuid2b --> TREATMENT_0081;  
  SYS_THERAPY_uuid3a --> TREATMENT_0002; 
  SYS_THERAPY_uuid3b --> TREATMENT_0002; 
  SYS_THERAPY_uuid4a --> TREATMENT_0082;  
  SYS_THERAPY_uuid4b --> TREATMENT_0082;  
  SYS_THERAPY_uuid5a --> TREATMENT_0003; 
  SYS_THERAPY_uuid5b --> TREATMENT_0003; 
  SYS_THERAPY_uuid6a --> TREATMENT_0083; 
  SYS_THERAPY_uuid6b --> TREATMENT_0083; 
  SYS_THERAPY_uuid7a --> TREATMENT_0004; 
  SYS_THERAPY_uuid7b --> TREATMENT_0004; 
  SYS_THERAPY_uuid8a --> TREATMENT_0084;
  SYS_THERAPY_uuid8b --> TREATMENT_0084;
  RADIATION_uuid1 --> TREATMENT_0001;
  RADIATION_uuid2 --> TREATMENT_0002; 
  RADIATION_uuid3 --> TREATMENT_0003;  
  RADIATION_uuid4 --> TREATMENT_0004;  
  SURGERY_uuid1 --> TREATMENT_0081;
  SURGERY_uuid2 --> TREATMENT_0082; 
  SURGERY_uuid3 --> TREATMENT_0083;  
  SURGERY_uuid4 --> TREATMENT_0084;  
```

---

## Follow ups

Follow ups is linked to Donor only or to Donor plus either a Primary Diagnosis or Treatment.

```mermaid
---
title: 20 FollowUps, linked to either donor +/- primary diagnosis or treatment
---
graph LR;  
  DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  DIAG_0003 --> DONOR_0003 --> PROGRAM_03;  
  DIAG_0004 --> DONOR_0004 --> PROGRAM_04;
  TREATMENT_0001 --> DIAG_0001; 
  TREATMENT_0002 --> DIAG_0002; 
  TREATMENT_0082 --> DIAG_0002;  
  TREATMENT_0003 --> DIAG_0003; 
  TREATMENT_0083 --> DIAG_0003; 
  TREATMENT_0004 --> DIAG_0004; 
  FOLLOW_UP_0001 --> DONOR_0001;  
  FOLLOW_UP_0002 --> DIAG_0002;
  FOLLOW_UP_0002 --> DONOR_0002; 
  FOLLOW_UP_0003 --> DONOR_0003; 
  FOLLOW_UP_0003 --> TREATMENT_0003;  
  FOLLOW_UP_0004 --> DONOR_0004
  
```

---

## Biomarkers, Comorbidities, Exposures to Donors

Biomarkers may be linked to Donor alone or Donor plus treatment, primary diagnosis, specimen or followup. Synthetic data is only linked to Donors for now. Half of donors have a linked biomarker object. Comorbidities are linked directly to Donors, half of the donors in the dataset have a linked comorbidity. Exposures are linked directly to Donors, half of donors have a linked exposure.

```mermaid
---
title: Biomarkers, Comorbidities, Exposures
---
graph LR;  
  BIOMARKER_uuid1 --> DONOR_0001 --> PROGRAM_01; 
  EXPOSURE_uuid1 --> DONOR_0021 --> PROGRAM_01;  
  BIOMARKER_uuid2 --> DONOR_0021;
  COMORBIDITY_uuid1 --> DONOR_0041 --> PROGRAM_01;
  EXPOSURE_uuid2 --> DONOR_0041;
  BIOMARKER_uuid3 --> DONOR_0002 --> PROGRAM_02;  
  EXPOSURE_uuid3 --> DONOR_0022 --> PROGRAM_02;
  BIOMARKER_uuid4 --> DONOR_0022;
  COMORBIDITY_uuid2 --> DONOR_0042 --> PROGRAM_02;
  EXPOSURE_uuid4 --> DONOR_0042;
  BIOMARKER_uuid5 --> DONOR_0003 --> PROGRAM_03;
  EXPOSURE_uuid5 --> DONOR_0023 --> PROGRAM_03;
  BIOMARKER_uuid6 --> DONOR_0023;
  COMORBIDITY_uuid3 --> DONOR_0043 --> PROGRAM_03;  
  EXPOSURE_uuid6 --> DONOR_0043;
  BIOMARKER_uuid7 --> DONOR_0004 --> PROGRAM_04;
  EXPOSURE_uuid7 --> DONOR_0024 --> PROGRAM_04;
  BIOMARKER_uuid8 --> DONOR_0024;
  COMORBIDITY_uuid4 --> DONOR_0044 --> PROGRAM_04;
  EXPOSURE_uuid8 --> DONOR_0044;
```

---
