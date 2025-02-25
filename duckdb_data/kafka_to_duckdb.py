from kafka import KafkaConsumer

print("Running kafka listener script...")

consumer = KafkaConsumer(
    "air-sensor.public.sensor_data",
    bootstrap_servers="kafka:29092", 
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="duckdb-consumer",
    value_deserializer=lambda x: x.decode("utf-8")
)

print("Connected to Kafka, waiting for messages...")
for message in consumer:
    print(f"Received: {message.value}")
