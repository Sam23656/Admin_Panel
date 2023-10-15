from django.db import models


# Create your models here.

class Stock(models.Model):
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.quantity


class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    items = models.ManyToManyField('Product')
    order_date = models.DateField()
    statuses = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )
    order_status = models.CharField(max_length=255, choices=statuses, default='Pending')

    def __str__(self):
        return f"{self.client.name} - {self.order_status}"


class Employee(models.Model):
    name = models.CharField(max_length=255)
    surename = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.surename} {self.last_name}"


class Client(models.Model):
    name = models.CharField(max_length=255)
    surename = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.surename} - {self.email}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.category}"
