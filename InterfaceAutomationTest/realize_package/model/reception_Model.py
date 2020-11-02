#测试用例属性

class test_Case_Property():

    #测试编号
    test_id = None

    #url
    test_url = None

    #请求方式
    test_request_way = None

    #header请求头
    test_header = None

    #param请求参数
    test_param = None

    #入参数据
    test_data = None

    #cookie
    test_cookie = None

    #返参数据
    test_return_data = None

    #断言
    test_assert = None

    #返回断言
    test_return_assert = None

    #断言结果
    test_assert_result = None

    #列表断言
    test_list_assert = None

    #列表断言结果
    test_list_assert_result = None

    #列表断言返回值
    test_return_list_assert = None

    #列表查询时列表的个数
    list_num = 0

    # 需要查询的key
    find_key = ""

    # 将需要查询的value封装成集合
    All_value = []

    #该条测试用例的行
    row = 0

    def dy(self):
        print(self.test_id)
        print(self.test_url)
        print(self.test_request_way)
        print(self.test_header)
        print(self.test_param)
        print(self.test_data)
        print(self.test_cookie)
        print(self.test_return_data)
        print(self.test_assert)
        print(self.test_return_assert)
        print(self.test_assert_result)
        print(self.test_list_assert)
        print(self.test_list_assert_result)
        print(self.list_num)
        print(self.find_key)
        print(self.All_value)
        print(self.row)