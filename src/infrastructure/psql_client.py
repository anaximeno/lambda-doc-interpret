import psycopg

from configs.settings import Settings


class PSQLClient:
    _instance = None
    
    def __init__(self):
        self._conn = psycopg.connect(
            dbname=Settings.POSTGRES_DB,
            user=Settings.POSTGRES_USER,
            password=Settings.POSTGRES_PASSWORD,
            host=Settings.POSTGRES_HOST,
            port=Settings.POSTGRES_PORT
        )

    @classmethod
    def get_instance(cls):
        """Ensure singleton."""
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
    
    def exec(self, statement: str, params: dict = None) -> bool:
        try:
            with self._conn.cursor() as cur:
                cur.execute(statement, params=params)
            self._conn.commit()
            return True
        except Exception as e:
            self._conn.cancel()
            print("Couldn't execute statement due to exception:", e)
            return False
    
    def query(self, query: str, params: dict = None) -> list[tuple] | None:
        try:
            with self._conn.cursor() as cur:
                cur.execute(query, params=params)
                results = cur.fetchall()
            return results
        except Exception as e:
            print("Couldn't execute query due to exception:", e)
            return None
