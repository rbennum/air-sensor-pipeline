import psycopg

def db_conn():
    return psycopg.connect("host=localhost dbname=air_sensor_db user=postgres password=postgres port=5432")