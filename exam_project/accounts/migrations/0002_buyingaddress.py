# Generated by Django 4.1.3 on 2022-12-04 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('town', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2, 'The town name must be a minimum of 2 chars')])),
                ('street', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2, 'The street name must be a minimum of 2 chars')])),
                ('post_code', models.IntegerField(validators=[django.core.validators.MinValueValidator(4)])),
            ],
        ),
    ]