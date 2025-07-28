from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'sua_chave_secreta'
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'pdf'}
    app.config['UPLOAD_FOLDER'] = 'uploads'

    app.register_blueprint(main)

    return app
