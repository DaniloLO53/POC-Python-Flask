from flask import Blueprint
from ...middlewares.schemaValidator import validateSchema
from functools import wraps

# cria blueprint para student
studentBp = Blueprint('student', __name__)


def wrap(*funcs):
    def wrapped(*args, **kwargs):
        finalReturn = None
        for func in funcs:
            finalReturn = func(*args, **kwargs)
        return finalReturn
    return wrapped


def register_controllers():
    # essa função resolve o problema de importação circular das rotas
    from .controllers import getAllStudents, getStudentByRegistration, createStudent, updateStudent, removeStudent

    # Registra as rotas no bluePrint e o controller nas rotas
    studentBp.get("/students")(getAllStudents)
    studentBp.get("/students/<matricula>")(getStudentByRegistration)
    studentBp.post(
        "/students", endpoint='create')(wrap(validateSchema, createStudent))
    studentBp.put(
        "/students/<matricula>", endpoint='update')(wrap(validateSchema, updateStudent))
    studentBp.delete(
        "/students/<matricula>", endpoint='delete')(wrap(validateSchema, removeStudent))


register_controllers()
