from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.forms import BooleanField, CharField, ImageField

from users.models import User


class UserEditInfo(UserChangeForm):
    first_name = CharField(required=False)
    last_name = CharField(required=False)
    username = CharField()
    image = ImageField(required=False)
    email_notifications = BooleanField(required=False)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "image",
            "email_notifications",
        )

class UserEditPassword(PasswordChangeForm):
    old_password = CharField()
    new_password1 = CharField()
    new_password2 = CharField()

    class Meta:
        model = User
        fields = {
            "old_password",
            "new_password1",
            "new_password2",
        }
        