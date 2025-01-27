import psycopg
from setting import DB_SETTINGS

# due to this project is a simple project, we don't need to use ORM
# and there is no need to use connection pool

def connect():
    return psycopg.connect(
        host=DB_SETTINGS['host'],
        user=DB_SETTINGS['user'],
        password=DB_SETTINGS['password'],
        db=DB_SETTINGS['db']
    )

