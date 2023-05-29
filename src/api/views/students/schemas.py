import re


def validateDateRegex(field, value, error):
    regex = re.compile(r'^(0[1-9]|1\d|2\d|3[01])-(0[1-9]|1[0-2])-\d{4}$')
    if not regex.match(value):
        error(field, "Formato de data inválido")


def validateEmailRegex(field, value, error):
    regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    if not regex.match(value):
        error(field, "Formato de email inválido")


def validatePhoneRegex(field, value, error):
    regex = re.compile(r'^\d{10}$|^\d{11}$')
    if not regex.match(value):
        error(field, "Formato de telefone inválido")


studentSchema = {
    'curso': {
        'type': 'string'
    },
    'email': {
        'type': 'string',
        'check_with': validateEmailRegex
    },
    'matricula': {
        'type': 'integer'
    },
    'nascimento': {
        'type': 'string',
        'check_with': validateDateRegex
    },
    'nome': {
        'type': 'string'
    },
    'sobrenome': {
        'type': 'string'
    },
    'telefone': {
        'type': 'string',
        'check_with': validatePhoneRegex
    }
}
