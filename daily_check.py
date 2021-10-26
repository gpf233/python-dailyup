import requests
import json


class DailyCheck(object):

    def __init__(self):
        self.cookies = dict()
        self.session = requests.sessions.Session()

    def login(self, username, password):
        url = "https://xxcapp.xidian.edu.cn/uc/wap/login/check"
        params = {"username": username,
                  "password": password
                  }
        r_login = self.session.post(url, data=params)
        self.cookies = requests.utils.dict_from_cookiejar(r_login.cookies)

    def check_login(self):
        url = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/index"
        r = self.session.get(url, cookies=self.cookies)
        if "操作成功" in r.text:
            return True
        else:
            return False

    def summit(self):
        url = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save"
        with open("data.json", "r", encoding="utf-8") as f:
            params = json.loads(f.read())
        r_check = self.session.post(url, data=params, cookies=self.cookies)
        return r_check.text
