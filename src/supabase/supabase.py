import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")


class SupabaseConnector:
    def __init__(self, url: str = SUPABASE_URL, key: str = SUPABASE_KEY):
        if not url or not key:
            raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set")
        self.client: Client = create_client(url, key)

    def select(self, table: str, columns: str = "*", filters: dict = None, limit: int = None):
        query = self.client.table(table).select(columns)
        if filters:
            for col, val in filters.items():
                query = query.eq(col, val)
        if limit:
            query = query.limit(limit)
        return query.execute().data

    def insert(self, table: str, data: dict | list[dict]):
        return self.client.table(table).insert(data).execute().data

    def update(self, table: str, data: dict, filters: dict):
        query = self.client.table(table).update(data)
        for col, val in filters.items():
            query = query.eq(col, val)
        return query.execute().data

    def delete(self, table: str, filters: dict):
        query = self.client.table(table).delete()
        for col, val in filters.items():
            query = query.eq(col, val)
        return query.execute().data

    def sign_up(self, email: str, password: str):
        return self.client.auth.sign_up({"email": email, "password": password})

    def sign_in(self, email: str, password: str):
        return self.client.auth.sign_in_with_password({"email": email, "password": password})



if __name__ == "__main__":
    db = SupabaseConnector()
    rows = db.select("users", filters={"active": True}, limit=10)
    print(rows)