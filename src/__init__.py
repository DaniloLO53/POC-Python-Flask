from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__.split('.')[0])

    # importa os blueprints
    from .api.students import studentBp

    # registra os blueprints
    app.register_blueprint(studentBp)

    return app
