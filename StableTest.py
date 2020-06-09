import datetime
import configparser
import importlib
import time
import threading
import logging

logger = logging.getLogger('changnwen')
handler = logging.FileHandler('changwen.txt', encoding='utf-8')
logger.addHandler(handler)

config = configparser.ConfigParser()
config.read("test1.ini", encoding="utf-8")
testlist = config.options("test_script")


# 长稳测试
class myThread(threading.Thread):
    module_name = "TePushItemTest1"
    fuc = "main"
    name = "APITest"

    def __init__(self, module_name, fuc, name, id, info, grep):
        threading.Thread.__init__(self)
        self.module_name = module_name
        self.fuc = fuc
        self.name = name
        self.id = id
        self.info = info
        self.grep = grep

    def run(self):
        subpicpath = 'image'
        glo = globals()
        eaitem = importlib.import_module("src.test_script." + self.module_name)
        print("当前请求发送时间:" + str(datetime.datetime.now()))
        t = time.time()
        thisresponse = eval("eaitem." + self.fuc + "(r'D:\!06/' + subpicpath, self.id, self.info, self.grep)")  # 修改参数
        eachTime = round((time.time() - t), 6)
        glo["alltime"][self.name] = glo["alltime"][self.name] + eachTime
        if thisresponse.status_code == 200:
            logger.error(str(datetime.datetime.now()) + ";" + str(thisresponse.status_code) + ";" + str(thisresponse.json()['object_list'][0]['object_id']) + ";" + str(thisresponse.text) + ";" + str(round(eachTime * 1000, 2)))
            print("结束：" + self.name + " 状态：" + str(thisresponse.status_code) + " 用时：" + str(eachTime) + "s   条目：" + str(thisresponse.json()['object_list'][0]['object_id']) + "     结果：" + str(thisresponse.json()["result"]) + "\n")
        else:
            logger.error(str(datetime.datetime.now()) + ";" + str(thisresponse.status_code) + ";NULL;" + str(thisresponse.text) + ";" + str(
                round(eachTime * 1000, 2)))
            print("返回体：" + thisresponse.text)


def test_interface(count, isConcurrent = False):

    glo = globals()
    glo["alltime"] = dict.fromkeys(testlist, 0)
    names = locals()
    index = 0
    imageList = ["71804.jpg", "40018.jpg",   "50013.jpg",   "60014.jpg",   "71403.jpg",
                 "10005.jpg", "9012003.jpg", "9020009.jpg", "9040011.jpg", "9060015.jpg",
                 "90024.jpg", "90002.jpg",   "9150004.jpg"]

    for i in range(count):
        for x in testlist:
            this_m_f = str(config.get("test_script", x)).split(".")
            this_model = this_m_f[0]
            fuc = this_m_f[1]
            for j in range(len(imageList)):

                if imageList[j] == "71804.jpg" or imageList[j] == "40018.jpg" or imageList[j] == "50013.jpg" or imageList[j] == "60014.jpg" or imageList[j] == "90002.jpg" or imageList[j] == "71403.jpg" :
                    info = ""
                    grep = "te"
                if imageList[j] == "9012003.jpg" or imageList[j] == "9020009.jpg" or imageList[j] == "9040011.jpg" or imageList[j] == "9060015.jpg" or imageList[j] == "9150004.jpg":
                    info = ""
                    grep = "ics"
                if imageList[j] == "toolkit.jpg" or imageList[j] == "obd.jpg" or imageList[j] == "Mask.jpg" or imageList[j] == "first_aid_box.jpg" or imageList[j] == "EHS_warning_card.jpg":
                    info = ""
                    grep = "ehs"

                if imageList[j] == "10005.jpg":
                    info = "C32"
                    grep = "te"
                if imageList[j] == "10006.jpg":
                    info = "160A"
                    grep = "te"
                if imageList[j] == "90024.jpg":
                    info = "pgnd"
                    grep = "te"

                print("开始：" + x + "    条目：" + imageList[j])
                names["my_thread" + str(index)] = myThread(this_model, fuc, x, imageList[j], info, grep)
                eval("my_thread" + str(index) + ".start()")
                index += 1
                if isConcurrent == False:
                    time.sleep(5)  # 长稳请求时间间隔设置
    legth = index
    index = 0
    for i in range(legth):
        eval("my_thread" + str(i) + ".join()")
    for x in testlist:
        print("over " + x + " alltime: " + str(round(glo["alltime"][x], 6)) + " s  平均时间： " + str(
            round(glo["alltime"][x] / count, 6)) + " s")


if __name__ == '__main__':
    while True:
        if time.time() < 1607787000:
            test_interface(3, False)  # 长稳请求发送次数设置
