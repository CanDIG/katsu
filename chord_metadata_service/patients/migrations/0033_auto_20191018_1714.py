# Generated by Django 2.2.6 on 2019-10-18 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0032_phenopacket_diseases'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biosample',
            old_name='historical_diagnosis',
            new_name='histological_diagnosis',
        ),
    ]
