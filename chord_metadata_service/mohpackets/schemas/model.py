from typing import List, Optional

from ninja import Field, Schema

from chord_metadata_service.mohpackets.schemas.base import (
    BaseBiomarkerSchema,
    BaseComorbiditySchema,
    BaseDonorSchema,
    BaseExposureSchema,
    BaseFollowUpSchema,
    BasePrimaryDiagnosisSchema,
    BaseProgramSchema,
    BaseRadiationSchema,
    BaseSampleRegistrationSchema,
    BaseSpecimenSchema,
    BaseSurgerySchema,
    BaseSystemicTherapySchema,
    BaseTreatmentSchema,
)

"""
Schemas for clinical models, inherted from base schemas.

Added "foreign keys" to link between models

Author: Son Chau
"""

########################################
#                                      #
#           MODEL SCHEMA               #
#                                      #
########################################


class ProgramModelSchema(BaseProgramSchema):
    pass


class DonorModelSchema(BaseDonorSchema):
    program_id: str = Field(..., alias="program_id_id")


class SampleRegistrationDetailSchema(Schema):
    submitter_sample_id: str
    tumour_normal_designation: Optional[str] = None


class QueryDonorSchema(BaseDonorSchema):
    program_id: str = Field(..., alias="program_id_id")
    primary_site: Optional[List[str]] = None
    treatment_type: Optional[List[str]] = None
    submitter_sample_ids: Optional[List[str]] = None
    sample_registrations: List[SampleRegistrationDetailSchema] = []

    # Per-sample detail (adds tumour/normal alongside the flat submitter_sample_ids).
    # Read from the sampleregistration_set already prefetched by query_donors(), so
    # this adds no extra DB query (no N+1). Lets the query service build its
    # sample->donor map from this response and drop its separate, unfiltered call to
    # /authorized/sample_registrations/.
    @staticmethod
    def resolve_sample_registrations(obj):
        return [
            {
                "submitter_sample_id": s.submitter_sample_id,
                "tumour_normal_designation": s.tumour_normal_designation,
            }
            for s in obj.sampleregistration_set.all()
        ]


class PrimaryDiagnosisModelSchema(BasePrimaryDiagnosisSchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str


class SpecimenModelSchema(BaseSpecimenSchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str
    submitter_primary_diagnosis_id: str


class SampleRegistrationModelSchema(BaseSampleRegistrationSchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str
    submitter_specimen_id: str


class TreatmentModelSchema(BaseTreatmentSchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str
    submitter_primary_diagnosis_id: str


class SurgeryModelSchema(BaseSurgerySchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str
    submitter_treatment_id: str


class RadiationModelSchema(BaseRadiationSchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str
    submitter_treatment_id: str


class SystemicTherapyModelSchema(BaseSystemicTherapySchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str
    submitter_treatment_id: str


class FollowUpModelSchema(BaseFollowUpSchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str
    submitter_primary_diagnosis_id: Optional[str] = None
    submitter_treatment_id: Optional[str] = None


class BiomarkerModelSchema(BaseBiomarkerSchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str


class ExposureModelSchema(BaseExposureSchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str


class ComorbidityModelSchema(BaseComorbiditySchema):
    program_id: str = Field(..., alias="program_id_id")
    submitter_donor_id: str
