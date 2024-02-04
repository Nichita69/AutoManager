from rest_framework import routers

from apps.Auto.views import AutoViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'Auto', AutoViewSet, basename='Auto')

urlpatterns = [
    *router.urls,
]
