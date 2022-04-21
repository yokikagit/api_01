class TpLogin:
    def __init__(self):
        self.verify_url = 'http://127.0.0.1/index.php?m=Home&c=User&a=verify'
        self.login_url = 'http://127.0.0.1/index.php?m=Home&c=User&a=do_login'

    def get_verity(self, session):
        return session.get(url=self.verify_url)

    def login(self, session, data):
        return session.post(url=self.login_url, data=data)
