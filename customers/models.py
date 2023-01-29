from django.db import models
from uuid import uuid4


class Customer(models.Model):
    id_customer = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    fullname = models.CharField(max_length=255)
    CPF = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=14)
    gender = models.CharField(max_length=255)
    CEP = models.CharField(max_length=8)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
