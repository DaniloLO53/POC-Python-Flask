from .repositories import findAll, findByMatricula, findByEmail, insertStudent, updateStudent, removeStudent
from flask import abort, jsonify
import json
from ...utils.statusCodes import statusCodes
from ...utils.messages import messages


def findAllStudents():
    dbStudents = findAll()
    student_dict_array = [dict(data) for data in dbStudents]
    return jsonify(student_dict_array)


def findStudentByEmail(email):
    dbStudent = findByEmail(email)
    if (len(dbStudent) != 0):
        return dict(dbStudent[0])
    return {}


def findStudentByRegistration(matricula):
    dbStudent = findByMatricula(matricula)
    if (len(dbStudent) != 0):
        return dict(dbStudent[0])
    return {}


def postStudent(studentData):
    previousStudentByEmail = findStudentByEmail(studentData["email"])
    previousStudentByRegistration = findStudentByRegistration(
        studentData["matricula"]
    )

    if len(previousStudentByEmail) != 0 | len(previousStudentByRegistration) != 0:
        abort(statusCodes.CONFLICT, messages.STUDENT_NOT_FOUND)
    insertStudent(studentData)

    student = findStudentByRegistration(studentData["matricula"])
    return jsonify(student)


def updateStudentByMatricula(matricula, studentData):
    outdatedStudent = findStudentByRegistration(matricula)
    if len(outdatedStudent) == 0:
        abort(statusCodes.NOT_FOUND, messages.STUDENT_NOT_FOUND)

    updateStudent(matricula, studentData)

    student = findStudentByRegistration(studentData["matricula"])
    return jsonify(student)


def destroyStudent(matricula):
    student = findStudentByRegistration(matricula)
    if len(student) == 0:
        abort(statusCodes.NOT_FOUND, messages.STUDENT_NOT_FOUND)

    removeStudent(matricula)

    return jsonify(student)
