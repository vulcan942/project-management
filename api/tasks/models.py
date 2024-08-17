from django.db import models
from ..attachments.models import AttachmentModel
from ..statuses.models import StatusModel
from ..sprints.models import SprintModel
from django.contrib.auth.models import User


class TaskModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    attachments = models.ManyToManyField(AttachmentModel,blank=True)
    status = models.ForeignKey(StatusModel, on_delete=models.CASCADE)
    sprint = models.ForeignKey(SprintModel, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)