from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = "my_user"

    nickname = models.CharField(max_length=256, default='')


class UserProfile(models.Model):
    class Meta:
        db_table = "user_profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    body = models.FloatField()
    tannin = models.FloatField()
    acidity = models.FloatField()
    sweetness = models.FloatField()


