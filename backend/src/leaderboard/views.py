from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

Users = get_user_model()

# User register POST request, if user doesnt exist
@api_view(["POST"])
def Register(request: Request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if Users.objects.filter(username=username).exists():
        return Response({"error":"Username already taken!"}, status=400)

    user = Users.objects.create_user(username=username, email=email, password=password)
    return Response({"message": "User registered!"}, status=201)

# The basic & required view for now, with authentication check
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Users.objects.all().order_by('-score')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
