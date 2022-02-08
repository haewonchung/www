# Generated by Django 4.0.1 on 2022-02-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='surveyed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='acidity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='body',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sweetness',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tannin',
            field=models.FloatField(),
        ),
    ]
