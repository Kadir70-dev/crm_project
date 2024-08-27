from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales')
    product = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Sale of {self.product} to {self.customer.name}"
