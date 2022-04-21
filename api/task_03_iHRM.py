import requests


class IHRMBack:

    def __init__(self):
        self.login_header = {"Content-Type": "application/json"}
        self.ithm_login_url = "http://ihrm-test.itheima.net/api/sys/login"

        self.token = ''
        self.ithm_uerInfo_url = "http://ihrm-test.itheima.net/api/sys/profile"

    def get_cookie(self, body):
        """
        :param body:传入的表单数据
        :return:返回请求结果
        """
        res_ithm_login = requests.post(url=self.ithm_login_url, json=body, headers=self.login_header)
        print(res_ithm_login.json())
        cookie = 'Bearer ' + res_ithm_login.json().get('data')
        self.token = cookie
        return self.token

    def user_info(self):
        """
        :return:返回请求结果
        """
        return requests.post(url=self.ithm_uerInfo_url,
                             headers={"Content-Type": "application/json", 'Authorization': self.token})
