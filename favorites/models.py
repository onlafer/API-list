from django.db import models
from category.models import Instructions

from users.models import User

class Favorites(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    instruction = models.ForeignKey(
        to=Instructions, on_delete=models.CASCADE, verbose_name="API"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Дата добавления"
    )

    class Meta:
        db_table = "favorites"
        verbose_name = "Понравившиеся API"
        verbose_name_plural = "Понравившиеся API"

    def __str__(self):
        return f'Избранное {self.user.username} | API {self.instruction}'
    