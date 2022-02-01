from django.db import models
from user.models import User, UserProfile


class Wine(models.Model):
    class Meta:
        db_table = "wine"

    user = models.ManyToManyField(User, blank=True)
    food = models.ManyToManyField('Food', blank=True)
    item = models.CharField(max_length=256)
    vintage = models.IntegerField()
    type = models.CharField(max_length=100)
    region = models.CharField(max_length=256)
    rating = models.IntegerField()
    price = models.IntegerField(null=True)
    primary_flavors = models.TextField(null=True)


class WineProfile(models.Model):
    class Meta:
        db_table = "wine_profile"

    wine = models.OneToOneField(Wine, on_delete=models.CASCADE)
    body = models.IntegerField()
    tannin = models.IntegerField()
    acidity = models.IntegerField()
    sweetness = models.IntegerField()


class Food(models.Model):
    class Meta:
        db_table = "food"

    item = models.CharField(max_length=256)
    description = models.TextField()


