from django.contrib import admin
from .models import SliderImage
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import mark_safe
from easy_thumbnails.files import get_thumbnailer


class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            # Настройки для thumbnail
            thumbnail_options = {'size': (50, 50), 'crop': True}
            thumbnail = get_thumbnailer(obj.image).get_thumbnail(thumbnail_options)
            return mark_safe(f'<img src="{thumbnail.url}">')
        return '-'

    image_preview.short_description = 'Фотография'

admin.site.register(SliderImage, SliderImageAdmin)
