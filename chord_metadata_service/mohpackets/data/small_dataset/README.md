# Small dataset relationships

The small dataset is composed of:
* 4 programs
* 20 Follow Ups
* 30 Exposures
* 40 Comorbidities, Biomarkers
* 80 Donors, Primary Diagnoses, Specimens, Radiations, Surgeries
* 160 TREATMENTs
* 240 Sample registrations
* 320 Systemic Therapies

Sub-objects are iterated over and assigned evenly to a parent object until all objects are exhausted. Identifiers show the pattern in the diagrams below.

Diagrams below show example linkage relationships for the different objects.

20 donors per program.

## Donors to Programs

```mermaid
---
title: 80 DONORs and 4 PROGRAMs, 20 donors per program
---
graph LR;  
  DONOR_0001,0005,0009,0013_0077 --> PROGRAM_01;  
  DONOR_0002,0006,0010,0014_0078 --> PROGRAM_02;
  DONOR_0003,0007,0011,0015_0079 --> PROGRAM_03;
  DONOR_0004,0008,0012,0016_0080 --> PROGRAM_04;
```

---

## Primary Diagnoses to Donors to Programs

```mermaid
---
title: 80 PrimaryDiagnoses, 1 Primary Diagnosis per Donor
---
graph LR;  
  DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  DIAG_0005 --> DONOR_0005 --> PROGRAM_01;  
  DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  DIAG_0003 --> DONOR_0003 --> PROGRAM_03;  
  DIAG_0004 --> DONOR_0004 --> PROGRAM_04;
  DIAG_0008 --> DONOR_0008 --> PROGRAM_04;
```

---

## Specimens to Primary Diagnoses to Donors to programs

```mermaid
---
title: 80 Specimens, 1 per Donor
---
graph LR;  
  SPECIMEN_0001 --> DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  SPECIMEN_0005 --> DIAG_0005 --> DONOR_0005 --> PROGRAM_01;  
  SPECIMEN_0002 --> DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  SPECIMEN_0003 --> DIAG_0003 --> DONOR_0003 --> PROGRAM_03;  
  SPECIMEN_0004 --> DIAG_0004 --> DONOR_0004 --> PROGRAM_04;
  SPECIMEN_0008 --> DIAG_0008 --> DONOR_0008 --> PROGRAM_04;
```

---

## Sample Registrations to Specimens to Primary Diagnoses to Donors to Programs

```mermaid
---
title: 240 SampleRegistrations, 3 per specimen
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

## Treatments to Primary Diagnoses to Donors to Programs

```mermaid
---
title: 160 TREATMENTs, 2 per Primary Diagnosis, examples
---
graph LR;  
  DIAG_0001 --> DONOR_0001 --> PROGRAM_01;   
  DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  DIAG_0003 --> DONOR_0003 --> PROGRAM_03;  
  DIAG_0004 --> DONOR_0004 --> PROGRAM_04;
  DIAG_0008 --> DONOR_0008 --> PROGRAM_04;
  TREATMENT_0001 --> DIAG_0001;
  TREATMENT_0081 --> DIAG_0001;  
  TREATMENT_0002 --> DIAG_0002; 
  TREATMENT_0082 --> DIAG_0002;  
  TREATMENT_0003 --> DIAG_0003; 
  TREATMENT_0083 --> DIAG_0003; 
  TREATMENT_0004 --> DIAG_0004; 
  TREATMENT_0084 --> DIAG_0004; 
  TREATMENT_0008 --> DIAG_0008; 
  TREATMENT_0088 --> DIAG_0008; 
```

---

## Systemic therapies to Treatments to Primary Diagnoses to Donors to Programs

```mermaid
---
title: 320 Systemic Therapies, 2 per Treatment
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
```

---

## Radiations, Systemic therapies to Treatments to Primary Diagnoses to Donors to Programs

```mermaid
---
title: 80 Radiations, 1 for half of treatments
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
```

---

## Surgeries, Radiations, Systemic therapies to Treatments to Primary Diagnoses to Donors to Programs

```mermaid
---
title: 80 Surgeries, 1 for other half of treatments
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

## Follw ups to Donor plus Primary Diagnosis or Treatment

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

## Biomarkers to Donors

```mermaid
---
title: 15 Biomarkers
---
graph LR;  
  Biomarker_1_5 ------> DONOR_1 --> PROGRAM_1;
  Biomarker_6_9 -----> DIAG_4 --> DONOR_2 --> PROGRAM_1;
  Biomarker_10_12 ----> SPECIMEN_13 ---> DONOR_3 --> PROGRAM_1;
  Biomarker_13_14 ---> TREATMENT_15 ----> DONOR_4 --> PROGRAM_1;
  Biomarker_15 --> FollowUp_31 -----> DONOR_7 --> PROGRAM_2;
```

---

## Comorbidities to Donors

```mermaid
---
title: 14 Comorbidities
---
graph LR;  
  Comorbidity_1_3 --> DONOR_1 --> PROGRAM_1;  
  Comorbidity_4_6 --> DONOR_2 --> PROGRAM_1;  
  Comorbidity_7_8 --> DONOR_3 --> PROGRAM_1;  
  Comorbidity_9_10 --> DONOR_4 --> PROGRAM_1;  
  Comorbidity_11_12 --> DONOR_5_6 --> PROGRAM_1;  
  Comorbidity_13_14 --> DONOR_7_8 --> PROGRAM_2;
```

---

## Exposures to Donors

```mermaid
---
title: 8 Exposures
---
graph LR;  
  Exposure_1_3 --> DONOR_1 --> PROGRAM_1;  
  Exposure_4_5 --> DONOR_2 --> PROGRAM_1;
  Exposure_6 --> DONOR_3 --> PROGRAM_1;    
  Exposure_7_8 --> DONOR_7_8 --> PROGRAM_2;
```

