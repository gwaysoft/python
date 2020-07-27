import unittest
from unittest_demo import app
import json


class LoginTest(unittest.TestCase):

    def setUp(self):
        # suggest testing True
        # app.config["TESTING"] = True
        app.testing = True
        self.client = app.test_client()

    def test_empty_username_password(self):
        """test"""

        ret = self.client.post("/login", data={})

        resp = ret.data

        resp = json.loads(resp)

        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

        # test username
        ret = self.client.post("/login", data={"user_name": "admin", "password": "2"})

        resp = ret.data
        print(resp)
        resp = json.loads(resp)
        print(resp)

        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)

    def test_wrong_username_password(self):
        ret = self.client.post("/login", data={"user_name": "admin", "password": "123456"})

        resp = ret.data
        print(resp)
        resp = json.loads(resp)
        print(resp)

        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 0)


if __name__ == '__main__':
    unittest.main()
