# urls.py
from django.urls import path
from apps.Auto.views import UserViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('auth/login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('auth/register/', UserViewSet.as_view({'post': 'post'}), name='user-register'),
]
