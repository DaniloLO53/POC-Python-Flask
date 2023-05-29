from cerberus import Validator
from flask import abort, request
from ..utils.messages import messages
from ..utils.statusCodes import statusCodes
from ..views.students.schemas import studentSchema
import json


def validateSchema():
    studentData = json.loads(request.data)
    print("DATA", studentData)
    v = Validator(studentSchema)
    if not v.validate(studentData):
        abort(statusCodes.UNPROCESSABLE_ENTITY, messages.INVALID_DATA)
    pass
