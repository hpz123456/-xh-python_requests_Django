#调用接口
import requests

class test_request():

    #测试post请求
    def test_post_get_deleter(self,url,request_way,cookies=None,header = None,data = None,params=None):

        if cookies == "" :
            cookies = None
        if header == "" :
            header = None
        if data == "" :
            data = None
        if params == "" :
            params = None

        # print(url)
        # print(request_way)
        # print(cookies)
        # print(header)
        # print(data)
        # print(params)

        #返回值
        return_data = None
        #如果请求有误，就将抛出的异常返回
        try:
            if request_way == "POST":
                return_data = requests.post(url=url,cookies=cookies,headers=header,data=data,params=params)
            elif request_way == "GET":
                return_data = requests.get(url=url, cookies=cookies, headers=header, data=data,params=params)
            elif request_way == "DELETER":
                return_data = requests.delete(url=url, cookies=cookies, headers=header, data=data,params=params)
        except Exception as e:
            return e
        #如果没有异常，就将返回的值传出去
        return return_data

if __name__ == '__main__':
    url = "tp://ttapi.research.itcast.cn/app/v1_0/authorizations"
    request_way = "POST"
    data = {"mobile":"18827024423","code":"888888"}
    header = {"Content-Type":"application/json"}
    aaa = test_request().test_post_get_deleter(url=url,request_way=request_way,header=header,data=data)
    bbb = isinstance(aaa, requests.models.Response)
    print(123 == False)
    print(bbb)
    print(type(str(aaa)))
    print(aaa)