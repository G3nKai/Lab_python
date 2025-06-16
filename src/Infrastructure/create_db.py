import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='QWERTY12345',
    host='localhost',
    port='5432'
)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

db_name = 'python_lab'

cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
exists = cursor.fetchone()
if not exists:
    cursor.execute(f"CREATE DATABASE {db_name}")
    print(f"Database '{db_name}' created")
else:
    print(f"Database '{db_name}' already exists")

cursor.close()
conn.close()