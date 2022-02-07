from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = "my_user"

    nickname = models.CharField(max_length=256, default='')
    surveyed = models.BooleanField(default=False)


class UserProfile(models.Model):
    class Meta:
        db_table = "user_profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    body = models.FloatField()
    tannin = models.FloatField()
    acidity = models.FloatField()
    sweetness = models.FloatField()
