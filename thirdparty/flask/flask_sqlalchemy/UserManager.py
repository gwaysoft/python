from flask import Flask
from gspackage.flask_sqlalchemy_mysql.gsmysql import init_db

app = Flask(__name__)
db = init_db(app)
app_ctx = app.app_context()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), nullable=False)


def create_table():
    with app_ctx:
        print("c")
        db.create_all()


def insert_user():
    with app_ctx:
        # 创建一个新用户对象
        user = User()
        user.username = 'fuyo22wwng'
        user.password = '123'

        # 将新创建的用户添加到数据库会话中
        db.session.add(user)
        # 将数据库会话中的变动提交到数据库中, 记住, 如果不 commit, 数据库中是没有变化的.
        db.session.commit()


def update_user(idd):
    with app_ctx:
        print("c")
        # 获取用户对象
        user = User.query.filter_by(id=idd).first()

        # 修改用户
        user.password = '123567'

        # 提交数据库会话

        db.session.commit()


def delete_user():
    with app_ctx:
        # 获取用户对象
        user = User.query.filter_by(id=1).first()

        # 删除用户
        db.session.delete(user)

        # 提交数据库会话
        db.session.commit()


def get_user(id):
    with app_ctx:
        user = User.query.filter_by(id=id).first()
        return user


if __name__ == '__main__':
    print(get_user(3))
