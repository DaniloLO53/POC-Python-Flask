import pytest
import os

from src import create_app
from src.database import get_db, query_db


@pytest.fixture(scope="session")
def app():
    app = create_app("students_test.db")

    # Limpa o banco de dados após todos os testes da sessão serem concluídos
    from src.database.database_path import DATABASE_PATH
    db_path = DATABASE_PATH
    if db_path and os.path.exists(db_path):
        os.remove(db_path)

    yield app  # não retorno pq preciso desse app no client abaixo


@pytest.fixture()
def client(app):  # esse é o app definido acima
    with app.app_context():
        # Limpa o banco de dados antes de cada teste
        query_db('DELETE FROM students')
        get_db().commit()

    # simula requisições
    return app.test_client()
