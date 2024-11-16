from flask import Flask
from app.controllers.art_controller import art_bp
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(art_bp, url_prefix="/api/art")

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/art.db"
    db.init_app(app)

    # Default route
    @app.route("/")
    def home():
        return "Welcome to ArtSphere Backend!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
