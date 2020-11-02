
from realize_package.API_request.reception_File import file_handing
from realize_package.tools.read_write_Excel import operation_Excel
from realize_package.model.reception_Model import test_Case_Property
from realize_package.tools.read_write_File import operation_File
from realize_package.tools.read_write_Json import operation_Json
from realize_package.API_request.test_Request_Way import test_request
from Interface_Integration.service import write_return_value
from Interface_Integration.service import common_assert
from Interface_Integration.service import business_dispose
from Interface_Integration.service import list_assert
import json
import requests
from apscheduler.scheduler import Scheduler
class realize_File():

    # operation_Excel实例化
    Exel = operation_Excel()
    #实例化文件写入读取工具
    of = operation_File()
    #实例化json转行工具
    oj = operation_Json()
    #实例化接口请求工具
    tr = test_request()
    #返回值写入类
    wrv = write_return_value.write_Return_Value()
    #普通断言
    ca = common_assert.c_assert()
    #业务处理类
    bd = business_dispose.business_Dispose()
    #列表断言处理
    la = list_assert.list_Assert()

    #操作测试用例，并返回值
    def Test_Case_Integration(self,test_Case_File):
        #将文件存入，并获取文件路径
        file_path_name = file_handing().stored_File(file_obj=test_Case_File)
        file_path = file_path_name["file_path"]
        file_name = file_path_name["file_name"]
        abbreviation = file_path_name["abbreviation"]
        #临时地址
        # file_path = "C:/Users/lx/Desktop/接口自动化/InterfaceAutomationTest/realize_package/File_data/A2BF350697F411EA89F0005056C00008接口自动化测试用例.xlsx"
        #打开Excel文件
        Excle_File = self.Exel.open_Excel(file_path=file_path)
        # 获取"是否执行"sheet页的用例条数
        Y_sheet_list = self.sheet_execute(Excle_File = Excle_File)
        # print(Y_sheet_list[0])
        #获取当前执行的sheet页的用例
        self.test_case_sheet(Excle_File=Excle_File,Y_sheet_list=Y_sheet_list)
        #保存文件
        self.Exel.save_File(Excle_File=Excle_File,file_path=file_path)
        #关闭文件
        # self.Exel.clos_Excel(Excle_File=Excle_File)
        #将文件转移到定期清理的文件夹
        file_new_path = self.of.copy(old_file_paht=file_path, file_name=file_name)
        #需要返回的文件信息
        return_file = {
            "file":self.of.file_iterator(file_name=file_name),
            "abbreviation":abbreviation,
            "file_name":file_name,
            "file_path":file_path,
            "file_new_path":file_new_path
        }
        #删除文件
        self.of.remove_file(file_name=file_name)
        return return_file

    #"是否执行"sheet页
    def sheet_execute(self,Excle_File):
        #获取“是否执行”的sheet文件
        sheet = self.Exel.get_sheet(Excle_File=Excle_File,sheet_name="是否执行")
        #获取文件的最大行和最大列
        row_col = self.Exel.all_Information(sheet=sheet)

        #获取首行所有名称
        Excel_list_row = self.Exel.get_fiest_line(sheet=sheet,max_col=row_col["max_columns"])

        #找出“执行”的列
        for i in Excel_list_row:
            if i.first_line_name == "执行":
                sheet_zx_col = i.col
        #获取"执行"的一列数据
        Excel_list_col = self.Exel.get_All_row(sheet=sheet,max_row=row_col["max_row"],col=sheet_zx_col)

        Y_sheet_list = []
        #获取”Y“所对应的sheet名称
        for i in Excel_list_col:
            if i.first_line_name == "Y":
                self.Exel.read_one_cell(sheet=sheet,row=i.row,col=i.col).value
                Y_sheet_list.append(self.Exel.read_one_cell(sheet=sheet,row=i.row,col=i.col-1).value)
        #将所有“执行”为“Y”的sheet名字返回
        return Y_sheet_list

    #测试用例sheet执行
    def test_case_sheet(self,Excle_File,Y_sheet_list):



        for Ysl in Y_sheet_list:
            # 循环所有的”执行“为”Y“的sheet
            inerease_row = 2
            # test_Case_Property集合
            tcp_list = []
            # 获取测试用例的sheet文件
            sheet = self.Exel.get_sheet(Excle_File=Excle_File, sheet_name=Ysl)
            # 获取文件的最大行和最大列
            row_col = self.Exel.all_Information(sheet=sheet)
            Excel_list_row = self.Exel.get_fiest_line(sheet=sheet, max_col=row_col["max_columns"])

            # 找出当前用例中入参所对应的列
            sheet_test_col = self.bd.get_first_line_r_c(Excel_list_row=Excel_list_row)

            #循环所有的测试用例并放入tcp中
            while inerease_row <=  row_col["max_row"]:
                # test_Case_Propert实例化
                tcp = test_Case_Property()
                # 测试编号
                tcp.test_id = None
                # url
                tcp.test_url = None
                # 请求方式
                tcp.test_request_way = None
                # header请求头
                tcp.test_header = None
                # param请求参数
                tcp.test_param = None
                # 入参数据
                tcp.test_data = None
                # cookie
                tcp.test_cookie = None
                # 返参数据
                tcp.test_return_data = None
                # 断言
                tcp.test_assert = None
                # 返回断言
                tcp.test_return_assert = None
                # 断言结果
                tcp.test_assert_result = None
                # 列表断言
                tcp.test_list_assert = None
                # 列表断言结果
                tcp.test_list_assert_result = None
                #列表断言获取值
                tcp.test_return_list_assert = None
                # 列表查询时列表的个数
                tcp.list_num = 0
                # 需要查询的key
                tcp.find_key = ""
                # 将需要查询的value封装成集合
                tcp.All_value = []
                # 该条测试用例的行
                tcp.row = 0


                #将当前行数放入测试用例中
                tcp.row = inerease_row
                #传值
                self.bd.test_Case_Property_by_value(sheet=sheet,inerease_row=inerease_row,sheet_test_col=sheet_test_col,tcp=tcp)
                tcp_list.append(tcp)
                inerease_row = inerease_row+1
            self.calling_Interface(tcp_list=tcp_list,sheet=sheet,sheet_test_col=sheet_test_col)

    #执行测试用例，调用接口
    def calling_Interface(self,tcp_list,sheet,sheet_test_col):
        for tcp in tcp_list:
            #将值存入文件中
            self.bd.in_parameter_write(tcp)
            #获取文件里面的值
            all_in_parameter = self.bd.get_File()
            #调用接口请求方法
            test_return_data = self.tr.test_post_get_deleter(
                url=tcp.test_url,
                request_way=tcp.test_request_way,
                cookies=all_in_parameter["cookie_Json"],
                header=all_in_parameter["header_Json"],
                data=all_in_parameter["data_Json"],
                params=all_in_parameter["param_Json"]
            )
            return_data_type = isinstance(test_return_data, requests.models.Response)
            if return_data_type == False:
                self.wrv.over_Return_Parameter(tcp=tcp,test_return_data=test_return_data,sheet=sheet,sheet_test_col=sheet_test_col)
                continue
            # 获取返回值并写入文件及Excel
            self.wrv.operation_Return_Parameter(tcp=tcp,test_return_data=test_return_data,sheet=sheet,sheet_test_col=sheet_test_col)
            # 对比传入的断言，判断断言，并将断言内容，断言结果写入Excel中
            self.ca.judge_assert(tcp=tcp,test_return_data=test_return_data,sheet=sheet,sheet_test_col=sheet_test_col)
            #列表断言
            self.la.list_judge_assert(tcp=tcp,sheet=sheet,sheet_test_col=sheet_test_col)


    #定时删除文件
    def remover_File(self):
        self.of.remover_scratch_File()


if __name__ == '__main__':
    realize_File().Test_Case_Integration(test_Case_File=123)
    # realize_File().get_File()
    #{"message": "The browser (or proxy) sent a request that this server could not understand."}
    #{'message': ['The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.', 'The browser (or proxy) sent a request that this server could not understand.']}
    #{'message': ['The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.', 'The browser (or proxy) sent a request that this server could not understand.']}