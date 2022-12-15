from django.core import exceptions


def validate_only_letters(value):
    for character in value:
        if not character.isalpha():
            raise exceptions.ValidationError('Only letters are allowed in this field!')


def validate_year_length(value):
    value_len = len(str(value))
    valid_year_length = 4

    if value_len != valid_year_length:
        raise exceptions.ValidationError('Year must be exactly 4 digits!')

