from flask import Flask
from gspackage.flask_sqlalchemy_mysql.gsmysql import init_db

# from flask_main import app
app = Flask(__name__)
db = init_db(app)
app_ctx = app.app_context()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    token = db.Column(db.String(80), nullable=True)


def create_table(app_ctx):
    with app_ctx:
        print("c")
        db.create_all()


def insert_user(user):
    with app_ctx:
        # 将新创建的用户添加到数据库会话中
        db.session.add(user)
        # 将数据库会话中的变动提交到数据库中, 记住, 如果不 commit, 数据库中是没有变化的.
        db.session.commit()


def update_token_by_name(username, token):
    with app_ctx:
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User()
            user.username = username
            user.token = token
            db.session.add(user)
        else:
            user.token = token
        db.session.commit();


def get_user_by_id(id):
    with app_ctx:
        user = User.query.filter_by(id=id).first()
        print(user.id)
        token = user.token
        return token


def get_user_by_token(token):
    with app_ctx:
        user = User.query.filter_by(token=token).first()
        return user


def update_user(user):
    print(user.id)
    # with app_ctx:
    #     user = get_user_by_id(user.id)
    #     user.token = "d2d"
    #     db.session.commit()


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
    # create table
    # create_table()

    # insert
    # user = User()
    # user.username = 'fuyo22wwng'
    # user.password = '123'
    # insert_user(user)

    # update
    update_token_by_name("ddd","eee")
