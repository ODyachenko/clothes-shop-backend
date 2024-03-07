from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    zip_code = models.CharField(max_length=5, default='')
    name = models.CharField(max_length=100, default='')
    number = models.CharField(max_length=16, default='')
    cvc = models.CharField(max_length=3, default='')
    expiry = models.CharField(max_length=7, default='')

    def __str__(self):
        return self.user.username