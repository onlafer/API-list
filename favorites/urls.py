from django.urls import path
from favorites import views

app_name = "favorites"

urlpatterns = [
    path("toggle-favorite/", views.toggle_favorite, name="toggle_favorite"),
]
