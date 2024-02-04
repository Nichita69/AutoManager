from rest_framework import routers

from apps.Paymet.views import PaymetViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'Paymet', PaymetViewSet, basename='Paymet')

urlpatterns = [
    *router.urls,
]
