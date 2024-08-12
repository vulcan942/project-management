from django.db import models

from ..users.models import UserModel

class WorkflowModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    steps = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)