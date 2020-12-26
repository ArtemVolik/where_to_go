from django.db import models


class Place(models.Model):
    """Места. """
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Название')
    description_short = models.CharField(max_length=255, verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Описание')
    lon = models.FloatField()
    lat = models.FloatField()
    unique_together = (("lon", "lat"),)
    index_together = ["lon", "lat"]

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

    def __str__(self):
        return f'{self.id} {self.title}'







