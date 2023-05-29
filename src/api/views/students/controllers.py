from .services import findAllStudents, findStudentByRegistration, postStudent, updateStudentByMatricula, destroyStudent
from flask import request
import json


def getAllStudents():
    return findAllStudents()


def getStudentByRegistration(matricula):
    return findStudentByRegistration(matricula)


def createStudent():
    studentData = json.loads(request.data)
    return postStudent(studentData)


def updateStudent(matricula):
    studentData = json.loads(request.data)
    return updateStudentByMatricula(matricula, studentData)


def removeStudent(matricula):
    return destroyStudent(matricula)
