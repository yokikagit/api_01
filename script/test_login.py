import unittest

import requests
from parameterized import parameterized

from api.tp_api_login import TpLogin


class TestLogin(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        if cls.session is None:
            cls.session = requests.Session()
        cls.tp_login = TpLogin()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    login_data = [('登录成功', {"username": 18800000001, "password": 123456, "verify_code": 8888}, 1, '登陆成功', 200),
                  ('用户名错误', {"username": 18700000001, "password": 123456, "verify_code": 8888}, -1, '账号不存在', 200),
                  ('密码错误', {"username": 18800000001, "password": 1234567, "verify_code": 8888}, -2, '密码错误', 200)]

    @parameterized.expand(login_data)
    def test_login(self, description, request_body, status, message, http_code):
        # self._testMethodName = description  # 测试方法名
        self._testMethodDoc = description  # 用例描述

        res_verity = self.tp_login.get_verity(self.session)
        # print(res_verity.content)
        self.assertIn("image", res_verity.headers.get("Content-Type"))

        res_login = self.tp_login.login(self.session, data=request_body)
        print(res_login.json())

        self.assertEqual(http_code, res_login.status_code)
        self.assertEqual(status, res_login.json().get('status'))
        self.assertIn(message, res_login.json().get('msg'))
