import sqlite3
import json
from flask import Flask, g, request
from markupsafe import escape

DATABASE_PATH = "students.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_PATH)
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


app = Flask(__name__.split('.')[0])


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    studentsSchemaPath = "students.sql"

    with app.app_context():
        db = get_db()
        with app.open_resource(studentsSchemaPath, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


init_db()


@app.delete("/students/<matricula>")
def destroy(matricula):
    student = getStudent(f'{escape(matricula)}')
    print(matricula)

    query_db('DELETE FROM students WHERE matricula = ?',
             [f'{escape(matricula)}'])

    get_db().commit()  # Commit the changes to the database

    return student


@app.post("/students")
def create():
    studentData = json.loads(request.data)
    query_db(
        'INSERT INTO students(matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)'
        'VALUES(?, ?, ?, ?, ?, ?, ?, ?)',
        [
            studentData["matricula"],
            studentData["nome"],
            studentData["sobrenome"],
            studentData["email"],
            studentData["telefone"],
            studentData["curso"],
            studentData["nascimento"],
            studentData["updated_at"]
        ]
    )
    print("Matricula no post: ", studentData["matricula"])

    get_db().commit()  # Commit the changes to the database

    student = getStudent(studentData["matricula"])
    return student


@app.get("/students")
def getAll():
    dbStudents = query_db('SELECT * FROM students')
    students = []

    for student in dbStudents:
        students.append({
            "Matrícula": student['matricula'],
            "Nome": student['nome'],
            "Sobrenome": student['sobrenome'],
            "Email": student['email'],
            "Telefone": student['telefone'],
            "Curso": student['curso'],
            "Nascimento": student['nascimento'],
        })
    return students


@app.get("/students/<matricula>")
def getStudent(matricula):
    print("Matricula no get: ", matricula)

    query = (
        "SELECT matricula, nome, sobrenome, email, telefone, curso, nascimento "
        "FROM students "
        "WHERE students.matricula = ?"
    )

    student = query_db(query, (int(matricula),))
    print('Student: ', student)
    if (len(student) != 0):
        student_dict = dict(student[0])
        return json.dumps(student_dict, default=str)
    return {}

# Diferença entre json.load e json.loads (erro )
# https://stackoverflow.com/questions/6541767/python-urllib-error-attributeerror-bytes-object-has-no-attribute-read
