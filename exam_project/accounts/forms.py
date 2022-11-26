from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UsernameField, UserChangeForm

UserModel = get_user_model()


class UserEditForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': auth_forms.UsernameField}
        #TODO add placeholders


class UserCreateForm(auth_forms.UserCreationForm):
    # TODO add placeholders
    # placeholders = {
    #     'username': 'Username',
    #     'email': 'Email',
    #     'password1': 'Password',
    #     'password2': 'Confirm password',
    # }

    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {
            'username': UsernameField,
        }
