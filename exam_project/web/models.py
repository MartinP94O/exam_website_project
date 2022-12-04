from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    MAX_LEN_PRODUCT_TYPE = 30
    MIN_LEN_PRODUCT_TYPE = 2

    MAX_LEN_PRODUCT_MODEL = 30
    MIN_LEN_PRODUCT_MODEL = 2

    MIN_PRICE = 0.01

    product_type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PRODUCT_TYPE,
        validators=(
            MinLengthValidator(MIN_LEN_PRODUCT_TYPE),
        ),

    )

    product_model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PRODUCT_MODEL,
        validators=(
            MinLengthValidator(MIN_LEN_PRODUCT_MODEL),
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
            MinValueValidator(MIN_PRICE),
        ),
    )


