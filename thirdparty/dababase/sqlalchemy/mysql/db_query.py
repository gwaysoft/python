from create_table import Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def query_data():
    # 初始化数据库连接
    engine = create_engine(
        "mysql+pymysql://root:123456@192.168.2.110:3306/pa",
        encoding="utf-8",
        echo=True
    )
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()

    # 查询所有place是CHN的人名
    # 创建Query查询，filter是where条件
    # 调用one()返回唯一行，如果调用all()则返回所有行:
    users = session.query(Users).filter(Users.name == 'JACK').all()
    print([use.name for use in users])
    # 输出：['Chen', 'Zhang']

    # 或者用如下查询
    users = session.query(Users.token).filter(Users.token == "null").all()
    print(users)
    # 输出：[('Chen',), ('Zhang',)]

    session.close()

def update_data():
    # 初始化数据库连接
    engine = create_engine("mysql+pymysql://root:@localhost:3306/orm_test", encoding="utf-8")
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()

    # 数据更新，将Jack的place修改为CHN
    update_obj = session.query(Users).filter(Users.name=='Jack').update({"place":"CHN"})
    session.commit()

    session.close()
    print("Update data successfully!")

def delete_data():
    # 初始化数据库连接
    engine = create_engine("mysql+pymysql://root:@localhost:3306/orm_test", encoding="utf-8")
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()

    # 数据更新，将Jack的记录删除
    update_obj = session.query(Users).filter(Users.name=='Jack').delete()
    session.commit()

    session.close()
    print("Delete data successfully!")


if __name__ == '__main__':
    query_data()
