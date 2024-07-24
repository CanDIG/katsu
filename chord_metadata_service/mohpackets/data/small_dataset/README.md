# Small dataset relationships

The small dataset is composed of:
* 4 Programs
* 20 Follow Ups
* 40 Comorbidities, Biomarkers, Exposures
* 80 Donors, Primary Diagnoses, Specimens, Radiations, Surgeries
* 160 Treatments
* 240 Sample registrations
* 320 Systemic Therapies

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
  SPECIMEN_0001_0020 --> DIAG_0001_0020 --> DONOR_0001_0020 --> PROGRAM_01;  
  SPECIMEN_00021_0040 --> DIAG_0021_40 --> DONOR_0021_40 --> PROGRAM_02;
  SPECIMEN_00041_0060 --> DIAG_0041_60 --> DONOR_0041_60 --> PROGRAM_03;
  SPECIMEN_00061_0080 --> DIAG_0061_80 --> DONOR_0061_80 --> PROGRAM_04;  
  SAMPLE_0001_0060--> SPECIMEN_0001_0020;
  SAMPLE_0061_0120--> SPECIMEN_00021_0040;
  SAMPLE_0121_0180--> SPECIMEN_00041_0060;
  SAMPLE_0181_0240--> SPECIMEN_00061_0080;
```

Each Specimen has three linked samples, example below with SPECIMEN_0001

```mermaid
graph LR;
  SAMPLE_0001 --> SPECIMEN_0001;
  SAMPLE_0002 --> SPECIMEN_0001;
  SAMPLE_0003 --> SPECIMEN_0001;
  SPECIMEN_0001 --> DONOR_0001 --> PROGRAM_01;
```

---

## Treatments and treatment types

Each diagnosis has two treatments, 

```mermaid
---
title: Treatments, Diagnoses, Donors
---
graph LR;  
  DIAG_0001_0020 --> DONOR_0001_0020 --> PROGRAM_01;  
  DIAG_0021_0040 --> DONOR_0021_0040 --> PROGRAM_03;  
  DIAG_0041_0060 --> DONOR_0041_0060 --> PROGRAM_03;  
  DIAG_0061_0080 --> DONOR_0061_0080 --> PROGRAM_04;
  TREATMENT_0001_0040 --> DIAG_0001_0020;
  TREATMENT_0021_0040 --> DIAG_0021_0040;  
  TREATMENT_0041_0060 --> DIAG_0041_0060; 
  TREATMENT_0061_0080 --> DIAG_0061_0080;
```
Each Diagnosis has two linked treatments, example below with DIAG_0001

```mermaid
graph LR;
  TREATMENT_0001 --> DIAG_0001;
  TREATMENT_0002 --> DIAG_0001;
  DIAG_0001 --> DONOR_0001 --> PROGRAM_01;
```

Each treatment has two systemic therapies and either a radiation or surgery.

```mermaid
graph LR;
  SYS_THERAPY_uuid1_80 --> TREATMENT_0001_0040;
  SYS_THERAPY_uuid81_160 --> TREATMENT_0041_80;
  SYS_THERAPY_uuid161_240 --> TREATMENT_0081_120;
  SYS_THERAPY_uuid241_320 --> TREATMENT_0121_160;  
  RADIATION_uuid1_20 --> TREATMENT_0002_0040_even_numbers;
  RADIATION_uuid21_40 --> TREATMENT_0042_0080_even_numbers; 
  RADIATION_uuid41_60 --> TREATMENT_0082_0120_even_numbers;  
  RADIATION_uuid61_80 --> TREATMENT_0122_0160_even_numbers;  
  SURGERY_uuid1_20 --> TREATMENT_0001_0039_odd_numbers;
  SURGERY_uuid21_40 --> TREATMENT_0041_0079_odd_numbers; 
  SURGERY_uuid41_60 --> TREATMENT_081_0119_odd_numbers;  
  SURGERY_uuid61_80 --> TREATMENT_0121_0159_odd_numbers;  
```

Radiations are linked to the even numbered treatments while Surgeries are linked to odd numbered treatments. Example with `TREATMENT_0001` below:

```mermaid
graph LR;
  TREATMENT_0001 --> DIAG_0001;
  TREATMENT_0002 --> DIAG_0001;
  DIAG_0001 --> DONOR_0001 --> PROGRAM_01;
  SYS_THERAPY_uuid1 --> TREATMENT_0001;
  SYS_THERAPY_uuid2 --> TREATMENT_0001;
  SYS_THERAPY_uuid3 --> TREATMENT_0002;
  SYS_THERAPY_uuid4 --> TREATMENT_0002;
  SURGERY_uuid1 --> TREATMENT_0001;
  RADIATION_uuid1 --> TREATMENT_0002;
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
