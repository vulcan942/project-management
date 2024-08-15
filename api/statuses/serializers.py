from rest_framework.serializers import ModelSerializer
from .models import StatusModel

class StatusSerializer(ModelSerializer):
    class Meta:
        model = StatusModel
        fields = '__all__'