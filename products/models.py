from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Tematic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    tematic = models.ForeignKey(Tematic, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']