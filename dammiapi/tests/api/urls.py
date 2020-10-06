from django.urls import path
from tests.api.views import (
    cementDetailComp,
    cementCreateComp,
    cementUpdateComp,
    cementDeleteComp,
    cementListComp,
    project_delete,
    project_create,
    project_detail,
    projectlist,
    project_update,
    is_author_of_project,
    cementResultComp,
    cementReportComp,
)

app_name = "tests"

urlpatterns = [
    # ! Project  Urls
    path("list_projects/", projectlist.as_view(), name="list"),
    path("create_project/", project_create, name="create"),
    path("update_project/<str:pk>/", project_update, name="update"),
    path("detail_project/<str:pk>/", project_detail, name="detail"),
    path("delete_project/<str:pk>/", project_delete, name="delete"),
    path("is_author_of_project/<str:pk>/", is_author_of_project, name="is_author"),
    # ! End Project urls
    #! Cement Compressive urls
    path(
        "cementListComp/",
        cementListComp.as_view(),
        name="cement_comps_list",
    ),
    path("cementCreateComp/", cementCreateComp, name="cement_comps_create"),
    path("cementUpdateComp/<str:pk>/", cementUpdateComp, name="cement_update"),
    path("cementDeleteComp/<str:pk>/", cementDeleteComp, name="cement_delete"),
    path("cementDetailComp/<str:pk>/", cementDetailComp, name="cement_details"),
    path("cementResultComp/<str:pk>/", cementResultComp, name="cementResultComp"),
    path("cementReportComp/<str:pk>/", cementReportComp, name="cementReportComp"),
]