from flask import request
from flask_restful import Resource

from pet_hotel.managers import DbManager

db_manager = DbManager()


class CheckIn(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        db_manager.check_in(data)
        return 'success'


class CheckOut(Resource):
    @staticmethod
    def post(pet_id):
        days = db_manager.check_out(pet_id=pet_id)
        response = {
            "totally days in hotel": days
        }
        return response


class Rooms(Resource):
    @staticmethod
    def get():
        free_rooms = db_manager.get_all_free_rooms()
        response = {
            "free_rooms": free_rooms
        }
        return response


class Activity(Resource):
    @staticmethod
    def get(pet_id):
        activities = db_manager.get_activities(pet_id=pet_id)
        if not activities:
            return "no activities for today"
        return {"activities": activities}
