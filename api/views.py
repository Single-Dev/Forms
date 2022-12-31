from django.shortcuts import render
from .serializers import *
from forms.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, filters, generics

# ----------------------------- Users API ----------------------------- #
# ----------------------------- All User API
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UsersApiView(request):
    users = CustomUser.objects.all()
    serializer = UsersApi(users, many=True)
    return Response(serializer.data)
# ----------------------------- All User API
# ----------------------------- View User
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UserProfileApi(request, username):
    user = CustomUser.objects.get(username=username)
    serializer = UsersApi(user, many=False)
    return Response(serializer.data)
# ----------------------------- View User
# ----------------------------- Users API ----------------------------- #

# ----------------------------- Forms API ----------------------------- #
# ----------------------------- All Form API
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def FormsApiView(request):
    forms = Form.objects.all()
    serializer = FormsApi(forms, many=True)
    return Response(serializer.data)
# ----------------------------- All Form API
# ----------------------------- One Form API
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def OneFormApiView(request, slug):
    form = Form.objects.get(slug=slug)
    serializer = FormsApi(form, many=False)
    return Response(serializer.data)
# ----------------------------- One Form API
# ----------------------------- Forms API ----------------------------- #

# ----------------------------- Form Request API ----------------------------- #
# ----------------------------- Requests View
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def RequestsApiView(request):
    requests = FormRequest.objects.all()
    serializer = RequestsApi(requests, many=True)
    return Response(serializer.data)
# ----------------------------- Requests View
# ----------------------------- Form Request API ----------------------------- #