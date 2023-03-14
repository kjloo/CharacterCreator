from flask import Blueprint

app_routes = Blueprint('routes', __name__)

@app_routes.route('/')
def hello():
    return "<p>Hello, World!</p>"

@app_routes.route('/api/name', methods=['GET'])
def get_name():
    return {'name': 'Bob'}
