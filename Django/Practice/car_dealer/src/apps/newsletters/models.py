from django.db import models


class NewsLetter(models.Model):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return 'email'
