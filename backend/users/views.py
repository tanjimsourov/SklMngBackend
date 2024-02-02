from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .models import User
from .otp import generateKey
from .serializers import SuperUserSerializer


class SuperuserRegister(GenericAPIView):
    authentication_classes = []
    serializer_class = SuperUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if User.objects.filter(is_superuser=True).exists():
                return response.Response({'message': "You can't register for admin"},
                                         status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data['token'], status=status.HTTP_201_CREATED)
        else:
            return response.Response({"Fuck You"}, status=status.HTTP_200_OK)


class LoginAPIView(GenericAPIView):
    authentication_classes = []

    def post(self, request):
        phone = request.data.get('phone', None)
        password = request.data.get('password', None)
        user = authenticate(username=phone, password=password)

        if user:
            return response.Response({"phone": user.phone, "username": user.username, "token": user.token},
                                     status=status.HTTP_200_OK)
        return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)
