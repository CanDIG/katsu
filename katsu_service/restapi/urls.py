from django.urls import path, include
from rest_framework import routers

from katsu_service.katsu import api_views as katsu_views
from katsu_service.experiments import api_views as experiment_views
from katsu_service.patients import api_views as individual_views
from katsu_service.phenopackets import api_views as phenopacket_views
from katsu_service.phenopackets.autocomplete_views import (
    DiseaseTermAutocomplete,
    PhenotypicFeatureTypeAutocomplete,
    BiosampleSampledTissueAutocomplete
)
from katsu_service.resources import api_views as resources_views
from .api_views import overview, public_search_fields, public_overview
from katsu_service.restapi.routers import BatchListRouter

__all__ = ["router", "batch_router", "urlpatterns"]

router = routers.DefaultRouter(trailing_slash=False)
batch_router = BatchListRouter()

# KATSU app urls
router.register(r'projects', katsu_views.ProjectViewSet)
router.register(r'datasets', katsu_views.DatasetViewSet, basename="datasets")
router.register(r'table_ownership', katsu_views.TableOwnershipViewSet)
router.register(r'tables', katsu_views.TableViewSet)

# Experiments app urls
router.register(r'experiments', experiment_views.ExperimentViewSet)
router.register(r'experimentresults', experiment_views.ExperimentResultViewSet)

# Patients app urls
router.register(r'individuals', individual_views.IndividualViewSet, basename="individuals")
batch_router.register(r'batch/individuals', individual_views.IndividualBatchViewSet, basename="batch/individuals")

# Phenopackets app urls
router.register(r'phenotypicfeatures', phenopacket_views.PhenotypicFeatureViewSet, basename="phenotypicfeatures")
router.register(r'procedures', phenopacket_views.ProcedureViewSet, basename="procedures")
router.register(r'htsfiles', phenopacket_views.HtsFileViewSet, basename="htsfiles")
router.register(r'genes', phenopacket_views.GeneViewSet, basename="genes")
router.register(r'variants', phenopacket_views.VariantViewSet, basename="variants")
router.register(r'diseases', phenopacket_views.DiseaseViewSet, basename="diseases")
router.register(r'metadata', phenopacket_views.MetaDataViewSet, basename="metadata")
router.register(r'biosamples', phenopacket_views.BiosampleViewSet, basename="biosamples")
router.register(r'phenopackets', phenopacket_views.PhenopacketViewSet, basename="phenopackets")
router.register(r'genomicinterpretations', phenopacket_views.GenomicInterpretationViewSet,
                basename="genomicinterpretations")
router.register(r'diagnoses', phenopacket_views.DiagnosisViewSet, basename="diagnoses")
router.register(r'interpretations', phenopacket_views.InterpretationViewSet, basename="interpretations")

# Resources app urls
router.register(r'resources', resources_views.ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(batch_router.urls)),
    # apps schemas
    path('katsu_phenopacket_schema', phenopacket_views.get_katsu_phenopacket_schema,
         name="katsu-phenopacket-schema"),
    path('experiment_schema', experiment_views.get_experiment_schema,
         name="experiment-schema"),
    # overview
    path('overview', overview, name="overview"),
    # autocomplete URLs
    path('disease_term_autocomplete', DiseaseTermAutocomplete.as_view(), name='disease-term-autocomplete',),
    path('phenotypic_feature_type_autocomplete', PhenotypicFeatureTypeAutocomplete.as_view(),
         name='phenotypic-feature-type-autocomplete',),
    path('biosample_sampled_tissue_autocomplete', BiosampleSampledTissueAutocomplete.as_view(),
         name='biosample-sampled-tissue-autocomplete',),
    # public
    path('public', individual_views.PublicListIndividuals.as_view(),
         name='public',),
    # public search fields schema
    path('public_search_fields', public_search_fields, name='public-search-fields',),
    # public overview
    path('public_overview', public_overview, name='public-overview',),
]
