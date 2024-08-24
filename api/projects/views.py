from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import ProjectModel
from .serializers import ProjectSerializer

class ProjectView(ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer
    authentication_class = [IsAuthenticated]