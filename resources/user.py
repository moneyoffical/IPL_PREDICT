from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

from db import db
from models.user import UserModel

class User(Resource):

    parser = reqparse.RequestParser()
    #name_parser = parser.add_argument('name',type=str,required=True,help='cannot empty')
    #parser.add_argument('password',type=str,required=True,help='cannot empty')
    #parser.add_argument('email',type=str,required=True,help='cannot empty')

    #to getting user 
    @jwt_required()
    def get(self,name):
        user = UserModel.find_by_name(name)
        if user:
            return user.json()
        return{'message':'User not found'},404

    # adding user
    def post(self,name):
        User.parser.add_argument('password',type=str,required=True,help='cannot empty')
        User.parser.add_argument('email',type=str,required=True,help='cannot empty')
        data = User.parser.parse_args()
        item = UserModel(name,**data)

        if UserModel.find_by_name(name):
            return {'message':'User already exists'},400

        if UserModel.find_by_email(data['email']):
            return {'message':'Email already exists'},400

        try:
            item.save_to_db()
        except:
            return {'message':"something wrong"},500
        return item.json(),201
        

    # updating user data
    def put(self,name):
        User.parser.add_argument('password',type=str,required=True,help='cannot empty')
        User.parser.add_argument('email',type=str,required=True,help='cannot empty')
        data = User.parser.parse_args()
        
        item = UserModel.find_by_name(name)
        if item is None:
            return {'message':'User Not exist'},400

        try:
            item.password = data['password']
            item.email = data['email']
            item.save_to_db()
        except:
            return {'message':'Something went wrong'}
        return {'message':'User Updated successfully'}

    # deleting user data
    def delete(self,name):
        user = UserModel.find_by_name(name)
        if user is None:
            return {'message':'User Not exist'},400

        try:
            user.delete_from_db()
        except:
            return {'message':'Something went wrong'},500
        return {'message':'User deleted successfully'}

    
class UserList(Resource):
    def get(self):
        return {'users':list(map(lambda x: x.json(),UserModel.query.all()))}
