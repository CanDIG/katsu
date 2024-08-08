from typing import Optional

from ninja import Field
from chord_metadata_service.mohpackets.schemas.base import (
    BaseBiomarkerSchema,
    BaseSystemicTherapySchema,
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
    BaseTreatmentSchema,
)


"""
Module with schema used for ingesting

All fields are derived from the model, with the fix for FK and uuid

Author: Son Chau
"""


########################################
#                                      #
#           INGEST SCHEMA              #
#                                      #
########################################


class ProgramIngestSchema(BaseProgramSchema):
    pass


class DonorIngestSchema(BaseDonorSchema):
    program_id_id: str = Field(..., alias="program_id")
    uuid: Optional[str] = None

    class Config(BaseDonorSchema.Config):
        use_enum_values = True


class PrimaryDiagnosisIngestSchema(BasePrimaryDiagnosisSchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    uuid: Optional[str] = None

    class Config(BasePrimaryDiagnosisSchema.Config):
        use_enum_values = True


class BiomarkerIngestSchema(BaseBiomarkerSchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    uuid: Optional[str] = None

    class Config(BaseBiomarkerSchema.Config):
        use_enum_values = True


class SystemicTherapyIngestSchema(BaseSystemicTherapySchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    submitter_treatment_id: str
    uuid: Optional[str] = None

    class Config(BaseSystemicTherapySchema.Config):
        use_enum_values = True


class ComorbidityIngestSchema(BaseComorbiditySchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    uuid: Optional[str] = None

    class Config(BaseComorbiditySchema.Config):
        use_enum_values = True


class ExposureIngestSchema(BaseExposureSchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    uuid: Optional[str] = None

    class Config(BaseExposureSchema.Config):
        use_enum_values = True


class FollowUpIngestSchema(BaseFollowUpSchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    submitter_primary_diagnosis_id: Optional[str] = None
    submitter_treatment_id: Optional[str] = None
    uuid: Optional[str] = None

    class Config(BaseFollowUpSchema.Config):
        use_enum_values = True




class RadiationIngestSchema(BaseRadiationSchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    submitter_treatment_id: str
    uuid: Optional[str] = None

    class Config(BaseRadiationSchema.Config):
        use_enum_values = True


class SampleRegistrationIngestSchema(BaseSampleRegistrationSchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    submitter_specimen_id: str
    uuid: Optional[str] = None

    class Config(BaseSampleRegistrationSchema.Config):
        use_enum_values = True


class SpecimenIngestSchema(BaseSpecimenSchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    submitter_primary_diagnosis_id: str
    uuid: Optional[str] = None

    class Config(BaseSpecimenSchema.Config):
        use_enum_values = True


class SurgeryIngestSchema(BaseSurgerySchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    submitter_treatment_id: str
    uuid: Optional[str] = None

    class Config(BaseSurgerySchema.Config):
        use_enum_values = True


class TreatmentIngestSchema(BaseTreatmentSchema):
    program_id_id: str = Field(..., alias="program_id")
    submitter_donor_id: str
    submitter_primary_diagnosis_id: str
    uuid: Optional[str] = None

    class Config(BaseTreatmentSchema.Config):
        use_enum_values = True
