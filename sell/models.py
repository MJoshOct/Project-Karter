from django.db import models

class Product(models.Model):
    TRANSACTION_TYPES = [
        ("SALE", "Sale"),
        ("EXCHANGE", "Exchange"),
        ("RENT", "Rent"),
        ("BARTER", "Barter"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_transaction_type_display()})"
