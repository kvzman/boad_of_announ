from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()


class Announce(models.Model):
    title = models.CharField(max_length=128)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('my_announces')

    def __str__(self):
        return self.title.title()


class Response(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('home')


class Mailer(models.Model):
    message = models.TextField()
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)

