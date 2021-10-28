from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    from converter_app.main.routes import main
    from converter_app.converter.routes import conv
    from converter_app.error.error import errors

    app.register_blueprint(main)
    app.register_blueprint(conv)
    app.register_blueprint(errors)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
