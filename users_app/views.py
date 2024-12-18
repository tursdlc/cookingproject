from rest_framework import viewsets
from users_app.models import User
from users_app.serializer import UserSerializer


# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()



