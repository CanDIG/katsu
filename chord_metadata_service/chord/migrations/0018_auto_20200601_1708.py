# Generated by Django 2.2.12 on 2020-06-01 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chord', '0017_dataset_additional_resources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tableownership',
            name='data_type',
        ),
        migrations.RemoveField(
            model_name='tableownership',
            name='sample',
        ),
    ]