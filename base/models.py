from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(verbose_name='date_created', auto_now_add=True)
    subject = models.CharField(max_length=150)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name