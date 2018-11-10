from flask_restful import Resource, reqparse

# Parse incoming data
parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message': 'User registration'}


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message': 'User login'}


class UserLogoutAccess(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message': 'Token refresh'}


class AllUsers(Resource):
    def get(self):
        data = parser.parse_args()
        return {'message': 'List of users'}

    def delete(self):
        data = parser.parse_args()
        return {'message': 'Delete all users'}


class SecretResource(Resource):
    def get(self):
        data = parser.parse_args()
        return {
            'answer': 42
        }