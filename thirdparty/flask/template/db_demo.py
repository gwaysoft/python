from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@192.168.2.110:3306/flask01"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


app.config.from_object(Config)

db = SQLAlchemy(app)


class User(db.Model):
    # table name
    __tablename__ = "tbl_users"
    # Integer, default increment
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))
    def __repr__(self):
        """define"""
        return "User object: name=%s" % (self.name)


class Role(db.Model):
    __tablename__ = "tbl_roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship("User", backref="role")
    def __repr__(self):
        """define"""
        return "Role object: name=%s" % (self.name)


@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0")
    # db.drop_all()
    # db.create_all()
    # role1 = Role(name="admin")
    # role2 = Role(name="user")
    # role3 = Role(name="user个")
    # db.session.add_all([role1, role2, role3])
    # # after commit, has role_id
    # db.session.commit()
    # user1 = User(name="wang", email="wang@ebaotech.com", password="123", role_id=role1.id)
    # user2 = User(name="zhu", email="zhu@ebaotech.com", password="123", role_id=role1.id)
    # user3 = User(name="chen", email="chen@ebaotech.com", password="123", role_id=role2.id)
    # user4 = User(name="ge", email="ge@ebaotech.com", password="123", role_id=role2.id)
    # db.session.add_all([user1, user2, user3, user4])
    # db.session.commit()
    # print(Role.query.all()[0].name)
    # r = Role.query.first()
    # Role.query.get(1).name  # index
    # db.session.query(Role).all()  # alchemy
    # user = User.query.filter_by(name="wang").all()[0]
    # User.query.filter_by(name="wang", role_id=1).all()
    # user = User.query.filter_by(name="wang", role_id=3).first()
    # type(user)
    # User.query.order_by("id").all()
    # User.query.order_by(User.name.desc()).all()
    # db.session.query(User.role_id).group_by(User.role_id)
    # db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id).all()
    # join
    role = Role.query.get(1)
    role.users

    user = User.query.get(1)
    # backref
    print(user)

    db.session.delete(user)
    db.session.commit()

