
from cgitb import reset
from functools import partial
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from users.models import UserRegistration
from users.serializer import UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework import viewsets

# Create your views here.


class UserResgisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print("xcvbn")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserView(APIView):
    def get(self, request):
        print("sdfghjk")
        users = UserRegistration.objects.all().order_by('-date_joined')

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# class UserManageView(APIView):

#     def get(self, request, id):

#         try:
#             users = UserRegistration.objects.get(id=id)
#         except UserRegistration.DoesNotExist:
#             return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(users)
#         return Response(serializer.data)

#     def put(self, request, id):

#         users = UserRegistration.objects.get(id=id)
#         serializer = UserSerializer(users, data=request.data, partial=False)
#         print(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             print(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         users = UserRegistration.objects.get(id=id)
#         users.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserManageView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserRegistration.objects.filter(
        is_superuser=0).order_by('-date_joined')
    print(queryset)
