from django.db import models

from .choices import ORDER_STATUS_CHOICES, ORDER_STATUS_OPEN


class Order(models.Model):
    car_id = models.ForeignKey(to="cars.Car", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    message = models.TextField(null=True)
    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS_CHOICES,
        default=ORDER_STATUS_OPEN
    )

    def __str__(self):
        return f'Order {self.pk}, status={self.status}'
