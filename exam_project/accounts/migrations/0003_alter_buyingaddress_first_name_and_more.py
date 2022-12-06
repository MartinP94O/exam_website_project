# Generated by Django 4.1.3 on 2022-12-06 13:04

import django.core.validators
from django.db import migrations, models
import exam_project.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_buyingaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyingaddress',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(2), exam_project.core.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='buyingaddress',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(2), exam_project.core.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='buyingaddress',
            name='post_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='buyingaddress',
            name='town',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3, 'The town name must be a minimum of 2 chars')]),
        ),
    ]
