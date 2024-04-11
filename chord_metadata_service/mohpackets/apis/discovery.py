from collections import Counter
from typing import Any, Dict, Type, List
from django.db.models import (
    Count,
    Model,
)
from ninja import Query, Router
from chord_metadata_service.mohpackets.models import (
    Biomarker,
    Chemotherapy,
    Comorbidity,
    Donor,
    Exposure,
    FollowUp,
    HormoneTherapy,
    Immunotherapy,
    PrimaryDiagnosis,
    Program,
    Radiation,
    SampleRegistration,
    Specimen,
    Surgery,
    Treatment,
)
from chord_metadata_service.mohpackets.permissible_values import (
    PRIMARY_SITE,
    TREATMENT_TYPE,
)
from chord_metadata_service.mohpackets.schemas.discovery import (
    DiscoverySchema,
    ProgramDiscoverySchema,
    QuerySampleRegistrationSchema
)
from chord_metadata_service.mohpackets.schemas.filter import (
    DonorFilterSchema,
)
import authx.auth


"""
Module with overview APIs for the summary page and discovery APIs.
These APIs do not require authorization but return only donor counts.

Author: Son Chau
"""

discovery_router = Router()
overview_router = Router()
discovery_router.add_router("/overview/", overview_router, tags=["overview"])


##########################################
#                                        #
#           HELPER FUNCTIONS             #
#                                        #
##########################################
def count_terms(terms):
    """
    Return a dictionary of counts for every term in a list, used in overview endpoints
    for fields with lists as entries.
    """
    # Unnest list if nested
    if terms and isinstance(terms[0], list):
        terms = sum(terms, [])

    # Convert None values to "null"
    terms = ["null" if term is None else term for term in terms]
    return Counter(terms)


def count_donors(model: Type[Model], filters=None) -> Dict[str, int]:
    queryset = model.objects.all()
    if model == Donor:
        count_field = "uuid"
    else:
        count_field = "donor_uuid"

    if filters is not None:
        queryset = filters.filter(queryset)

    item_counts = (
        queryset.values("program_id")
        .annotate(donor_count=Count(count_field, distinct=True))
        .order_by("program_id")
    )

    return {f"{item['program_id']}": item["donor_count"] for item in item_counts}


# Query gets a bit more information from certain endpoints
def request_is_from_query(request):
    if "X-Service-Token" in request.headers:
        return authx.auth.verify_service_token(service="query", token=request.headers["X-Service-Token"])
    return False


###############################################
#                                             #
#               DISCOVERY API                 #
#                                             #
###############################################
@discovery_router.get("/programs/", response=List[ProgramDiscoverySchema])
def discover_programs(request):
    return Program.objects.only("program_id", "metadata")


@discovery_router.get("/donors/", response=DiscoverySchema)
def discover_donors(request, filters: DonorFilterSchema = Query(...)):
    donors = count_donors(Donor, filters)
    return DiscoverySchema(donors_by_cohort=donors)


@discovery_router.get("/specimen/", response=DiscoverySchema)
def discover_specimens(request):
    specimens = count_donors(Specimen)
    return DiscoverySchema(donors_by_cohort=specimens)


@discovery_router.get("/sample_registrations/", response=DiscoverySchema)
def discover_sample_registrations(request):
    sample_registrations = count_donors(SampleRegistration)
    return DiscoverySchema(donors_by_cohort=sample_registrations)

@discovery_router.get("/sample_registrations_query/", response=QuerySampleRegistrationSchema)
def discover_sample_registrations_query(request):
    if request_is_from_query(request):
        # Append the actual sample registrations for Query
        registration_query = SampleRegistration.objects.all().values("submitter_sample_id")
        print([item['submitter_sample_id'] for item in registration_query])
        return QuerySampleRegistrationSchema(sample_ids = [item['submitter_sample_id'] for item in registration_query])

@discovery_router.get("/primary_diagnoses/", response=DiscoverySchema)
def discover_primary_diagnoses(request):
    primary_diagnoses = count_donors(PrimaryDiagnosis)
    return DiscoverySchema(donors_by_cohort=primary_diagnoses)


@discovery_router.get("/treatments/", response=DiscoverySchema)
def discover_treatments(request):
    treatments = count_donors(Treatment)
    return DiscoverySchema(donors_by_cohort=treatments)


@discovery_router.get("/chemotherapies/", response=DiscoverySchema)
def discover_chemotherapies(request):
    chemotherapies = count_donors(Chemotherapy)
    return DiscoverySchema(donors_by_cohort=chemotherapies)


@discovery_router.get("/hormone_therapies/", response=DiscoverySchema)
def discover_hormone_therapies(request):
    hormone_therapies = count_donors(HormoneTherapy)
    return DiscoverySchema(donors_by_cohort=hormone_therapies)


@discovery_router.get("/radiations/", response=DiscoverySchema)
def discover_radiations(request):
    radiations = count_donors(Radiation)
    return DiscoverySchema(donors_by_cohort=radiations)


@discovery_router.get("/immunotherapies/", response=DiscoverySchema)
def discover_immunotherapies(request):
    immunotherapies = count_donors(Immunotherapy)
    return DiscoverySchema(donors_by_cohort=immunotherapies)


@discovery_router.get("/surgeries/", response=DiscoverySchema)
def discover_surgeries(request):
    surgeries = count_donors(Surgery)
    return DiscoverySchema(donors_by_cohort=surgeries)


@discovery_router.get("/follow_ups/", response=DiscoverySchema)
def discover_follow_ups(request):
    follow_ups = count_donors(FollowUp)
    return DiscoverySchema(donors_by_cohort=follow_ups)


@discovery_router.get("/biomarkers/", response=DiscoverySchema)
def discover_biomarkers(request):
    biomarkers = count_donors(Biomarker)
    return DiscoverySchema(donors_by_cohort=biomarkers)


@discovery_router.get("/comorbidities/", response=DiscoverySchema)
def discover_comorbidities(request):
    comorbidities = count_donors(Comorbidity)
    return DiscoverySchema(donors_by_cohort=comorbidities)


@discovery_router.get("/exposures/", response=DiscoverySchema)
def discover_exposures(request):
    exposures = count_donors(Exposure)
    return DiscoverySchema(donors_by_cohort=exposures)


###############################################
#                                             #
#                OVERVIEW API                 #
#                                             #
###############################################
@discovery_router.get("/sidebar_list/", response=Dict[str, Any])
def discover_sidebar_list(request):
    """
    Retrieve the list of available values for all fields (including for
    datasets that the user is not authorized to view)
    """
    # Drugs queryable for chemotherapy
    chemotherapy_drug_names = list(
        Chemotherapy.objects.exclude(drug_name__isnull=True)
        .values_list("drug_name", flat=True)
        .order_by("drug_name")
        .distinct()
    )
    # Drugs queryable for immunotherapy
    immunotherapy_drug_names = list(
        Immunotherapy.objects.exclude(drug_name__isnull=True)
        .values_list("drug_name", flat=True)
        .order_by("drug_name")
        .distinct()
    )

    # Drugs queryable for hormone therapy
    hormone_therapy_drug_names = list(
        HormoneTherapy.objects.exclude(drug_name__isnull=True)
        .values_list("drug_name", flat=True)
        .order_by("drug_name")
        .distinct()
    )

    # Create a dictionary of results
    results = {
        "treatment_types": TREATMENT_TYPE,
        "tumour_primary_sites": PRIMARY_SITE,
        "chemotherapy_drug_names": chemotherapy_drug_names,
        "immunotherapy_drug_names": immunotherapy_drug_names,
        "hormone_therapy_drug_names": hormone_therapy_drug_names,
    }

    return results


@overview_router.get("/cohort_count/", response=Dict[str, int])
def discover_cohort_count(request):
    """
    Return the number of cohorts in the database.
    """
    return {"cohort_count": Program.objects.count()}


@overview_router.get("/patients_per_cohort/", response=Dict[str, int])
def discover_patients_per_cohort(request):
    """
    Return the number of patients per cohort in the database.
    """
    cohorts = Donor.objects.values_list("program_id", flat=True)
    return count_terms(cohorts)


@overview_router.get("/individual_count/", response=Dict[str, int])
def discover_individual_count(request):
    """
    Return the number of individuals in the database.
    """

    return {"individual_count": Donor.objects.count()}


@overview_router.get("/gender_count/", response=Dict[str, int])
def discover_gender_count(request):
    """
    Return the count for every gender in the database.
    """
    genders = Donor.objects.values_list("gender", flat=True)
    return count_terms(genders)


@overview_router.get("/cancer_type_count/", response=Dict[str, int])
def discover_cancer_type_count(request):
    """
    Return the count for every cancer type in the database.
    """
    cancer_types = list(Donor.objects.values_list("primary_site", flat=True))

    # Handle missing values as empty arrays
    for i in range(len(cancer_types)):
        if cancer_types[i] is None:
            cancer_types[i] = [None]

    return count_terms(cancer_types)


@overview_router.get("/treatment_type_count/", response=Dict[str, int])
def discover_treatment_type_count(request):
    """
    Return the count for every treatment type in the database.
    """
    treatment_types = list(Treatment.objects.values_list("treatment_type", flat=True))

    # Handle missing values as empty arrays
    for i in range(len(treatment_types)):
        if treatment_types[i] is None:
            treatment_types[i] = [None]

    return count_terms(treatment_types)


@overview_router.get("/diagnosis_age_count/", response=Dict[str, int])
def discover_diagnosis_age_count(request):
    """
    Return the count for age of diagnosis by calculating the date of birth interval.
    """
    months_in_year = 12

    age_counts = {
        "null": 0,
        "0-19": 0,
        "20-29": 0,
        "30-39": 0,
        "40-49": 0,
        "50-59": 0,
        "60-69": 0,
        "70-79": 0,
        "80+": 0,
    }

    donors = Donor.objects.values("date_of_birth")

    for donor in donors:
        age = -1
        if donor["date_of_birth"] and donor["date_of_birth"].get("month_interval"):
            age = abs(donor["date_of_birth"]["month_interval"]) // months_in_year

        if age < 0:
            age_counts["null"] += 1
        elif age <= 19:
            age_counts["0-19"] += 1
        elif age <= 29:
            age_counts["20-29"] += 1
        elif age <= 39:
            age_counts["30-39"] += 1
        elif age <= 49:
            age_counts["40-49"] += 1
        elif age <= 59:
            age_counts["50-59"] += 1
        elif age <= 69:
            age_counts["60-69"] += 1
        elif age <= 79:
            age_counts["70-79"] += 1
        else:
            age_counts["80+"] += 1

    return age_counts
