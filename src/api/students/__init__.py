from flask import Blueprint

# cria blueprint para student
studentBp = Blueprint('student', __name__)


def register_controllers():
    # essa função resolve o problema de importação circular das rotas
    from src.api.students.controllers import getAllStudents, getStudentByMatricula, createStudent, updateStudent, removeStudent

    # Registra as rotas no bluePrint e o controller nas rotas
    studentBp.get("/students")(getAllStudents)
    studentBp.get("/students/<matricula>")(getStudentByMatricula)
    studentBp.post("/students")(createStudent)
    studentBp.put("/students/<matricula>")(updateStudent)
    studentBp.delete("/students/<matricula>")(removeStudent)


register_controllers()
