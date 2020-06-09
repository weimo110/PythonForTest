import csv
import xlwt

c_path = r"C:\Users\wwx879828\Desktop\changwen.txt"
x_path = r"C:\Users\wwx879828\Desktop\长稳.xls"

def csv_to_xlsx():
    with open(c_path, 'r', encoding='utf-8') as f:
        read = csv.reader(f, delimiter=";")
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')  # 创建一个sheet表格
        l = 0
        for line in read:
            print(line)
            r = 0
            for i in line:
                print(i)
                sheet.write(l, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            l = l + 1

        workbook.save(x_path)  # 保存Excel



if __name__ == '__main__':
    csv_to_xlsx()
