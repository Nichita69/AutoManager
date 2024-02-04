from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.common.views import CustomGenericViewSet
from apps.Paymet.models import Paymet
from apps.Paymet.serializers import PaymetSerializer


class PaymetViewSet(CustomGenericViewSet, ModelViewSet):
    serializer_class = PaymetSerializer
    queryset = Paymet.objects.all()
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
