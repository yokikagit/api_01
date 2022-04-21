import unittest
from api.task_03_iHRM import IHRMBack


class TestTaskBaiDu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ithm = IHRMBack()

    def test_task_03_ithm(self):
        self._testMethodDoc = "获取用户信息"

        request_body = {"mobile": "13800000002", "password": "123456"}
        res_ithm_login = self.ithm.get_cookie(body=request_body)
        print(res_ithm_login)

        res_ithm_user_info = self.ithm.user_info()
        print(res_ithm_user_info.json())
