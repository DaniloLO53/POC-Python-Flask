from flask import Flask

app = Flask(__name__.split('.')[0])


@app.route("students")
def getAll():
    return "hello world"
