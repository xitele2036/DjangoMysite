from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):

    # 去app目录下的templates目录寻找user_list.html,Django会根据app注册顺序依次寻找
    return render(request,'user_list.html')

def user_add(request):
    return render(request,'user_add.html')

def tpl(request):
    name = "Jason"
    roles = ["管理员","CEO","保安"]
    user_info = {"name":"PIT","salary":10000,"role":"CTO"}
    date_list = [
        {"name": "JACK", "salary": 10000, "role": "CTO"},
        {"name": "PIT", "salary": 10000, "role": "CTO"},
        {"name": "TOM", "salary": 10000, "role": "CTO"},
    ]
    return render(request,'tpl.html',{"n1":name,"n2":roles,"n3":user_info,"n4":date_list})