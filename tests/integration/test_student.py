from faker import Faker
import json
from src.api.views.students.services import findAllStudents

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
        response = client.post('/students', json=studentData)

        with app.app_context():
            students = findAllStudents()
            # assert students == None
            assert response.status.split(' ')[0] == '422'
            assert response.data == None
    test_successs()
    test_fail()
