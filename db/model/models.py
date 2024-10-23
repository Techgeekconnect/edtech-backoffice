import sqlalchemy
from db import Base

class StudentManager(Base):
    __tablename__ = 'studentmanager'

    studentid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    studentname = sqlalchemy.Column(sqlalchemy.String(128),unique=True)
    studentemailid = sqlalchemy.Column(sqlalchemy.String(128), unique=True)
    studentaddress = sqlalchemy.Column(sqlalchemy.String(512), unique=True)
    studentphone = sqlalchemy.Column(sqlalchemy.BIGINT,unique=True)
    studentcollege = sqlalchemy.Column(sqlalchemy.String(512), unique=True)
    studentresume = sqlalchemy.Column(sqlalchemy.LargeBinary, unique=True)
    studentphoto = sqlalchemy.Column(sqlalchemy.LargeBinary, unique=True)
    studentstream = sqlalchemy.Column(sqlalchemy.String(128), unique=True)

class TrainerManager(Base):
    __tablename__ = 'trainermanager'

    studentid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    studentname = sqlalchemy.Column(sqlalchemy.String(128),unique=True)
    studentemailid = sqlalchemy.Column(sqlalchemy.String(128), unique=True)
    studentaddress = sqlalchemy.Column(sqlalchemy.String(512), unique=True)
    studentphone = sqlalchemy.Column(sqlalchemy.BIGINT,unique=True)
    studentcollege = sqlalchemy.Column(sqlalchemy.String(512), unique=True)
    studentresume = sqlalchemy.Column(sqlalchemy.LargeBinary, unique=True)
    studentphoto = sqlalchemy.Column(sqlalchemy.LargeBinary, unique=True)
    studentstream = sqlalchemy.Column(sqlalchemy.String(128), unique=True)