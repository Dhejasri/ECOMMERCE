from django.db import models

class Product(models.Model):
    catlog=[
        ('Ethnicwear','Ethnicwear'),
        ('Westernwear','Westernwear'),
        ('footwears','footwears'),
        ('electronics','electronics')
    ]

    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=20,choices=catlog)
    image=models.ImageField(upload_to='products/',blank=True, null=True)
    
    
    def __str__(self):
        return self.name 
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"{self.product.name} - Image"
