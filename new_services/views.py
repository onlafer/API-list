from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

from category.models import Categories
from .forms import AddApiForm


@login_required
def add_api(request):
    if request.method == "POST":
        form = AddApiForm(data=request.POST, files=request.FILES)
        selected_categories = request.POST.getlist("categories")
        if form.is_valid() and len(selected_categories) <= 6:
            messages.success(
                request,
                "Заявка на добавление API успешно отправлнена. Текущий статус отправленной заявки можно посмотреть в личном кабинете.",
            )
            new_api = form.save(commit=False)
            new_api.user = request.user
            new_api.save()
            new_api.categories.add(
                *Categories.objects.filter(id__in=selected_categories)
            )
            return redirect("user:profile")
        else:
            messages.warning(request, "Проверьте правильность заполнения формы")

    else:
        form = AddApiForm()
    context = {"title": "Форма добавления API", "form": form}
    return render(request, "new_services/add_api.html", context)
