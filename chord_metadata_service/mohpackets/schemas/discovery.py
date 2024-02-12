from typing import Dict, List

from ninja import Schema

"""
Module with schema used for discovery response

Author: Son Chau
"""


class ProgramDiscoverySchema(Schema):
    program_id: str
    metadata: object


class DiscoverySchema(Schema):
    donors_by_cohort: Dict[str, int]
