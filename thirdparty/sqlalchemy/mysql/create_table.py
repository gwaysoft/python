from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# users表结构
class Users(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(256), nullable=False)
    token = Column(VARCHAR(256), nullable=True)

    def __init__(self, id, name, token):
        self.id = id
        self.name = name
        self.taken = token


def init_db():
    engine = create_engine(
        "mysql+pymysql://root:123456@192.168.2.110:3306/pa",
        encoding="utf-8",
        echo=True
    )
    Base.metadata.create_all(engine)
    print('Create table successfully!')


if __name__ == '__main__':
    init_db()
