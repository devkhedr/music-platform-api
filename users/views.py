from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status, permissions


User = get_user_model()


class UserView(APIView):

    permission_classes = {permissions.IsAuthenticatedOrReadOnly}

    def get(self, request, *args, **kwargs):
        User = get_user_model()
        id = int(kwargs['pk'])
        is_exist = User.objects.filter(id=id).exists()
        if is_exist == True:
            serializer = UserSerializer(User.objects.get(id=id))
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        User = get_user_model()
        id = int(kwargs['pk'])
        if request.user.id != id:
            return Response({"id": "invalid user id"})
        serializer = UserSerializer(User.objects.get(
            id=id), data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        User = get_user_model()

        id = int(kwargs['pk'])
        if request.user.id != id:
            return Response({"id": "invalid user id"})
        serializer = UserSerializer(User.objects.get(
            id=id), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
