from utils.db_conn import db_conn

def generate_table():
    with db_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS sensors (
                    id INT GENERATED ALWAYS AS IDENTITY,
                    lat FLOAT,
                    long FLOAT,
                    city TEXT,
                    is_active BOOLEAN,
                    created_at TIMESTAMP DEFAULT NOW(),
                    PRIMARY KEY(id)
                );
                """)
            cur.execute("ALTER TABLE sensors REPLICA IDENTITY FULL")
            cur.execute("""
                CREATE TABLE IF NOT EXISTS sensor_data (
                    id INT GENERATED ALWAYS AS IDENTITY,
                    sensor_id INT,
                    pm2_5 FLOAT,
                    pm10 FLOAT,
                    co2 FLOAT,
                    temperature FLOAT,
                    humidity FLOAT,
                    created_at TIMESTAMP DEFAULT NOW(),
                    PRIMARY KEY(id),
                    CONSTRAINT fk_sensors FOREIGN KEY(sensor_id) REFERENCES sensors(id)
                );
                """)
            cur.execute("ALTER TABLE sensor_data REPLICA IDENTITY FULL")
