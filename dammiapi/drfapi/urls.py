from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token


# from account.views import (
#     registration_view,
#     logout_view,
#     login_view,
#     profile_view,
#     must_authenticate_view,
# )

urlpatterns = [
    # !Admin
    path("admin/", admin.site.urls),
    # ! Authentication
    path("", include("api.urls")),
    path("login/", obtain_auth_token, name="api_auth_token"),
    path("api/account/", include("account.api.urls", "account_api")),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/password_change.html"
        ),
        name="password_change",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # ! Test Api urls
    path("api/tests/", include("tests.api.urls", "tests_api")),
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
]
# ! Extra Settings for Files static and Media
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)