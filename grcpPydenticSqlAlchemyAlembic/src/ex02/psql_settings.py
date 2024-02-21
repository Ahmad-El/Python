from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv
import os

## loading environment variables
load_dotenv()
ENV = os.getenv

## connecting to postgresql and creating session
db_url = f"postgresql://{ENV('user')}:{ENV('password')}@{ENV('host')}:{ENV('port')}/{ENV('dbname')}"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    ## creating data models if they are not exist(tables)
    Base.metadata.create_all(engine)
    session = Session()
    session.close()
