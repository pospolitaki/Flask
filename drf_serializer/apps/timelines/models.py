from django.db import models
from django.conf import settings
from django.template.defaultfilters import truncatechars

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self):
        return truncatechars(self.text, 20)


