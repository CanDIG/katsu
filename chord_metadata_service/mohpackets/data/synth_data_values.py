import math

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
