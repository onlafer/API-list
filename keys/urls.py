from django.urls import path
from keys import views

app_name = "api"

urlpatterns = [
    path("create/", views.create_api, name="create_api"),
    path("keys/", views.user_api_keys, name="keys"),
    path("delete_api_key/", views.removal_api_key, name="delete_api_key"),
    path("change_api_key_status/", views.change_api_key_status, name="change_api_key_status"),
]
