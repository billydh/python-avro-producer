from argparse import ArgumentParser


def parse_command_line_args():
    arg_parser = ArgumentParser()

    arg_parser.add_argument("--topic", required=True, help="Topic name")
    arg_parser.add_argument("--bootstrap-servers", required=False, default="localhost:9092", help="Bootstrap server address")
    arg_parser.add_argument("--schema-registry", required=False, default="http://localhost:8081", help="Schema Registry url")
    arg_parser.add_argument("--schema-file", required=False, help="File name of Avro schema to use")
    arg_parser.add_argument("--record-key", required=False, type=str, help="Record key. If not provided, will be a random UUID")
    arg_parser.add_argument("--record-value", required=False, help="Record value")
    arg_parser.add_argument("--security-protocol", required=False, default="plaintext", help="Security Protocol.  Either ssl or plaintext.")
    arg_parser.add_argument("--ssl-ca-location", required=False, help="Location of ca file.  Required if security is ssl.")
    arg_parser.add_argument("--ssl-cert-location", required=False, help="Location of cert file.  Required if security is ssl.")
    arg_parser.add_argument("--ssl-key-location", required=False, help="Location of key file.  Required if security is ssl.")

    return arg_parser.parse_args()
