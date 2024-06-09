from django.urls import path
from edit_profile import views

app_name = "edit_profile"

urlpatterns = [
    path("info", views.edit_info, name="edit_info"),
    path("password", views.edit_password, name="edit_password"),
]
