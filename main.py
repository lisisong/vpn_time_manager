# coding=utf-8
import time
import os
import httplib
import urllib
import json


def kill_progress(pid):
    os.system("kill -9 " + pid)


def find_kill_list():
    params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    headers = {"Content-type": "application/json"}
    conn = httplib.HTTPConnection("127.0.0.1:8080")
    conn.request("GET", "/api/vpn/findKillList", params, headers)
    response = conn.getresponse()
    json_to_python = json.loads(response.read())
    return json_to_python


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
    online_list = find_online_user()
    for i in find_kill_list()['killList']:
        if online_list['user_name'].find(i['USER_NAME']) != -1:
            kill_progress(online_list['pid'])
            kill_report(i['USER_NAME'])
