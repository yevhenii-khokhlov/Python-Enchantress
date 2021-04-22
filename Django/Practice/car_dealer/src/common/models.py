from django.db import models


class BaseDateAuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MyBaseModel(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True
