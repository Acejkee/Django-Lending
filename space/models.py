from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = FilerImageField(null=True, on_delete=models.CASCADE, verbose_name="Фотография")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

        ordering = ['sort_order']

    def __str__(self):
        return self.title
