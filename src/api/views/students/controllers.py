from . import services
from ...utils.statusCodes import statusCodes
from flask import request, make_response, jsonify
import json


def getAll():
    students = services.getAll()
    return make_response(jsonify(students), statusCodes.OK)


def get(matricula):
    student = services.get(matricula)
    return make_response(jsonify(student), statusCodes.OK)


def create():
    studentData = json.loads(request.data)
    student = services.create(studentData)
    return make_response(jsonify(student), statusCodes.CREATED)


def update(matricula):
    studentData = json.loads(request.data)
    student = services.update(matricula, studentData)
    return make_response(jsonify(student), statusCodes.CREATED)


def remove(matricula):
    student = services.remove(matricula)
    return make_response(jsonify(student), statusCodes.CREATED)
