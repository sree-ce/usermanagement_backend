from django import views
from django.urls import include

from django.urls import path
from users.views import UserResgisterView, MyTokenObtainPairView, UserManageView, UserView
from rest_framework.routers import DefaultRouter
from users.views import UserManageView

u = DefaultRouter()
u.register(r'user', UserManageView, basename='user')


urlpatterns = [
    path('signup/', UserResgisterView.as_view(), name='signup'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    # path('users', UserView.as_view(), name='users'),
    # path('users/<int:id>', UserManageView.as_view(), name='users'),
    path('users/', include(u.urls))
]
