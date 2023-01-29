from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from customers.api import serializers
from customers import models


class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_customer', 'fullname', 'CPF']
