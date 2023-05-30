from flask import Blueprint, make_response, jsonify
from . import services
from ...utils.statusCodes import statusCodes
from flask import request, make_response, jsonify
import json
from ...middlewares.schemaValidator import validateSchema

# cria blueprint para student
studentBp = Blueprint('student', __name__)


@studentBp.get('/students')
def getAll():
    students = services.getAll()
    return make_response(jsonify(students), statusCodes.OK)


@studentBp.get('/students/<matricula>')
def get(matricula):
    student = services.get(matricula)
    return make_response(jsonify(student), statusCodes.OK)


@studentBp.post('/students', endpoint="post")
@validateSchema
def create():
    studentData = json.loads(request.data)
    student = services.create(studentData)
    return make_response(jsonify(student), statusCodes.CREATED)


@studentBp.put('/students/<matricula>', endpoint="put")
@validateSchema
def update(matricula):
    studentData = json.loads(request.data)
    student = services.update(matricula, studentData)
    return make_response(jsonify(student), statusCodes.CREATED)


@studentBp.delete('/students/<matricula>')
def remove(matricula):
    student = services.remove(matricula)
    return make_response(jsonify(student), statusCodes.CREATED)
