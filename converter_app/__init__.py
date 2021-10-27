from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    from converter_app.main.routes import main
    from converter_app.converter.routes import conv
    app.register_blueprint(main)
    app.register_blueprint(conv)
    return app
