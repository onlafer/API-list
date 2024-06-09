from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from edit_profile.forms import UserEditInfo, UserEditPassword


@login_required
def edit_info(request):
    if request.method == "POST":
        form = UserEditInfo(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            if request.POST.get('ResetImage') == 'true':
                request.user.image = None
            form.save()
            messages.success(
                request,
                "Настройки успешно сохранены.",
            )
            return redirect("edit_profile:edit_info")
    else:
        form = UserEditInfo(instance=request.user)
    context = {"title": "Настройки профиля", "form": form}
    return render(request, "edit_profile/edit_info.html", context)


@login_required
def edit_password(request):
    if request.method == "POST":
        form = UserEditPassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request,
                "Новый пароль успешно сохранён.",
            )
            return redirect("edit_profile:edit_password")
    else:
        form = UserEditPassword(request.user)
    context = {"title": "Изменение пароля", "form": form}
    return render(request, "edit_profile/edit_password.html", context)
