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
    MIN_LEN_FIRSTNAME = 2
    MAX_LEN_FIRSTNAME = 20

    MIN_LEN_LASTNAME = 2
    MAX_LEN_LASTNAME = 20

    MIN_LEN_TOWN = 3
    MAX_LEN_TOWN = 15

    MIN_LEN_STREET = 2
    MAX_LEN_STREET = 20

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_FIRSTNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRSTNAME),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_LASTNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRSTNAME),
            validate_only_letters,
        ),
    )

    town = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_TOWN,
        validators=(
            MinLengthValidator(MIN_LEN_TOWN, 'The town name must be a minimum of 2 chars'),
        ),
    )

    street = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_STREET,
        validators=(
            MinLengthValidator(MIN_LEN_STREET, 'The street name must be a minimum of 2 chars'),
        ),
    )

    post_code = models.IntegerField(
        null=False,
        blank=False,
    )



