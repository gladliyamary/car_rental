# Generated by Django 4.1.7 on 2023-04-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_cardetail_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetail',
            name='Available_places',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
