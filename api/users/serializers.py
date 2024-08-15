from rest_framework.serializers import ModelSerializer
from .models import UserModel

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined','role')
