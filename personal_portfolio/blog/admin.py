from django.contrib import admin
from .models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['title', 'body']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['author', 'body']


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
