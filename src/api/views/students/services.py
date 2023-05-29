from .repositories import findAll, findByMatricula, findByEmail, insertStudent, updateStudent, removeStudent
from flask import abort, jsonify
import json
from ...utils.statusCodes import statusCodes
from ...utils.messages import messages


def findAllStudents():
    dbStudents = findAll()
    student_dict_array = [dict(data) for data in dbStudents]
    return student_dict_array


def findStudent(data, dataType="registration"):
    dbStudent = findByEmail(
        data) if dataType == "email" else findByMatricula(data)

    if (len(dbStudent) != 0):
        return dict(dbStudent[0])
    return {}


def postStudent(studentData):
    previousStudentByEmail = findStudent(studentData["email"], "email")
    previousStudentByRegistration = findStudent(
        studentData["matricula"]
    )

    if len(previousStudentByEmail) != 0 or len(previousStudentByRegistration) != 0:
        abort(statusCodes.CONFLICT, messages.STUDENT_ALREADY_REGISTERED)
    insertStudent(studentData)

    student = findStudent(studentData["matricula"])
    return student


def updateStudentByMatricula(matricula, studentData):
    outdatedStudent = findStudent(matricula)
    if len(outdatedStudent) == 0:
        abort(statusCodes.NOT_FOUND, messages.STUDENT_NOT_FOUND)

    updateStudent(matricula, studentData)

    student = findStudent(studentData["matricula"])
    return student


def destroyStudent(matricula):
    student = findStudent(matricula)
    if len(student) == 0:
        abort(statusCodes.NOT_FOUND, messages.STUDENT_NOT_FOUND)

    removeStudent(matricula)

    return student
