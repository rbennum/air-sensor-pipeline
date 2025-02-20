from utils.db_conn import db_conn

def generate_sensors():
    with db_conn() as conn:
        with conn.cursor() as cur:
            # check if the main sensors already exist
            cur.execute("SELECT * FROM sensors")
            if len(cur.fetchall()) > 0:
                conn.commit()
                return
            cur.execute(
                """
                    INSERT INTO sensors (lat, long, city, is_active) 
                    VALUES (%s, %s, %s, %s)
                """, 
                (-6.194917, 106.823007, "Jakarta", True),
            )
            cur.execute(
                """
                    INSERT INTO sensors (lat, long, city, is_active) 
                    VALUES (%s, %s, %s, %s)
                """, 
                (-6.917218, 107.618124, "Bandung", True),
            )
            cur.execute(
                """
                    INSERT INTO sensors (lat, long, city, is_active) 
                    VALUES (%s, %s, %s, %s)
                """, 
                (-7.257943, 112.751492, "Surabaya", True),
            )
            conn.commit()

