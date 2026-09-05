from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=50)
    desciption=models.TextField(null=False)
    def __str__(self):
        return f"{self.name}-{self.desciption}"


class Product(models.Model):
    name=models.CharField(max_length=50)    
    content=models.TextField(null=False)
    price=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField()
    image_pro=models.URLField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')

    def __str__(self):
        return f"{self.name}"