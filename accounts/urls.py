from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

# router.register(r'user-preferences', )

urlpatterns = [
    path('',include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='user-list'),

]
