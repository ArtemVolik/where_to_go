"""Models of Places and related images."""

from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """Места."""

    title = models.CharField(
        max_length=100, unique=True,
        db_index=True, verbose_name='Название')
    short_description = models.TextField(
        verbose_name='Короткое описание')
    long_description = HTMLField(verbose_name='Описание')
    lon = models.FloatField()
    lat = models.FloatField()
    unique_together = [("lon", "lat")]
    index_together = ["lon", "lat"]

    class Meta:
        verbose_name = 'Место на карте'
        verbose_name_plural = 'Места на карте'

    def __str__(self):
        return self.title

    def short_title(self) -> str:
        start = self.title.find('«')
        end = self.title.find('»')
        if start + end > 0:
            return self.title[start+1:end]
        return self.title


class Image(models.Model):
    """Картинки."""

    image_place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='images', verbose_name='Название места картинки')
    image = models.ImageField(verbose_name='Картинка')
    image_order = models.PositiveIntegerField(
        verbose_name='Позиция', default=0)

    class Meta:
        ordering = ["image_order"]
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.id} {self.image_place}'
