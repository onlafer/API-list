from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from api_list.settings import DEBUG
from api_list import settings
from new_services.views import add_api
from about.views import about

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("category/", include("category.urls", namespace="category")),
    path("user/", include("users.urls", namespace="user")),
    path("edit-profile/", include("edit_profile.urls", namespace="edit_profile")),
    path("favorite/", include("favorites.urls", namespace="favorite")),
    path("add-api/", add_api, name="add_api"),
    path("api/", include("keys.urls", namespace="api")),

    path("about/", about, name="about"),
]

if DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
