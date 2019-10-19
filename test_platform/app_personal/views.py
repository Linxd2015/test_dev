from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
# 用来写请求的处理逻辑


def hello(request):
    return render(request, "hello.html")


def login(request):
    """
    登录页面
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "" or password == "":
            return render(request, "login.html", {"error": "用户名或密码为空"})

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/manage/")
        else:
            return render(request, "login.html", {"error": "用户名或密码错误"})


@login_required
def manage(request):
    return render(request, "manage.html")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
