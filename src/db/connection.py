import os, psycopg2

class PostgresConnection:
    def __init__(self):
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.database = os.getenv("POSTGRES_DB")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.port = os.getenv("POSTGRES_PORT", "5432")
        self.conn = None
    
    def __enter__(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port
        )
        return self.conn
    
    def __exit__(self , exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is not None:
                print("Rollback para evitar errores")
                self.conn.rollback()
            else:
                self.conn.commit()
            self.conn.close()