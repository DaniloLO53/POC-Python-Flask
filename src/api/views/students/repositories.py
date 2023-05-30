import time
from src.database import query_db, get_db
from markupsafe import escape


def findMany():
    return query_db('SELECT * FROM students')


def findByRegister(matricula):
    query = (
        'SELECT matricula, nome, sobrenome, email, telefone, curso, nascimento '
        'FROM students '
        'WHERE students.matricula = ?'
    )

    return query_db(query, (int(matricula),))


def findByEmail(email):
    query = (
        'SELECT matricula, nome, sobrenome, email, telefone, curso, nascimento '
        'FROM students '
        'WHERE students.email = ?'
    )

    return query_db(query, (email,))


def createOne(studentData):
    query_db(
        'INSERT INTO students(matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)'
        'VALUES(?, ?, ?, ?, ?, ?, ?, ?)',
        [
            studentData['matricula'],
            studentData['nome'],
            studentData['sobrenome'],
            studentData['email'],
            studentData['telefone'],
            studentData['curso'],
            studentData['nascimento'],
            int(time.time())
        ]
    )

    get_db().commit()  # Commita pro db
    return


def updateOne(matricula, studentData):
    query_db(
        'UPDATE students '
        'SET matricula = ?, nome = ?, sobrenome = ?, email = ?, '
        'telefone = ?, curso = ?, nascimento = ?, updated_at = ? '
        'WHERE students.matricula = ?',
        [
            studentData['matricula'],
            studentData['nome'],
            studentData['sobrenome'],
            studentData['email'],
            studentData['telefone'],
            studentData['curso'],
            studentData['nascimento'],
            int(time.time()),
            matricula
        ]
    )

    get_db().commit()

    return


def removeOne(matricula):
    query_db('DELETE FROM students WHERE matricula = ?',
             [f'{escape(matricula)}'])

    get_db().commit()
    return
