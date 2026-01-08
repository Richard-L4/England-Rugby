from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone} | {self.address}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} | {self.email} | {self.address}"

    class Meta:
        verbose_name = "Register"
        verbose_name_plural = "Register"
