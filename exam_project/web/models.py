from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# class Profile(models.Model):
#     username = models.CharField(
#         null=False,
#         blank=False,
#         max_length=10,
#         validators=(
#             MinLengthValidator(2, 'The username must be a minimum of 2 chars'),
#         ),
#     )
#
#     email = models.EmailField(
#         null=False,
#         blank=False,
#     )
#
#     age = models.IntegerField(
#         null=False,
#         blank=False,
#         validators=(
#             MinValueValidator(18),
#         ),
#     )
#
#     password = models.CharField(
#         max_length=30,
#     )
#
#     first_name = models.CharField(
#         null=True,
#         blank=True,
#         max_length=30,
#     )
#
#     last_name = models.CharField(
#         null=True,
#         blank=True,
#         max_length=30,
#     )
#
#     profile_picture = models.URLField(
#         null=True,
#         blank=True,
#     )

UserModel = get_user_model()


class Product(models.Model):
    product_type = models.CharField(
        null=False,
        blank=False,
        max_length=30,

    )

    product_model = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            MinLengthValidator(2),
        ),
    )

    product_year = models.IntegerField(
        null=False,
        blank=False,
    )

    product_image = models.URLField(
        null=False,
        blank=False,
    )

    product_price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(1),
        ),
    )

    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.RESTRICT,
    # )
