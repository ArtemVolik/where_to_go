from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    """Места. """
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Название')
    description_short = models.CharField(max_length=255, verbose_name='Короткое описание')
    description_long = HTMLField(verbose_name='Описание')
    lon = models.FloatField()
    lat = models.FloatField()
    unique_together = (("lon", "lat"),)
    index_together = ["lon", "lat"]

    class Meta:
        verbose_name = u'Место на карте'
        verbose_name_plural = u'Места на карте'

    def __str__(self):
        return self.title

    def short_title(self):
        start = self.title.find('«')
        end = self.title.find('»')
        if start + end > 0:
            return self.title[start+1:end]
        return self.title


class Image(models.Model):
    """Картинки. """
    title = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Картинка')
    image_order = models.PositiveIntegerField(verbose_name='Позиция', default=0)

    class Meta:
        ordering = ["image_order"]
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения'

    def __str__(self):
        return f'{self.id} {self.title}'







