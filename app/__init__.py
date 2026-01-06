from flask import Flask
from flask_cors import CORS
import os
from .models import board
from .db import db, migrate
from .routes.board_routes import bp as boards_bp
from .routes.card_routes import bp as cards_bp


def create_app(config=None):
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/inspiration_board_api_development'

    if config:
        app.config.update(config)
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(boards_bp)
    app.register_blueprint(cards_bp)

   

    return app
