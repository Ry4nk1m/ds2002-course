import requests
import mysql.connector
import datetime
import time

DBHOST = 'ds2002.cgls84scuy1e.us-east-1.rds.amazonaws.com'
DBUSER = 'ds2002'
DBPASS = 'Xf3$fa57CwD!'
DBNAME = 'iss'
MY_ID = 'qec4gc'
MY_NAME = 'Ryan Kim'

def get_db_connection():
    return mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)

def main():
    print("--- STARTING ISS TRACKER ---")
    db = get_db_connection()
    cursor = db.cursor()
    
    # Check/Register
    cursor.execute("SELECT reporter_id FROM reporters WHERE reporter_id = %s", (MY_ID,))
    if cursor.fetchone() is None:
        print(f"Registering reporter: {MY_ID}")
        cursor.execute("INSERT INTO reporters (reporter_id, reporter_name) VALUES (%s, %s)", (MY_ID, MY_NAME))
        db.commit()

    for i in range(10):
        try:
            resp = requests.get("http://api.open-notify.org/iss-now.json", timeout=10).json()
            lat, lon = resp['iss_position']['latitude'], resp['iss_position']['longitude']
            ts = datetime.datetime.fromtimestamp(resp['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
            
            cursor.execute(
                "INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id) VALUES (%s, %s, %s, %s, %s)",
                ('success', lat, lon, ts, MY_ID)
            )
            db.commit()
            print(f"[{i+1}/10] Logged ISS at {lat}, {lon}")
            time.sleep(1)
        except Exception as e:
            print(f"Error on loop {i+1}: {e}")
            time.sleep(2)

    cursor.close()
    db.close()
    print("--- FINISHED ---")

if __name__ == "__main__":
    main()
