from django.db import models
from django.conf import settings
from django.template.defaultfilters import truncatechars

# class Status(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'statuses'

#     def __str__(self):
#         return truncatechars(self.text, 20)

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __str__(self):
        return '%d: track: %s album: %s' % (self.order, self.title, self.album)

