from flask.ext.migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from sqlalchemy import Column, Integer, String, Text, ForeignKey,  Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
import uuid


migrate = Migrate()
db = SQLAlchemy()
login_manager = LoginManager()


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    uuid = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    # is_authenticated = Column(Boolean)
    # is_active  =  Column(Boolean)
    # is_anonymous =  Column(Boolean)

    # @staticmethod
    # def find_by_email(email):
    #     user = db.session.query(User).find(User.email == email).get()
    #     return user

    def __init__(self, email=email, username=username, password=""):
        self.uuid = str(uuid.uuid4())
        self.email = email
        self.username = username



    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @staticmethod
    def validate(args):
        username = args["username"]
        email = args["email"]
        password = args["password"]

        if username=="" or email =="" or password=="":
            return False, "Blank Fields"
        if username==None or email ==None or password==None:
            return False, "No Data Provided "

        #check user
        exists = User.query.filter(User.email==email).first()
        if exists:
            return False, "Duplicate Email"

        exists2 = User.query.filter(User.username == username).first()
        if exists2:
            return False, "Username is already taken"

        return True, "OK"



        #check_password_hash(hash, 'foobar')


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)

