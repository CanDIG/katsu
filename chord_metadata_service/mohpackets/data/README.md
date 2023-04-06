# Synthetic Data for MoH Models

This folder contains the necessary tools to generate synthetic data. Each dataset is organized into the following subfolders:

- `mockaroo_schemas`: contains the blueprints needed to generate data using the Mockaroo service.
- `no_relationships_data`: generated mock data that doesn't include any relationships.
- `synthetic_data`: assigned relationships data, can be used for ingestion.
- `fixtures`: contains Django-formatted data that can be directly loaded into the database (skip ingestion).

## Loading Fixtures

The following commands will:

- Set the path where the fixtures JSON files are located
- Create an array of the fixtures names
- Load each fixture into the database

```bash
fixtures_path="chord_metadata_service/mohpackets/data/small_dataset/fixtures"
fixtures_name=(Program Donor PrimaryDiagnosis Specimen SampleRegistration Treatment Chemotherapy HormoneTherapy Radiation Immunotherapy Surgery FollowUp Biomarker Comorbidity)
for fixture in ${fixtures_name}; do python manage.py loaddata $fixtures_path/$fixture.json; done
```

## Clean up data

To start again, use:

```bash
python manage.py flush
```

## Customize and Generate the Data Yourself

If you want to modify the mock data to your preferences, you can follow these steps:

1. Create a [Mockaroo](https://www.mockaroo.com/) account
2. Load the blueprints from `mockaroo_schemas`
3. Make changes
4. Download the data as a JSON file, and put it in `no_relationships_data`
5. Modify `relationships.json` if needed
6. Run `convert.py` to generate the final data

```python
python chord_metadata_service/mohpackets/data/convert.py
```
