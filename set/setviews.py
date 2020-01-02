from django.shortcuts import render

# Create your views here.
from set.models import Set
#设置管理
def set_manage(request):
    username = request.session.get('user', '')
    set_list = Set.objects.all()
    return render(request, "set_manage.html", {"user": username,"sets": set_list})
from django.contrib.auth.models import User
#用户管理
def set_user(request):

    user_list = User.objects.all()

    username = request.session.get('user','')
    return render(request, "set_user.html", {"user": username,"users": user_list})
