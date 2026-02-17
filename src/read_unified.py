import sys
import csv
import os

sys.path.append(os.path.dirname(__file__))

from schemas import UNIFIED_READER_SCHEMA
from fastavro import reader, parse_schema

schema = parse_schema(UNIFIED_READER_SCHEMA)

avro_path = sys.argv[1]

fields = ["id", "event_time", "total_amount", "user_email", "currency"]

out = csv.writer(sys.stdout)
out.writerow(fields)

with open(avro_path, "rb") as f:
    for rec in reader(f, reader_schema=schema):
        out.writerow([rec[field] for field in fields])
