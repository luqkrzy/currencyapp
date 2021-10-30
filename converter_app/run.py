from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import Config

db = SQLAlchemy()

def create_app(config_class=Config) -> Flask:
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


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
