from flask import Flask
from flask_migrate import Migrate

from pet_hotel.models import db
from pet_hotel.config import Config
from pet_hotel.routes import check_in_bp, check_out_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(check_in_bp)
    app.register_blueprint(check_out_bp)
    return app
