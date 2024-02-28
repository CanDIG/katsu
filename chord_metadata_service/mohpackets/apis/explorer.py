from typing import List
from django.db.models.functions import Abs
from ninja import Query, Router
from django.db.models import Q
from django.db.models import Case, When, IntegerField, CharField, Value
from django.db.models import Func
from django.db.models import OuterRef, Subquery
from django.db.models.functions import Cast
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.postgres.expressions import ArraySubquery
from chord_metadata_service.mohpackets.models import (
    Donor,
    Treatment,
)
from chord_metadata_service.mohpackets.schemas.explorer import (
    DonorExplorerSchema,
)
from chord_metadata_service.mohpackets.schemas.filter import (
    DonorExplorerFilterSchema,
)


explorer_router = Router()


@explorer_router.get("/donors/", response=List[DonorExplorerSchema])
def explorer_donor(request, filters: DonorExplorerFilterSchema = Query(...)):
    filter_dict = filters.dict()
    queryset = (
        Donor.objects.select_related("program_id")
        .prefetch_related(
            "treatment_set",
            "chemotherapy_set",
            "hormonetherapy_set",
            "immunotherapy_set",
            "sampleregistration_set",
        )
        .distinct()
    )

    if filter_dict["primary_site"]:
        queryset = queryset.filter(primary_site__overlap=filter_dict["primary_site"])

    if filter_dict["treatment_type"]:
        queryset = queryset.filter(
            treatment__treatment_type__overlap=filter_dict["treatment_type"]
        )

    if filter_dict["chemotherapy_drug_name"]:
        queryset = queryset.filter(
            chemotherapy__drug_name__in=filter_dict["chemotherapy_drug_name"]
        )

    if filter_dict["immunotherapy_drug_name"]:
        queryset = queryset.filter(
            immunotherapy__drug_name__in=filter_dict["immunotherapy_drug_name"]
        )

    if filter_dict["hormone_therapy_drug_name"]:
        queryset = queryset.filter(
            hormonetherapy__drug_name__in=filter_dict["hormone_therapy_drug_name"]
        )

    if filter_dict["exclude_cohorts"]:
        queryset = queryset.exclude(program_id__in=filter_dict["exclude_cohorts"])

    class Unnest(Func):
        contains_subquery = True
        function = "unnest"

    treatment_type_names = (
        Treatment.objects.filter(donor_uuid_id=OuterRef("uuid"))
        .annotate(treatment_type_list=Unnest("treatment_type"))
        .values_list("treatment_type_list", flat=True)
    )

    donors = queryset.annotate(
        abs_month_interval=Abs(
            Cast("date_of_birth__month_interval", output_field=IntegerField())
        ),
        age_at_diagnosis=Case(
            When(Q(date_of_birth__isnull=True), then=Value(None)),
            When(abs_month_interval__lt=240, then=Value("0-19")),
            When(abs_month_interval__lt=360, then=Value("20-29")),
            When(abs_month_interval__lt=480, then=Value("30-39")),
            When(abs_month_interval__lt=600, then=Value("40-49")),
            When(abs_month_interval__lt=720, then=Value("50-59")),
            When(abs_month_interval__lt=840, then=Value("60-69")),
            When(abs_month_interval__lt=960, then=Value("70-79")),
            default=Value("80+"),
            output_field=CharField(),
        ),
        submitter_sample_ids=ArrayAgg(
            "sampleregistration__submitter_sample_id", distinct=True
        ),
        treatment_type=ArraySubquery(Subquery(treatment_type_names)),
    ).values(
        "program_id",
        "submitter_donor_id",
        "submitter_sample_ids",
        "primary_site",
        "treatment_type",
        "age_at_diagnosis",
    )
    return donors
