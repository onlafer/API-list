# favorite_tags.py
from django import template
from favorites.models import Favorites

register = template.Library()

@register.simple_tag
def is_favorite(item_id, user):
    return Favorites.objects.filter(instruction_id=item_id, user=user).exists()

@register.simple_tag()
def tag_favorites(api_id, user=None):
    if user and Favorites.objects.filter(instruction_id=api_id, user_id=user).exists():
        return 'Удалить из избранного <i class="bi bi-suit-heart-fill"></i>'
    else:
        return 'Добавить в избранное <i class="bi bi-suit-heart"></i>'
    