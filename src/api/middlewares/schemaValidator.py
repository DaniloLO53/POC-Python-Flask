from cerberus import Validator
from flask import abort, request
from ..utils.statusCodes import statusCodes
from ..views.students.schemas import studentSchema
import json


def validateSchema():
    studentData = json.loads(request.data)
    v = Validator(studentSchema)
    validation = v.validate(studentData)

    if not validation:
        abort(statusCodes.UNPROCESSABLE_ENTITY, v.errors)
