from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Models import Answer, Question, Test

class Controller:
    def __init__(self)->None:
        engine=create_engine(
            "sqlite:///C:\\Users\\OWNER\\Desktop\\InterfazTK\\testsdb\\tests.db"
        )
        Session=sessionmaker(bind=engine)
        self.session=Session()

        