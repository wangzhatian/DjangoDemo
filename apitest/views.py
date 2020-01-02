from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apitest.models import Apitest,Apistep,Apis
#退出登录
def logout(request):
    auth.logout(request)
    return render(request,"login.html")
#home目录
def home(request):
    return render(request,"home.html")
#登录
def login(request):
    if request.POST:
        # username=password=""
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        user=auth.authenticate(username=username,password=password)
        if user is not  None and user.is_active:
            auth.login(request,user)
            request.session["user"]=username
            response=HttpResponseRedirect("/home/")
            return response
        else:
            return render(request,"login.html",{"error":"用户名或密码错误"})
    return render(request,"login.html")
#测试界面
def test(request):
    return HttpResponse("hello test")
#接口管理
@login_required
def apitest_manage(request):
    apitest_list=Apitest.objects.all()#读取所有流程接口数据
    username=request.session.get("user","")
    return render(request,"apitest_manage.html",{"user":username,"apisteps":apitest_list})
#接口步骤管理
def apistep_manage(request):
    username=request.session.get("user","")
    apistep_list=Apistep.objects.all()
    return render(request,"apistep_manage.html",{"user":username,"apisteps":apistep_list})
def api_manage(request):
    username = request.session.get('user', '')

    apis_list = Apis.objects.all()

    return render(request, "api_manage.html", {"user": username,"apiss": apis_list})
