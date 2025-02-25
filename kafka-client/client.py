from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "air-sensor.public.sensor_data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="duckdb-consumer",
    value_deserializer=lambda x: x.decode("utf-8")
)

print("connected to kafka, waiting for messages")
for message in consumer:
    print(f"received: {message.value}")