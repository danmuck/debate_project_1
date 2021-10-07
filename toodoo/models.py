from django.db import models
from django.urls import reverse

# Create your models here.

class TooDoo(models.Model):
    title       = models.CharField(max_length=50) #max length req
    # date        = models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
    description = models.TextField(blank=True, null=True)
    complete    = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f'/editor/{self.id}'
