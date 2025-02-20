from utils.db_conn import db_conn
import random
from faker import Faker

pm_statuses = [
    "good",
    "moderate",
    "unhealthy",
    "hazardous"
]

pm_metrics = {
    "good": random.uniform(0, 12.0),
    "moderate": random.uniform(12.1, 35.4),
    "unhealthy": random.uniform(35.5, 250.4),
    "hazardous": random.uniform(250.5, 999)
}

co2_metrics = {
    "good": random.uniform(0, 449),
    "moderate": random.uniform(450, 999),
    "unhealthy": random.uniform(1000, 4999),
    "hazardous": random.uniform(5000, 9999)
}

def generate_sensor_data():
    sensor_id = random.randint(1, 3)
    status = random.choice(pm_statuses)
    pm2_5 = round(pm_metrics[status], 2)
    co2 = round(co2_metrics[status], 2)
    temperature = round(random.uniform(23, 40), 2)
    humidity = round(random.uniform(60, 100), 2)

    with db_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                    INSERT INTO sensor_data (sensor_id, pm2_5, pm10, co2, temperature, humidity) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, 
                (sensor_id, pm2_5, pm2_5, co2, temperature, humidity),
            )
            conn.commit()
