import json
from realize_package.tools.read_write_Excel import operation_Excel
from realize_package.tools.read_write_File import operation_File


#返回值写入类
class write_Return_Value():
    # operation_Excel实例化
    Exel = operation_Excel()
    # 实例化文件写入读取工具
    of = operation_File()
    # 获取返回值并写入文件及Excel(tcp：测试用例类，test_return_data：返回值，sheet：当前的sheet，sheet_test_col：首行名称所对应的坐标)
    def operation_Return_Parameter(self, tcp, test_return_data, sheet, sheet_test_col):
        # 将返回值放入测试用例对象中
        tcp.test_return_data = json.loads(test_return_data.text)
        # 将返回值写入返回值文件中
        self.of.write_File(file_name="return_Data_Json.json", write_let=tcp.test_return_data)
        # 将返回值写入Excel中
        self.Exel.write_Excel(sheet=sheet, row=tcp.row, col=sheet_test_col["返回参数"], content=tcp.test_return_data)

    # 如果请求接口抛出异常，就将异常写入Excel中
    def over_Return_Parameter(self, tcp, test_return_data, sheet, sheet_test_col):
        # 将返回值放入测试用例对象中
        tcp.test_return_data = str(test_return_data)
        # 将返回值写入返回值文件中
        self.of.write_File(file_name="return_Data_Json.json", write_let=tcp.test_return_data)
        # 将返回值写入Excel中
        self.Exel.write_Excel(sheet=sheet, row=tcp.row, col=sheet_test_col["返回参数"], content=tcp.test_return_data)

