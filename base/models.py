from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(verbose_name='date_created', auto_now_add=True)
    subject = models.TextField(max_length=300)
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Post(models.Model):
    post_title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    link = models.URLField(max_length=200)
    thumbnail = models.ImageField(upload_to ='posts/%Y/%m/%d/')

    def __str__(self):
        return self.post_title