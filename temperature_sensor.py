import requests
import json
import random  # Import the random module

TOPIC_NAME = "temperature_sensor"
REGISTERED_SCHEMA_ID = 1
url = f"http://154.56.57.22:8082/topics/{TOPIC_NAME}"

def send_sensor_data(schema_id, data):
    headers = {
        "Content-Type": "application/vnd.kafka.avro.v2+json",
        "Accept": "application/vnd.kafka.v2+json"
    }

    # Generate random temperature data
    data["temperature_celsius"] = round(random.uniform(20, 30), 2)
    data["temperature_fahrenheit"] = round((data["temperature_celsius"] * 9/5) + 32, 2)

    payload = {
        "value_schema_id": schema_id,
        "records": [{"value": data}]
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Successfully sent temperature sensor data to the REST Proxy.")
    else:
        print(f"Failed to send temperature sensor data. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    temperature_data = {
        "sensor_id": "TS001",
        "sensor_type": "Temperature",
        "factory_number": "FCTRY-123",
        "timestamp": "2023-07-24T12:30:00Z",
        "temperature_celsius": 25.5,
        "temperature_fahrenheit": 77.9
    }

    for _ in range(1000):
        print("Sending data")
        send_sensor_data(REGISTERED_SCHEMA_ID, temperature_data)

