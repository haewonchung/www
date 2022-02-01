from django.db import models
from user.models import userModel, userProfile


class wine(models.Model):
    class Meta:
        db_table = "wine_list"

    user = models.ForeignKey(userModel, on_delete=models.CASCADE)
    item = models.CharField(max_length=256)
    vintage = models.IntegerField()
    type = models.CharField(max_length=100)
    region = models.CharField(max_length=256)
    rating = models.IntegerField()
    price = models.IntegerField(null=True)
    primary_flavors = models.TextField(null=True)
    chefs_note = models.TextField(null=True)


class recommendation(models.Model):
    class Meta:
        db_table = "recommendation"

    user = models.ForeignKey(userModel, on_delete=models.CASCADE)
    wine = models.ForeignKey(wine, on_delete=models.CASCADE)
    user_taste = models.ForeignKey(userProfile, on_delete=models.CASCADE)


class wineTaste(models.Model):
    class Meta:
        db_table = "wine_taste"

    body = models.IntegerField()
    tannin = models.IntegerField()
    acidity = models.IntegerField()
    sweetness = models.IntegerField()


class food(models.Model):
    class Meta:
        db_table = "food_list"

    item = models.CharField(max_length=256)
    description = models.TextField()

