from http import HTTPStatus
from typing import Type, List

from django.http import HttpResponse, JsonResponse
from ninja import Router

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
from chord_metadata_service.mohpackets.schemas.ingestion import (
    BiomarkerIngestSchema,
    ChemotherapyIngestSchema,
    ComorbidityIngestSchema,
    DonorIngestSchema,
    ExposureIngestSchema,
    FollowUpIngestSchema,
    HormoneTherapyIngestSchema,
    ImmunotherapyIngestSchema,
    PrimaryDiagnosisIngestSchema,
    ProgramIngestSchema,
    RadiationIngestSchema,
    SampleRegistrationIngestSchema,
    SpecimenIngestSchema,
    SurgeryIngestSchema,
    TreatmentIngestSchema,
)

"""
Module with create APIs for clinical data.
These APIs require admin authorization

Author: Son Chau
"""

router = Router()


def create_instances(payload: List, model_cls: Type):
    instances = []
    try:
        for item in payload:
            instance = model_cls.objects.create(**item.dict())
            instances.append(instance)
    except Exception as e:
        return JsonResponse(
            status=HTTPStatus.BAD_REQUEST,
            data={"error": str(e)},
        )

    created_instances = [str(instance) for instance in instances]
    return JsonResponse(
        status=HTTPStatus.CREATED,
        data={"created": created_instances},
    )


@router.post("/programs/")
def create_programs(
    request, payload: List[ProgramIngestSchema], response: HttpResponse
):
    return create_instances(payload, Program)


@router.post("/donors/")
def create_donors(request, payload: List[DonorIngestSchema], response: HttpResponse):
    return create_instances(payload, Donor)


@router.post("/biomarkers/")
def create_biomarkers(
    request, payload: List[BiomarkerIngestSchema], response: HttpResponse
):
    return create_instances(payload, Biomarker)


@router.post("/chemotherapies/")
def create_chemotherapies(
    request, payload: List[ChemotherapyIngestSchema], response: HttpResponse
):
    return create_instances(payload, Chemotherapy)


@router.post("/comorbidities/")
def create_comorbidities(
    request, payload: List[ComorbidityIngestSchema], response: HttpResponse
):
    return create_instances(payload, Comorbidity)


@router.post("/exposures/")
def create_exposures(
    request, payload: List[ExposureIngestSchema], response: HttpResponse
):
    return create_instances(payload, Exposure)


@router.post("/followups/")
def create_followups(
    request, payload: List[FollowUpIngestSchema], response: HttpResponse
):
    return create_instances(payload, FollowUp)


@router.post("/hormone_therapies/")
def create_hormone_therapies(
    request, payload: List[HormoneTherapyIngestSchema], response: HttpResponse
):
    return create_instances(payload, HormoneTherapy)


@router.post("/immunotherapies/")
def create_immunotherapies(
    request, payload: List[ImmunotherapyIngestSchema], response: HttpResponse
):
    return create_instances(payload, Immunotherapy)


@router.post("/primary_diagnoses/")
def create_primary_diagnoses(
    request, payload: List[PrimaryDiagnosisIngestSchema], response: HttpResponse
):
    return create_instances(payload, PrimaryDiagnosis)


@router.post("/radiations/")
def create_radiations(
    request, payload: List[RadiationIngestSchema], response: HttpResponse
):
    return create_instances(payload, Radiation)


@router.post("/sample_registrations/")
def create_sample_registrations(
    request, payload: List[SampleRegistrationIngestSchema], response: HttpResponse
):
    return create_instances(payload, SampleRegistration)


@router.post("/specimens/")
def create_specimens(
    request, payload: List[SpecimenIngestSchema], response: HttpResponse
):
    return create_instances(payload, Specimen)


@router.post("/surgeries/")
def create_surgeries(
    request, payload: List[SurgeryIngestSchema], response: HttpResponse
):
    return create_instances(payload, Surgery)


@router.post("/treatments/")
def create_treatments(
    request, payload: List[TreatmentIngestSchema], response: HttpResponse
):
    return create_instances(payload, Treatment)
