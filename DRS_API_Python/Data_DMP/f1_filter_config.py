from pymongo import MongoClient
from datetime import datetime

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")  # Adjust if needed
db = client["DRS_Database"]  # Replace with your database name
collection = db["F1_filter_config"]  # Replace with your collection name

# Data to Insert
filters = [
    {
        "filter_id": 1,
        "filter_rule": "BSS Credit Class",
        "operator": "equal",
        "rule_values": [{"value": 3}, {"value": 7}, {"value": 10}, {"value": 43}],
        "create_dtm": datetime.strptime("2025-02-18T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        "end_dtm": ""
    },
    {
        "filter_id": 2,
        "filter_rule": "Arrears level",
        "operator": "less than",
        "rule_values": [{"value": "threshold limit"}],  # Corrected syntax issue
        "create_dtm": datetime.strptime("2025-02-18T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        "end_dtm": ""
    },
    {
        "filter_id": 3,
        "filter_rule": "Customer Type Name",
        "operator": "equal",
        "rule_values": [{"value": "SLT"}],  # Corrected missing quotes
        "create_dtm": datetime.strptime("2025-02-18T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        "end_dtm": ""
    },
    {
        "filter_id": 4,
        "filter_rule": "Main Product Status",
        "operator": "equal",
        "rule_values": [{"value": "Active"}],  # Corrected missing quotes
        "create_dtm": datetime.strptime("2025-02-18T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        "end_dtm": ""
    },
    {
        "filter_id": 5,
        "filter_rule": "Customer Segment",
        "operator": "equal",
        "rule_values": [{"value": 2}, {"value": 4}, {"value": 6}, {"value": 7}],
        "create_dtm": datetime.strptime("2025-02-18T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        "end_dtm": ""
    },
    {
        "filter_id": 6,
        "filter_rule": "Product Status",
        "operator": "equal",
        "rule_values": [{"value": "TA.SU"}],  # Corrected missing quotes
        "create_dtm": datetime.strptime("2025-02-18T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        "end_dtm": ""
    },
    {
        "filter_id": 7,
        "filter_rule": "Specific Customer Name",
        "operator": "like",
        "rule_values": [
            {"value": "Banks"}, {"value": "Brandix"}, {"value": "MAS"},
            {"value": "Mobitel"}, {"value": "Hutch"}, {"value": "Etisalat"},
            {"value": "Airtel"}, {"value": "Lanka Bell"}, {"value": "Dialog"},
            {"value": "Suntel"}
        ],
        "create_dtm": datetime.strptime("2025-02-18T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        "end_dtm": ""
    }
]

# Insert data into MongoDB
result = collection.insert_many(filters)
print(f"Inserted IDs: {result.inserted_ids}")
