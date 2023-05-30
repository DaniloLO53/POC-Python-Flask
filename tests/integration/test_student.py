from faker import Faker
import json
from src.api.views.students.services import findAllStudents, findByMatricula

fake = Faker()


def test_createStudent(client, app):
    def test_successs():
        register = fake.random_int(min=5000, max=6000)
        studentData = {
            "nome": fake.first_name(),
            "sobrenome": fake.last_name(),
            "curso": "Medicina",
            "nascimento": "29-05-1996",
            "telefone": "21995484778",
            "email": fake.email(),
            "matricula": register
        }
        response = client.post('/students', json=studentData)

        with app.app_context():
            students = findAllStudents()
            assert len(students) == 1
            assert response.json == studentData
            assert response.status.split(' ')[0] == '201'

    def test_fail():
        register = fake.word()
        studentData = {
            "nome": fake.first_name(),
            "sobrenome": fake.last_name(),
            "curso": "Medicina",
            "nascimento": "05-20-1996",  # MM-DD-YYYY
            "telefone": "219954847789",  # > 12 digitos
            "email": fake.word(),
            "matricula": register
        }

        expectedErrorJson = {
            "error": {
                "email": [
                    "Formato de email inválido"
                ],
                "matricula": [
                    "must be of integer type"
                ],
                "nascimento": [
                    "Formato de data inválido"
                ],
                "telefone": [
                    "Formato de telefone inválido"
                ]
            }
        }
        response = client.post('/students', json=studentData)

        with app.app_context():
            students = findAllStudents()
            # assert students == None
            assert response.status.split(' ')[0] == '422'
            assert response.content_type == 'application/json'
            assert response.json == expectedErrorJson
    test_successs()
    test_fail()


def test_updateStudent(client, app):
    def test_successs():
        register = fake.random_int(min=5000, max=6000)
        studentData = {
            "nome": fake.first_name(),
            "sobrenome": fake.last_name(),
            "curso": "Medicina",
            "nascimento": "29-05-1996",
            "telefone": "21995484778",
            "email": fake.email(),
            "matricula": register
        }
        updatedStudentData = {
            "nome": fake.first_name(),
            "sobrenome": fake.last_name(),
            "curso": "Engenharia",
            "nascimento": "29-06-1996",
            "telefone": "21995484778",
            "email": fake.email(),
            "matricula": register
        }
        client.post('/students', json=studentData)
        response = client.put(
            f'/students/{register}', json=updatedStudentData)

        with app.app_context():
            assert response.json == updatedStudentData
            assert response.status.split(' ')[0] == '201'

    def test_fail():
        register = fake.word()
        studentData = {
            "nome": fake.first_name(),
            "sobrenome": fake.last_name(),
            "curso": "Medicina",
            "nascimento": "05-12-1996",
            "telefone": "21995484789",
            "email": fake.email(),
            "matricula": register
        }
        updatedStudentData = {
            "nome": fake.first_name(),
            "sobrenome": fake.last_name(),
            "curso": "Engenharia",
            "nascimento": "29-30-1996",
            "telefone": "219954x778",
            "email": fake.word(),
            "matricula": register
        }
        expectedErrorJson = {
            "error": {
                "email": [
                    "Formato de email inválido"
                ],
                "matricula": [
                    "must be of integer type"
                ],
                "nascimento": [
                    "Formato de data inválido"
                ],
                "telefone": [
                    "Formato de telefone inválido"
                ]
            }
        }
        client.post('/students', json=studentData)
        response = client.put(
            f'/students/{register}', json=updatedStudentData)

        with app.app_context():
            assert response.status.split(' ')[0] == '422'
            assert response.content_type == 'application/json'
            assert response.json == expectedErrorJson
    test_successs()
    test_fail()


def test_getAllStudent(client, app):
    def test_successs():
        register = fake.random_int(min=5000, max=6000)
        register2 = fake.random_int(min=5000, max=6000)
        studentData = {
            "nome": fake.first_name(),
            "sobrenome": fake.last_name(),
            "curso": "Medicina",
            "nascimento": "29-05-1996",
            "telefone": "21995484778",
            "email": fake.email(),
            "matricula": register
        }
        studentData2 = {
            "nome": fake.first_name(),
            "sobrenome": fake.last_name(),
            "curso": "Medicina",
            "nascimento": "29-05-1996",
            "telefone": "21995484778",
            "email": fake.email(),
            "matricula": register2
        }
        client.post('/students', json=studentData)
        client.post('/students', json=studentData2)
        response = client.get('/students')

        with app.app_context():
            assert response.status.split(' ')[0] == '200'
            assert len(response.json) == 2
            assert response.json[0] == studentData
            assert response.json[1] == studentData2

    test_successs()
