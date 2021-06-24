#!/usr/bin/env python

import json
import uuid

from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import  AvroSerializer

from utils.load_avro_schema_from_file import load_avro_schema_from_file
from utils.load_avro_schema_as_string import load_avro_schema_as_string
from utils.parse_command_line_args import parse_command_line_args


def send_record(args):
    if args.record_value is None:
        raise AttributeError("--record-value is not provided.")

    if args.schema_file is None:
        raise AttributeError("--schema-file is not provided.")

    # key_schema, value_schema = load_avro_schema_from_file(args.schema_file)
    # producer_config = {
    #     "bootstrap.servers": args.bootstrap_servers,
    #     "schema.registry.url": args.schema_registry
    # }

    value_schema_str = load_avro_schema_as_string(args.schema_file)


    schema_registry_conf = {'url': args.schema_registry}
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    avro_serializer = AvroSerializer(schema_str=value_schema_str,
                                    schema_registry_client=schema_registry_client)

    producer_conf = {'bootstrap.servers': args.bootstrap_servers,
                     'key.serializer': StringSerializer('utf_8'),
                     'value.serializer': avro_serializer}

    producer = SerializingProducer(producer_conf)
    

    # producer = SerializingProducer(producer_config, default_key_schema=key_schema, default_value_schema=value_schema)

    key = args.record_key if args.record_key else str(uuid.uuid4())
    value = json.loads(args.record_value)

    try:
        producer.produce(topic=args.topic, key=key, value=value)
    except Exception as e:
        print(f"Exception while producing record value - {value} to topic - {args.topic}: {e}")
    else:
        print(f"Successfully producing record value - {value} to topic - {args.topic}")

    producer.flush()


if __name__ == "__main__":
    send_record(parse_command_line_args())
