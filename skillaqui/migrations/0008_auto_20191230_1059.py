# Generated by Django 2.1.8 on 2019-12-30 17:59

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skillaqui', '0007_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=49000),
        ),
    ]
