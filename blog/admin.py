from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",),}
    list_display = ['title', 'body']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",),}
    list_display = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
