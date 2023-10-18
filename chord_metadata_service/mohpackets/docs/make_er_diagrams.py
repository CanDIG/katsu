import yaml




def main():
    with open("schema.yml") as f:
        schemas = yaml.load(f, Loader=yaml.FullLoader)

    authorized_keys = {key: value for key, value in schemas['paths'].items() if 'authorized' in key}
    model_dict = {}
    for key, value in authorized_keys.items():
        schema_name = (key.split("/")[3])
        if 'get' in value.keys():
            schema_params = value['get']['parameters']
        else:
            continue
        param_list = []
        for param in schema_params:
            if param['name'] in ['page', 'page_size']:
                continue
            else:
                simple_param = {
                    "name": param['name'],
                    "data_type": param['schema']['type']
                }
                param_list.append(simple_param)
        model_dict[schema_name] = param_list

    with open("full_katsu_er_diagram.md", "w+") as f:
        f.write("```mermaid\nerDiagram\n")
        for schema, params in model_dict.items():
            f.write(f"\t{schema} {{\n")
            for param in params:
                f.write(f"\t\t{param['data_type']} {param['name']}\n")
            f.write("}\n\n")

        # linking entities
        f.write('donors ||--|{ primary_diagnoses : "have"\n')
        f.write('donors ||--o{ comorbidities : "have"\n')
        f.write('donors ||--o{ biomarkers : "have"\n')
        f.write('donors ||--o{ exposures : "have"\n')
        f.write('donors ||--o{ follow_ups : "have"\n')
        f.write('primary_diagnoses ||--|{ specimens : "have"\n')
        f.write('primary_diagnoses ||--|{ treatments : "have"\n')
        f.write('primary_diagnoses ||--|{ treatments : "have"\n')
        f.write('primary_diagnoses ||--o{ follow_ups : "have"\n')
        f.write('specimens ||--|{ sample_registrations : "have"\n')
        f.write('treatments ||--|{ chemotherapies : "have"\n')
        f.write('treatments ||--|{ hormone_therapies : "have"\n')
        f.write('treatments ||--|{ immunotherapies : "have"\n')
        f.write('treatments ||--|{ radiations : "have"\n')
        f.write('treatments ||--|{ surgeries : "have"\n')
        f.write('treatments ||--|{ follow_ups : "have"\n')
        f.write('\n```\n')


if __name__ == '__main__':
    main()


