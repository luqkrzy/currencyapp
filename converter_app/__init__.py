from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import Config, DevelopmentConfig

db = SQLAlchemy()


def create_app(config_class=DevelopmentConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)
    from converter_app.main.routes import main
    from converter_app.converter.routes import conv
    from converter_app.error.error import errors

    app.register_blueprint(main)
    app.register_blueprint(conv)
    app.register_blueprint(errors)
    db.init_app(app)
    return app
