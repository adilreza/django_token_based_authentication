# Generated by Django 3.0.3 on 2020-02-18 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0003_auto_20200218_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restmodel2',
            old_name='this is data1',
            new_name='thisName',
        ),
    ]
