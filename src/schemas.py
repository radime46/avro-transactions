# src/schemas.py

V1_SCHEMA = {
    "type": "record",
    "name": "TransactionV1",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "event_time", "type": "string"},
        {"name": "user_email", "type": "string"},
        {"name": "amount", "type": "string"},
    ],
}
V2_SCHEMA = {
    "type": "record",
    "name": "TransactionV1",   
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "event_time", "type": "string"},
        {"name": "total_amount", "type": "string", "aliases": ["amount"]},
        {"name": "currency", "type": "string"},
    ],
}



UNIFIED_READER_SCHEMA = {
    "type": "record",
    "name": "TransactionV1",   
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "event_time", "type": "string"},
        {"name": "total_amount", "type": "string", "aliases": ["amount"]},
        {"name": "user_email", "type": "string", "default": ""},
        {"name": "currency", "type": "string", "default": ""},
    ],
}

