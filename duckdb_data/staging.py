from kafka import KafkaConsumer
import duckdb
import json
import time

conn = duckdb.connect("/data/air_quality.duckdb")

conn.execute("CREATE SCHEMA IF NOT EXISTS staging;")
conn.execute("USE staging;")
conn.execute("""
    CREATE TABLE IF NOT EXISTS sensors (
        id BIGINT,
        lat FLOAT,
        long FLOAT,
        city TEXT,
        is_active BOOLEAN,
        created_at BIGINT,
        ingestion_timestamp BIGINT
    );
""")
conn.execute("""
    CREATE TABLE IF NOT EXISTS sensor_data (
        id BIGINT,
        sensor_id INT,
        pm2_5 FLOAT,
        pm10 FLOAT,
        co2 FLOAT,
        temperature FLOAT,
        humidity FLOAT,
        created_at BIGINT,
        ingestion_timestamp BIGINT
    );
""")

print("Running kafka consumer...")
consumer = KafkaConsumer(
    *["air-sensor.public.sensor_data", "air-sensor.public.sensors"],
    bootstrap_servers="kafka:29092", 
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="duckdb-consumer",
    value_deserializer=lambda x: x.decode("utf-8")
)
for message in consumer:
    src = json.loads(message.value)
    payload = src["payload"]
    data = payload["after"]
    source = payload["source"]
    if source["table"] == 'sensor_data':
        print(f"Consuming: sensor_data, id:{data['id']}")
        conn.execute(f"""
            INSERT INTO sensor_data
            VALUES (
                {data['id']},
                {data['sensor_id']},
                {data['pm2_5']},
                {data['pm10']},
                {data['co2']},
                {data['temperature']},
                {data['humidity']},
                {data['created_at']},
                {int(time.time())},
            )
        """)
    else:
        print(f"Consuming: sensors, id:{data['id']}")
        conn.execute(f"""
            INSERT INTO sensors
            VALUES (
                {data['id']},
                {data['lat']},
                {data['long']},
                {data['city']},
                {data['is_active']},
                {data['created_at']},
                {int(time.time())},
            )
        """)

conn.close()