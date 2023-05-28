import json
from src.database import query_db, get_db
from markupsafe import escape


def findAll():
    return query_db('SELECT * FROM students')


def findByMatricula(matricula):
    print("Matricula no get: ", matricula)

    query = (
        "SELECT matricula, nome, sobrenome, email, telefone, curso, nascimento "
        "FROM students "
        "WHERE students.matricula = ?"
    )

    return query_db(query, (int(matricula),))


def insertStudent(studentData):
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
    return


def updateStudent(matricula, studentData):
    student = query_db(
        'UPDATE students SET matricula = ?, nome = ?, sobrenome = ?, email = ?, telefone = ?, curso = ?, nascimento = ?, updated_at = ? '
        'WHERE students.matricula = ?',
        [
            studentData["matricula"],
            studentData["nome"],
            studentData["sobrenome"],
            studentData["email"],
            studentData["telefone"],
            studentData["curso"],
            studentData["nascimento"],
            studentData["updated_at"],
            matricula
        ]
    )

    get_db().commit()  # Commit the changes to the database

    return student


def removeStudent(matricula):
    query_db('DELETE FROM students WHERE matricula = ?',
             [f'{escape(matricula)}'])

    get_db().commit()  # Commit the changes to the database
    return
