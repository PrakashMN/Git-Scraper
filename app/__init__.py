from flask import Flask
from flask_cors import CORS
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # CORS for future SPA integrations or if calling from different origin
    CORS(app)  # default allows all origins; tighten in production

    from .routes import bp
    app.register_blueprint(bp)

    return app