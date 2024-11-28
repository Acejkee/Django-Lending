from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    title = models.CharField(max_length=255)
    image = FilerImageField(null=True, on_delete=models.CASCADE)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

        ordering = ['sort_order']

    def __str__(self):
        return self.title
