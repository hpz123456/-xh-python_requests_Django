from realize_package.tools.read_write_Excel import operation_Excel
from realize_package.tools.read_write_Json import operation_Json
from realize_package.tools.read_write_File import operation_File

#普通断言
class c_assert():
    # operation_Excel实例化
    Exel = operation_Excel()
    #实例化文件写入读取工具
    of = operation_File()
    #实例化json转行工具
    oj = operation_Json()
    # 对比传入的断言，判断断言，并将断言内容，断言结果写入Excel中(tcp：测试用例类，test_return_data：返回值，sheet：当前的sheet，sheet_test_col：首行名称所对应的坐标)
    def judge_assert(self, tcp, test_return_data, sheet, sheet_test_col):
        # 取出断言文件中的内容
        assert_Json = self.of.read_File(file_name="assert_Json.json")
        if assert_Json == "":
            return None
        # 断言内容转换为JSON格式
        assert_Json = self.oj.read_Json(test_Json=assert_Json, Json_name="断言")
        # 将返回参数转换为JSON格式
        # print("返回值：" + test_return_data.text)
        # test_return_data1 = json.loads(test_return_data.text)
        # 将返回值装进字典集合中
        test_return_assert = {}
        is_succeed = "成功"
        # 循环断言的每个值，并作出判断
        for assert_key in assert_Json:
            tcp.find_key = assert_key
            self.oj.assert_Json(r=tcp.test_return_data, model_find=tcp)
            # 将返回的断言对应打的值放入字典中
            test_return_assert[assert_key] = tcp.All_value[0]
            # print("123:" + assert_Json[assert_key])
            # print("123:" + tcp.All_value[0])
            if assert_Json[assert_key] != tcp.All_value[0]:
                is_succeed = "失败"
        # 将返回断言值放入测试用例对象中
        tcp.test_return_assert = test_return_assert
        # 将返回的断言值写入返回断言值文件中
        self.of.write_File(file_name="return_Assert_Json.json", write_let=test_return_assert)
        # 将返回值写入Excel中
        self.Exel.write_Excel(sheet=sheet, row=tcp.row, col=sheet_test_col["断言的获取值"], content=str(test_return_assert))
        # 将断言结果写入Excel中
        self.Exel.write_Excel(sheet=sheet, row=tcp.row, col=sheet_test_col["断言结果"], content=is_succeed)
