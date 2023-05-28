from .repositories import findAll, findByMatricula, insertStudent, updateStudent, removeStudent
import json


def formatDbStudentsToJSON(dbStudents):
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


def findAllStudents():
    dbStudents = findAll()
    return formatDbStudentsToJSON(dbStudents)


def findStudentByMatricula(matricula):
    dbStudent = findByMatricula(matricula)
    print('Student: ', dbStudent)
    if (len(dbStudent) != 0):
        student_dict = dict(dbStudent[0])
        return json.dumps(student_dict, default=str)
    return {}


def postStudent(studentData):
    insertStudent(studentData)

    student = findStudentByMatricula(studentData["matricula"])
    return student


def updateStudentByMatricula(matricula, studentData):
    updateStudent(matricula, studentData)

    student = findStudentByMatricula(studentData["matricula"])
    return student


def destroyStudent(matricula):
    student = findStudentByMatricula(matricula)

    removeStudent(matricula)

    return student
