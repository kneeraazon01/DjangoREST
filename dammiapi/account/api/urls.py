from django.urls import path

from account.api.views import (
    registration_view,
    account_properties_view,
    profile_update,
    does_account_exist_view,
    ChangePasswordView,
)


from rest_framework.authtoken.views import obtain_auth_token
from .views import logout_view

app_name = "account"

urlpatterns = [
    path(
        "check_if_account_exists/",
        does_account_exist_view,
        name="check_if_account_exists",
    ),
    path("change_password/", ChangePasswordView.as_view(), name="change_password"),
    path("profile/", account_properties_view, name="profile"),
    path("profile_update/", profile_update, name="profile_update"),
    path("login/", obtain_auth_token, name="login"),
    path("register/", registration_view, name="register"),
    path("logout/", logout_view, name="logout"),
]