# Generated by Django 3.2.10 on 2022-02-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0003_remove_userinfo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=10),
        ),
    ]