import unittest
from db_demo import app, db, Role


class DatabaseTest(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@192.168.2.110:3306/flask02"
        db.create_all()

    def test_add_item(self):
        role = Role(name="test")
        db.session.add(role)
        db.session.commit()

        ret = Role.query.filter_by(name="test").first()
        self.assertIsNotNone(ret)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
