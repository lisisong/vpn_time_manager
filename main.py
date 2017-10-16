# coding=utf-8
import time
import os
import httplib
import urllib
import re


def kill_progress(pid):
    os.system("kill -9 " + pid)


def find_kill_list():
    params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    headers = {"Content-type": "application/json"}
    conn = httplib.HTTPConnection("127.0.0.1:8080")
    conn.request("POST", "/vpn/killList", params, headers)
    response = conn.getresponse()
    return response.user_list

def kill_report(user):
    params = urllib.urlencode({'kill': user})
    headers = {"Content-type": "application/json"}
    conn = httplib.HTTPConnection("127.0.0.1:8080")
    conn.request("POST", "/vpn/killReport", params, headers)
    response = conn.getresponse()
    return response.status

def find_online_user():
    r = os.popen("last | grep still | grep ppp")
    text = r.read()
    r.close()
    return text




while True:
    time.sleep(1)
    kill_progress(1)
    kill_list = find_kill_list()
    if kill_list.size != 0:
        txt = find_online_user()
        os.exe
        kill_report(kill_list[0].userName)




