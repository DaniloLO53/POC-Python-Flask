from src import create_app
from flask import g, jsonify
from werkzeug.exceptions import HTTPException

app = create_app('students.db')


@app.errorhandler(HTTPException)
def handle_http_exception(error):
    response = jsonify({'error': error.description})
    response.status_code = error.code
    return response


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
