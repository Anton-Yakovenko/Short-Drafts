"""code to send mail"""

import smtplib
from typing import List
import yaml

with open(r'conf.yml') as file:
    date = {}
    date_yml = yaml.load(file, yaml.Loader)
    date['login'] = date_yml[0]['login']
    date['password'] = date_yml[1]['password']
    date['recipient'] = date_yml[2]['recipient']


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587  # default port


def send_email(from_addr: str, to_addr: List[str], subject: str) -> None:
    msg = f"From: {from_addr}\r\nTo: {','.join(to_addr)}\r\nSubject: {subject}\r\n"

    with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as server:
        server.starttls()
        server.login(date['login'], date['password'])
        # If server.login goes wrong,try to disable third-party application protection in your gmail
        server.sendmail(from_addr, to_addr, msg)


if __name__ == '__main__':

    for x in range(1):  # send messages loop (x = count of mail)
        msg = f"Hello, it`s test message from me {x + 1}"
        send_email(date['login'], [date['recipient'], "over.uran@gmail.com"], msg)
        print("[SENT]")
