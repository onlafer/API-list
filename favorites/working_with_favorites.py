from category.models import Instructions


def get_favorites(user):
    return Instructions.objects.filter(favorites__user_id=user.id)
