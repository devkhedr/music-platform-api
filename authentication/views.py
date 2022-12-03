from knox.auth import AuthToken
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from users.models import CustomUser as User
from .serializers import UserModelSerializer, UserRegiserSerializer
from .permissions import IsNotAuthenticated
# Create your views here.


class LoginView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer
    permission_classes = (IsNotAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)
        return Response({
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio
            }
        },  status=status.HTTP_201_CREATED)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegiserSerializer
    permission_classes = (IsNotAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = UserRegiserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        model_serializer = UserModelSerializer(data=serializer.data)
        model_serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.validated_data['username'], email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        _, token = AuthToken.objects.create(user)

        return Response({
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio
            }
        },  status=status.HTTP_201_CREATED)
