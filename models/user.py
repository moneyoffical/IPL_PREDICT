from db import db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(30))
    email = db.Column(db.String(50))

    def __init__(self,name,password,email):
        self.name = name
        self.password = password
        self.email = email

    def json(self):
        return {'name':self.name,'password':self.password,'email':self.email}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_email(cls,email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return {'message:':'wrong with the code'}

