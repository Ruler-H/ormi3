from django.contrib import admin
from .models import TubePost, Comment, Tag

admin.site.register(TubePost)
admin.site.register(Comment)
admin.site.register(Tag)
