from django.db import models


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
