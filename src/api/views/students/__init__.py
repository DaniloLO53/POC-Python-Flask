from flask import Blueprint
from ...middlewares.schemaValidator import validateSchema

# cria blueprint para student
studentBp = Blueprint('student', __name__)


def wrap(*funcs):
    def wrapped(*args, **kwargs):
        for func in funcs:
            func(*args, **kwargs)
    return wrapped


def register_controllers():
    # essa função resolve o problema de importação circular das rotas
    from .controllers import getAllStudents, getStudentByRegistration, createStudent, updateStudent, removeStudent

    # Registra as rotas no bluePrint e o controller nas rotas
    studentBp.get("/students")(getAllStudents)
    studentBp.get("/students/<matricula>")(getStudentByRegistration)
    studentBp.post("/students")(wrap(validateSchema, createStudent))
    studentBp.put("/students/<matricula>")(wrap(validateSchema, updateStudent))
    studentBp.delete(
        "/students/<matricula>")(wrap(validateSchema, removeStudent))


register_controllers()
