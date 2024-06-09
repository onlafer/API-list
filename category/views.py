from datetime import timedelta

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.utils import timezone
from category.utils import q_search
from category.models import Instructions, Categories
from favorites.working_with_favorites import get_favorites


def category(request, category_slug=None):

    page = request.GET.get("page", 1)
    api_type = request.GET.get("api_type", None)
    novelty = request.GET.get("novelty", None)
    graph_impl = request.GET.get("graph_impl", None)
    orig_doc = request.GET.get("orig_doc", None)
    query = request.GET.get("q", None)
    category_name = None

    if category_slug == "all" or query == "":
        services = Instructions.objects.all()
        title = "Список всех API"
    elif category_slug == "favorites":
        if request.user.is_authenticated:
            services = get_favorites(user=request.user)
            title = f"Список понравившихся API пользователя {request.user.username}"
            category_name = "Понравившиеся"
        else:
            return redirect("user:login")
    elif query:
        services = q_search(query)
        title = f"Список API по запросу '{query}'"
    else:
        services = Instructions.objects.filter(categories__slug=category_slug)
        title = f"Список API из категории {category_slug}"
        category_name = Categories.objects.get(slug=category_slug).name
    if novelty:
        thirty_days_ago = timezone.now() - timedelta(days=30)
        services = services.filter(created_at__gt=thirty_days_ago)
    if api_type and api_type != "default":
        services = services.filter(api_type=api_type)
    if graph_impl:
        services = services.exclude(realization=None)
    if orig_doc:
        services = services.exclude(original=None)

    paginator = Paginator(services, 6)
    current_page = paginator.page(page)

    context = {
        "title": title,
        "services": current_page,
        "slug_url": category_slug,
        "category_name": category_name,
        "api_list_status": "active",
    }
    
    return render(request, "category/index.html", context)
