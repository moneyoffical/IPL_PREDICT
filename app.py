from flask import Flask,render_template
from flask_restful import Api
from flask_jwt import JWT

from resources.user import User,UserList
from resources.predict import Predict
from security import authenticate,identity

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

#JWT 
app.secret_key = 'sangam'
app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app,authenticate,identity)

api = Api(app)

"""@app.before_first_request
def create_table():
    db.create_all()"""

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('home.html')

api.add_resource(User,'/user/<string:name>')

api.add_resource(UserList,'/users')

api.add_resource(Predict,'/predict')

#from db import db
#db.__init__(app)

if __name__ == '__main__':
    app.run()