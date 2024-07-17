# Small dataset relationships

The small dataset is composed of:
* 4 programs
* 20 Follow Ups
* 30 Exposures
* 40 Comorbidities, Biomarkers
* 80 Donors, Primary Diagnoses, Specimens, Radiations, Surgeries
* 160 Treatments
* 240 Sample registrations
* 320 Systemic Therapies

Sub-objects are iterated over and assigned evenly to a parent object until all objects are exhausted. Identifiers show the pattern in the diagrams below.

e.g.

This is a diagram of the synthetic relationships between the models in the dataset.

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
title: 80 PrimaryDiagnoses, 1 Primary Diagnosis per Donor, examples
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
title: 80 Specimens, 1 per Donor, examples
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
title: 240 SampleRegistrations, 3 per specimen, examples
---
graph LR;  
  SAMPLE_0001--> SPECIMEN_0001 --> DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  SAMPLE_0081--> SPECIMEN_0001 --> DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  SAMPLE_0161--> SPECIMEN_0001 --> DIAG_0001 --> DONOR_0001 --> PROGRAM_01;  
  SPECIMEN_0005 -->DIAG_0005 --> DONOR_0005 --> PROGRAM_01;  
  SPECIMEN_0085 -->DIAG_0005 --> DONOR_0005 --> PROGRAM_01;  
  SPECIMEN_0165 -->DIAG_0005 --> DONOR_0005 --> PROGRAM_01;  
  SPECIMEN_0002 -->DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  SPECIMEN_0082 -->DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  SPECIMEN_0162 -->DIAG_0002 --> DONOR_0002 --> PROGRAM_02;  
  SPECIMEN_0003 -->DIAG_0003 --> DONOR_0003 --> PROGRAM_03;  
  SPECIMEN_0083 -->DIAG_0003 --> DONOR_0003 --> PROGRAM_03;  
  SPECIMEN_0163 -->DIAG_0003 --> DONOR_0003 --> PROGRAM_03;  
  SPECIMEN_0004 -->DIAG_0004 --> DONOR_0004 --> PROGRAM_04;
  SPECIMEN_0084 -->DIAG_0004 --> DONOR_0004 --> PROGRAM_04;
  SPECIMEN_0164 -->DIAG_0004 --> DONOR_0004 --> PROGRAM_04;
  SPECIMEN_0008 -->DIAG_0008 --> DONOR_0008 --> PROGRAM_04;
  SPECIMEN_0088 -->DIAG_0008 --> DONOR_0008 --> PROGRAM_04;
  SPECIMEN_0168 -->DIAG_0008 --> DONOR_0008 --> PROGRAM_04;
```

---

```mermaid
---
title: 25 Treatments
---
graph LR;  
  Treatment_1_3 --> DIAG_1 --> DONOR_1 --> PROGRAM_1;  
  Treatment_4_6 --> DIAG_2 --> DONOR_1 --> PROGRAM_1;  
  Treatment_7_9 --> DIAG_3 --> DONOR_1 --> PROGRAM_1;  
  Treatment_10_11 --> DIAG_4 --> DONOR_2 --> PROGRAM_1;  
  Treatment_12_13 --> DIAG_5 --> DONOR_2 --> PROGRAM_1;  
  Treatment_14_15 --> DIAG_6 --> DONOR_2 --> PROGRAM_1; 
  Treatment_16_17 --> DIAG_7_8 --> DONOR_3 --> PROGRAM_1;  
  Treatment_18_19 --> DIAG_9_10 --> DONOR_4 --> PROGRAM_1;  
  Treatment_20_21 --> DIAG_11_12 --> DONOR_5_6 --> PROGRAM_1;  
  Treatment_22_25 --> DIAG_13_16 --> DONOR_7_10 --> PROGRAM_2;
```

---

```mermaid
---
title: 15 Chemotherapies
---
graph LR;  
  Chemotherapy_1_3 --> Treatment_1 --> DONOR_1 --> PROGRAM_1;  
  Chemotherapy_4_6 --> Treatment_2 --> DONOR_1 --> PROGRAM_1;  
  Chemotherapy_7_9 --> Treatment_3 --> DONOR_1 --> PROGRAM_1;
  Chemotherapy_10_11 --> Treatment_4 --> DONOR_1 --> PROGRAM_1;
  Chemotherapy_12_13 --> Treatment_5 --> DONOR_1 --> PROGRAM_1;
  Chemotherapy_14_15 --> Treatment_6_7 --> DONOR_1 --> PROGRAM_1;
```

---

```mermaid
---
title: 14 HormoneTherapies
---
graph LR;  
  HormoneTherapy_1_3 --> Treatment_8 --> DONOR_1 --> PROGRAM_1;  
  HormoneTherapy_4_6 --> Treatment_9 --> DONOR_1 --> PROGRAM_1;  
  HormoneTherapy_7_9 --> Treatment_10 --> DONOR_2 --> PROGRAM_1;  
  HormoneTherapy_10_11 --> Treatment_11 --> DONOR_2 --> PROGRAM_1;  
  HormoneTherapy_12_13 --> Treatment_12 --> DONOR_2 --> PROGRAM_1;  
  HormoneTherapy_14 --> Treatment_13 --> DONOR_2 --> PROGRAM_1;   
```

---

```mermaid
---
title: 11 Immunotherapies
---
graph LR;  
  Immunotherapy_1_3 --> Treatment_14 --> DONOR_2 --> PROGRAM_1; 
  Immunotherapy_4_6 --> Treatment_15 --> DONOR_2 --> PROGRAM_1;  
  Immunotherapy_7_8 --> Treatment_16 --> DONOR_3 --> PROGRAM_1;  
  Immunotherapy_9_10 --> Treatment_17 --> DONOR_3 --> PROGRAM_1;  
  Immunotherapy_11 --> Treatment_18 --> DONOR_4 --> PROGRAM_1;   
```

---

```mermaid
---
title: 4 Radiations
---
graph LR;  
  Radiation_1_3 --> Treatment_19_21 --> DONOR_4_6 --> PROGRAM_1;  
  Radiation_4 --> Treatment_22 --> DONOR_7 --> PROGRAM_2; 
```

---

```mermaid
---
title: 3 Surgeries
---
graph LR;  
  Surgery_1_3 --> Treatment_23_25 --> DONOR_8_10 --> PROGRAM_2;  
```

---

```mermaid
---
title: 34 FollowUps
---
graph LR;  
  FollowUp_1_3 --> Treatment_1 --> DIAG_1 --> DONOR_1 --> PROGRAM_1;  
  FollowUp_4_6 --> Treatment_2 --> DIAG_1 --> DONOR_1 --> PROGRAM_1;  
  FollowUp_7_9 --> Treatment_3 --> DIAG_1 --> DONOR_1 --> PROGRAM_1;  
  FollowUp_10_11 --> Treatment_4 --> DIAG_2 --> DONOR_1 --> PROGRAM_1; 
  FollowUp_12_13 --> Treatment_5 --> DIAG_2 --> DONOR_1 --> PROGRAM_1; 
  FollowUp_14_15 --> Treatment_6 --> DIAG_2 --> DONOR_1 --> PROGRAM_1; 
  FollowUp_16_18 --> Treatment_7_9 --> DIAG_3 --> DONOR_1 --> PROGRAM_1;
  FollowUp_19_20 --> Treatment_10_11 --> DIAG_4 --> DONOR_2 --> PROGRAM_1;  
  FollowUp_21_22 --> Treatment_12_13 --> DIAG_5 --> DONOR_2 --> PROGRAM_1;  
  FollowUp_23_24 --> Treatment_14_15 --> DIAG_6 --> DONOR_2 --> PROGRAM_1; 
  FollowUp_25_26 --> Treatment_16_17 --> DIAG_7_8 --> DONOR_3 --> PROGRAM_1;  
  FollowUp_27_28 --> Treatment_18_19 --> DIAG_9_10 --> DONOR_4 --> PROGRAM_1;  
  FollowUp_29_30 --> Treatment_20_21 --> DIAG_11_12 --> DONOR_5_6 --> PROGRAM_1;  
  FollowUp_31_34 --> Treatment_22_25 --> DIAG_13_16 --> DONOR_7_10 --> PROGRAM_2;
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
  Biomarker_13_14 ---> Treatment_15 ----> DONOR_4 --> PROGRAM_1;
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
