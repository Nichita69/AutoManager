from rest_framework import routers

from apps.Contact.views import ContactViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'Contact', ContactViewSet, basename='Contact')

urlpatterns = [
    *router.urls,
]
