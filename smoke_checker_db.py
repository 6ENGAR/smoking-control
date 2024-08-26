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

current_date = datetime.date.today()

def add_new_user_to_db(message):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE user_tg_id = '%s';", (message.from_user.id,))
            user_exists = cursor.fetchone()

            if user_exists:
                print(f'[x] USER {message.from_user.id} is already in DB. Clicked on /start once again')
            else:
                cursor.execute("INSERT INTO users (user_tg_id, username) VALUES (%s, %s);",
                               (message.from_user.id, message.from_user.username))
                connection.commit()
                print(f'[+] NEW USER | {message.from_user.id} added to the DB at {datetime.datetime.now()}')
    except Exception as e:
        print(f'[x] Error checking or adding user in DB — {e} for {message.from_user.id}')


def create_user_data_row(message):
    try:
        with connection.cursor() as cursor:

            query = "SELECT * FROM user_data WHERE tg_user_id = '%s' AND date = %s;"
            cursor.execute(query, (message.from_user.id, current_date))
            row_exists = cursor.fetchall()

            if not row_exists:
                cursor.execute("INSERT INTO user_data (tg_user_id, date, timer) VALUES (%s, %s, %s);",
                               (message.from_user.id, current_date, 0))
                connection.commit()
                print(f'[+] {current_date} row has been added to db for {message.from_user.id}')
            else:
                print(f'[x] Data for {message.from_user.id} is already in DB. Clicked on /start once again')
    except Exception as e:
        print(f'[x] Error creating user-data row — {e} for {message.from_user.id}')


def set_timer(timer, user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE user_data SET timer = %s WHERE tg_user_id = %s;", (timer, user_id))
            connection.commit()
            print(f'[+] Timer for {user_id} has been set')
    except Exception as e:
        print(f'[x] Error updating timer value — {e}')


def increase_counter(user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE user_data SET counter = counter + 1 WHERE date = %s AND tg_user_id = '%s';",
                           (current_date, user_id))
            connection.commit()
            print(f'[+] Daily cigarettes counter for {user_id} has been updated')
    except Exception as e:
        print(f'[x] Error updating counter — {e}')


def get_timer_value(user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT timer FROM user_data WHERE tg_user_id = %s", (str(user_id),))
            timer = cursor.fetchone()
            return int(timer[0])
    except Exception as e:
        print(f'[x] Error getting timer value counter — {e}')


def get_counter_value(user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT counter FROM user_data WHERE tg_user_id = %s AND date = %s;", (user_id, current_date))
            cigarettes_counter = cursor.fetchone()
            return int(cigarettes_counter[0])
    except Exception as e:
        print(f'[x] Error getting counter value counter — {e}')
