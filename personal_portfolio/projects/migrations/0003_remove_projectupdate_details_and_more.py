# Generated by Django 4.1.6 on 2023-02-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectupdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectupdate',
            name='details',
        ),
        migrations.AddField(
            model_name='project',
            name='responsibilities',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='projectupdate',
            name='description',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectupdate',
            name='responsibilities',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='static/img'),
        ),
        migrations.AlterField(
            model_name='projectupdate',
            name='image',
            field=models.FilePathField(path='static/img'),
        ),
    ]