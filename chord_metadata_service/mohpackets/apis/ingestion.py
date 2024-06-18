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


def create_instances(payloads: List, model_cls: Type):
    instances = []
    try:
        for item in payloads:
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
    request, payloads: List[ProgramIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Program)


@router.post("/donors/")
def create_donors(request, payloads: List[DonorIngestSchema], response: HttpResponse):
    return create_instances(payloads, Donor)


@router.post("/biomarkers/")
def create_biomarkers(
    request, payloads: List[BiomarkerIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Biomarker)


@router.post("/chemotherapies/")
def create_chemotherapies(
    request, payloads: List[ChemotherapyIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Chemotherapy)


@router.post("/comorbidities/")
def create_comorbidities(
    request, payloads: List[ComorbidityIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Comorbidity)


@router.post("/exposures/")
def create_exposures(
    request, payloads: List[ExposureIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Exposure)


@router.post("/followups/")
def create_followups(
    request, payloads: List[FollowUpIngestSchema], response: HttpResponse
):
    return create_instances(payloads, FollowUp)


@router.post("/hormone_therapies/")
def create_hormone_therapies(
    request, payloads: List[HormoneTherapyIngestSchema], response: HttpResponse
):
    return create_instances(payloads, HormoneTherapy)


@router.post("/immunotherapies/")
def create_immunotherapies(
    request, payloads: List[ImmunotherapyIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Immunotherapy)


@router.post("/primary_diagnoses/")
def create_primary_diagnoses(
    request, payloads: List[PrimaryDiagnosisIngestSchema], response: HttpResponse
):
    return create_instances(payloads, PrimaryDiagnosis)


@router.post("/radiations/")
def create_radiations(
    request, payloads: List[RadiationIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Radiation)


@router.post("/sample_registrations/")
def create_sample_registrations(
    request, payloads: List[SampleRegistrationIngestSchema], response: HttpResponse
):
    return create_instances(payloads, SampleRegistration)


@router.post("/specimens/")
def create_specimens(
    request, payloads: List[SpecimenIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Specimen)


@router.post("/surgeries/")
def create_surgeries(
    request, payloads: List[SurgeryIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Surgery)


@router.post("/treatments/")
def create_treatments(
    request, payloads: List[TreatmentIngestSchema], response: HttpResponse
):
    return create_instances(payloads, Treatment)
