from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=50) #max length req
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    email     = models.EmailField(default='n/a')
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("render", kwargs={"product_id": self.id})
    

