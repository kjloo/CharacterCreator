from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<p>Hello, World!</p>"

@app.route('/api/name')
def get_name():
    return {'name': 'Bob'}