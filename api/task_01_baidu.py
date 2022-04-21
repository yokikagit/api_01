import requests


class BaiDu:

    def __init__(self):
        self.baidu_url = "http://www.baidu.com/s"

    def get_baidu(self, search):
        return requests.get(url=self.baidu_url, params={'w': search})
