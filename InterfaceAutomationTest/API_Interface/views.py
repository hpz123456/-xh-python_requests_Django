from django.shortcuts import render
from django.shortcuts import HttpResponse
from Interface_Integration.service.realize import realize_File
from django.utils.encoding import escape_uri_path
from django.http import HttpResponse,HttpResponseRedirect
import sys
rootPath = ""
for i in (sys.path[0].split("\\")):
    rootPath = rootPath + i + "/"
    if i == "InterfaceAutomationTest":
        break

from django.http import FileResponse
# Create your views here.


def index(request):
    return HttpResponse('Hello World')

def index1(request):
    print("准备")
    return render(request,"index.html")

def entrance(request):
    print("入口")
    return render(request,"entrance.html")

def receive_file(request):
    print("开始")
    if request.method == 'POST':# 获取对象
        test_Case_File = request.FILES.get('test_case')
        if test_Case_File == None:
            # return render(request,"entrance.html")
            return HttpResponseRedirect('/entrance')
        # 将文件传入实现层
        return_file = realize_File().Test_Case_Integration(test_Case_File=test_Case_File)
        abbreviation = return_file["abbreviation"]
        file_new_path = return_file["file_new_path"]

    file = open(file_new_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(abbreviation))
    return response

def instructions(request):
    print("使用说明")
    Files_Path = "realize_package/tool_File/"
    file_name = "使用说明.docx"
    file_specification_path = rootPath + Files_Path + file_name
    file = open(file_specification_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
    return response

def test_test_case(request):
    print("测试文件")
    Files_Path = "realize_package/tool_File/"
    file_name = "接口自动化测试用例_测试.xlsx"
    file_specification_path = rootPath + Files_Path + file_name
    file = open(file_specification_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
    return response



def aaa():
    realize_File().remover_File()