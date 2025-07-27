from rest_framework.viewsets import ModelViewSet
from .models import UserEntry
from .serializers import UserSerializer

#the basic, required view for now
class UserViewSet(ModelViewSet):
    queryset = UserEntry.objects.all().order_by('-score')
    serializer_class = UserSerializer
