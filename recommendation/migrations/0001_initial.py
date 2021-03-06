# Generated by Django 4.0.1 on 2022-02-08 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=256, null=True)),
            ],
            options={
                'db_table': 'food',
            },
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100, null=True)),
                ('rating', models.FloatField()),
                ('primary_flavors', models.CharField(max_length=256, null=True)),
                ('comment', models.TextField(null=True)),
                ('purchase_link', models.URLField(max_length=256, null=True)),
                ('image', models.URLField(max_length=256, null=True)),
                ('saved_count', models.PositiveIntegerField(default=0)),
                ('ytinfo', models.TextField(null=True)),
                ('yturl', models.URLField(max_length=256, null=True)),
            ],
            options={
                'db_table': 'wine',
            },
        ),
        migrations.CreateModel(
            name='WineFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'food_for_wine',
            },
        ),
        migrations.CreateModel(
            name='WineProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.FloatField()),
                ('tannin', models.FloatField()),
                ('acidity', models.FloatField()),
                ('sweetness', models.FloatField()),
            ],
            options={
                'db_table': 'wine_profile',
            },
        ),
        migrations.CreateModel(
            name='WineRecommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'user_recommend',
            },
        ),
    ]
