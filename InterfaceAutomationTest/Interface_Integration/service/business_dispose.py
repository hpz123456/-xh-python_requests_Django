from realize_package.tools.read_write_Excel import operation_Excel
from realize_package.tools.read_write_Json import operation_Json
from realize_package.tools.read_write_File import operation_File

class business_Dispose():
    # operation_Excel实例化
    Exel = operation_Excel()
    #实例化文件写入读取工具
    of = operation_File()
    #实例化json转行工具
    oj = operation_Json()
    #将入参写入文件
    def in_parameter_write(self,tcp):
        self.of.write_File(file_name="header_Json.json",write_let=tcp.test_header)
        self.of.write_File(file_name="param_Json.json", write_let=tcp.test_param)
        self.of.write_File(file_name="data_Json.json",write_let=tcp.test_data)
        self.of.write_File(file_name="cookie_Json.json",write_let=tcp.test_cookie)
        self.of.write_File(file_name="assert_Json.json",write_let=tcp.test_assert)
        self.of.write_File(file_name="list_assert_Json.json", write_let=tcp.test_list_assert)
        #列表断言，暂时不实现
        # of.write_File(file_name="cookie_Json.json",write_let=tcp.test_list_assert)


    #test_Case_Property传值（sheet:sheet页面，inerease_row:行，sheet_test_col:列的集合（dick））
    def test_Case_Property_by_value(self,sheet,inerease_row,sheet_test_col,tcp):
        tcp.test_id = self.Exel.read_one_cell(sheet=sheet, row=inerease_row, col=sheet_test_col["用例编号(不可为空，不可重复)"]).value
        tcp.test_url = self.Exel.read_one_cell(sheet=sheet, row=inerease_row, col=sheet_test_col["url"]).value
        tcp.test_request_way = self.Exel.read_one_cell(sheet=sheet, row=inerease_row, col=sheet_test_col["请求方式"]).value
        tcp.test_header = self.Exel.read_one_cell(sheet=sheet, row=inerease_row, col=sheet_test_col["header请求头"]).value
        tcp.test_param = self.Exel.read_one_cell(sheet=sheet, row=inerease_row, col=sheet_test_col["param请求参数"]).value
        tcp.test_data = self.Exel.read_one_cell(sheet=sheet, row=inerease_row, col=sheet_test_col["入参数据"]).value
        tcp.test_cookie = self.Exel.read_one_cell(sheet=sheet, row=inerease_row, col=sheet_test_col["cookie"]).value
        tcp.test_assert = self.Exel.read_one_cell(sheet=sheet, row=inerease_row, col=sheet_test_col["断言"]).value
        tcp.test_list_assert = self.Exel.read_one_cell(sheet=sheet, row=inerease_row, col=sheet_test_col["列表断言"]).value



    #获取文件
    def get_File(self):
        #入参文件值的集合
        all_in_parameter = {}
        #获取需要的文件，并读取文件的值
        header_Json = self.of.read_File(file_name="header_Json.json")
        param_Json = self.of.read_File(file_name="param_Json.json")
        data_Json = self.of.read_File(file_name="data_Json.json")
        cookie_Json = self.of.read_File(file_name="cookie_Json.json")
        assert_Json = self.of.read_File(file_name="assert_Json.json")

        #如果文件里面有内容，就转为json，如果没有，就不转换
        if header_Json != "" and header_Json != None :
            header_Json = self.oj.read_Json(Json_name="header",test_Json=header_Json)
        if param_Json != "" and param_Json != None :
            param_Json = self.oj.read_Json(Json_name="param",test_Json=param_Json)
        if data_Json != "" and data_Json != None :
            data_Json = self.oj.read_Json(Json_name="data",test_Json=data_Json)
        if cookie_Json != "" and cookie_Json != None :
            cookie_Json = self.oj.read_Json(Json_name="cookie",test_Json=cookie_Json)
        if assert_Json != "" and assert_Json != None :
            assert_Json = self.oj.read_Json(Json_name="assert",test_Json=assert_Json)
        #将转换后的数据存入集合
        all_in_parameter["header_Json"] = header_Json
        all_in_parameter["param_Json"] = param_Json
        all_in_parameter["data_Json"] = data_Json
        all_in_parameter["cookie_Json"] = cookie_Json
        all_in_parameter["assert_Json"] = assert_Json


        return all_in_parameter


    # 获取首行需要的坐标值
    def get_first_line_r_c(self, Excel_list_row):
        # 入参数据取出
        need_find_name = []
        need_find_name.append("用例编号(不可为空，不可重复)")
        need_find_name.append("url")
        need_find_name.append("请求方式")
        need_find_name.append("header请求头")
        need_find_name.append("param请求参数")
        need_find_name.append("入参数据")
        need_find_name.append("cookie")
        need_find_name.append("断言")
        need_find_name.append("列表断言")
        # 返参数据取出
        need_find_name.append("返回参数")
        need_find_name.append("断言的获取值")
        need_find_name.append("断言结果")
        need_find_name.append("列表断言结果")
        need_find_name.append("列表断言获取值")

        # 找出当前用例中入参所对应的列
        sheet_test_col = {}
        for k in need_find_name:
            for i in Excel_list_row:
                if i.first_line_name == k:
                    sheet_test_col[k] = i.col

        return sheet_test_col