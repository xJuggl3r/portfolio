# Generated by Django 4.1.6 on 2023-02-03 18:14

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, default='', upload_to=blog.models.header_image_path),
        ),
    ]