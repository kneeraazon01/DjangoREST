from tests.models import cementCompressive, NewProject
from tests.api.serializers import (
    cementCompressiveSerializer,
    newProjectserializers,
    cementResultCompressiveSerializers,
    reportInfoCementSerializers,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView

SUCCESS = "success"
ERROR = "error"
DELETE_SUCCESS = "deleted"
UPDATE_SUCCESS = "updated"
CREATE_SUCCESS = "created"

# ! DONT TOUCH THE CODE BELOW


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def project_create(request):
    if request.method == "POST":
        data = request.data
        data["author"] = request.user.pk
        serializer = newProjectserializers(data=data)
        data = {}
        if serializer.is_valid():
            project = serializer.save()
            data["response"] = CREATE_SUCCESS
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def project_detail(request, pk):

    try:
        project = NewProject.objects.get(pk=pk)
    except NewProject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = newProjectserializers(project)
        return Response(serializer.data)


@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def project_update(request, pk):

    try:
        project = NewProject.objects.get(pk=pk)
    except NewProject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if project.author != user:
        return Response({"response": "You don't have permission to edit that."})

    if request.method == "PUT":
        serializer = newProjectserializers(project, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["response"] = UPDATE_SUCCESS

            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def is_author_of_project(request, pk):
    try:
        project = NewProject.objects.get(pk=pk)
    except NewProject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = {}
    user = request.user
    if project.author != user:
        data["response"] = "You don't have permission to edit that."
        return Response(data=data)
    data["response"] = "You have permission to edit that."
    return Response(data=data)


@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def project_delete(request, pk):

    try:
        project = NewProject.objects.get(pk=pk)
    except NewProject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if project.author != user:
        return Response({"response": "You don't have permission to delete that."})

    if request.method == "DELETE":
        operation = project.delete()
        data = {}
        if operation:
            data["response"] = DELETE_SUCCESS
        return Response(data=data)


class projectlist(ListAPIView):
    queryset = NewProject.objects.all()
    serializer_class = newProjectserializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


# ! DONT TOUCH THE CODE ABOVE

# ! CEMENT Compressive Test STARTS HERE


class cementListComp(ListAPIView):
    queryset = cementCompressive.objects.all()
    serializer_class = cementCompressiveSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


@permission_classes([])
@permission_classes((IsAuthenticated,))
@api_view(["POST"])
def cementCreateComp(request):
    if request.method == "POST":
        serializer = cementCompressiveSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            cements = serializer.save()
            data["response"] = CREATE_SUCCESS
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([])
@permission_classes((IsAuthenticated,))
@api_view(["GET"])
def cementDetailComp(request, pk):
    cements = cementCompressive.objects.get(id=pk)
    serializer = cementCompressiveSerializer(cements, many=False)
    return Response(serializer.data)


# ! UPDATE


@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def cementUpdateComp(request, PK):

    try:
        cements = NewProject.objects.get(PK=PK)
    except NewProject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if cements.author != user:
        return Response({"response": "You don't have permission to edit that."})

    if request.method == "PUT":
        serializer = cementCompressiveSerializer(
            cements, data=request.data, partial=True
        )
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["response"] = UPDATE_SUCCESS
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ! DELETE
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def cementDeleteComp(request, pk):

    try:
        cements = cementCompressive.objects.get(pk=pk)
    except cementCompressive.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if cements.author != user:
        return Response({"response": "You don't have permission to delete that."})
    if request.method == "DELETE":
        operation = cements.delete()
        data = {}
        if operation:
            data["response"] = DELETE_SUCCESS
        return Response(data=data)


# ! Let's Work on Results
@permission_classes([])
@permission_classes((IsAuthenticated,))
@api_view(["GET"])
def cementResultComp(request, pk):
    cements = cementCompressive.objects.get(id=pk)
    serializer = cementResultCompressiveSerializers(cements, many=False)
    return Response(serializer.data)


# ! Finally lets finish for the report
@permission_classes([])
@permission_classes((IsAuthenticated,))
@api_view(["GET"])
def cementReportComp(request, pk):
    cements = cementCompressive.objects.get(id=pk)
    serializer = reportInfoCementSerializers(cements, many=False)
    return Response(serializer.data)


#  ! Done with the Cement Compressive test
