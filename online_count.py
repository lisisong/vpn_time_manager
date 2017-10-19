# coding=utf-8
import time
import os
import httplib
import urllib


def online_report(count):
    params = urllib.urlencode({'count': count})
    headers = {"Content-type": "application/json"}
    conn = httplib.HTTPConnection("127.0.0.1:8080")
    conn.request("POST", "/api/vpn/onlineReport", params, headers)
    response = conn.getresponse()
    return response.status


while True:
    time.sleep(1)
    r = os.popen("ps -ef | grep pppd  | grep ipparam")
    text = r.read()
    count = text.count("plugin")
    online_report(count)
