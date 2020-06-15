import json
import os
import uuid

from dateutil.parser import isoparse
from typing import Callable

from chord_metadata_service.chord.data_types import DATA_TYPE_EXPERIMENT, DATA_TYPE_PHENOPACKET
from chord_metadata_service.chord.models import Table, TableOwnership
from chord_metadata_service.experiments import models as em
from chord_metadata_service.phenopackets import models as pm
from chord_metadata_service.resources import models as rm, utils as ru
from chord_metadata_service.restapi.fhir_ingest import (
    ingest_patients,
    ingest_observations,
    ingest_conditions,
    ingest_specimens
)


__all__ = [
    "METADATA_WORKFLOWS",
    "WORKFLOWS_PATH",
    "ingest_resource",
    "WORKFLOW_INGEST_FUNCTION_MAP",
]

WORKFLOW_PHENOPACKETS_JSON = "phenopackets_json"
WORKFLOW_EXPERIMENTS_JSON = "experiments_json"
WORKFLOW_FHIR_JSON = "fhir_json"

METADATA_WORKFLOWS = {
    "ingestion": {
        WORKFLOW_PHENOPACKETS_JSON: {
            "name": "Bento Phenopackets-Compatible JSON",
            "description": "This ingestion workflow will validate and import a Phenopackets schema-compatible "
                           "JSON document.",
            "data_type": DATA_TYPE_PHENOPACKET,
            "file": "phenopackets_json.wdl",
            "inputs": [
                {
                    "id": "json_document",
                    "type": "file",
                    "required": True,
                    "extensions": [".json"]
                }
            ],
            "outputs": [
                {
                    "id": "json_document",
                    "type": "file",
                    "value": "{json_document}"
                }
            ]
        },
        WORKFLOW_EXPERIMENTS_JSON: {
            "name": "Bento Experiments JSON",
            "description": "This ingestion workflow will validate and import a Bento Experiments schema-compatible "
                           "JSON document.",
            "data_type": DATA_TYPE_EXPERIMENT,
            "file": "experiments_json.wdl",
            "inputs": [
                {
                    "id": "json_document",
                    "type": "file",
                    "required": True,
                    "extensions": [".json"]
                }
            ],
            "outputs": [
                {
                    "id": "json_document",
                    "type": "file",
                    "value": "{json_document}"
                }
            ]
        },
        WORKFLOW_FHIR_JSON: {
            "name": "FHIR Resources JSON",
            "description": "This ingestion workflow will validate and import a FHIR schema-compatible "
                           "JSON document, and convert it to the Bento metadata service's internal Phenopackets-based "
                           "data model.",
            "data_type": DATA_TYPE_PHENOPACKET,
            "file": "fhir_json.wdl",
            "inputs": [
                {
                    "id": "patients",
                    "type": "file",
                    "required": True,
                    "extensions": [".json"]
                },
                {
                    "id": "observations",
                    "type": "file",
                    "required": False,
                    "extensions": [".json"]
                },
                {
                    "id": "conditions",
                    "type": "file",
                    "required": False,
                    "extensions": [".json"]
                },
                {
                    "id": "specimens",
                    "type": "file",
                    "required": False,
                    "extensions": [".json"]
                },
                {
                    "id": "created_by",
                    "required": False,
                    "type": "string"
                },

            ],
            "outputs": [
                {
                    "id": "patients",
                    "type": "file",
                    "value": "{patients}"
                },
                {
                    "id": "observations",
                    "type": "file",
                    "value": "{observations}"
                },
                {
                    "id": "conditions",
                    "type": "file",
                    "value": "{conditions}"
                },
                {
                    "id": "specimens",
                    "type": "file",
                    "value": "{specimens}"
                },
                {
                    "id": "created_by",
                    "type": "string",
                    "value": "{created_by}"
                },

            ]
        }
    },
    "analysis": {}
}

WORKFLOWS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "workflows")


def create_phenotypic_feature(pf):
    pf_obj = pm.PhenotypicFeature(
        description=pf.get("description", ""),
        pftype=pf["type"],
        negated=pf.get("negated", False),
        severity=pf.get("severity"),
        modifier=pf.get("modifier", []),  # TODO: Validate ontology term in schema...
        onset=pf.get("onset", None),
        evidence=pf.get("evidence")  # TODO: Separate class?
    )

    pf_obj.save()
    return pf_obj


def _query_and_check_nulls(obj: dict, key: str, transform: Callable = lambda x: x):
    value = obj.get(key)
    return {f"{key}__isnull": True} if value is None else {key: transform(value)}


def ingest_resource(resource: dict) -> rm.Resource:
    namespace_prefix = resource["namespace_prefix"].strip()
    version = resource.get("version", "").strip()
    assigned_resource_id = ru.make_resource_id(namespace_prefix, version)

    rs_obj, _ = rm.Resource.objects.get_or_create(
        # If this doesn't match assigned_resource_id, it'll throw anyway
        id=resource.get("id", assigned_resource_id),
        name=resource["name"],
        namespace_prefix=namespace_prefix,
        url=resource["url"],
        version=version,
        iri_prefix=resource["iri_prefix"]
    )

    return rs_obj


def ingest_experiment(experiment_data, table_id) -> em.Experiment:
    """Ingests a single experiment."""

    new_experiment_id = experiment_data.get("id", str(uuid.uuid4()))

    reference_registry_id = experiment_data.get("reference_registry_id")
    qc_flags = experiment_data.get("qc_flags", [])
    experiment_type = experiment_data["experiment_type"]
    experiment_ontology = experiment_data.get("experiment_ontology", [])
    molecule_ontology = experiment_data.get("molecule_ontology", [])
    molecule = experiment_data.get("molecule")
    library_strategy = experiment_data["library_strategy"]
    other_fields = experiment_data.get("other_fields", {})
    biosample = experiment_data.get("biosample")

    if biosample is not None:
        biosample = pm.Biosample.objects.get(id=biosample)  # TODO: Handle error nicer

    new_experiment = em.Experiment.objects.create(
        id=new_experiment_id,
        reference_registry_id=reference_registry_id,
        qc_flags=qc_flags,
        experiment_type=experiment_type,
        experiment_ontology=experiment_ontology,
        molecule_ontology=molecule_ontology,
        molecule=molecule,
        library_strategy=library_strategy,
        other_fields=other_fields,
        biosample=biosample,
        table=Table.objects.get(ownership_record_id=table_id, data_type=DATA_TYPE_EXPERIMENT)
    )

    return new_experiment


def ingest_phenopacket(phenopacket_data, table_id) -> pm.Phenopacket:
    """Ingests a single phenopacket."""

    new_phenopacket_id = phenopacket_data.get("id", str(uuid.uuid4()))

    subject = phenopacket_data.get("subject")
    phenotypic_features = phenopacket_data.get("phenotypic_features", [])
    biosamples = phenopacket_data.get("biosamples", [])
    genes = phenopacket_data.get("genes", [])
    diseases = phenopacket_data.get("diseases", [])
    meta_data = phenopacket_data["meta_data"]

    if subject:
        # Be a bit flexible with the subject date_of_birth field for Signature; convert blank strings to None.
        subject["date_of_birth"] = subject.get("date_of_birth") or None
        subject_query = _query_and_check_nulls(subject, "date_of_birth", transform=isoparse)
        for k in ("alternate_ids", "age", "sex", "karyotypic_sex", "taxonomy"):
            subject_query.update(_query_and_check_nulls(subject, k))
        subject, _ = pm.Individual.objects.get_or_create(id=subject["id"], **subject_query)

    phenotypic_features_db = [create_phenotypic_feature(pf) for pf in phenotypic_features]

    biosamples_db = []
    for bs in biosamples:
        # TODO: This should probably be a JSON field, or compound key with code/body_site
        procedure, _ = pm.Procedure.objects.get_or_create(**bs["procedure"])

        bs_query = _query_and_check_nulls(bs, "individual_id", lambda i: pm.Individual.objects.get(id=i))
        for k in ("sampled_tissue", "taxonomy", "individual_age_at_collection", "histological_diagnosis",
                  "tumor_progression", "tumor_grade"):
            bs_query.update(_query_and_check_nulls(bs, k))

        bs_obj, bs_created = pm.Biosample.objects.get_or_create(
            id=bs["id"],
            description=bs.get("description", ""),
            procedure=procedure,
            is_control_sample=bs.get("is_control_sample", False),
            diagnostic_markers=bs.get("diagnostic_markers", []),
            **bs_query
        )

        if bs_created:
            bs_pfs = [create_phenotypic_feature(pf) for pf in bs.get("phenotypic_features", [])]
            bs_obj.phenotypic_features.set(bs_pfs)

        # TODO: Update phenotypic features otherwise?

        biosamples_db.append(bs_obj)

    # TODO: May want to augment alternate_ids
    genes_db = []
    for g in genes:
        # TODO: Validate CURIE
        # TODO: Rename alternate_id
        g_obj, _ = pm.Gene.objects.get_or_create(
            id=g["id"],
            alternate_ids=g.get("alternate_ids", []),
            symbol=g["symbol"]
        )
        genes_db.append(g_obj)

    diseases_db = []
    for disease in diseases:
        # TODO: Primary key, should this be a model?
        d_obj, _ = pm.Disease.objects.get_or_create(
            term=disease["term"],
            disease_stage=disease.get("disease_stage", []),
            tnm_finding=disease.get("tnm_finding", []),
            **_query_and_check_nulls(disease, "onset")
        )
        diseases_db.append(d_obj.id)

    resources_db = [ingest_resource(rs) for rs in meta_data.get("resources", [])]

    meta_data_obj = pm.MetaData(
        created_by=meta_data["created_by"],
        submitted_by=meta_data.get("submitted_by"),
        phenopacket_schema_version="1.0.0-RC3",
        external_references=meta_data.get("external_references", [])
    )
    meta_data_obj.save()

    meta_data_obj.resources.set(resources_db)

    new_phenopacket = pm.Phenopacket(
        id=new_phenopacket_id,
        subject=subject,
        meta_data=meta_data_obj,
        table=Table.objects.get(ownership_record_id=table_id, data_type=DATA_TYPE_PHENOPACKET)
    )

    new_phenopacket.save()

    new_phenopacket.phenotypic_features.set(phenotypic_features_db)
    new_phenopacket.biosamples.set(biosamples_db)
    new_phenopacket.genes.set(genes_db)
    new_phenopacket.diseases.set(diseases_db)

    return new_phenopacket


def _map_if_list(fn, data, *args):
    # TODO: Any sequence?
    return [fn(d, *args) for d in data] if isinstance(data, list) else fn(data, *args)


def ingest_experiments_workflow(workflow_outputs, table_id):
    with open(workflow_outputs["json_document"], "r") as jf:
        json_data = json.load(jf)

        dataset = TableOwnership.objects.get(table_id=table_id).dataset

        for rs in json_data.get("resources", []):
            dataset.additional_resources.add(ingest_resource(rs))

        return [ingest_experiment(exp, table_id) for exp in json_data.get("experiments", [])]


def ingest_phenopacket_workflow(workflow_outputs, table_id):
    with open(workflow_outputs["json_document"], "r") as jf:
        json_data = json.load(jf)
        return _map_if_list(ingest_phenopacket, json_data, table_id)


def ingest_fhir_workflow(workflow_outputs, table_id):
    with open(workflow_outputs["patients"], "r") as pf:
        patients_data = json.load(pf)
        phenopacket_ids = ingest_patients(
            patients_data,
            table_id,
            workflow_outputs.get("created_by") or "Imported from file.",
        )

    if "observations" in workflow_outputs:
        with open(workflow_outputs["observations"], "r") as of:
            observations_data = json.load(of)
            ingest_observations(phenopacket_ids, observations_data)

    if "conditions" in workflow_outputs:
        with open(workflow_outputs["conditions"], "r") as cf:
            conditions_data = json.load(cf)
            ingest_conditions(phenopacket_ids, conditions_data)

    if "specimens" in workflow_outputs:
        with open(workflow_outputs["specimens"], "r") as sf:
            specimens_data = json.load(sf)
            ingest_specimens(phenopacket_ids, specimens_data)


WORKFLOW_INGEST_FUNCTION_MAP = {
    WORKFLOW_EXPERIMENTS_JSON: ingest_experiments_workflow,
    WORKFLOW_PHENOPACKETS_JSON: ingest_phenopacket_workflow,
    WORKFLOW_FHIR_JSON: ingest_fhir_workflow,
}
