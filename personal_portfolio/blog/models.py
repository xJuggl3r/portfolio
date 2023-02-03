from django.db import models
from django.conf import settings
from PIL import Image
import os

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


def header_image_path(instance, filename):
    return '{{MEDIA_URL}}/{0}/{1}'.format(instance.pk, filename)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    header_image = models.ImageField(
        upload_to=header_image_path, blank=True, default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Check if header_image already exists
        if self.header_image:
            return

        # Create header_image
        # redefine header_image upload location
        self.header_image.name = '{{MEDIA_URL}}/posts/{0}/header_image.png'.format(
            str(self.pk))

        img = Image.new('RGB', (1200, 400), color='gray')
        media_path = os.path.join(settings.BASE_DIR, 'media')
        image_path = os.path.join(media_path, 'posts', str(self.pk))

        # Make sure the directory exists
        os.makedirs(image_path, exist_ok=True)

        # Save the image
        img.save(os.path.join(image_path, 'header_image.png').replace('\\', '/'))

        # Set header_image field
        # self.header_image.name = '{{MEDIA_URL}}/posts/{0}/header_image.png'.format(
        #     str(self.pk))

        self.header_image.name = os.path.join(
            'posts', str(self.pk), 'header_image.png').replace('\\', '/')
        super().save(*args, **kwargs)

    image1 = models.ImageField(null=True, blank=True, upload_to='images/')
    image2 = models.ImageField(null=True, blank=True, upload_to='images/')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
