from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
def apiOverview(request):
    return render(request, "api/home.html")


@api_view(["GET"])
def Apis(request):
    api_urls = {
        "admin": "admin",
        "register": "api/account/register",
        "login": "api/account/login",
        "profile": "api/account/profile",
        "profile update": "api/account/profile/update",
        "logout": "api/account/logout",
        "change password": "api/account/change_password",
        "check check": "api/account/check_if_account_exists",
        "Cements": "Cement Ko eha Bata Tala",
        "list cement tests": "api/tests/cement_comps_test_list/",
        "cement details": "api/tests/cement_details/",
        "create cement test": "api/tests/cement_create_comps/",
        "update cement test": "api/tests/cement_update/",
        "delete a cement test": "api/tests/cement_delete/",
    }

    return Response(api_urls)
