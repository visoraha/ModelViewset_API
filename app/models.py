from django.db import models


# Create your models here.
class Product_catagory(models.Model):
    catagory_name=models.CharField(max_length=100)
    pid=models.IntegerField()

    def __str__(self) -> str:
        return self.catagory_name
    
class Product(models.Model):
    catagory=models.ForeignKey(Product_catagory,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    prise=models.IntegerField()
    id=models.IntegerField(primary_key=True)
    def __str__(self) -> str:
        return self.pname

