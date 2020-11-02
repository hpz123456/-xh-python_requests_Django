"""InterfaceAutomationTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from API_Interface import views
from django.conf.urls import url
from apscheduler.scheduler import Scheduler
from API_Interface.views import aaa
urlpatterns = [
    url(r'^$',views.index1,name='index'),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('entrance/',views.entrance),
    # path('receive_file/',views.receive_file)
    url(r'^entrance/receive_file/',views.receive_file,name='receive_file/'),
    # url('^article/(?P<year>[0-9]{4})/$',views.receive_file,name='receive_file/'),
    # path('instructionss/',views.instructions),
    url(r'^entrance/instructions/',views.instructions,name='instructions/'),
    url(r'^entrance/test_test_case/',views.test_test_case,name='test_test_case/'),
    # path('test_test_case/',views.instructions),

]

sched = Scheduler()  # 实例化，固定格式
@sched.interval_schedule(seconds=5)  # 装饰器，seconds=60意思为该函数为1分钟运行一次
def mytask():
    aaa()
sched.start()  # 启动该脚本