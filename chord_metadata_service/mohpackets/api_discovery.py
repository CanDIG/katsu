from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from katsu_service.mohpackets.permissions import CanDIGAdminOrReadOnly
from katsu_service.mohpackets.filters import (
    DonorFilter,
    SpecimenFilter,
    SampleRegistrationFilter,
    PrimaryDiagnosisFilter,
    TreatmentFilter,
    ChemotherapyFilter,
    HormoneTherapyFilter,
    RadiationFilter,
    ImmunotherapyFilter,
    SurgeryFilter,
    FollowUpFilter,
    BiomarkerFilter,
    ComorbidityFilter,
)
from katsu_service.mohpackets.serializers import (
    DonorSerializer,
    SpecimenSerializer,
    SampleRegistrationSerializer,
    PrimaryDiagnosisSerializer,
    TreatmentSerializer,
    ChemotherapySerializer,
    HormoneTherapySerializer,
    RadiationSerializer,
    ImmunotherapySerializer,
    SurgerySerializer,
    FollowUpSerializer,
    BiomarkerSerializer,
    ComorbiditySerializer,
)
from katsu_service.mohpackets.models import (
    Donor,
    Specimen,
    SampleRegistration,
    PrimaryDiagnosis,
    Treatment,
    Chemotherapy,
    HormoneTherapy,
    Radiation,
    Immunotherapy,
    Surgery,
    FollowUp,
    Biomarker,
    Comorbidity,
)

"""
    This Views module based on the api_views.py module, but only contains
    the ListModelMixin, meaning the user cannot use any create, update,
    or view details APIs.
    It overrides the list function to return the count of patients for discovery purposes.
    NOTE: This is a temporary solution until we implement Beacon discovery features.
"""

##########################################
#                                        #
#           HELPER FUNCTIONS             #
#                                        #
##########################################


def get_discovery_response(self):
    """
    This function returns the count of unique submitter_donor_ids
    (aka the number of patients the queryset has).
    """
    queryset = self.filter_queryset(self.get_queryset())
    count = queryset.values_list("submitter_donor_id").distinct().count()
    return Response({"discovery_count": count})


###############################################
#                                             #
#           DISCOVERY API VIEWS               #
#                                             #
###############################################


class DiscoveryDonorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DonorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DonorFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = Donor.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoverySpecimenViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SpecimenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SpecimenFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = Specimen.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoverySampleRegistrationViewSet(
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = SampleRegistrationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SampleRegistrationFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = SampleRegistration.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoveryPrimaryDiagnosisViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PrimaryDiagnosisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PrimaryDiagnosisFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = PrimaryDiagnosis.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoveryTreatmentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TreatmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TreatmentFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = Treatment.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoveryChemotherapyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ChemotherapySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChemotherapyFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = Chemotherapy.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoveryHormoneTherapyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = HormoneTherapySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HormoneTherapyFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = HormoneTherapy.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoveryRadiationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RadiationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RadiationFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = Radiation.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoveryImmunotherapyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ImmunotherapySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ImmunotherapyFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = Immunotherapy.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoverySurgeryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SurgerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SurgeryFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = Surgery.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoveryFollowUpViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FollowUpSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FollowUpFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = FollowUp.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoveryBiomarkerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BiomarkerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BiomarkerFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = Biomarker.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)


class DiscoveryComorbidityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ComorbiditySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComorbidityFilter
    permission_classes = [CanDIGAdminOrReadOnly]
    queryset = Comorbidity.objects.all()

    def list(self, request, *args, **kwargs):
        return get_discovery_response(self)
