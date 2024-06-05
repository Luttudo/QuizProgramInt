# user_registration_api/users/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)  # Use um campo seguro para senhas

    def __str__(self):
        return self.username

# user_registration_api/users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

# user_registration_api/users/views.py
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

# user_registration_api/users/urls.py
from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]
