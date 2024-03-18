from apps.User.views import UserViewSet
from django.urls import path
from rest_framework import routers



# Create your patterns here.

app_name = "User"  # noqa

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"User", UserViewSet, basename="User")

urlpatterns = [
    *router.urls,
]