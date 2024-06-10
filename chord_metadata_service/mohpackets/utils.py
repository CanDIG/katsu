import json
import logging
import re
from enum import Enum

logger = logging.getLogger(__name__)

def get_schema_version():
    """
    Reads the version number from the schema file.
    """
    file_path = "chord_metadata_service/mohpackets/docs/schema_version.txt"
    with open(file_path, "r") as file:
        version = file.read().strip()
    return int(version)


def list_to_enum(enum_name, value_list):
    enum_dict = {}
    for item in value_list:
        enum_member_name = item.upper().replace(" ", "_")
        enum_dict[enum_member_name] = item
    return Enum(enum_name, enum_dict)
