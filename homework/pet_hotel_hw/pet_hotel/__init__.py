from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from pet_hotel.err import NoSuchId
from pet_hotel.models import db
from pet_hotel.config import Config
from pet_hotel.middleware import OurMiddleware
from pet_hotel.resources import CheckIn, CheckOut, Rooms, Activity


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.wsgi_app = OurMiddleware(app.wsgi_app)

    api = Api(app=app)
    db.init_app(app)
    migrate = Migrate(app, db)

    api.add_resource(CheckIn, "/check-in")
    api.add_resource(CheckOut, "/check-out/<int:pet_id>")
    api.add_resource(Rooms, "/rooms")
    api.add_resource(Activity, "/activity/<int:pet_id>")

    @app.errorhandler(NoSuchId)
    def no_such_user_error_handler(error):
        return {"Error": str(error)}, 404

    return app
