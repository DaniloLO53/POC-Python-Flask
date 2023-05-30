from flask import Flask
from .database import init_db
from .api.views.students import studentBp


def create_app(dbPath='students.db') -> Flask:
    app = Flask(__name__.split('.')[0])

    # registra os blueprints
    app.register_blueprint(studentBp)

    init_db(app, dbPath)

    return app
