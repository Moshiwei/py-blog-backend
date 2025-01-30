import psycopg
from psycopg.rows import dict_row
from setting import DB_SETTINGS
from typing import List, Dict, Optional, Any


class Database:
    def __init__(self, settings):
        self.settings = settings
    
    def _execute(self, sql: str, params: Optional[tuple] = None, fetch: bool = False) -> Optional[List[Dict[str, Any]]]:
        try:
            with psycopg.connect(
                host=self.settings['host'],
                user=self.settings['user'],
                dbname=self.settings['dbname'],
                row_factory=dict_row
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, params)
                    if fetch:
                        return cur.fetchall()
                    conn.commit()
        except Exception as e:
            print(f"Database error: {e}")
            raise 
    
    def query(self, sql:str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
        return self._execute(sql, params, fetch=True)
    
    # execute add update delete
    def execute(self, sql: str, params: Optional[tuple] = None) -> None:
        self._execute(sql, params, fetch=False)
    
    def query_one(self, sql: str, params: Optional[tuple] = None) -> Optional[Dict[str, Any]]:
        result = self._execute(sql, params, fetch=True)
        return result[0] if result else None

db = Database(settings=DB_SETTINGS)

