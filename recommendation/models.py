from django.db import models
from user.models import User, UserProfile
from taggit.managers import TaggableManager


class Wine(models.Model):
    class Meta:
        db_table = "wine"

    mypic = models.ManyToManyField(User, related_name='my_pic', blank=True)  # some_user.my_pic.all()
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True)
    national_flag = models.URLField(max_length=256, null=True)
    rating = models.FloatField()
    primary_flavors = models.CharField(max_length=256, null=True)
    tags = TaggableManager(blank=True)    # for primary_flavors
    comment = models.TextField(null=True)
    purchase_link = models.URLField(max_length=256, null=True)
    image = models.URLField(max_length=256, null=True)
    saved_count = models.PositiveIntegerField(default=0)
    ytinfo = models.TextField(null=True)
    yturl = models.URLField(max_length=256, null=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Wine._meta.fields]


class WineProfile(models.Model):
    class Meta:
        db_table = "wine_profile"

    wine = models.OneToOneField(Wine, on_delete=models.CASCADE)
    body = models.FloatField()
    tannin = models.FloatField()
    acidity = models.FloatField()
    sweetness = models.FloatField()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in WineProfile._meta.fields]


class Food(models.Model):
    class Meta:
        db_table = "food"

    name = models.CharField(max_length=256)
    description = models.TextField()
    link = models.URLField(max_length=256, null=True)


class WineRecommend(models.Model):
    class Meta:
        db_table = "user_recommend"

    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'surveyed': True})
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)


class WineFood(models.Model):
    class Meta:
        db_table = "food_for_wine"

    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, unique=False)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
