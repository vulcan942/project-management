from django.db import models

from django.contrib.auth.models import User

class WorkflowModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    steps = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)