import os.path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config_parser import parse_file

file_path=os.path.dirname(os.path.dirname(__file__))
config=parse_file(os.path.join(file_path,'server_config.json'))

if not config:
    raise RuntimeError("Unable tp find server config json")

user= config['user']
password=config['password']
host=config['host']
port=config['port']
databasename=config['database']

url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user,password,host,port,databasename)
engine=create_engine(url)
Session=sessionmaker(bind=engine)
Base=declarative_base()

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()