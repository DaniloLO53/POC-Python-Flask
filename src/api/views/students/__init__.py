from flask import Blueprint
from ...middlewares.schemaValidator import validateSchema

# cria blueprint para student
studentBp = Blueprint('student', __name__)


def wrap(*funcs):  # recebe os middlewares e o controller
    # a requisição passa por todos os middlewares e o controller que essa função recebe
    # no fim, é retornado o retorno do controller (a resposta http final)
    def wrapped(*args, **kwargs):
        finalReturn = None
        for func in funcs:
            # middlewares controller recebe os
            finalReturn = func(*args, **kwargs)
            # argumentos e valores que estao sendo passados para wrapped
        return finalReturn  # retorna a reposta http do ultimo controller
    return wrapped


def register_controllers():
    # essa função resolve o problema de importação circular das rotas
    from .controllers import getAll, get, create, update, remove

    # Registra as rotas no bluePrint e o controller nas rotas
    studentBp.get('/students')(getAll)
    studentBp.get('/students/<matricula>')(get)
    studentBp.put(
        '/students/<matricula>', endpoint='update')(wrap(validateSchema, update))
    studentBp.post(
        '/students', endpoint='create')(wrap(validateSchema, create))
    studentBp.delete(
        '/students/<matricula>', endpoint='delete')(remove)


register_controllers()
