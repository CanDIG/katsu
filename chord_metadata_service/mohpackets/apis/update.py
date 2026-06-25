from enum import Enum
from http import HTTPStatus
from typing import Any, Dict

from ninja import Router, Schema
from ninja.responses import Status

from chord_metadata_service.mohpackets.models import Program
from chord_metadata_service.mohpackets.schemas.base import ProgramUpdateSchema

"""
Update APIs for Program.

Two separate routers with different authorization:
    - update_router: clinical fields, authorized for program curators/admins
      (mounted with DeleteAuth). The metadata field is NOT updatable here.
    - metadata_router: the metadata field only, authorized for the ingest
      service token (mounted with ServiceTokenAuth). Users cannot reach it.

Author: Son Chau
"""


def _to_value(value):
    """Convert Enum members (and lists of them) to their raw values for storage."""
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, list):
        return [item.value if isinstance(item, Enum) else item for item in value]
    return value


##########################################
#                                        #
#       CLINICAL FIELD UPDATE            #
#                                        #
##########################################
update_router = Router()


@update_router.patch(
    "/programs/{program_id}/",
    response={200: Dict[str, str], 404: Dict[str, str]},
)
def update_program(request, program_id: str, payload: ProgramUpdateSchema):
    """
    Partially update a Program's clinical fields.

    Only the fields present in the request body are modified; the metadata
    field is excluded from ProgramUpdateSchema and is never touched here.
    """
    try:
        program = Program.objects.get(pk=program_id)
    except Program.DoesNotExist:
        return Status(
            HTTPStatus.NOT_FOUND,
            {"error": "Program matching query does not exist"},
        )

    data = payload.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(program, field, _to_value(value))

    program.save(update_fields=[*data.keys(), "updated"])
    return Status(HTTPStatus.OK, {"updated": program_id})


##########################################
#                                        #
#          METADATA UPDATE               #
#                                        #
##########################################
metadata_router = Router()


class MetadataSchema(Schema):
    metadata: Dict[str, Any]


@metadata_router.patch(
    "/programs/{program_id}/metadata/",
    response={200: Dict[str, str], 404: Dict[str, str]},
)
def update_program_metadata(request, program_id: str, payload: MetadataSchema):
    """
    Update a Program's metadata field. Restricted to the ingest service token.
    """
    try:
        program = Program.objects.get(pk=program_id)
    except Program.DoesNotExist:
        return Status(
            HTTPStatus.NOT_FOUND,
            {"error": "Program matching query does not exist"},
        )

    program.metadata = payload.metadata
    program.save(update_fields=["metadata", "updated"])
    return Status(HTTPStatus.OK, {"updated": program_id})
