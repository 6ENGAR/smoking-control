import psycopg2
import datetime
from config import DB_PASSWORD

connection = psycopg2.connect(
    database="smoke_control",
    user="postgres",
    password=f"{DB_PASSWORD}",
    host="127.0.0.1",
    port="5432"
)


# once new user launch the bot his username and userid will be saved to db
def add_new_user_to_db(message):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users WHERE user_tg_id='{message.from_user.id}';")
            user_exists = cursor.fetchone()

            if user_exists:
                print(f'[x] USER {message.from_user.id} is already in DB. Clicked on /start once again')

            else:
                cursor.execute(f"INSERT INTO users (user_tg_id, username) VALUES ({message.from_user.id}, "
                               f"'{message.from_user.username}');")
                connection.commit()
                print(f'[+] NEW USER | {message.from_user.id} added to the DB at {datetime.datetime.now()}')
    except Exception as e:
        print(f'[x] Error checking or adding user in DB — {e} for {message.from_user.id}')

