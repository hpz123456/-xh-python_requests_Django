#接受文件并做处理
import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = curPath[:curPath.find("InterfaceAutomationTest\\")+len("InterfaceAutomationTest\\")]  # 获取myProject，也就是项目的根路径
import sys
rootPath = ""
for i in (sys.path[0].split("\\")):
    rootPath = rootPath + i + "/"
    if i == "InterfaceAutomationTest":
        break
import uuid

class file_handing():

    Files_Path = "realize_package/File_data/"

    def stored_File(self,file_obj):
        order_number = str(uuid.uuid1()).upper().replace('-', '')
        file_name = order_number + file_obj.name
        file_path = rootPath + self.Files_Path
        file_path_name = file_path + "/" + file_name
        f = open(file_path_name, 'wb')
        for chunk in file_obj.chunks(1024):
            f.write(chunk)
        f.close()
        fp = file_path + file_name
        file_path_name = {
            "file_path":fp,
            "file_name":file_name,
            "abbreviation":file_obj.name
        }
        return file_path_name