from django.db import models
from ..projects.models import ProjectModel
class SprintModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    