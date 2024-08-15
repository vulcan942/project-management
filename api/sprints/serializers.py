from rest_framework.serializers import ModelSerializer
from .models import SprintModel

class SprintSerializer(ModelSerializer):
    class Meta:
        model = SprintModel
        fields = '__all__'