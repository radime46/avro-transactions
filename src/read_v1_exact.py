import sys
import csv
from fastavro import reader

def main():
    avro_path = "data/transactions_v1.avro"
    fields = ["id", "event_time", "user_email", "amount"]

    out = csv.writer(sys.stdout, lineterminator="\n")
    out.writerow(fields)

    with open(avro_path, "rb") as f:
        for rec in reader(f):
            out.writerow([rec[k] for k in fields])

if __name__ == "__main__":
    main()
