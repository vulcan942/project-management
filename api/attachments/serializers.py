from rest_framework.serializers import ModelSerializer

from .models import AttachmentModel

class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = AttachmentModel
        fields = '__all__'