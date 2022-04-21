import unittest

from lxml import etree
from parameterized import parameterized

from api.task_01_baidu import BaiDu


class TestTaskBaiDu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.baidu = BaiDu()

    search_data = [("接口测试", "接口测试")]

    @parameterized.expand(search_data)
    def test_task_01_baidu(self, description, search):
        self._testMethodDoc = description

        res_baidu = self.baidu.get_baidu(search=search)

        print(res_baidu.content.decode('utf-8'))
        res = etree.HTML(res_baidu.content.decode('utf-8'))
        title = res.xpath("//title/text()")

        self.assertIn(search, title)
