from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    from converter_app.main.routes import main
    app.register_blueprint(main)
    return app
