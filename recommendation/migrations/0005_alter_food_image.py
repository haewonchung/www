# Generated by Django 4.0.1 on 2022-02-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_alter_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.URLField(max_length=256, null=True),
        ),
    ]
