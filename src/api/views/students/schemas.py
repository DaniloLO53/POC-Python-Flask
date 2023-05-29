from cerberus import Validator

studentSchema = {
    'curso': {
        'type': 'string'
    },
    'email': {
        'type': 'string'
    },
    'matricula': {
        'type': 'integer'
    },
    'nascimento': {
        'type': 'date'
    },
    'nome': {
        'type': 'string'
    },
    'sobrenome': {
        'type': 'string'
    },
    'telefone': {
        'type': 'string'
    },
}
