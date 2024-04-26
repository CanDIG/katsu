import json
import logging
import re
from enum import Enum

logger = logging.getLogger(__name__)


def get_schema_url():
    """
    Retrieve the SHA URL from schema.json.
    It reads the first 6 lines of the JSON file and extracts the URL from the "description".
    """
    url_pattern = r"https://[^\s]+"  # get everything after https

    schema_url = "None"

    try:
        with open(
            "chord_metadata_service/mohpackets/docs/schema.json", "r"
        ) as json_file:
            # Read the first 6 lines of the JSON file only
            # The line we are looking for is on the 6th
            first_6_lines = [next(json_file) for _ in range(6)]
            first_6_lines.extend(["}", "}"])  # make valid JSON
            # Concatenate the lines to form a JSON string
            json_str = "".join(first_6_lines)
            data = json.loads(json_str)
            desc_str = data["info"]["description"]
            schema_url = re.search(url_pattern, desc_str).group()
    except Exception as e:
        logger.debug(
            f"An error occurred while fetching the schema URL. Details: {str(e)}"
        )

    return schema_url


def list_to_enum(enum_name, value_list):
    enum_dict = {}
    for item in value_list:
        enum_member_name = item.upper().replace(" ", "_")
        enum_dict[enum_member_name] = item
    return Enum(enum_name, enum_dict)
