import uuid
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from views_library.decorators import ajax_login_required

from .models import ApiKey


@csrf_exempt
@ajax_login_required
def create_api(request):
    if request.method == "POST":
        if request.user.number_of_keys <= 5:
            user = request.user
            api_key = ApiKey(user=user, key=uuid.uuid4().hex)
            api_key.save()
            user.number_of_keys += 1
            user.save()
            return JsonResponse(
                {
                    "status": "created",
                    "key": api_key.key,
                    "key_id": api_key.id,
                    "objects": [
                        {
                            "id": "#api-key",
                            "value": f"API-ключ: {api_key.key}",
                        },
                        {
                            "id": "#staticBackdropLabel",
                            "value": "API ключ успешно создан",
                        },
                    ],
                }
            )
        return JsonResponse(
            {
                "status": "error",
                "objects": [
                    {
                        "id": "#api-key",
                        "value": "Вы достигли лимита ключей",
                    },
                    {
                        "id": "#staticBackdropLabel",
                        "value": "Ошибка создания API ключа",
                    },
                ],
            }
        )
    return JsonResponse(
        {
            "status": "error",
            "objects": [
                {
                    "id": "#api-key",
                    "value": "Попробуйте создать ключ позже",
                },
                {
                    "id": "#staticBackdropLabel",
                    "value": "Ошибка создания API ключа",
                },
            ],
        }
    )


@login_required
def user_api_keys(request):
    context = {"user": request.user}
    return render(request, "keys/user_keys.html", context)


@csrf_exempt
@ajax_login_required
def removal_api_key(request):
    if request.method == "POST":
        user = request.user
        api_key = ApiKey.objects.get(id=request.POST.get("item_id"), user=user)
        api_key.delete()
        user.number_of_keys -= 1
        user.save()
        return JsonResponse({"status": "deleted"})
    return JsonResponse({"status": "error", "error": "Ошибка удаления ключа"})


@csrf_exempt
@ajax_login_required
def change_api_key_status(request):
    if request.method == "POST":
        api_key = ApiKey.objects.get(id=request.POST.get("item_id"), user=request.user)
        api_key.is_active = not api_key.is_active
        api_key.save()
        return JsonResponse({"status": "included" if api_key.is_active else "excluded"})
    return JsonResponse(
            {"status": "error", "error": "Ошибка изменения статуса ключа"}
        )
