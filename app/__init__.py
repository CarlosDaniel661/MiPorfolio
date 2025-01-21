from flask import Flask
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object('config.Config')

    from .routes import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
