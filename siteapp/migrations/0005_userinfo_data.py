# Generated by Django 3.2.10 on 2022-02-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0004_userinfo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='data',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
