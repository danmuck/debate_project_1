from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title       = models.TextField()
    date        = models.DateField(auto_now=False, auto_now_add=True)
    subject     = models.TextField(null='', blank=True)
    blogpost    = models.TextField()
    
    def get_absolute_url(self):
        return reverse("postal:articles", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = ("article")
        verbose_name_plural = ("articles")
