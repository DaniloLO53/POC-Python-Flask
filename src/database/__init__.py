import sqlite3
from flask import g
from .database_path import DATABASE_PATH


def init_db(app, db_path):
    global DATABASE_PATH
    studentsSchemaPath = '../students.sql'
    DATABASE_PATH = db_path

    with app.app_context():
        db = get_db(DATABASE_PATH)
        with app.open_resource(studentsSchemaPath, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db(db_path=DATABASE_PATH):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    cur = get_db(DATABASE_PATH).execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
