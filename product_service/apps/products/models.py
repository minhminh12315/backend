from django.db import models
from utils.sharedModel import SharedModel
from utils.sku import generate_unique_sku
from utils.codeInvoice import generate_code_invoice


# Create your models here.
class Category(SharedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
class Product(SharedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Variant(SharedModel):
    sku = models.CharField(max_length=100, unique=True, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    volume = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='variant_images/', blank=True, null=True)


    class Meta:
        unique_together = ('product', 'volume')
    def __str__(self):
        return f"{self.product.name}"
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = generate_unique_sku(type(self))
        super().save(*args, **kwargs)
        
class Invoice(SharedModel):
    invoice_code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    customer = models.IntegerField(null=True, blank=True)  # Assuming customer is an integer ID, adjust as necessary
    
    def save(self, *args, **kwargs):
        if not self.invoice_code:
            self.invoice_code = generate_code_invoice(type(self))
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Invoice {self.invoice_code} - Customer ID: {self.customer}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant,related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f"Invoice {self.invoice.invoice_code} - Item: {self.variant.product.name} (x{self.quantity})"
    def save(self, *args, **kwargs):
        if not self.totalPrice:
            self.totalPrice = self.variant.price * self.quantity
        super().save(*args, **kwargs)