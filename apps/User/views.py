from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated, AllowAny

from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from str2bool import str2bool

from apps.User.serializers import UserSerializer, LoginSerializer, RegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_superuser', 'is_staff']
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = User.objects.create_user(
                username=validated_data['email'],
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                is_active=False
            )
            return Response({"code": 201, "message": "Wait until administrator will approve your account"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = User.objects.filter(email=email).first()
            if user is not None and user.check_password(password):
                if user.is_active:
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    expiration = datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
                    return Response({
                        "user_id": user.id,
                        "user_name": user.username,
                        "user_email": user.email,
                        "role": "admin" if user.is_superuser else "user",
                        "jwt_token": token,
                        "expiration": expiration
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Your account is not active"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
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
