from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import SprintModel
from .serializers import SprintSerializer


class SprintView(ModelViewSet):
    queryset = SprintModel.objects.all()
    serializer_class = SprintSerializer
    permission_classes = [IsAuthenticated]