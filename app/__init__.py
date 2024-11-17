from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/art.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Register Blueprints
    from app.controllers.art_controller import art_bp
    app.register_blueprint(art_bp, url_prefix="/api/art")

    # Create tables
    with app.app_context():
        db.create_all()

    # Default route
    @app.route("/")
    def home():
        return "Welcome to ArtSphere Backend!"

    return app
