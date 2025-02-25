#!/bin/sh

curl -X POST http://localhost:8083/connectors \
-H "Content-Type: application/json" \
-d '{
    "name": "air-sensor-connector",
    "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.hostname": "postgres",
        "database.port": "5432",
        "database.user": "postgres",
        "database.password": "postgres",
        "database.dbname": "air_sensor_db",
        "topic.prefix": "air-sensor",
        "table.include.list": "public.sensors,public.sensor_data",
        "plugin.name": "pgoutput"
    }
}'
