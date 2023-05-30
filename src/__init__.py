from flask import Flask
from .database import init_db


def create_app(dbPath="students.db") -> Flask:
    app = Flask(__name__.split('.')[0])

    # importa os blueprints
    from .api.views.students import studentBp

    # registra os blueprints
    app.register_blueprint(studentBp)

    init_db(app, dbPath)

    return app
