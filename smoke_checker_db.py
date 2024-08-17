import psycopg2
from config import DB_PASSWORD

connection = psycopg2.connect(
    database="smoke_control",
    user="postgres",
    password=f"{DB_PASSWORD}",
    host="127.0.0.1",
    port="5432"
)

cursor = connection.cursor()
