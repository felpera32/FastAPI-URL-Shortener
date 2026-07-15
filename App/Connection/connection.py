import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

dbHost = os.getenv('DB_HOST')
dbName = os.getenv('DB_NAME')
dbUser = os.getenv('DB_USER')
dbPassword = os.getenv('DB_PASSWORD')


def getConnection():
    return psycopg.connect(
        host=dbHost,
        dbname=dbName,
        user=dbUser,
        password=dbPassword
    )