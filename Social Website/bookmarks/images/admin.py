from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'thumbnail', 'created']
    list_filter = ['created']
    readonly_fields = ['preview']

    def thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

    def preview(self,obj):
        return mark_safe(f'<img src="{obj.image.url}">')