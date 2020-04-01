import datetime
from django.test import TestCase
from chord_metadata_service.patients.models import Individual
from ..models import *
from .constants import *
from rest_framework import serializers
from django.core.validators import ValidationError

class GeneticVariantTestedTest(TestCase):
    """ Test module for GeneticVariantTested model """

    def setUp(self):
        GeneticVariantTested.objects.create(**VALID_GENETIC_VARIANT_TESTED)

    def test_variant_tested(self):
        variant_tested = GeneticVariantTested.objects.get(id='variant_tested:01')
        self.assertIsInstance(variant_tested.method, dict)
        self.assertEqual(variant_tested.method['label'], 'Polymerase Chain Reaction')
        self.assertEqual(variant_tested.variant_tested_identifier['id'],
                         variant_tested.variant_tested_identifier['label'])
        self.assertIsInstance(variant_tested.variant_tested_hgvs_name, list)
        self.assertIn("NM_001346897.2:c.-237A>G", variant_tested.variant_tested_hgvs_name)
        self.assertIsInstance(variant_tested.variant_tested_description, str)
        self.assertEqual(variant_tested.variant_tested_description, 'single nucleotide variant')
        self.assertEqual(variant_tested.data_value['id'], 'LA6576-8')
        self.assertEqual(variant_tested.data_value['label'], 'Positive')

    def create(self, **kwargs):
        e = GeneticVariantTested(**kwargs)
        e.full_clean()
        e.save()

    def test_validation(self):
        self.assertRaises(serializers.ValidationError, self.create, **INVALID_GENETIC_VARIANT_TESTED)


class GeneticVariantFoundTest(TestCase):
    """ Test module for GeneticVariantFound model """

    def setUp(self):
        GeneticVariantFound.objects.create(**VALID_GENETIC_VARIANT_FOUND)

    def test_variant_found(self):
        variant_found = GeneticVariantFound.objects.get(id='variant_found:01')
        self.assertIsInstance(variant_found.method, dict)
        self.assertEqual(variant_found.method['label'], 'Polymerase Chain Reaction')
        self.assertEqual(variant_found.variant_found_identifier['id'],
                         variant_found.variant_found_identifier['label'])
        self.assertIsInstance(variant_found.variant_found_hgvs_name, list)
        self.assertIn("NM_001346897.2:c.-237A>G", variant_found.variant_found_hgvs_name)
        self.assertIsInstance(variant_found.variant_found_description, str)
        self.assertEqual(variant_found.variant_found_description, 'single nucleotide variant')
        self.assertEqual(variant_found.genomic_source_class['id'], 'LA6684-0')
        self.assertEqual(variant_found.genomic_source_class['label'], 'Somatic')


class GenomicsReportTest(TestCase):
    """ Test module for Genomics Report model """

    def setUp(self):
        self.variant_tested = GeneticVariantTested.objects.create(**VALID_GENETIC_VARIANT_TESTED)
        self.variant_found = GeneticVariantFound.objects.create(**VALID_GENETIC_VARIANT_FOUND)
        self.genomics_report = GenomicsReport.objects.create(**valid_genetic_report())
        self.genomics_report.genetic_variant_tested.set([self.variant_tested])
        self.genomics_report.genetic_variant_found.set([self.variant_found])

    def test_genomics_report(self):
        genomics_report = GenomicsReport.objects.get(id='genomics_report:01')
        self.assertEqual(genomics_report.test_name['id'], 'GTR000567625.2')
        self.assertIsInstance(genomics_report.specimen_type, dict)
        self.assertIsNotNone(genomics_report.genetic_variant_tested)
        self.assertEqual(genomics_report.genetic_variant_tested.count(), 1)
        self.assertEqual(genomics_report.genetic_variant_found.count(), 1)


class LabsVitalTest(TestCase):
    """ Test module for LabsVital model """

    def setUp(self):
        self.individual = Individual.objects.create(**VALID_INDIVIDUAL)
        self.labs_vital = LabsVital.objects.create(**valid_labs_vital(self.individual))

    def test_labs_vital(self):
        labs_vital = LabsVital.objects.get(id='labs_vital:01')
        self.assertEqual(labs_vital.body_height['value'], 1.70)
        self.assertEqual(labs_vital.body_height['unit'], 'm')
        self.assertEqual(labs_vital.body_weight['value'], 60)
        self.assertEqual(labs_vital.blood_pressure_diastolic['value'], 80)
        self.assertEqual(labs_vital.blood_pressure_systolic['value'], 120)
        self.assertIsInstance(labs_vital.tumor_marker_test, dict)
        self.assertIsInstance(labs_vital.tumor_marker_test['code'], dict)
        self.assertEqual(labs_vital.tumor_marker_test['data_value']['value'], 10)

    def test_validation(self):
        invalid_obj = valid_labs_vital(self.individual)
        invalid_obj["id"] = "labs_vital:02"
        invalid_obj["tumor_marker_test"]["code"] = {
            "coding": [
                {
                    "code": "50610-5",
                    "display": "Alpha-1-Fetoprotein",
                    "system": "loinc.org"
                }
            ]
        }
        invalid = LabsVital.objects.create(**invalid_obj)
        with self.assertRaises(serializers.ValidationError):
            invalid.full_clean()


class CancerConditionTest(TestCase):
    """ Test module for CancerCondition model """

    def setUp(self):
        self.cancer_condition = CancerCondition.objects.create(**valid_cancer_condition())

    def test_cancer_condition(self):
        cancer_condition = CancerCondition.objects.get(id='cancer_condition:01')
        self.assertEqual(cancer_condition.condition_type, 'primary')
        self.assertIsInstance(cancer_condition.body_location_code, list)
        self.assertEqual(cancer_condition.body_location_code[0]['id'], '442083009')
        self.assertEqual(cancer_condition.clinical_status['id'], 'active')
        condition_code_keys = [key for key in cancer_condition.condition_code.keys()]
        self.assertEqual(condition_code_keys, ['id', 'label'])
        self.assertEqual(cancer_condition.histology_morphology_behavior['id'], '372147008')


class TNMStagingTest(TestCase):
    """ Test module for TNMstaging model """

    # TODO URI syntax examples for tests https://tools.ietf.org/html/rfc3986

    def setUp(self):
        self.cancer_condition = CancerCondition.objects.create(**valid_cancer_condition())
        self.tnm_staging = TNMStaging.objects.create(**invalid_tnm_staging(self.cancer_condition))

    def test_tnm_staging(self):
        tnm_staging = TNMStaging.objects.get(id='tnm_staging:01')
        self.assertEqual(tnm_staging.tnm_type, 'clinical')
        # this should fails in validation below
        self.assertIsInstance(tnm_staging.stage_group['data_value']['coding'], list)

    def test_validation(self):
        invalid_obj = invalid_tnm_staging(self.cancer_condition)
        invalid_obj["id"] = "tnm_staging:02"
        invalid = TNMStaging.objects.create(**invalid_obj)
        with self.assertRaises(serializers.ValidationError):
            invalid.full_clean()


class CancerRelatedProcedureTest(TestCase):
    """ Test module for CancerRelatedProcedure model """

    def setUp(self):
        self.cancer_related_procedure = CancerRelatedProcedure.objects.create(
            **valid_cancer_related_procedure()
        )

    def test_cancer_related_procedure(self):
        cancer_related_procedure = CancerRelatedProcedure.objects.get(id='cancer_related_procedure:01')
        self.assertEqual(cancer_related_procedure.procedure_type, 'radiation')
        self.assertEqual(cancer_related_procedure.code['id'], '33356009')
        self.assertEqual(cancer_related_procedure.occurence_time_or_period['value']['start'], '2018-11-13T20:20:39+00:00')
        self.assertIsInstance(cancer_related_procedure.target_body_site, list)
        self.assertEqual(cancer_related_procedure.treatment_intent['label'], 'Curative - procedure intent')


class MedicationStatementTest(TestCase):
    """ Test module for MedicationStatement model """

    def setUp(self):
        self.cancer_related_procedure = MedicationStatement.objects.create(
            **valid_medication_statement()
        )

    def test_cancer_related_procedure(self):
        medication_statement = MedicationStatement.objects.get(id='medication_statement:01')
        self.assertEqual(medication_statement.medication_code['id'], '92052')
        self.assertIsInstance(medication_statement.termination_reason, list)
        self.assertEqual(medication_statement.treatment_intent['label'], 'Curative - procedure intent')
        for date in [medication_statement.start_date, medication_statement.end_date, medication_statement.date_time]:
            self.assertIsInstance(date, datetime.datetime)
