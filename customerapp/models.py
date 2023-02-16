from django.db import models

class Customers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    pan_number = models.CharField(max_length=255)
    credit_card_number = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    salary = models.FloatField()
