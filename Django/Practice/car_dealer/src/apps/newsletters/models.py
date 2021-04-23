from django.db import models


class NewsLetter(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return 'email'
