# Generated by Django 2.2.17 on 2021-03-16 16:40

import katsu_service.restapi.validators
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_v1_0_0'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiment',
            old_name='other_fields',
            new_name='extra_properties',
        ),
        migrations.AlterField(
            model_name='experiment',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Extra properties that are not supported by current schema.', validators=[katsu_service.restapi.validators.JsonSchemaValidator({'$id': 'katsu_service:key_value_object_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'The schema represents a key-value object.', 'patternProperties': {'^.*$': {'type': 'string'}}, 'title': 'Key-value object', 'type': 'object'}, formats=None)]),
        ),
        migrations.AddField(
            model_name='experiment',
            name='extraction_protocol',
            field=models.CharField(blank=True, help_text='The protocol used to isolate the extract material.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='file_location',
            field=models.CharField(blank=True, help_text='The location of the file that contains the analysis of sequencing data.', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='experiment_type',
            field=models.CharField(help_text="(Controlled Vocabulary) The assay target (e.g. ‘DNA Methylation’, ‘mRNA-Seq’, ‘smRNA-Seq’, 'Histone H3K4me1').", max_length=200),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='library_strategy',
            field=models.CharField(blank=True, help_text='(Controlled Vocabulary) The assay used. These are defined within the SRA metadata specifications with a controlled vocabulary (e.g. ‘Bisulfite-Seq’, ‘RNA-Seq’, ‘ChIP-Seq’). For a complete list, see https://www.ebi.ac.uk/ena/submit/reads-library-strategy.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='molecule',
            field=models.CharField(blank=True, help_text='(Controlled Vocabulary) The type of molecule that was extracted from the biological material.Include one of the following: total RNA, polyA RNA, cytoplasmic RNA, nuclear RNA, small RNA, genomic DNA, protein, or other.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='qc_flags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(help_text='Any quality control observations can be noted here. This field can be omitted if empty', max_length=200), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='reference_registry_id',
            field=models.CharField(blank=True, help_text='The IHEC EpiRR ID for this dataset, only for IHEC Reference Epigenome datasets. Otherwise leave empty.', max_length=200, null=True),
        ),
    ]
