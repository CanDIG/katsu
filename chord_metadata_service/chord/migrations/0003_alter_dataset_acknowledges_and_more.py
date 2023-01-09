# Generated by Django 4.1.1 on 2022-11-29 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katsu', '0002_auto_20210409_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='acknowledges',
            field=models.JSONField(blank=True, default=list, help_text='The grant(s) which funded the work reported by the dataset.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='alternate_identifiers',
            field=models.JSONField(blank=True, default=list, help_text='Alternate identifiers for the dataset.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='citations',
            field=models.JSONField(blank=True, default=list, help_text='The publication(s) that cite this dataset.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='creators',
            field=models.JSONField(blank=True, default=list, help_text='The person(s) or organization(s) which contributed to the creation of the dataset.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='data_use',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='dates',
            field=models.JSONField(blank=True, default=list, help_text='Relevant dates for the datasets, a date must be added, e.g. creation date or last modification date should be added.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='dimensions',
            field=models.JSONField(blank=True, default=list, help_text='The different dimensions (granular components) making up a dataset.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='distributions',
            field=models.JSONField(blank=True, default=list, help_text='The distribution(s) by which datasets are made available (for example: mySQL dump).'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='extra_properties',
            field=models.JSONField(blank=True, help_text='Extra properties that do not fit in the previous specified attributes.', null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='has_part',
            field=models.ManyToManyField(blank=True, help_text="A Dataset that is a subset of this Dataset; Datasets declaring the 'hasPart' relationship are considered a collection of Datasets, the aggregation criteria could be included in the 'description' field.", to='katsu.dataset'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='keywords',
            field=models.JSONField(blank=True, default=list, help_text='Tags associated with the dataset, which will help in its discovery.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='licenses',
            field=models.JSONField(blank=True, default=list, help_text='The terms of use of the dataset.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='linked_field_sets',
            field=models.JSONField(blank=True, default=list, help_text='Data type fields which are linked together.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='primary_publications',
            field=models.JSONField(blank=True, default=list, help_text='The primary publication(s) associated with the dataset, usually describing how the dataset was produced.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='produced_by',
            field=models.JSONField(blank=True, help_text='A study process which generated a given dataset, if any.', null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='related_identifiers',
            field=models.JSONField(blank=True, default=list, help_text='Related identifiers for the dataset.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='spatial_coverage',
            field=models.JSONField(blank=True, default=list, help_text='The geographical extension and span covered by the dataset and its measured dimensions/variables.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='stored_in',
            field=models.JSONField(blank=True, help_text='The data repository hosting the dataset.', null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='types',
            field=models.JSONField(blank=True, default=list, help_text='A term, ideally from a controlled terminology, identifying the dataset type or nature of the data, placing it in a typology.'),
        ),
    ]
