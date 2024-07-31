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
  SPECIMEN_0001_0020 --> DIAG_0001_0020 --> DONOR_0001_0020 --> SYNTH_01;  
  SPECIMEN_00021_0040 --> DIAG_0021_40 --> DONOR_0021_40 --> SYNTH_02;
  SPECIMEN_00041_0060 --> DIAG_0041_60 --> DONOR_0041_60 --> SYNTH_03;
  SPECIMEN_00061_0080 --> DIAG_0061_80 --> DONOR_0061_80 --> SYNTH_04;  
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
  DIAG_0001_0020 --> DONOR_0001_0020 --> SYNTH_01;  
  DIAG_0021_0040 --> DONOR_0021_0040 --> SYNTH_02;  
  DIAG_0041_0060 --> DONOR_0041_0060 --> SYNTH_03;  
  DIAG_0061_0080 --> DONOR_0061_0080 --> SYNTH_04;
  TREATMENT_0001_0040 --> DIAG_0001_0020;
  TREATMENT_0041_0080 --> DIAG_0021_0040;  
  TREATMENT_0081_0120 --> DIAG_0041_0060; 
  TREATMENT_0121_0160 --> DIAG_0061_0080;
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

Follow ups are linked to the first 10 donors of each program. 

The first four are linked to a primary diagnosis as well as a Donor.

The next four are linked to the first treatment as well as the Donor.

The remaining 2 are linked only to the Donor.

```mermaid
---
title: 40 FollowUps, linked to either donor +/- primary diagnosis or treatment
---
graph LR;  
  DIAG_0001_0004 --> DONOR_0001_0004 --> SYNTH_01;
  FOLLOW_UP_0001_0004 --> DONOR_0001_0004;
  FOLLOW_UP_0001_0004 --> DIAG_0001_0004;
  TREATMENT_0009_11_13_15 --> DIAG_0005_0008 --> DONOR_0005_0008 --> SYNTH_01;
  FOLLOW_UP_0005_0008 --> DONOR_0005_0008;
  FOLLOW_UP_0005_0008 --> TREATMENT_0009_11_13_15;
  FOLLOW_UP_0009_0010 --> DONOR_0009_10 --> SYNTH_01;

  DIAG_0021_0024 --> DONOR_0021_0024 --> SYNTH_02;
  FOLLOW_UP_0011_0014 --> DONOR_0021_0024;
  FOLLOW_UP_0011_0014 --> DIAG_0021_0024;
  TREATMENT_0049_51_53_55 --> DIAG_0025_0028 --> DONOR_0025_0028 --> SYNTH_02;
  FOLLOW_UP_0015_0018 --> DONOR_0025_0028;
  FOLLOW_UP_0015_0018 --> TREATMENT_0049_51_53_55;
  FOLLOW_UP_0019_0020 --> DONOR_0029_30 --> SYNTH_02;

  DIAG_00041_0044 --> DONOR_0041_0044 --> SYNTH_03;
  FOLLOW_UP_0021_0024 --> DONOR_0041_0044;
  FOLLOW_UP_0021_0024 --> DIAG_0041_0044;
  TREATMENT_0089_91_93_95 --> DIAG_0045_0048 --> DONOR_0045_0048 --> SYNTH_03;
  FOLLOW_UP_0025_0028 --> DONOR_0045_0048;
  FOLLOW_UP_0025_0028 --> TREATMENT_0089_91_93_95;
  FOLLOW_UP_0029_0030 --> DONOR_0049_50 --> SYNTH_03;

  DIAG_00061_0064 --> DONOR_0061_0064 --> SYNTH_04;
  FOLLOW_UP_0031_0034 --> DONOR_0061_0064;
  FOLLOW_UP_0031_0034 --> DIAG_0061_0064;
  TREATMENT_0129_131_133_135 --> DIAG_0065_0068 --> DONOR_0065_0068 --> SYNTH_04;
  FOLLOW_UP_0035_0038 --> DONOR_0065_0068;
  FOLLOW_UP_0035_0038 --> TREATMENT_0129_131_133_135;
  FOLLOW_UP_0039_0040 --> DONOR_0069_70 --> SYNTH_04;
  
  
```

---

## Biomarkers, Comorbidities, Exposures to Donors

Synthetic data is only links Biomarkers to Donors Only. 

The first 10 donors have a linked biomarker objects

The second 10 donors have a linked comorbidity object

Exposures are linked to the 'middle' 10 donors, sometimes linked with comorbidities, sometimes with biomarkers

```mermaid
---
title: Biomarkers, Comorbidities, Exposures
---
graph LR;  
  BIOMARKER_uuid1_10 --> DONOR_0001_0010 --> SYNTH_01; 
  COMORBIDITY_uuid1_10 --> DONOR_0011_0020 --> SYNTH_01;
  EXPOSURE_uuid1_10 --> DONOR_007_16 --> SYNTH_01;
  
  BIOMARKER_uuid11_20 --> DONOR_0021_30 --> SYNTH_02;
  COMORBIDITY_uuid11_20 --> DONOR_0031_0040 --> SYNTH_02;
  EXPOSURE_uuid11_20 --> DONOR_0027_36 --> SYNTH_02;

  BIOMARKER_uuid21_30 --> DONOR_0041_50 --> SYNTH_03;
  COMORBIDITY_uuid21_30 --> DONOR_0051_0060 --> SYNTH_03;
  EXPOSURE_uuid21_30 --> DONOR_0047_56 --> SYNTH_03;

  BIOMARKER_uuid31_40 --> DONOR_0061_70 --> SYNTH_04;
  COMORBIDITY_uuid31_40 --> DONOR_0071_0080 --> SYNTH_04;
  EXPOSURE_uuid31_40 --> DONOR_0067_76 --> SYNTH_04;  
  
```

Example relationships 

```mermaid
graph LR;
  BIOMARKER_uuid1 --> DONOR_0001 --> SYNTH_01;
  BIOMARKER_uuid7  --> DONOR_0007 --> SYNTH_01;
```


---
