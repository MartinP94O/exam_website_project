from django.contrib.auth import models as auth_models
from django.core import validators
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_project.core.validators import validate_only_letters


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRSTNAME = 2
    MAX_LEN_FIRSTNAME = 20

    MIN_LEN_LASTNAME = 2
    MAX_LEN_LASTNAME = 20

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_FIRSTNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRSTNAME),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_LASTNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LASTNAME),
            validate_only_letters,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )


class BuyingAddress(models.Model):

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    town = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(
            MinLengthValidator(2, 'The town name must be a minimum of 2 chars'),
        ),
    )

    street = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            MinLengthValidator(2, 'The street name must be a minimum of 2 chars'),
        ),
    )

    post_code = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(4),
        ),
    )



