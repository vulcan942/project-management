from rest_framework.serializers import ModelSerializer
from .models import WorkflowModel

class WorkflowSerializer(ModelSerializer):
    class Meta:
        model = WorkflowModel
        fields = '__all__'