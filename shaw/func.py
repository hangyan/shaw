#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import random
import string

from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

__author__ = 'Hang Yan'


def rand_low_str(length, upper=False, lower=True, digit=False, punc=False):
    choice = ''
    if upper:
        choice += string.ascii_uppercase
    if lower:
        choice += string.ascii_lowercase
    if digit:
        choice += string.digits
    if punc:
        choice += string.punctuation
    if not choice:
        return choice
    return ''.join(random.choice(choice) for _ in range(length))


def rand_str(length):
    return rand_low_str(length, upper=True, digit=True, punc=True)


def dumps(data):
    return "\n" + json.dumps(data, indent=4, sort_keys=True)


def send_mail(server, fro, to, subject, text, files=None, is_html=False):
    assert type(server) == dict
    assert type(fro) == str
    assert type(to) == list
    assert type(subject) == str
    assert type(text) == str

    files = [] if not files else files

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg['To'] = ','.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(text, 'html' if is_html else 'plain', 'utf8'))

    for f in files:
        att = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att.add_header("Content-Disposition", "attachment", filename=os.path.basename(f))
        msg.attach(att)

    import smtplib
    smtp = smtplib.SMTP_SSL(server['name'], server['port'])
    smtp.login(server['user'], server['password'])
    smtp.sendmail(fro, to, msg.as_string())
    smtp.close()
