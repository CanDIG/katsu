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

1 Primary Diagnosis per donor.

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

```mermaid
---
title: 160 TREATMENTs, 2 per Primary Diagnosis, examples
---
graph LR;  
  TREATMENT_0001 --> DIAG_0001 --> DONOR_0001 --> PROGRAM_01;
  TREATMENT_0081 --> DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  TREATMENT_0002 --> DIAG_0002 --> DONOR_0002 --> PROGRAM_02; 
  TREATMENT_0082 --> DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  TREATMENT_0003 --> DIAG_0003 --> DONOR_0003 --> PROGRAM_03; 
  TREATMENT_0083 --> DIAG_0003 --> DONOR_0003 --> PROGRAM_03; 
  TREATMENT_0004 --> DIAG_0004 --> DONOR_0004 --> PROGRAM_03; 
  TREATMENT_0084 --> DIAG_0004 --> DONOR_0004 --> PROGRAM_03; 
```

---

```mermaid
---
title: 320 Systemic Therapies, 2 per Treatment
---
graph LR;  
  sys_therapy_uuid1 --> TREATMENT_0001 --> DIAG_0001 --> DONOR_0001 --> PROGRAM_01;
  sys_therapy_uuid2 --> TREATMENT_0081 --> DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  sys_therapy_uuid3 --> TREATMENT_0002 --> DIAG_0002 --> DONOR_0002 --> PROGRAM_02; 
  sys_therapy_uuid4 --> TREATMENT_0082 --> DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  sys_therapy_uuid5 --> TREATMENT_0003 --> DIAG_0003 --> DONOR_0003 --> PROGRAM_03; 
  sys_therapy_uuid6 --> TREATMENT_0083 --> DIAG_0003 --> DONOR_0003 --> PROGRAM_03; 
  sys_therapy_uuid7 --> TREATMENT_0004 --> DIAG_0004 --> DONOR_0004 --> PROGRAM_03; 
  sys_therapy_uuid8 --> TREATMENT_0084 --> DIAG_0004 --> DONOR_0004 --> PROGRAM_03; 
```

---

```mermaid
---
title: 80 Radiations, 1 for half of treatments
---
graph LR;  
  Radiation_1_3 --> TREATMENT_19_21 --> DONOR_4_6 --> PROGRAM_1;  
  Radiation_4 --> TREATMENT_22 --> DONOR_7 --> PROGRAM_2; 
```

---

```mermaid
---
title: 80 Surgeries, 1 for other half of treatments
---
graph LR;  
  Surgery_1_3 --> TREATMENT_23_25 --> DONOR_8_10 --> PROGRAM_2;  
```

---

```mermaid
---
title: 34 FollowUps
---
graph LR;  
  FollowUp_1_3 --> TREATMENT_1 --> DIAG_1 --> DONOR_1 --> PROGRAM_1;  
  FollowUp_4_6 --> TREATMENT_2 --> DIAG_1 --> DONOR_1 --> PROGRAM_1;  
  FollowUp_7_9 --> TREATMENT_3 --> DIAG_1 --> DONOR_1 --> PROGRAM_1;  
  FollowUp_10_11 --> TREATMENT_4 --> DIAG_2 --> DONOR_1 --> PROGRAM_1; 
  FollowUp_12_13 --> TREATMENT_5 --> DIAG_2 --> DONOR_1 --> PROGRAM_1; 
  FollowUp_14_15 --> TREATMENT_6 --> DIAG_2 --> DONOR_1 --> PROGRAM_1; 
  FollowUp_16_18 --> TREATMENT_7_9 --> DIAG_3 --> DONOR_1 --> PROGRAM_1;
  FollowUp_19_20 --> TREATMENT_10_11 --> DIAG_4 --> DONOR_2 --> PROGRAM_1;  
  FollowUp_21_22 --> TREATMENT_12_13 --> DIAG_5 --> DONOR_2 --> PROGRAM_1;  
  FollowUp_23_24 --> TREATMENT_14_15 --> DIAG_6 --> DONOR_2 --> PROGRAM_1; 
  FollowUp_25_26 --> TREATMENT_16_17 --> DIAG_7_8 --> DONOR_3 --> PROGRAM_1;  
  FollowUp_27_28 --> TREATMENT_18_19 --> DIAG_9_10 --> DONOR_4 --> PROGRAM_1;  
  FollowUp_29_30 --> TREATMENT_20_21 --> DIAG_11_12 --> DONOR_5_6 --> PROGRAM_1;  
  FollowUp_31_34 --> TREATMENT_22_25 --> DIAG_13_16 --> DONOR_7_10 --> PROGRAM_2;
```

---

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

---

```mermaid
---
title: 20 Follow Ups
---
graph LR;  
  Exposure_1_3 --> DONOR_1 --> PROGRAM_1;  
  Exposure_4_5 --> DONOR_2 --> PROGRAM_1;
  Exposure_6 --> DONOR_3 --> PROGRAM_1;    
  Exposure_7_8 --> DONOR_7_8 --> PROGRAM_2;
```
