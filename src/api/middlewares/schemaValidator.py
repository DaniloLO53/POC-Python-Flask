from cerberus import Validator
from flask import abort, request
from ..utils.statusCodes import statusCodes
from ..views.students.schemas import studentSchema
import json


def validateSchema(func):
    def wrapper(*args, **kwargs):
        studentData = json.loads(request.data)
        v = Validator(studentSchema)
        validation = v.validate(studentData)

        if not validation:
            abort(statusCodes.UNPROCESSABLE_ENTITY, v.errors)

        return func(*args, **kwargs)

    return wrapper
