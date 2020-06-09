# -*- coding: utf-8 -*-#

# 脚本功能：实现指定文件夹下图片转化为base64编码
# 脚本增加点：转化base64文件名称为图像名称+“_base64.txt”,更具备识别性
# 参数介绍：
# _imagePath #图片路径
# _imageBasePath = #图片base64之后的结果路径


import os, base64

# 图片路径
_imagePath = r"C:\Users\\Desktop\image\image"

# 图片base64之后的路径
_imageBasePath = r"C:\Users\Desktop\base64"

def getImage():
    # 获取指定路径下文件列表
    fileNameList = os.listdir(_imagePath)
    print("fileNameList:%s" % fileNameList)

    return fileNameList


def encodeImage(fileNameList):
    i = 0
    for image in fileNameList:
        # print(image)
        image_path = os.path.join(_imagePath, image)
        # print(image.split("."))
        with open(image_path, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            s = base64_data.decode()

        generateFile = open(os.path.join(_imageBasePath, image.split(".")[0]) + ".txt", 'w')
        generateFile.write(s)
        generateFile.close()
        i += 1
    print("图片个数：%s" % i)


def main():
    fileNameList = getImage()
    encodeImage(fileNameList)


if __name__ == '__main__':
    main()
