from src import create_app
from flask import g
from src.database import get_db

app = create_app()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    studentsSchemaPath = "../students.sql"

    with app.app_context():
        db = get_db()
        with app.open_resource(studentsSchemaPath, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


init_db()

if __name__ == '__main__':
    app.run()
