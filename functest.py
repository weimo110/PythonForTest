import datetime
import configparser
import importlib
import time
import threading
import requests
import os
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

config = configparser.ConfigParser()
# config.read("test.ini", encoding="utf-8")
testlist = config.options("test_script")


class myThread(threading.Thread):
    module_name = ""
    fuc = ""
    name = ""
    token = ""

    def __init__(self, module_name, fuc, name, token):
        threading.Thread.__init__(self)
        self.module_name = module_name
        self.fuc = fuc
        self.name = name
        self.token = token

    def run(self):
        glo = globals()
        eaitem = importlib.import_module("src.test_script." + self.module_name)
        token = self.token
        # object_id = get_objectid(picpath, filename)
        # base64_data = get_base64_data(picpath, filename)
        # print(object_id)
        # print(token)
        t = time.time()
        thisresponse = eval("eaitem." + self.fuc + "(token)")
        eachTime = round((time.time() - t), 6)
        glo["alltime"][self.name] = glo["alltime"][self.name] + eachTime
        if thisresponse.status_code == 200:
            print("用时：" + str(eachTime) + "   " + str(thisresponse.text))
            # print("成功：" + self.name + "   状态：" + str(thisresponse.status_code) + "   用时：" + str(eachTime) + "s   条目：" + str(thisresponse.json()['object_list'][0]['object_id']) + "     结果：" + str(thisresponse.json()["result"]) + "   数量：" + str(thisresponse.json()['object_list'][0]['num']) + "\n")
        else:
            print("用时：" + str(eachTime) + "   " + str(thisresponse.text))
            # print("失败：" + self.name + "   状态：" + str(thisresponse.status_code) + "   用时：" + str(eachTime) + "s" + "\n")

def test_interface(count, isConcurrent = False):
    glo = globals()
    glo["alltime"] = dict.fromkeys(testlist, 0)
    names = locals()
    index = 0
    mid_time = 60 / (count)

    # print("开始发送请求时间：" + str(curr_time))
    for i in range(count):
        for x in testlist:
            this_m_f = str(config.get("test_script", x)).split(".")
            this_model = this_m_f[0]
            fuc = this_m_f[1]
            curr_time = datetime.datetime.now()
            print(str(curr_time) + "    请求+1")
            names["my_thread" + str(index)] = myThread(this_model, fuc, x, get_token())
            eval("my_thread" + str(index) + ".start()")
            index += 1
            if isConcurrent == False:
                time.sleep(mid_time)
    len = index
    index = 0
    for i in range(len):
        eval("my_thread" + str(i) + ".join()")
    for x in testlist:
        print("总时间: " + str(round(glo["alltime"][x], 6)) + " s  平均时间： " + str(
                round(glo["alltime"][x] / (count), 6)) + " s")

def get_token():
    url = 'https://10.137.106.120:8343/v1/apigw/oauth2/token'
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'client_credentials',
        # qcheck
        # 'client_id': '',
        # 'client_secret': '',
        'client_id': '',
        'client_secret': '',
        'scope': 'default',
    }
    resp = requests.post(url, headers=headers, data=data, verify=False)
    return resp.json()["access_token"]


if __name__ == '__main__':
    test_interface(10,  False)
