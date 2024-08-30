from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrvX8szwybkA8_2wFG8BrFkHVcQJFaVA6H_g&s')

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
