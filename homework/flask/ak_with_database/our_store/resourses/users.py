from flask_restful import Resource, marshal_with
from flask import g
from our_store.db import get_db


class Users(Resource):
    def get(self, user_id):
        get_db()
        return g.db_adapter.users.get(user_id)
