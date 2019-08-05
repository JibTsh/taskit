from django.db import models

# Create your models here.

class Category(models.Model):
    #category_image = models.ImageField()
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

class Service(models.Model):
    service_name = models.CharField(max_length=15)
    service_description = models.CharField(max_length = 200)
    #service_renderer =  models.ForeignKey('User', on_delete=models.CASCADE)
    service_price = models.DecimalField(max_digits=6, decimal_places=2)
    service_category = models.ForeignKey('Category',on_delete=models.CASCADE)
    def __str__(self):
        return self.service_name