from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=50, unique=True, blank=True, null=True, verbose_name="URL"
    )
    icon = models.CharField(
        max_length=100, unique=True, blank=True, null=True, verbose_name="Иконка"
    )

    class Meta:
        db_table = "category"
        verbose_name = "категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Instructions(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=75, unique=True, blank=True, null=True, verbose_name="URL"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Дата добавления"
    )
    logo = models.ImageField(
        upload_to="category_images",
        blank=True,
        null=True,
        verbose_name="Логотип сервиса",
    )
    summary = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Краткая информация",
    )
    content = models.TextField(blank=True, null=True, verbose_name="Инструкция")
    date = models.DateField(auto_now=True, verbose_name="Последнее изменение")
    categories = models.ManyToManyField(
        to=Categories, default=None, verbose_name="Категории"
    )
    realization = models.URLField(
        max_length=300, blank=True, null=True, verbose_name="Графическая реализация"
    )
    original = models.URLField(
        max_length=300, blank=True, null=True, verbose_name="Оригинальная документация"
    )

    PAID = "paid"
    FREE = "free"
    TYPE_CHOICES = [(PAID, "платный"), (FREE, "бесплатный")]
    api_type = models.CharField(
        max_length=4, choices=TYPE_CHOICES, default=PAID, verbose_name="Тип API"
    )

    class Meta:
        db_table = "instructions"
        verbose_name = "API"
        verbose_name_plural = "API сервисы"
        ordering = ("id",)

    def __str__(self):
        return self.name
