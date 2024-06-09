from django.urls import path
from new_services import views

app_name = "new_services"

urlpatterns = [
    path("add-api", views.add_api, name="add_api"),
]