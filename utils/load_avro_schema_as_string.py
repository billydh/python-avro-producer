

def load_avro_schema_as_string(schema_file):
    with open("./avro/" +schema_file, 'r') as file:
        data = file.read().replace('\n', '')
    
    return data
