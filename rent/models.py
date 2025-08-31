from django.db import models
from django.contrib.auth.models import User

# Product table (items available for sell/rent)
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images/")  # stored inside MEDIA_ROOT/product_images/

    def __str__(self):
        return self.name


# Rent Request table (transaction records)
class RentRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # who requested
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    duration_value = models.PositiveIntegerField()
    duration_unit = models.CharField(
        max_length=10,
        choices=[("hour", "Hour"), ("day", "Day"), ("week", "Week"), ("month", "Month")],
        default="day",
    )
    notes = models.TextField(blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.product.name} ({self.date_requested.date()})"
