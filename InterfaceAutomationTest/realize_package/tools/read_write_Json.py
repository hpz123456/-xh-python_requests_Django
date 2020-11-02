#操作json文件

import json
from realize_package.tools import read_write_File
from realize_package.model import reception_Model
#操作Json
class operation_Json():

    #将字符串变成json
    def read_Json(self,test_Json,Json_name):
        exection = Json_name + "不是json格式"
        try:
            return_Json = json.loads(test_Json)
        except:
            return exection

        return return_Json

    #json断言
    # 此方法通过key，找出所有key的value（r:传入的json  key_value:封装对象）
    def assert_Json(self,r,model_find):

        #将传入的json强转为list
        list_key = (list)(r.keys())
        #遍历list_key
        for i in list_key:
            a = r
            #查找list_key中需要查找的key（精确）
            if i == model_find.find_key:
                #如果有一个查找key，num就+1
                model_find.list_num = model_find.list_num + 1
                #如果有查找key，就将其value装进key_value
                model_find.All_value.append(r.get(i))

            #判断list_key中的dick的value的类型是否为dick
            if isinstance(r.get(i), dict):
                #如果是，就递归，将value进行遍历，继续查找key所对应打的value，并将key_value一起带入
                operation_Json().assert_Json(r = r.get(i),model_find = model_find)

            #判断list_key中的dick的value的类型是否为list
            if isinstance(r.get(i), list):
                #如果是，就将value传入Find_List进行遍历
                operation_Json().Find_List(List=r.get(i),model_find = model_find)

        return model_find

    #查询list中的dick
    def Find_List(self,List,model_find):
        #遍历传进来的list
        for i in List:
            #判断list中的值是否为dick（一般情况下，都为dick，因为是json类型）
            if isinstance(i, dict):
                #如果为dick，就将值传入All_Key_Value，进行key和value的查找
                operation_Json().assert_Json(r=i,model_find = model_find)

# if __name__ == '__main__':
#      a = "article_add.json"
#      b = read_write_File.operation_File().read_File(file_name=a)
#      # print(b)
#      c = operation_Json().read_Json(test_Json=b,Json_name="cookie")
#      # operation_Json().assert_Json(r=c,key_value="title")
#      print(c)
#      model = reception_Model.test_Case_Property()
#      model.test_data = b
#      model.find_key = "title"
#      operation_Json().assert_Json(r=c, model_find=model)
#      print(model.All_value)
#      print(model.list_num)