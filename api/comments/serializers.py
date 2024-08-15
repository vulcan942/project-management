from rest_framework.serializers import ModelSerializer
from .models import CommentModel

class CommentSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'