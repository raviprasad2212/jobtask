from flask import Flask
from flask import jsonify, make_response
from modules.mytasks import Api, Tasks, Tasks2

app = Flask(__name__)
api = Api(app)

# If yit is enable you have to use postman for testing.
# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

# Routes
api.add_resource(Tasks, '/', '/todo/api/v1.0/tasks')
api.add_resource(Tasks2, '/', '/todo/api/v1.0/tasks/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)