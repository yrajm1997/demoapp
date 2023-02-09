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


## CREATE TABLE `customerapp_customers` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `first_name` varchar(30) NOT NULL, `last_name` varchar(40) NOT NULL, `date_of_birth` date NOT NULL, `pan_number` varchar(10) NOT NULL, `credit_card_number` varchar(19) NOT NULL, `email` varchar(254) NOT NULL, `address` varchar(50) NOT NULL, `salary` double precision NOT NULL);
