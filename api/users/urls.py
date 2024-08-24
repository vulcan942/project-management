from .views import UserView
from rest_framework.routers import DefaultRouter
from django.urls import path
router = DefaultRouter()
router.register('users', UserView)

urlpatterns = [
    path(r'users/', UserView.as_view({'get': 'list'}), name='user-list'),
    path(r'users/<int:pk>/', UserView.as_view({'get': 'retrieve','put':'update','delete':'destroy'}), name='user-detail'),
]