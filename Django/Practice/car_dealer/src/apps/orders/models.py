from django.db import models


class Order(models.Model):
    ORDER_STATUS_OPEN = 'o'
    ORDER_STATUS_CLOSE = 'c'

    ORDER_STATUS_CHOICES = (
        (ORDER_STATUS_OPEN, 'open'),
        (ORDER_STATUS_CLOSE, 'close'),
    )

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
