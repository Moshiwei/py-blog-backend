import psycopg
from setting import DB_SETTINGS

# due to this project is a simple project, we don't need to use ORM
# and there is no need to use connection pool

def execute_sql(sql, *params):
    try:
        with psycopg.connect(
            host=DB_SETTINGS['host'],
            user=DB_SETTINGS['user'],
            dbname=DB_SETTINGS['dbname']
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                conn.commit()
                result = cur.fetchall()
                return result
    except Exception as e:
        print(e)
        return None
                


