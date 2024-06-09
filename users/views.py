from django.contrib import auth, messages
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.decorators import login_required
from favorites.working_with_favorites import get_favorites
from users.models import User

from users.base_avatar import get_basic_svg

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(
                    request,
                    f"Пользователь <b>{user.username}</b> успешно вошел в аккаунт",
                )
                if request.POST.get("next", None):
                    return redirect(request.POST.get("next"))
                return redirect(
                    "category:list_filter",
                    "all",
                )
    else:
        form = UserLoginForm()
    context = {"title": "Вход", "form": form}
    return render(request, "users/login.html", context)


def send_auth_email(request, user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    url = request.build_absolute_uri(
        reverse("user:authenticate", kwargs={"uidb64": uid, "token": token})
    )
    send_mail(
        "Подтвердите ваш адрес электронной почты",
        f"Для подтверждения перейдите по ссылке: {url}",
        "service.api.list@gmail.com",
        [user.email],
    )
    messages.info(
        request,
        f"Чтобы подтвердить регистрацию аккаунта, перейдите по ссылке, отправленной на вашу почту <b>{user.email}</b>.<br><b>Примечание:</b> Проверьте папку со спамом.",
    )


def authenticate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.basesvg = get_basic_svg(user.username)
        user.is_active = True
        user.save()
        auth.login(request, user)
        messages.success(request, "Аккаунт успешно создан.")
    else:
        messages.warning(request, "Ошибка создания аккаунта.")

    return redirect(
        "category:list_filter",
        "all",
    )


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_auth_email(request, user)
            return redirect(
                "category:list_filter",
                "all",
            )
    else:
        form = UserRegistrationForm()
    context = {"title": "Регистрация", "form": form}
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    page = request.GET.get("page", 1)

    services = services = get_favorites(user=request.user)
    paginator = Paginator(services, 5)
    current_page = paginator.page(page)

    context = {
        "title": "Личный кабинет",
        "user": request.user,
        "services": current_page,
    }
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(
        "category:list_filter",
        "all",
    )
