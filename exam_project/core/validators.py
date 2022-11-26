from django.core import exceptions


def validate_only_letters(value):
    for character in value:
        if not character.isalpha():
            raise exceptions.ValidationError('Only letters are allowed in this field!')
