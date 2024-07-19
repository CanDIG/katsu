# Medium dataset relationships

The medium dataset is composed of:
* 4 Programs
* 200 Follow Ups
* 400 Comorbidities, Biomarkers, Exposures
* 800 Donors, Primary Diagnoses, Specimens, Radiations, Surgeries
* 1600 Treatments
* 2400 Sample registrations
* 3200 Systemic Therapies

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
  SAMPLE_0801--> SPECIMEN_0001;  
  SAMPLE_1601--> SPECIMEN_0001;  
  SAMPLE_0005--> SPECIMEN_0005;  
  SAMPLE_0805--> SPECIMEN_0005;  
  SAMPLE_1605--> SPECIMEN_0005;  
  SAMPLE_0002--> SPECIMEN_0002;  
  SAMPLE_0802--> SPECIMEN_0002;  
  SAMPLE_1602--> SPECIMEN_0002;  
  SAMPLE_0003--> SPECIMEN_0003;  
  SAMPLE_0803--> SPECIMEN_0003;  
  SAMPLE_1603--> SPECIMEN_0003;  
  SAMPLE_0004--> SPECIMEN_0004;
  SAMPLE_0804--> SPECIMEN_0004;
  SAMPLE_1604--> SPECIMEN_0004;
  SAMPLE_0008--> SPECIMEN_0008;
  SAMPLE_0808--> SPECIMEN_0008;
  SAMPLE_1608--> SPECIMEN_0008;
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
  TREATMENT_0801 --> DIAG_0001;  
  TREATMENT_0002 --> DIAG_0002; 
  TREATMENT_0802 --> DIAG_0002;  
  TREATMENT_0003 --> DIAG_0003; 
  TREATMENT_0803 --> DIAG_0003; 
  TREATMENT_0004 --> DIAG_0004; 
  TREATMENT_0804 --> DIAG_0004; 
  SYS_THERAPY_uuid1a --> TREATMENT_0001;
  SYS_THERAPY_uuid1b --> TREATMENT_0001;
  SYS_THERAPY_uuid2a --> TREATMENT_0801;
  SYS_THERAPY_uuid2b --> TREATMENT_0801;  
  SYS_THERAPY_uuid3a --> TREATMENT_0002; 
  SYS_THERAPY_uuid3b --> TREATMENT_0002; 
  SYS_THERAPY_uuid4a --> TREATMENT_0802;  
  SYS_THERAPY_uuid4b --> TREATMENT_0802;  
  SYS_THERAPY_uuid5a --> TREATMENT_0003; 
  SYS_THERAPY_uuid5b --> TREATMENT_0003; 
  SYS_THERAPY_uuid6a --> TREATMENT_0803; 
  SYS_THERAPY_uuid6b --> TREATMENT_0803; 
  SYS_THERAPY_uuid7a --> TREATMENT_0004; 
  SYS_THERAPY_uuid7b --> TREATMENT_0004; 
  SYS_THERAPY_uuid8a --> TREATMENT_0804;
  SYS_THERAPY_uuid8b --> TREATMENT_0804;
  RADIATION_uuid1 --> TREATMENT_0001;
  RADIATION_uuid2 --> TREATMENT_0002; 
  RADIATION_uuid3 --> TREATMENT_0003;  
  RADIATION_uuid4 --> TREATMENT_0004;  
  SURGERY_uuid1 --> TREATMENT_0801;
  SURGERY_uuid2 --> TREATMENT_0802; 
  SURGERY_uuid3 --> TREATMENT_0803;  
  SURGERY_uuid4 --> TREATMENT_0804;  
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
  TREATMENT_0802 --> DIAG_0002;  
  TREATMENT_0003 --> DIAG_0003; 
  TREATMENT_0803 --> DIAG_0003; 
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
  EXPOSURE_uuid1 --> DONOR_0201 --> PROGRAM_01;  
  BIOMARKER_uuid2 --> DONOR_0201;
  COMORBIDITY_uuid1 --> DONOR_0401 --> PROGRAM_01;
  EXPOSURE_uuid2 --> DONOR_0401;
  BIOMARKER_uuid3 --> DONOR_0002 --> PROGRAM_02;  
  EXPOSURE_uuid3 --> DONOR_0202 --> PROGRAM_02;
  BIOMARKER_uuid4 --> DONOR_0202;
  COMORBIDITY_uuid2 --> DONOR_0402 --> PROGRAM_02;
  EXPOSURE_uuid4 --> DONOR_0402;
  BIOMARKER_uuid5 --> DONOR_0003 --> PROGRAM_03;
  EXPOSURE_uuid5 --> DONOR_0203 --> PROGRAM_03;
  BIOMARKER_uuid6 --> DONOR_0203;
  COMORBIDITY_uuid3 --> DONOR_0403 --> PROGRAM_03;  
  EXPOSURE_uuid6 --> DONOR_0403;
  BIOMARKER_uuid7 --> DONOR_0004 --> PROGRAM_04;
  EXPOSURE_uuid7 --> DONOR_0204 --> PROGRAM_04;
  BIOMARKER_uuid8 --> DONOR_0204;
  COMORBIDITY_uuid4 --> DONOR_0404 --> PROGRAM_04;
  EXPOSURE_uuid8 --> DONOR_0404;
```

---
