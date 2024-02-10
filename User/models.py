from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default='USER')
    photo = models.ImageField(upload_to='user_photo', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username