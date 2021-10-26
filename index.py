from email_sender import EmailSender
from daily_check import DailyCheck
import json


def main_handler():
    dailyCheck = DailyCheck()
    with open("users.json", "r", encoding="utf-8") as f:
        users = json.loads(f.read())
    contents = ""
    for user in users:
        content = user["username"]
        dailyCheck.login(user["username"], user["password"])
        if dailyCheck.check_login():
            content += dailyCheck.summit()
        else:
            content += "登录失败"
        if (user["email"] != ""):
            EmailSender.send(user["email"], "晨午晚检", content)
        contents += content
        contents += "\n"
        print(content)
    EmailSender.send("admin@admin.com", "晨午晚检", contents)

main_handler()