import psycopg
from setting import DB_SETTINGS

INIT_TABLES_SQL = """
CREATE TABLE IF NOT EXISTS blogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def init_db():
    with psycopg.connect(
        host=DB_SETTINGS['host'],
        user=DB_SETTINGS['user'],
        password=DB_SETTINGS['password'],
        db=DB_SETTINGS['db']
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(INIT_TABLES_SQL)
            conn.commit()
