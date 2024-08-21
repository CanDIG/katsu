# Synthetic Data for MoH Models

Synthetic data is generated based on the factory boy factories in [`../tests/factories.py`](../tests/factories.py)


This folder contains the necessary tools to generate synthetic data. Each dataset is organized into the following subfolders:

- `synthetic_data`: assigned relationships data, can be used for ingest APIs.

## To load data

```python
python chord_metadata_service/mohpackets/data/data_loader.py
```

## To clean up data

```python
python manage.py flush
```

## Customize and Generate the Data Yourself

You should not need to run this script unless you want to modify the synthetic data to your preferences. If you do, you would need to edit the factories in [`../tests/factories.py`](../tests/factories.py)

Then run the [`data_factory.py`](data_factory.py) with the parameters of the size of dataset you would like to generate.

Using the `s/m/l` options will overwrite the data contained in the `small_dataset`/`medium_dataset`/`large_dataset` folders.

> [!CAUTION]
> Running this script will load test data into your running katsu database. It is not recommended to run this in a production environment. To experiment with creating synthetic data, please use a local environment.

```python
# To specify a size, use: --size {xs, s, m, l} (default: xs)
python chord_metadata_service/mohpackets/data/data_factory.py
```

`data_factory.py` can also be run with the options `--num-programs` and `--total-donors` to specify a custom dataset. In this case, the number of donors given by `--total-donors` will be distributed amongst the number of programs given by `--num-programs`. Other objects are created in proportion to the number of total donors. The below example will generate 8 programs with 100 donors in each program and will output to a folder called `custom_8P_800D_dataset`.

```python
python chord_metadata_service/mohpackets/data/data_factory.py --num-programs 8 --total-donors 800
```

*NOTE*: The synthetic data provided here is intended for frontend testing, and the logic is not strictly enforced. We do our best to make the date meet logical requirements but it is possible there are still errors in logic. For other types of testing purposes, it is recommended to create your own data to ensure accuracy.
