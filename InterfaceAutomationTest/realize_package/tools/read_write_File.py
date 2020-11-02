# coding=UTF-8
#读取和写入File
from shutil import copyfile
import os
import time
import datetime
import sys
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = curPath[:curPath.find("InterfaceAutomationTest\\")+len("InterfaceAutomationTest\\")]  # 获取myProject，也就是项目的根路径
rootPath = ""
for i in (sys.path[0].split("\\")):
    rootPath = rootPath + i + "/"
    if i == "InterfaceAutomationTest":
        break

class operation_File():

    Files_Path = "realize_package/File_data/"

    # def bbb(self):
    #     path = ""
    #     for i in (sys.path[0].split("\\")):
    #         rootPath = rootPath + i + "/"
    #         if i == "InterfaceAutomationTest":
    #             break

    #读取文件
    def read_File(self,file_name):
        file_path = rootPath + self.Files_Path + file_name

        # print(file_path)
        # read_file_text = open(file_path,"r")

        with open(file_path, "r", encoding="UTF-8") as f:
            return f.read()

    def file_iterator(self,file_name, chunk_size=512):  # 用于形成二进制数据
        file_path = rootPath + self.Files_Path + file_name
        with open(file_path, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break



    #写入文件
    def write_File(self,file_name,write_let):
        file_path = rootPath + self.Files_Path + file_name
        #如果当前参数为空，清除文件内容
        if write_let == None:
            open(file_path, "r+").truncate()
        else:
            with open(file_path, 'w', encoding="UTF-8") as file_object:
                file_object.write(str(write_let))

    #删除文件
    def remove_file(self,file_name):
        file_path = rootPath + self.Files_Path + file_name
        os.remove(file_path)
    #文件复制
    def copy(self,old_file_paht,file_name):
        new_paht = "realize_package/remover_File/"
        file_path = rootPath + new_paht + file_name
        # print(old_file_paht)
        # print(c)
        copyfile(old_file_paht, file_path)
        return file_path

    def remover_scratch_File(self):
        # print(123)
        #删除文件的文件夹地址
        new_paht = "realize_package/remover_File/"
        file_path = rootPath + new_paht
        #获取文件夹名称
        All_File_Nmae = os.listdir(file_path)
        #如果文件夹不为空，就执行删除
        if len(All_File_Nmae) != 0:
            #遍历当前文件名称
            for file_name in All_File_Nmae:
                #文件名称拼接
                present_file = file_path + file_name
                #获取文件创建时间
                present_file_time = time.localtime(os.stat(present_file).st_mtime)
                #文件创建时间格式化
                file_time = time.strftime("%Y-%m-%d %H:%M:%S", present_file_time)
                #获取少于当前时间10秒钟的时间
                reduce_time = self.reduce_time()
                # print()
                #判断文件创建时间是否下雨当前时间10秒前
                if file_time < reduce_time:
                    os.remove(present_file)


    def reduce_time(self):
        today = datetime.datetime.now()
        # 计算偏移量
        offset = datetime.timedelta(seconds=-5)
        # 获取修改后的时间并格式化
        re_date = (today + offset).strftime('%Y-%m-%d %H:%M:%S')
        return re_date



if __name__ == '__main__':
#     a = "article_add.json"
#     b = operation_File().read_File(file_name=a)
#     print(b)
#     a = "article_Json.json"
#     operation_File().write_File(file_name=a,write_let=b)
    print(rootPath)
    path = ""
    for i in (sys.path[0].split("\\")):
        path = path + i+ "/"
        if i == "InterfaceAutomationTest":
            break
    print(path)