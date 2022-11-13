from django.contrib.auth import login
from rest_framework import generics, status, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView
from .serializers import RegistrationSerializer
from users.serializers import UserSerializer

class RegisterUserView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
                    "token": AuthToken.objects.create(user)[1],
                    "user": UserSerializer(user, context=self.get_serializer_context()).data
                }, status=status.HTTP_201_CREATED)


class LoginUserView(LoginView):
    permission_classes = {permissions.AllowAny}

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        return Response({
            "token": AuthToken.objects.create(user)[1],
            "user": {
                "id": user.pk,
                "username": user.username,
                "email": user.email,
                "bio": user.bio,
            }
        }, status=status.HTTP_200_OK)