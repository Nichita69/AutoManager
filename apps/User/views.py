from datetime import timedelta

from django.contrib.auth.models import User
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from str2bool import str2bool
from apps.User.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_superuser', 'is_staff']
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data.get('first_name', ''),
                is_staff=True
            )
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        now = timezone.now()
        interval = now - timedelta(hours=2)  # 2 Hours

        queryset = super(UserViewSet, self).get_queryset()
        if is_online := self.request.query_params.get("is_online", None):
            is_online = str2bool(is_online)

            queryset = (
                queryset.filter(Q(last_login__lte=interval) | Q(last_login__isnull=True))
                if not is_online
                else queryset.filter(Q(last_login__gte=interval))
            )
        return queryset
