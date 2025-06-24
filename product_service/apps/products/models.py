from django.db import models
from utils.sharedModel import SharedModel
from utils.sku import generate_unique_sku


# Create your models here.
class Category(SharedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
class Product(SharedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Variant(SharedModel):
    sku = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    volume = models.CharField(max_length=50, blank=True, null=True, unique=True)
    image = models.ImageField(upload_to='variant_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.product.name}"
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = generate_unique_sku(self.product)
        super().save(*args, **kwargs)

        
