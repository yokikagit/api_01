import requests


class UserReg:

    def __init__(self):
        self.reg_verity_url = "http://127.0.0.1/index.php/Home/User/verify/type/user_reg.html"
        self.reg_url = "http://127.0.0.1/index.php/Home/User/reg.html"

        self.login_verity_url = "http://127.0.0.1/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login"

        # self.header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    def get_reg_verity(self, session):
        return session.get(url=self.reg_verity_url)

    def user_reg(self, session, body):
        return session.post(url=self.reg_url, data=body)

    def get_login_verity(self, session):
        return session.get(url=self.login_verity_url)

    def user_login(self, session, body):
        return session.post(url=self.login_url, data=body)
