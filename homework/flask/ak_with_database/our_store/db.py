import psycopg2
from our_store.models import User
from flask import g, current_app


def get_db():
    config = current_app.config
    if "db_adapter" not in g:
        conn = psycopg2.connect(
            user=config["DB_USER"],
            port=config["DB_PORT"],
            host=config["DB_HOST"],
            password=config["DB_PASS"]
        )
        db_adapter = DatabaseAdapter(connection=conn)
        g.db_adapter = db_adapter
    return g.db_adapter


class UserAdapter:
    def __init__(self, adapter):
        self.adapter = adapter

    def get(self, _id: int):
        self.adapter.cursor.execute("SELECT id, name, email from users where %s", (_id,))
        return User(*self.cursor.fetch_one())


class DatabaseAdapter:
    def __init__(self, connection):
        self.con = connection
        self.cursor = self.con.cursor()
        self.users = UserAdapter(self)
