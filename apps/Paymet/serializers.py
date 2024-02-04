from rest_framework import serializers

from apps.Paymet.models import *


class PaymetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paymet
        fields = '__all__'
