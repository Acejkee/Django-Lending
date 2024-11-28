from django.contrib import admin
from .models import SliderImage
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import mark_safe


class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 50px; height: auto;" />')
        return '-'  # более читабельное значение, чем пустая строка

admin.site.register(SliderImage, SliderImageAdmin)
