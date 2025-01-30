import psycopg
from setting import DB_SETTINGS

INIT_TABLES_SQL = """
CREATE TABLE IF NOT EXISTS blogs (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
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
        dbname=DB_SETTINGS['dbname']
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(INIT_TABLES_SQL)
            conn.commit()


if __name__ == '__main__':
    init_db()
    print("Database initialized")