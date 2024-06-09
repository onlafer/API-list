from django.db import models

from category.models import Categories
from users.models import User


class NewAPI(models.Model):
    user = models.ForeignKey(
        to=User,
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    logo = models.ImageField(
        upload_to="category_images",
        blank=True,
        null=True,
        verbose_name="Логотип сервиса",
    )
    logo_svg = models.FileField(
        upload_to="category_images",
        blank=True,
        null=True,
        verbose_name="Логотип сервиса",
    )
    BEING_CHECHED = "being_checked"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    STATUS_CHOICES = [
        (BEING_CHECHED, "Проверяется"),
        (ACCEPTED, "Одобрено"),
        (REJECTED, "Отклонено"),
    ]
    status = models.CharField(choices=STATUS_CHOICES, default=BEING_CHECHED, max_length=13)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, blank=True, null=True, verbose_name="Дата добавления"
    )
    summary = models.CharField(max_length=100, verbose_name="Краткая информация")
    content = models.TextField(max_length=300, verbose_name="Подробная информация")
    categories = models.ManyToManyField(to=Categories, verbose_name="Категории")
    realization = models.URLField(
        max_length=300, blank=True, null=True, verbose_name="Графическая реализация"
    )
    original = models.URLField(
        max_length=300, blank=True, null=True, verbose_name="Оригинальная документация"
    )
    github = models.URLField(
        max_length=100, blank=True, null=True, verbose_name="Ссылка на ваш github"
    )

    PAID = "paid"
    FREE = "free"
    TYPE_CHOICES = [
        (PAID, "платный"),
        (FREE, "бесплатный")
    ]
    api_type = models.CharField(
        max_length=4, choices=TYPE_CHOICES, default=PAID, verbose_name="Тип API"
    )

    class Meta:
        db_table = "new_api"
        verbose_name = "New_API"
        verbose_name_plural = "Новые API"
        ordering = ("id",)

    def __str__(self):
        return self.name
