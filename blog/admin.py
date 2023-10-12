from django.contrib import admin
from blog.models import Tag, Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "published_at", "slug"]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)