import os

from django.apps import apps
from django.db.models import Prefetch
from django.http import JsonResponse
from drf_spectacular import openapi
from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiTypes,
    extend_schema,
    extend_schema_view,
    inline_serializer,
)
from rest_framework import serializers, status, viewsets
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response

from chord_metadata_service.mohpackets.api_base import (
    BaseBiomarkerViewSet,
    BaseChemotherapyViewSet,
    BaseComorbidityViewSet,
    BaseDonorViewSet,
    BaseExposureViewSet,
    BaseFollowUpViewSet,
    BaseHormoneTherapyViewSet,
    BaseImmunotherapyViewSet,
    BasePrimaryDiagnosisViewSet,
    BaseProgramViewSet,
    BaseRadiationViewSet,
    BaseSampleRegistrationViewSet,
    BaseSpecimenViewSet,
    BaseSurgeryViewSet,
    BaseTreatmentViewSet,
)
from chord_metadata_service.mohpackets.authentication import (
    LocalAuthentication,
    TokenAuthentication,
)
from chord_metadata_service.mohpackets.models import Biomarker, Donor, FollowUp, Program
from chord_metadata_service.mohpackets.pagination import StandardResultsSetPagination
from chord_metadata_service.mohpackets.serializers_nested import (
    DonorWithClinicalDataSerializer,
)
from chord_metadata_service.mohpackets.throttling import MoHRateThrottle

"""
    This module inheriting from the base views and adding the authorized mixin,
    which returns the objects related to the datasets that the user is authorized to see.
"""


##########################################
#                                        #
#           HELPER FUNCTIONS             #
#                                        #
##########################################


class AuthorizedMixin:
    """
    This mixin should be used for viewsets that need to restrict access.

    The authentication classes are set based on the `DJANGO_SETTINGS_MODULE`.
    If the env is "dev" or "prod", the `TokenAuthentication` class is
    used. Otherwise, the `LocalAuthentication` class is used.

    Methods
    -------
    get_queryset()
        Returns a filtered queryset that includes only the objects that the user is
        authorized to see based on their permissions.
    """

    pagination_class = StandardResultsSetPagination
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
    auth_methods = []
    # Use jwt token auth in prod/dev environment
    if "dev" in settings_module or "prod" in settings_module:
        auth_methods.append(TokenAuthentication)
    else:
        auth_methods.append(LocalAuthentication)
    authentication_classes = auth_methods

    def get_queryset(self):
        authorized_datasets = self.request.authorized_datasets
        filtered_queryset = (
            super().get_queryset().filter(program_id__in=authorized_datasets)
        )
        return filtered_queryset


##############################################
#                                            #
#           AUTHORIZED API VIEWS             #
#                                            #
##############################################


class AuthorizedProgramViewSet(AuthorizedMixin, BaseProgramViewSet):
    """
    Retrieves a list of authorized programs.
    """

    pass


class AuthorizedDonorViewSet(AuthorizedMixin, BaseDonorViewSet):
    """
    Retrieves a list of authorized donors.
    """

    pass


class AuthorizedSpecimenViewSet(AuthorizedMixin, BaseSpecimenViewSet):
    """
    Retrieves a list of authorized specimens.
    """

    pass


class AuthorizedSampleRegistrationViewSet(
    AuthorizedMixin, BaseSampleRegistrationViewSet
):
    """
    Retrieves a list of authorized sample registrations.
    """

    pass


class AuthorizedPrimaryDiagnosisViewSet(AuthorizedMixin, BasePrimaryDiagnosisViewSet):
    """
    Retrieves a list of authorized primary diagnosises.
    """

    pass


class AuthorizedTreatmentViewSet(AuthorizedMixin, BaseTreatmentViewSet):
    """
    Retrieves a list of authorized treatments.
    """

    pass


class AuthorizedChemotherapyViewSet(AuthorizedMixin, BaseChemotherapyViewSet):
    """
    Retrieves a list of authorized chemotherapies.
    """

    pass


class AuthorizedHormoneTherapyViewSet(AuthorizedMixin, BaseHormoneTherapyViewSet):
    """
    Retrieves a list of authorized hormone therapies.
    """

    pass


class AuthorizedRadiationViewSet(AuthorizedMixin, BaseRadiationViewSet):
    """
    Retrieves a list of authorized radiations.
    """

    pass


class AuthorizedImmunotherapyViewSet(AuthorizedMixin, BaseImmunotherapyViewSet):
    """
    Retrieves a list of authorized immuno therapies.
    """

    pass


class AuthorizedSurgeryViewSet(AuthorizedMixin, BaseSurgeryViewSet):
    """
    Retrieves a list of authorized surgeries.
    """

    pass


class AuthorizedFollowUpViewSet(AuthorizedMixin, BaseFollowUpViewSet):
    """
    Retrieves a list of authorized follow ups.
    """

    pass


class AuthorizedBiomarkerViewSet(AuthorizedMixin, BaseBiomarkerViewSet):
    """
    Retrieves a list of authorized biomarkers.
    """

    pass


class AuthorizedComorbidityViewSet(AuthorizedMixin, BaseComorbidityViewSet):
    """
    Retrieves a list of authorized comorbidities.
    """

    pass


class AuthorizedExposureViewSet(AuthorizedMixin, BaseExposureViewSet):
    """
    Retrieves a list of authorized exposures.
    """

    pass


###############################################
#                                             #
#           CUSTOM API ENDPOINTS              #
#                                             #
###############################################


# TODO: redo this overview endpoint
@extend_schema(
    description="MoH Overview schema",
    responses={
        200: inline_serializer(
            name="moh_overview_schema_response",
            fields={
                "cohort_count": serializers.IntegerField(),
                "individual_count": serializers.IntegerField(),
            },
        )
    },
)
@api_view(["GET"])
@throttle_classes([MoHRateThrottle])
def moh_overview(_request):
    """
    Return a summary of the statistics for the database:
    - cohort_count: number of datasets
    - individual_count: number of individuals
    - ethnicity: the count of each ethenicity
    - gender: the count of each gender
    """
    return Response(
        {
            "cohort_count": Program.objects.count(),
            "individual_count": Donor.objects.count(),
            # where to get ethnicity and gender?
        }
    )


class CustomResquestSerializer(serializers.Serializer):
    model = serializers.CharField()
    include_fields = serializers.CharField()


@api_view(["POST"])
@throttle_classes([MoHRateThrottle])
@extend_schema(
    request=CustomResquestSerializer,
    responses={201: OpenApiTypes.STR},
)
def custom_response(request):
    model_name = request.GET.get("model")
    include_fields = request.GET.getlist("include_fields")

    try:
        model = apps.get_model(model_name)
    except LookupError:
        return Response(
            {"error": f"Model '{model_name}' not found."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    queryset = model.objects.only(*include_fields)

    # Perform any necessary operations on the queryset

    serialized_data = list(queryset.values())

    return Response(serialized_data)


class CustomViewSet(viewsets.ViewSet):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="model",
                description="Model name",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="include_fields",
                description="Comma-separated list of included fields",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
            ),
        ],
        responses={201: OpenApiTypes.STR},
    )
    def list(self, request):
        model_name = request.query_params.get("model")
        include_fields = request.query_params.getlist("include_fields")

        try:
            model = apps.get_model("mohpackets", model_name)
        except LookupError:
            return Response(
                {"error": f"Model '{model_name}' not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        queryset = model.objects.values(*include_fields)

        return Response(queryset)


@extend_schema_view(
    list=extend_schema(
        description="Retrieves a list of authorized Donor with clinical data."
    )
)
class AuthorizedDonorWithClinicalDataViewSet(AuthorizedMixin, BaseDonorViewSet):
    """
    This viewset provides access to Donor model and its related clinical data.
    It uses the DonorWithClinicalDataSerializer for serialization.

    The viewset pre-fetches related objects using the `prefetch_related` method
    to minimize database queries. This ensures that all the related objects are
    available in a single database query, improving the performance of the viewset.
    """

    serializer_class = DonorWithClinicalDataSerializer
    donor_biomarkers_prefetch = Prefetch(
        "biomarker_set",
        queryset=Biomarker.objects.filter(
            submitter_primary_diagnosis_id__isnull=True,
            submitter_specimen_id__isnull=True,
            submitter_treatment_id__isnull=True,
            submitter_follow_up_id__isnull=True,
        ),
    )
    primary_diagnosis_biomarkers_prefetch = Prefetch(
        "primarydiagnosis_set__biomarker_set",
        queryset=Biomarker.objects.filter(
            submitter_primary_diagnosis_id__isnull=False,
            submitter_specimen_id__isnull=True,
            submitter_treatment_id__isnull=True,
            submitter_follow_up_id__isnull=True,
        ),
    )
    specimen_biomarkers_prefetch = Prefetch(
        "primarydiagnosis_set__specimen_set__biomarker_set",
        queryset=Biomarker.objects.filter(
            submitter_specimen_id__isnull=False,
            submitter_follow_up_id__isnull=True,
        ),
    )
    treatment_biomarkers_prefetch = Prefetch(
        "primarydiagnosis_set__treatment_set__biomarker_set",
        queryset=Biomarker.objects.filter(
            submitter_treatment_id__isnull=False,
            submitter_follow_up_id__isnull=True,
        ),
    )
    followup_biomarkers_prefetch = Prefetch(
        "primarydiagnosis_set__treatment_set__followup_set__biomarker_set",
        queryset=Biomarker.objects.filter(
            submitter_follow_up_id__isnull=False,
        ),
    )

    donor_followups_prefetch = Prefetch(
        "followup_set",
        queryset=FollowUp.objects.filter(
            submitter_primary_diagnosis_id__isnull=True,
            submitter_treatment_id__isnull=True,
        ),
    )

    primary_diagnosis_followups_prefetch = Prefetch(
        "primarydiagnosis_set__followup_set",
        queryset=FollowUp.objects.filter(
            submitter_primary_diagnosis_id__isnull=False,
            submitter_treatment_id__isnull=True,
        ),
    )

    queryset = Donor.objects.prefetch_related(
        donor_biomarkers_prefetch,
        primary_diagnosis_biomarkers_prefetch,
        specimen_biomarkers_prefetch,
        treatment_biomarkers_prefetch,
        followup_biomarkers_prefetch,
        donor_followups_prefetch,
        primary_diagnosis_followups_prefetch,
        "comorbidity_set",
        "primarydiagnosis_set__treatment_set__chemotherapy_set",
        "primarydiagnosis_set__treatment_set__hormonetherapy_set",
        "primarydiagnosis_set__treatment_set__immunotherapy_set",
        "primarydiagnosis_set__treatment_set__radiation",
        "primarydiagnosis_set__treatment_set__surgery",
        "primarydiagnosis_set__specimen_set__sampleregistration_set",
    ).all()
