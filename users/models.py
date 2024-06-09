from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users_images", blank=True, null=True, verbose_name="Аватар"
    )
    basesvg = models.FileField(
        upload_to="users_base_svg", blank=True, null=True, verbose_name="Базовый аватар"
    )
    email = models.EmailField(_("email address"), blank=True, unique=True)
    email_notifications = models.BooleanField(
        default=True, verbose_name="Уведомления на почту"
    )
    number_of_keys = models.IntegerField(default=0, verbose_name="Количество ключей", validators=[MinValueValidator(0), MaxValueValidator(6)])
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username
