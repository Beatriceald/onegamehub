from django.db import models

# Create your models here.
class Urls(models.Model):
    url_slug = models.URLField(verbose_name='URL')

    def __str__(self):
        return f'{self.url_slug}'

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLS'