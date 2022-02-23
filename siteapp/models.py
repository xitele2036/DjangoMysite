from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField(default = 10)
    data = models.IntegerField(null=True,blank=True)

class Department(models.Model):
    title = models.CharField(max_length=16)


class Role(models.Model):
    caption = models.CharField(max_length=16)



"""
在models创建类
ORM 会根据这个类区创建相应的表项
create table siteapp_userinfo(
    id bigint auto_increment primary key,
    name varchar(32)
    password varchar(64),
    age int
)
在命令行执行两个命令
1.python manage.py makemigrations
2.python manage.py migrate
app必须先注册才可以
"""