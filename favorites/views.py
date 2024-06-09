from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from views_library.decorators import ajax_login_required

from .models import Favorites


@csrf_exempt
@ajax_login_required
def toggle_favorite(request):
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        user_id = request.user.id
        if Favorites.objects.filter(instruction_id=item_id, user_id=user_id).exists():
            Favorites.objects.filter(instruction_id=item_id, user_id=user_id).delete()
            return JsonResponse({"status": "removed"})
        else:
            Favorites.objects.create(instruction_id=item_id, user_id=user_id)
            return JsonResponse({"status": "added"})
    return JsonResponse({"status": "error"})
