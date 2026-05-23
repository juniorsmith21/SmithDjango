from rest_framework.viewsets import ModelViewset
from users.api.serializers import UserSerializer
from users.models import User




class userApiViewset(ModelViewset):
    serializers_class=UserSerializer
    queryset= User.objects.all()