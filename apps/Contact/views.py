from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.common.views import CustomGenericViewSet
from apps.Contact.models import Contact
from apps.Contact.serializers import ContactSerializer


class ContactViewSet(CustomGenericViewSet, ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = (IsAuthenticated,)
    ordering = '-updated_at'
    filterset_fields = '__all__'
    search_fields = '__all__'
    serializers_by_action = {
        'default': serializer_class,
    }
    permission_by_action = {
        'default': permission_classes,
    }
