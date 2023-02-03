from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    image1 = models.ImageField(null=True, blank=True, upload_to='images/')
    image2 = models.ImageField(null=True, blank=True, upload_to='images/')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
