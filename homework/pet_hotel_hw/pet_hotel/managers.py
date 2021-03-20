import datetime
from random import randint

from pet_hotel.err import NoSuchId
from pet_hotel.models import db
from pet_hotel.models import Owner, Pet, Activity


class DbManager:
    def check_in(self, data: dict):
        name = data.get("name")
        phone = data.get("phone")
        owner = Owner(
            name=name,
            phone=phone
        )
        db.session.add(owner)
        db.session.commit()

        nickname = data.get("nickname")
        room_number = self.get_room()
        date = data.get("check_in_date") if data.get("check_in_date") \
            else datetime.date.today()
        pet = Pet(
            nickname=nickname,
            owner_id=owner.id,
            room_number=room_number,
            check_in_date=date
        )
        db.session.add(pet)
        db.session.commit()

        activities = data.get("activity")
        activity_types = activities.keys()
        for activity_type in activity_types:
            time_values = activities.get(activity_type)
            for time_value in time_values:
                activity = Activity(
                    pet_id=pet.id,
                    activity_type=activity_type,
                    time=time_value
                    )
                db.session.add(activity)
        db.session.commit()

    def check_out(self, pet_id: int) -> int:
        pet = Pet.query.get(pet_id)
        if not pet:
            raise NoSuchId(pet_id)
        else:
            owner_id = pet.owner_id
            check_in_date = pet.check_in_date
            activities = Activity.query.filter_by(pet_id=pet_id)

            for activity in activities:
                db.session.delete(activity)
            db.session.delete(pet)
            if not self.is_another_owners_pets_in_hotel(owner_id):
                owner = Owner.query.get(owner_id)
                db.session.delete(owner)

            db.session.commit()
            return self.get_total_days(check_in_date)

    @staticmethod
    def get_activities(pet_id: int):
        pet = Pet.query.get(pet_id)
        if not pet:
            raise NoSuchId(pet_id)
        else:
            raw_activities = Activity.query.filter_by(pet_id=pet_id)
            activities = []
            for activity in raw_activities:
                activities.append(
                    {
                        "activity_type": activity.activity_type,
                        "time": str(activity.time)
                    }
                )
            return activities

    @staticmethod
    def is_another_owners_pets_in_hotel(owner_id: int):
        pets = Pet.query.filter_by(owner_id=owner_id).all()
        if pets:
            return True
        return False

    def get_room(self):
        rooms = self.get_all_free_rooms()
        return rooms[0] if rooms[0] else randint(1, 21)

    @staticmethod
    def get_all_free_rooms():
        available_rooms = [r for r in range(1, 21)]
        occupied_rooms = list(Pet.query.with_entities(Pet.room_number))
        for room in occupied_rooms:
            if room[0] in available_rooms:
                available_rooms.remove(room[0])
        return available_rooms

    @staticmethod
    def get_total_days(check_in_date):
        return (datetime.date.today() - check_in_date).days
