import requests
from api.task_02_tp_user_reg import UserReg
import unittest


class TestTaskBaiDu(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        if cls.session is None:
            cls.session = requests.Session()
        cls.user_reg = UserReg()

    @classmethod
    def tearDownClass(cls):
        if cls.session is not None:
            cls.session.close()

    def test_task_02_reg(self):
        res_verity = self.user_reg.get_reg_verity(self.session)
        self.assertIn('image', res_verity.headers.get("Content-Type"))
        print(res_verity.headers.get("Content-Type"))

        reg_request_body = {'scene': 1, 'username': 18257348880, 'verify_code': 8888, 'password': 123456,
                            'password2': 123456, 'invite': ''}
        res_user_reg = self.user_reg.user_reg(session=self.session, body=reg_request_body)
        print(res_user_reg.json())

        res_login_verity = self.user_reg.get_login_verity(self.session)
        login_request_body = {'username': 18257348880, 'password': 123456, 'verify_code': 8888}
        res_user_login = self.user_reg.user_login(session=self.session, body=login_request_body)
        print(res_user_login.json())
