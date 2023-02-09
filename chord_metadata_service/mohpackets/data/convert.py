import json
import os
from pathlib import Path


def convert_to_fixtures():
    """
    Converts the raw data generated by Mockaroo into Django fixtures
    by wrapping each object with the model name and fields.
    """

    # Path to the synthetic data folder
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    synthetic_folder_path = os.path.join(script_dir, "synthetic_data")
    fixtures_folder_path = os.path.join(script_dir, "fixtures")
    # create fixtures folder if it doesn't exist
    Path(fixtures_folder_path).mkdir(parents=True, exist_ok=True)

    # get all the json names in the directory data
    json_names = []
    for file in os.listdir(synthetic_folder_path):
        if file.endswith(".json"):
            json_names.append(file)

    # open each json file
    for file_name in json_names:
        print(f"Processing {file_name}...")
        obj_name = file_name.split(".")[0].lower()
        dj_fixtures = []
        with open(f"{synthetic_folder_path}/{file_name}") as f:
            data = json.load(f)

            for line in data:
                # create new json object
                dj_fixture = {"model": "mohpackets." + obj_name, "fields": line}
                dj_fixtures.append(dj_fixture)

        # write to new json file
        with open(f"{fixtures_folder_path}/{file_name}", "w") as f:
            json.dump(dj_fixtures, f, indent=4)


def set_foreign_keys():
    # Open the file
    with open(
        "chord_metadata_service/mohpackets/data/relationship_template.json", "r"
    ) as f:
        rules = json.load(f)

    name_dict = {
        # "programs": "Program.json",
        # "donors": "Donor.json",
        "primary_diagnoses": "PrimaryDiagnosis.json",
        # "specimens": "Specimen.json",
        # "sample_registrations": "SampleRegistration.json",
        # "treatments": "Treatment.json",
        # "chemotherapies": "Chemotherapy.json",
        # "hormone_therapies": "HormoneTherapy.json",
        # "radiations": "Radiation.json",
        # "immunotherapies": "Immunotherapy.json",
        # "surgeries": "Surgery.json",
        # "follow_ups": "FollowUp.json",
        # "biomarkers": "Biomarker.json",
        # "comorbidities": "Comorbidity.json",
    }

    # Load the JSON data from the ordered_name_dict
    for model_name, file_name in name_dict.items():
        with open(
            f"chord_metadata_service/mohpackets/data/template_data/{file_name}", "r"
        ) as f:
            data = json.load(f)
        # rule = rules.get(model_name)
        rule = rules.get("primary_diagnoses")

        replace_values(data, rule)


def replace_values(data, rule):
    # loop through rule
    for item in rule:
        item_start_range, item_end_range = item["range"]
        item_range = item_end_range - item_start_range + 1
        for target in item["targets"]:
            field_name = target["field_name"]
            field_value = target["field_value"]
            target_start_range, target_end_range = target["range"]
            for i in range(item_range):
                item_index = item_start_range + i - 1
                target_index = target_start_range + i
                if target_index > target_end_range:
                    target_index = target_start_range + (i % target_end_range)
                data[item_index][field_name] = field_value + str(target_index)

    # write to new json file
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def main():
    print("Select an option:")
    print("1. Set Foreign Keys")
    print("2. Convert to Django fixtures")
    print("3. Exit")

    choice = int(input("Enter your choice [1-3]: "))

    if choice == 1:
        set_foreign_keys()
    elif choice == 2:
        convert_to_fixtures()
    elif choice == 3:
        exit()
    else:
        print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
