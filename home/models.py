from statistics import mode
from django.db import models

# Create your models here.
class Fruits(models.Model):
    fruit_name = models.CharField(max_length=100)
    price = models.IntegerField(help_text="in dollars")
    manfacture_date = models.DateField()
    fruits_description = models.TextField()
    is_fresh = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.fruit_name} and price is {self.price}"
    
