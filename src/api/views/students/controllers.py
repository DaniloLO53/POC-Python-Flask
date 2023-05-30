from .services import findAllStudents, findStudent, postStudent, updateStudentByMatricula, destroyStudent
from ...utils.statusCodes import statusCodes
from flask import request, make_response, jsonify
import json


def getAllStudents():
    students = findAllStudents()
    return make_response(jsonify(students), statusCodes.OK)


def getStudentByRegistration(matricula):
    student = findStudent(matricula)
    return make_response(jsonify(student), statusCodes.OK)


def createStudent():
    studentData = json.loads(request.data)
    student = postStudent(studentData)
    return make_response(jsonify(student), statusCodes.CREATED)


def updateStudent(matricula):
    studentData = json.loads(request.data)
    student = updateStudentByMatricula(matricula, studentData)
    return make_response(jsonify(student), statusCodes.CREATED)


def removeStudent(matricula):
    student = destroyStudent(matricula)
    return make_response(jsonify(student), statusCodes.CREATED)
