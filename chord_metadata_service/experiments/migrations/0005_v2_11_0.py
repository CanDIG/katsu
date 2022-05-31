# Generated by Django 2.2.28 on 2022-05-31 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_v2_9_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentresult',
            name='data_output_type',
            field=models.CharField(blank=True, help_text='The type of data output: Raw or Derived data.Raw data - the data output type that can be converted back to the original result set. Derived data - the data output type that cannot be converted back to the original result set.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experimentresult',
            name='file_format',
            field=models.CharField(blank=True, help_text='(Controlled Vocabulary) File format.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='experimentresult',
            name='genome_assembly_id',
            field=models.CharField(blank=True, help_text='Reference genome assembly ID.', max_length=50, null=True),
        ),
    ]
