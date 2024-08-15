from rest_framework.serializers import ModelSerializer
from .models import LabelModel

class LabelSerializer(ModelSerializer):
    class Meta:
        model = LabelModel
        fields = '__all__'
        