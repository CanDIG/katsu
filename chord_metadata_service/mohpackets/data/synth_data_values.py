import math
import chord_metadata_service.mohpackets.permissible_values as PERM_VAL


def add_nulls(complete_list: list, prop=0.2):
    """ Returns a list with 20% of the list as 'None' """
    num_nulls = math.ceil(len(complete_list) * prop)
    complete_list.extend([None] * num_nulls)
    return complete_list


# add 20% nulls to all enums
GENDER = PERM_VAL.GENDER + [None]
SEX_AT_BIRTH = add_nulls(PERM_VAL.SEX_AT_BIRTH)

BASIS_OF_DIAGNOSIS = add_nulls(PERM_VAL.BASIS_OF_DIAGNOSIS)
PRIMARY_DIAGNOSIS_LATERALITY = add_nulls(PERM_VAL.PRIMARY_DIAGNOSIS_LATERALITY)
TUMOUR_STAGING_SYSTEM = add_nulls(PERM_VAL.TUMOUR_STAGING_SYSTEM)
T_CATEGORY = add_nulls(PERM_VAL.T_CATEGORY)
N_CATEGORY = add_nulls(PERM_VAL.N_CATEGORY)
M_CATEGORY = add_nulls(PERM_VAL.M_CATEGORY)
STAGE_GROUP = add_nulls(PERM_VAL.STAGE_GROUP)

STORAGE = add_nulls(PERM_VAL.STORAGE)
SPECIMEN_PROCESSING = add_nulls(PERM_VAL.SPECIMEN_PROCESSING)
TOPOGRAPHY_CODES = add_nulls(PERM_VAL.TOPOGRAPHY_CODES)
SPECIMEN_LATERALITY = add_nulls(PERM_VAL.SPECIMEN_LATERALITY)
CONFIRMED_DIAGNOSIS_TUMOUR = add_nulls(PERM_VAL.CONFIRMED_DIAGNOSIS_TUMOUR)
TUMOUR_GRADE = add_nulls(PERM_VAL.TUMOUR_GRADE)
TUMOUR_GRADING_SYSTEM = add_nulls(PERM_VAL.TUMOUR_GRADING_SYSTEM)
PERCENT_CELLS_RANGE = add_nulls(PERM_VAL.PERCENT_CELLS_RANGE)
CELLS_MEASURE_METHOD = add_nulls(PERM_VAL.CELLS_MEASURE_METHOD)

SPECIMEN_TISSUE_SOURCE = add_nulls(PERM_VAL.SPECIMEN_TISSUE_SOURCE)
SPECIMEN_TYPE = add_nulls(PERM_VAL.SPECIMEN_TYPE)
SAMPLE_TYPE = add_nulls(PERM_VAL.SAMPLE_TYPE)
TUMOUR_DESIGNATION = add_nulls(PERM_VAL.TUMOUR_DESIGNATION)

TREATMENT_TYPE = add_nulls(PERM_VAL.TREATMENT_TYPE)

# remove typed treatments, they get added if there is a specific treatment linked
TREATMENT_TYPE_FOR_ALL = [
    "Bone marrow transplant",
    "No treatment",
    "Other targeting molecular therapy",
    "Photodynamic therapy",
    "Stem cell transplant",
]
TREATMENT_INTENT = add_nulls(PERM_VAL.TREATMENT_INTENT)
TREATMENT_RESPONSE_METHOD = add_nulls(PERM_VAL.TREATMENT_RESPONSE_METHOD)
TREATMENT_RESPONSE = add_nulls(PERM_VAL.TREATMENT_RESPONSE)
TREATMENT_STATUS = add_nulls(PERM_VAL.TREATMENT_STATUS)

DOSAGE_UNITS = add_nulls(PERM_VAL.DOSAGE_UNITS)

RADIATION_THERAPY_MODALITY = add_nulls(PERM_VAL.RADIATION_THERAPY_MODALITY)
RADIATION_ANATOMICAL_SITE = add_nulls(PERM_VAL.RADIATION_ANATOMICAL_SITE)
THERAPY_TYPE = add_nulls(PERM_VAL.THERAPY_TYPE)

SURGERY_LOCATION = add_nulls(PERM_VAL.SURGERY_LOCATION)
TUMOUR_FOCALITY = add_nulls(PERM_VAL.TUMOUR_FOCALITY)
TUMOUR_CLASSIFICATION = add_nulls(PERM_VAL.TUMOUR_CLASSIFICATION)
LYMPHOVACULAR_INVASION = add_nulls(PERM_VAL.LYMPHOVACULAR_INVASION)
PERINEURAL_INVASION = add_nulls(PERM_VAL.PERINEURAL_INVASION)
MARGIN_TYPES = add_nulls(PERM_VAL.MARGIN_TYPES)

ER_PR_HPV_STATUS = add_nulls(PERM_VAL.ER_PR_HPV_STATUS)
HER2_STATUS = add_nulls(PERM_VAL.HER2_STATUS)

UBOOLEAN = add_nulls(PERM_VAL.UBOOLEAN)
MALIGNANCY_LATERALITY = add_nulls(PERM_VAL.MALIGNANCY_LATERALITY)

DISEASE_STATUS_FOLLOWUP = add_nulls(PERM_VAL.DISEASE_STATUS_FOLLOWUP)
PROGRESSION_STATUS_METHOD = add_nulls(PERM_VAL.PROGRESSION_STATUS_METHOD)

# Restricted values for synthetic data generation

PRIMARY_SITE = ["Breast",
                "Bronchus and lung",
                "Colon",
                "Skin",
                None]

# ICD disease codes, not all are correct but will match regex in model
c_codes = ['C' + str(x).rjust(2, '0') for x in list(range(0, 97))]
d_codes = ['D' + str(x).rjust(2, '0') for x in list(range(0, 9)) + list(range(37, 48))]
CANCER_CODES = c_codes + d_codes + [None]
CANCER_CODES.extend([None] * math.floor(len(CANCER_CODES)*.2))
# some codes from diseases of the circulatory system, diseases of the blood
NON_CANCER_CODES = ['D' + str(x) for x in list(range(50, 89)) + list(range(37, 48))] + \
                   ['I' + str(x).rjust(2, '0') for x in list(range(0, 99))]
CANCER_CODES.extend([None] * math.floor(len(NON_CANCER_CODES)*.2))

ALL_CODES = CANCER_CODES + NON_CANCER_CODES

SMOKER_TOBACCO_TYPE = [
    "Chewing Tobacco",
    "Cigar",
    "Cigarettes",
    "Electronic cigarettes",
    "Pipe",
    "Roll-ups",
    "Snuff",
    "Unknown",
    "Waterpipe",
]

# Systemic Therapy Drugs
CHEMO_DRUGS = {
    "Methotrexate": {"RxNorm": "6851",
                     "PubChem": "126941",
                     "NCI Thesaurus": "C642"},
    "Fludarabine": {"RxNorm": "24698",
                    "PubChem": "657237",
                    "NCI Thesaurus": "C1094"},
    "Carboplatin": {"RxNorm": "40048",
                    "PubChem": "426756",
                    "NCI Thesaurus": "C1282"},
    "Idarubicin": {"RxNorm": "5650",
                   "PubChem": "42890",
                   "NCI Thesaurus": "C562"},
    "Paclitaxel": {"RxNorm": "56946",
                   "PubChem": "36314",
                   "NCI Thesaurus": "C1411"},
    None: {}

}

IMMUNO_DRUGS = {
    "Atezolizumab": {"RxNorm": "1792776",
                     "PubChem": "469690927",
                     "NCI Thesaurus": "C106250"},
    "Durvalumab": {"RxNorm": "1919503",
                   "PubChem": "481101604",
                   "NCI Thesaurus": "C103194"},
    "Nivolumab": {"RxNorm": "1597876",
                  "PubChem": "469753496",
                  "NCI Thesaurus": "C68814"},
    "Pembrolizumab": {"RxNorm": "1547545",
                      "PubChem": "469691028",
                      "NCI Thesaurus": "C106432"},
    "Ipilimumab": {"RxNorm": "1094833",
                   "PubChem": "472634117",
                   "NCI Thesaurus": "C2654"},
    None: {}

}

HORMONE_DRUGS = {
    "Tamoxifen": {"RxNorm": "10324",
                  "PubChem": "2733526",
                  "NCI Thesaurus": "C62078"},
    "Fluoxymesterone": {"RxNorm": "4494",
                        "PubChem": "6446",
                        "NCI Thesaurus": "C507"},
    "Diethylstilbestrol": {"RxNorm": "3390",
                           "PubChem": "448537",
                           "NCI Thesaurus": "C433"},
    "Buserelin": {"RxNorm": "1825",
                  "PubChem": "50225",
                  "NCI Thesaurus": "C320"},
    "Degarelix": {"RxNorm": "475230",
                  "PubChem": "16136245",
                  "NCI Thesaurus": "C48385"},
    None: {}
}

SURGERY_TYPE = {
    "Biopsy": {"NCIt": "C15189",
               "SNOMED": "86273004",
               "UMLS": "C0005558",
               None: None},
    "Bypass Gastrojejunostomy": {"NCIt": "C51758",
                                 "SNOMED": "49245001",
                                 "UMLS": "C0399839",
                                 None: None},
    "Exploratory laparotomy": {"NCIt": "C51779",
                               "SNOMED": "74770008",
                               "UMLS": "C0085704",
                               None: None},
    "Total Mastectomy": {"NCIt": "C15281",
                         None: None},
    "Mastectomy with excision of regional lymph nodes": {"SNOMED": "66398006",
                                                         None: None},
    "Radical prostatectomy": {"NCIt": "C15399",
                              "SNOMED": "26294005",
                              "UMLS": "C0194810",
                              None: None},
    "Total gastrectomy": {"NCIt": "C185240",
                          "SNOMED": "26452005",
                          "UMLS": "C1304782",
                          None: None},
    None: {None: None}
}

RISS_DURIE_STAGES = ["Stage I",
                     "Stage II",
                     "Stage III"]

LUGANO_STAGES = ["Stage I",
                 "Stage IA",
                 "Stage IB",
                 "Stage IE",
                 "Stage II",
                 "Stage II bulky",
                 "Stage IIE",
                 "Stage IIA",
                 "Stage IIB",
                 "Stage III",
                 "Stage IIIA1",
                 "Stage IV"]

ST_JUDE = ["Stage I",
           "Stage II",
           "Stage III",
           "Stage IV"]

ANN_ARBOR = ["Stage I",
             "Stage II",
             "Stage III",
             "Stage IV",
             "Stage IA",
             "Stage IIA",
             "Stage IIIA",
             "Stage IVA",
             "Stage IB",
             "Stage IIB",
             "Stage IIIB",
             "Stage IVB",
             "Stage IE",
             "Stage IIE",
             "Stage IIIE",
             "Stage IVE",
             "Stage IS",
             "Stage IIS",
             "Stage IIIS",
             "Stage IVS"
             ]

FIGO_STAGING = [
    "Stage IA",
    "Stage IA1",
    "Stage IA2",
    "Stage IB",
    "Stage IB1",
    "Stage IB2",
    "Stage IIA",
    "Stage IAB",
    "Stage IIIA",
    "Stage IIIB",
    "Stage IVA",
    "Stage IVB"
]

BINET_STAGING = [
    "Stage A",
    "Stage B",
    "Stage C"
]

RAI_STAGING = [
    "Stage 0",
    "Stage I",
    "Stage II",
    "Stage III",
    "Stage IV"
]

STAGE_GROUP_KEY = {
    "Ann Arbor staging system": ANN_ARBOR,
    "Binet staging system": BINET_STAGING,
    "Durie-Salmon staging system": RISS_DURIE_STAGES,
    "FIGO staging system": FIGO_STAGING,
    "Lugano staging system": LUGANO_STAGES,
    "Rai staging system": RAI_STAGING,
    "Revised International staging system(R-ISS)": RISS_DURIE_STAGES,
    "St Jude staging system": ST_JUDE
}
