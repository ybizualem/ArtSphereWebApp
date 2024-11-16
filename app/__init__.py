from flask import Flask
from app.controllers.art_controller import art_bp

def create_app():
    app = Flask(__name__)

    # Registering Blueprints for routes
    app.register_blueprint(art_bp)



    return app

print('hello world')