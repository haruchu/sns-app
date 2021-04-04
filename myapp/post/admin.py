from django.contrib import admin

from .models import Post, Like, Reply

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Reply)

