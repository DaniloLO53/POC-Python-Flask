from src import create_app
from flask import g, jsonify
from werkzeug.exceptions import HTTPException

app = create_app('students.db')


@app.errorhandler(HTTPException)
def handle_http_exception(error):
    print('TESTEEEEEE')
    responseToJSON = jsonify({'error': error.description})
    responseToJSON.headers["Content-Type"] = "application/json"
    responseToJSON.status_code = error.code
    return responseToJSON


@app.teardown_appcontext
def close_connection(exception):
    print('OIIIII')
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
