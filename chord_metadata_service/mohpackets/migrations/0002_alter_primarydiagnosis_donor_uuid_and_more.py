# Generated by Django 4.2.3 on 2023-10-23 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mohpackets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarydiagnosis',
            name='donor_uuid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mohpackets.donor'),
        ),
        migrations.AlterField(
            model_name='primarydiagnosis',
            name='submitter_donor_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='primarydiagnosis',
            name='submitter_primary_diagnosis_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
