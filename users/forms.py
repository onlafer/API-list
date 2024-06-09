from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django.forms import CharField, EmailField

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = EmailField()
    password = CharField()

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    username = CharField()
    email = EmailField()
    password1 = CharField()
    password2 = CharField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
