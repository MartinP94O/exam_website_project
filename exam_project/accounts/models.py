from django.contrib.auth import models as auth_models
from django.core import validators
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
