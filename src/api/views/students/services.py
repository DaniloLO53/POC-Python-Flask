from . import repositories
from flask import abort
from ...utils.statusCodes import statusCodes
from ...utils.messages import messages
from .utils import sqliteRowToDict


def getAll():
    dbStudents = repositories.findMany()
    student_dict_array = [dict(data) for data in dbStudents]

    for student in student_dict_array:
        student.pop('updated_at', None)
        student.pop('created_at', None)

    return student_dict_array


def get(data, dataType='registration'):
    dbStudent = repositories.findByEmail(
        data) if dataType == 'email' else repositories.findByRegister(data)

    return sqliteRowToDict(dbStudent)


def create(studentData):
    previousStudentByEmail = get(studentData['email'], 'email')
    previousStudentByRegistration = repositories.findByRegister(
        studentData['matricula']
    )

    if len(previousStudentByEmail) != 0 or len(previousStudentByRegistration) != 0:
        abort(statusCodes.CONFLICT, messages.STUDENT_ALREADY_REGISTERED)
    repositories.createOne(studentData)
    return get(studentData['matricula'])


def update(matricula, studentData):
    outdatedStudent = get(matricula)
    if len(outdatedStudent) == 0:
        abort(statusCodes.NOT_FOUND, messages.STUDENT_NOT_FOUND)

    repositories.updateOne(matricula, studentData)
    return get(studentData['matricula'])


def remove(matricula):
    student = get(matricula)
    if len(student) == 0:
        abort(statusCodes.NOT_FOUND, messages.STUDENT_NOT_FOUND)

    repositories.removeOne(matricula)

    return student
