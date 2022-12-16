# Generated by Django 4.1.3 on 2022-12-15 15:39

import django.core.validators
from django.db import migrations, models
import exam_project.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_product_product_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(2), exam_project.core.validators.validate_only_letters])),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(2), exam_project.core.validators.validate_only_letters])),
                ('town', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3, 'The town name must be a minimum of 2 chars')])),
                ('street', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2, 'The street name must be a minimum of 2 chars')])),
                ('post_code', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_year',
            field=models.IntegerField(validators=[exam_project.core.validators.validate_year_length]),
        ),
    ]