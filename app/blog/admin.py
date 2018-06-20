from django.contrib import admin
from blog.models import User, UserInfo, Post, Comment

admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(Post)
admin.site.register(Comment)
