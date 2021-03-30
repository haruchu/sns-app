from django.contrib import admin

from .models import Post, Like, Reply, ReplyLike

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Reply)
admin.site.register(ReplyLike)

