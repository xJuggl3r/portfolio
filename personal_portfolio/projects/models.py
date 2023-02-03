from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    stack = models.CharField(max_length=100)
    image = models.FilePathField(path="static/img")
    responsibilities = models.TextField(default="")
    # url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class ProjectUpdate(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    stack = models.CharField(max_length=100)
    image = models.FilePathField(path='static/img')
    responsibilities = models.TextField(default="")
    # url = models.URLField(blank=True)

    def __str__(self):
        return self.title
