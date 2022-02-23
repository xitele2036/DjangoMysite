import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from siteapp.models import Department,UserInfo

Headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    'User-Agent': "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    'User-Agent': "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)"
    }
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


def news(req):
    # 定义一些新闻（字典或者列表），数据库，网络请求去联通新闻
    # 向地址发送请求
    # 第三方模块：requests

    res = requests.get("https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=80&type=T",headers=Headers)
    # data_list = json.loads(res.text)
    # print(res.text)
    return render(req,'news.html',{"news_list":res.text})

def something(request):
    # request是一个对象，封装了用户通过浏览器发过来的所有数据
    # 获取请求方式：GET/POST
    print(request.method)

    #在URL上传递值 ?n1=123&n2=999
    print(request.GET)

    #在请求中提交数据
    print(request.POST)

    # HttpResponse("返回内容") 将字符串内容返回给请求者
    # return HttpResponse("返回内容")

    #读取HTML的内容 + 渲染（替换） -> 字符串，返还给请求者
    # return render(request,'something.html',{"title":" come on"})

    #重定向一个地址给请求者
    return redirect("https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=80&type=T")

def login(request):
    if request.method == "GET":
        return render(request,"login.html")

    # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    # print(username)
    # print(password)
    if username == "root" and password == "admin123":
        # return HttpResponse("登入成功")
        return redirect("https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=20&type=T")

        # return HttpResponse("登入失败")
    return render(request,"login.html",{"error_msg":"登入失败"})

def orm(request):
    #测试ORM操作数据库的数据
    ####新建####
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="运营部")

    # UserInfo.objects.create(name='JASON',password='admin12333',age=22)
    # UserInfo.objects.create(name='TOM',password='admin12333',age=22)
    # UserInfo.objects.create(name='BIT',password='admin12333',age=22)

    ####删除####
    # UserInfo.objects.filter(id=3).delete()
    # Department.objects.all().delete()

    ###获取数据####
    # data_list= UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)
    # data_list= UserInfo.objects.filter(id=2).first()
    # print(data_list.id, data_list.name, data_list.password, data_list.age)

    ###更新数据####
    # UserInfo.objects.all().update(password=9999)
    UserInfo.objects.filter(name='JASON').update(age=9999)


    return HttpResponse("成功")