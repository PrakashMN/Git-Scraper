from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .config import Config
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)

    from .routes import bp
    app.register_blueprint(bp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app