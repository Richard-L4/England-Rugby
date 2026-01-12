from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone} | {self.message}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class CardText(models.Model):
    title = models.CharField(max_length=20, blank=True)
    content = models.TextField()
    image_name = models.CharField(
        max_length=30,
        help_text="Enter the image filename (eg 'squad-pic.jpg')",
        default='default.jpg',
        blank=True
    )

    def __str__(self):
        return self.title or f"Card for {self.image_name}"
