from flask import request
from flask_restful import Resource

from pet_hotel.managers import HotelStayManager

manager = HotelStayManager()


class CheckIn(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        manager.check_in(data)
        return 'success'


class CheckOut(Resource):
    @staticmethod
    def post(pet_id):
        days = manager.check_out(pet_id=pet_id)
        response = {
            "totally days in hotel": days
        }
        return response


class Rooms(Resource):
    @staticmethod
    def get():
        free_rooms = manager.get_all_free_rooms()
        response = {
            "free_rooms": free_rooms
        }
        return response


class Activity(Resource):
    @staticmethod
    def get(pet_id):
        activities = manager.get_activities(pet_id=pet_id)
        if not activities:
            return "no activities for today"
        return {"activities": activities}
