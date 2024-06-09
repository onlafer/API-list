from django.urls import path
from category import views

app_name = "category"

urlpatterns = [
    path("search/", views.category, name="search"),
    path("<slug:category_slug>/", views.category, name="list_filter"),
]
