import time
#将时间戳转换为标准时间格式
def timestamp_to_fomat(timestamp=None,format='%Y-%m-%d %H:%M:%S'):
    #默认返回当前格式化好的时间
    #传入时间戳的话，把时间戳转换成格式化好的时间，返回
    if timestamp:
        time_tuple = time.localtime(timestamp)
        res = time.strftime(format,time_tuple)
    else:
        res = time.strftime(format)#默认读取当前时间
    return res

# 将标准时间转换为时间戳
def strToTimestamp(str=None,format='%Y-%m-%d %H:%M:%S'):
        if str:
            tp = time.strptime(str,format)#转成时间元组
            res = time.mktime(tp)#再转成时间戳
        else:
            res = time.time()#默认获取当前时间戳
        return int(res)
def main():
    print(timestamp_to_fomat())
    print(strToTimestamp('2020-12-12 23:30:00'))
    print(strToTimestamp('2020-12-12 23:30:00'))

if __name__ == '__main__':
    main()
