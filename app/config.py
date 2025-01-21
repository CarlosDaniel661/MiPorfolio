import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')  # Cambia 'default-secret-key' por algo seguro
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
