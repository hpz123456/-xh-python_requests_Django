import json
from realize_package.tools.read_write_Excel import operation_Excel
from realize_package.tools.read_write_File import operation_File
from realize_package.tools.read_write_Json import operation_Json

class list_Assert():
    # operation_Excel实例化
    Exel = operation_Excel()
    # 实例化文件写入读取工具
    of = operation_File()
    #实例化json转行工具
    oj = operation_Json()

    # 对比传入的断言，判断断言，并将断言内容，断言结果写入Excel中(tcp：测试用例类，test_return_data：返回值，sheet：当前的sheet，sheet_test_col：首行名称所对应的坐标)
    def list_judge_assert(self, tcp, sheet, sheet_test_col):
        # # 取出模糊查询的数据
        # dim_find = list_assert_dick["dim_find"]
        # # 取出精确查询的数据
        # precise_find = list_assert_dick["precise_find"]
        # # 取出数量
        # num = list_assert_dick["num"]
        # 取出列表断言中的值，并做处理
        list_assert_dick = self.list_assert_data_out()
        #层数
        tier = list_assert_dick["tier"]
        # 取出列表名
        data_name = list_assert_dick["列表名"]
        # 获取列表
        tcp.All_value = []
        tcp.find_key = data_name
        self.oj.assert_Json(r=tcp.test_return_data, model_find=tcp)
        if len(tcp.All_value) < (tier-1):
            self.Exel.write_Excel(sheet=sheet, row=tcp.row, col=sheet_test_col["列表断言结果"], content="失败")
            return
        #取出列表
        list_data = tcp.All_value[tier-1]
        #判断成功还是失败
        is_succeed = self.juder(list_data = list_data,list_assert_dick=list_assert_dick)
        #结果写入
        self.write_Excel(tcp=tcp,list_data=list_data,is_succeed=is_succeed,sheet=sheet,sheet_test_col=sheet_test_col)

    def write_Excel(self,tcp,list_data,is_succeed,sheet,sheet_test_col):
        # 将返回断言值放入测试用例对象中
        tcp.test_return_list_assert = list_data
        # 将返回的断言值写入返回断言值文件中
        self.of.write_File(file_name="return_List_Assert_Json.json", write_let=list_data)
        # 将列表返回值写入Excel中
        self.Exel.write_Excel(sheet=sheet, row=tcp.row, col=sheet_test_col["列表断言获取值"], content=str(list_data))
        # 将断言结果写入Excel中
        self.Exel.write_Excel(sheet=sheet, row=tcp.row, col=sheet_test_col["列表断言结果"], content=is_succeed)

    # 判断断言成功还是失败
    def juder(self,list_data,list_assert_dick):
        is_succeed = "失败"
        # 取出模糊查询的数据
        dim_find = list_assert_dick["dim_find"]
        # 取出精确查询的数据
        precise_find = list_assert_dick["precise_find"]
        # 取出列表名
        data_name = list_assert_dick["列表名"]
        # 取出数量
        num = list_assert_dick["num"]
        # 层数
        tier = list_assert_dick["tier"]
        #交并
        intersection_or_union = list_assert_dick["交并"]
        jp = self.juder_precise(list_data=list_data, precise_find=precise_find)
        jd = self.juder_dim(list_data=list_data, dim_find=dim_find)
        jn = self.juder_num(list_data=list_data, num=num)
        if jn:
            return is_succeed
        if self.juder_key(self,list_data=list_data, precise_find=precise_find, dim_find=dim_find):
            return is_succeed
        if intersection_or_union == "交":
            if jp and jd:
                is_succeed = "成功"
                return is_succeed
        elif intersection_or_union == "并":
            if self.juder_union(list_data=list_data,precise_find=precise_find,dim_find=dim_find):
                is_succeed = "成功"
                return is_succeed

        return is_succeed

    #key值判断
    def juder_key(self,list_data,precise_find,dim_find):
        precise_dim = []
        for pf in precise_find:
            precise_dim.append(pf)
        for df in dim_find:
            precise_dim.append(df)

        for pd in precise_dim:
            is_succeed = False
            for ld in list_data:
                for l in ld:
                    if pd == l:
                        is_succeed = True
                        break
                if is_succeed == False:
                    return is_succeed
        return True


    #并集判断
    def juder_union(self,list_data,precise_find,dim_find):
        for ld in list_data:
            for pf in precise_find:
                if precise_find[pf] != ld[pf]:
                    return False
            for df in dim_find:
                if precise_find[df] not in precise_find[df]:
                    return False
        return True




    #精确判断成功还是失败
    def juder_precise(self,list_data,precise_find):
        if precise_find == {}:
            return True
        for pf in precise_find:
            for ld in list_data:
                if ld[pf] != precise_find[pf]:
                    return False
        return True

    # 模糊判断成功还是失败
    def juder_dim(self, list_data, dim_find):
        if dim_find == {}:
            return True
        for pf in dim_find:
            for ld in list_data:
                if ld[pf] not in dim_find[pf]:
                    return False
        return True

    #数量判断成功还是失败
    def juder_num(self,list_data,num):
        if num == -1:
            return True
        if len(list_data) != num:
            return False
        return True


    # 取出列表断言中的值，并做处理（return：list_assert_dick：num(num),交并(交并)，dim_find(模糊查询),precise_find(精确查询)）
    def list_assert_data_out(self):
        # 取出列表断言文件中的内容
        list_assert_Json = self.of.read_File(file_name="list_assert_Json.json")
        # 断言内容转换为JSON格式
        list_assert_Json = self.oj.read_Json(test_Json=list_assert_Json, Json_name="断言列表")

        # 列表查询的dick调整后的dick
        list_assert_dick = {}

        # 获取num”，“交并”，“模糊查询”的值
        list_assert_dick["num"] = list_assert_Json["num"]
        list_assert_dick["交并"] = list_assert_Json["交并"]
        list_assert_dick["列表名"] = list_assert_Json["列表名"]
        list_assert_dick["tier"] = list_assert_Json["tier"]
        # 需要模糊查询的值
        fuzzy_query = list_assert_Json["模糊查询"]
        # 将需要模糊查询的值转换为list
        fuzzy_query_list = fuzzy_query.split(",")
        # 获取需要查询的值
        dim_find = {}  # 模糊查询
        precise_find = {}  # 精确查询
        # 将模糊查询的值和精确查询的值分开
        for laj in list_assert_Json:
            if laj != "num" and laj != "交并" and laj != "模糊查询" and laj != "列表名" and laj != "tier":
                i = 0
                for fql in fuzzy_query_list:
                    if fql == laj:
                        dim_find[laj] = list_assert_Json[laj]
                        break
                    i = i + 1
                    if i == len(fuzzy_query_list):
                        precise_find[laj] = list_assert_Json[laj]
        # 将模糊查询和精确查询装入dick中
        list_assert_dick["dim_find"] = dim_find
        list_assert_dick["precise_find"] = precise_find
        return list_assert_dick
