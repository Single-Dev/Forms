from django.shortcuts import render
from .serializers import *
from forms.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, filters, generics

# ----------------------------- Users API ----------------------------- #
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UsersApiView(request):
    user = CustomUser.objects.all()
    serializer = UsersApi(user, many=True)
    return Response(serializer.data)
# ----------------------------- Users API ----------------------------- #