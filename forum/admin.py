from django.contrib import admin
from .models import Post, Discussion, Response

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('post', 'created_at')
