import uuid
from django.db import models


class ApiKey(models.Model):
    key = models.CharField(max_length=100, unique=True, verbose_name="Ключ")
    user = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Дата добавления"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    is_used = models.BooleanField(default=False, verbose_name="Использован")
    
    class Meta:
        db_table = "api_keys"
        verbose_name = "api_key"
        verbose_name_plural = "API ключи"

    def __str__(self):
        return self.user.username
