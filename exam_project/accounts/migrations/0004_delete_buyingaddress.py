# Generated by Django 4.1.3 on 2022-12-15 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_buyingaddress_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BuyingAddress',
        ),
    ]
