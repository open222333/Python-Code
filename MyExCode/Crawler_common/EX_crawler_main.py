import requests


class Login():
    def __init__(self, **kwargs) -> None:
        self.login_page = ''

    def login(self):
        headers = {
            'user_agent': ''
        }
        datas = {
            'username': '',
            'password': ''
        }
        reg = requests.post(self.login_page, headers=headers, data=datas)
        return reg.cookies
