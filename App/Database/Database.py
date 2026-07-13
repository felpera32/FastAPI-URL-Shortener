import psycopg
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import os

load_dotenv()

dbHost = os.getenv('DB_HOST')
dbName = os.getenv('DB_NAME')
dbUser = os.getenv('DB_USER')
dbPassword = os.getenv('DB_PASSWORD')



conn = psycopg.connect(host=dbHost, dbname=dbName, user=dbUser, password=dbPassword, port=5432)

scheduler =  BackgroundScheduler()

def saveData(code, originalLink, clicks, encurtedLink):
    time = datetime.now()
    expireTime = time + timedelta(days=30)
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO links (code, original_url, clicks, created_at, expires_at, encurted_url)
            VALUES ( %s, %s, %s, %s, %s, %s)
            """,
            (code, originalLink, clicks, time, expireTime, encurtedLink)
        )
    conn.commit()





def getData(code):
    with conn.cursor() as cur: 
        cur.execute("""
            SELECT original_url
            FROM links
            WHERE code = %s;
        """, (code,))
        result = cur.fetchone()
    return result[0] if result else None




def updateClicks(code):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE links
            SET clicks = clicks + 1
            WHERE code = %s;
            """, (code,)
        )
        update = cur.rowcount
    conn.commit()
        

def deleteTime():
    with conn.cursor() as cur:
        cur.execute(
            """
            DELETE FROM links
            WHERE expires_at < NOW();
        """
        )
    conn.commit()

scheduler.add_job(deleteTime, "interval", days=1)
scheduler.start()