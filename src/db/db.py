import os
import pymysql
import dotenv

dotenv.load_dotenv()

HOST = os.environ.get("MYSQL_HOST")
PORT = os.environ.get("MYSQL_PORT")
SQL_USER = os.environ.get("MYSQL_USER")
SQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB = os.environ.get("MYSQL_DB")


def connection():
    return pymysql.connect(
        host=HOST,
        user=SQL_USER,
        password=SQL_PASSWORD,
        database=DB,
        cursorclass=pymysql.cursors.DictCursor,
    )


def query(conn, sql):
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


def fetch(conn, sql, values):
    with conn.cursor() as cursor:
        cursor.execute(sql, values)
        result = cursor.fetchall()
        return result


def update(conn, sql, values, should_commit=True):
    with conn.cursor() as cursor:
        cursor.execute(sql, values)
        if should_commit:
            conn.commit()


def load_subreddits(conn):
    select_all_subreddits = "SELECT * FROM subreddit"
    subreddits = query(conn, select_all_subreddits)
    return subreddits
