from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    from converter_app.main.routes import main
    from converter_app.converter.routes import conv
    from converter_app.errors.error import errors
    app.register_blueprint(main)
    app.register_blueprint(conv)
    app.register_blueprint(errors)
    return app
