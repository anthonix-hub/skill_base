# Generated by Django 2.1.8 on 2019-12-26 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skillaqui', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
    ]
