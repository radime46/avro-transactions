import csv
import sys
import os

sys.path.append(os.path.dirname(__file__))

from schemas import V2_SCHEMA
from fastavro import writer, parse_schema

csv_path = "data/transactions_v2.csv"
avro_path = "data/transactions_v2.avro"

schema = parse_schema(V2_SCHEMA)

with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    records = list(reader)

with open(avro_path, "wb") as out:
    writer(out, schema, records)

print("transactions_v2.avro created")
