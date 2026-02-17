import csv
import sys
import os

# Make Python look inside src folder
sys.path.append(os.path.dirname(__file__))

from schemas import V1_SCHEMA
from fastavro import writer, parse_schema

csv_path = "data/transactions_v1.csv"
avro_path = "data/transactions_v1.avro"

schema = parse_schema(V1_SCHEMA)

with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    records = list(reader)

with open(avro_path, "wb") as out:
    writer(out, schema, records)

print("transactions_v1.avro created")
