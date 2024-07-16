from django.contrib import admin
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'thumbnail', 'created']
    list_filter = ['created']
    readonly_fields = ['preview']

    def thumbnail(self, obj):
        if obj.image:
            thumbnailer = get_thumbnailer(obj.image)
            try:
                thumbnail = thumbnailer.get_thumbnail({'size': (50, 50)})
                return mark_safe(f'<img src="{thumbnail.url}" width="50" height="50" />')
            except Exception as e:
                return f'Error generating thumbnail: {str(e)}'
        else:
            return 'No image available'

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')
