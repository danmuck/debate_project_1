from django.db import models
from django.urls import reverse

# Create your models here.

class Evidence(models.Model):
    title       = models.CharField(max_length=1000) #max length req
    description = models.TextField(blank=True, null=True)
    speaker     = models.CharField(max_length=50, null=True, default='n/a')
    source      = models.URLField(max_length=200, default='n/a', null=True)

    def get_absolute_url(self):
        return f'/ev_editor/{self.id}'

