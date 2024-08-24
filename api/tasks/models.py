from django.db import models
from ..attachments.models import AttachmentModel
from ..statuses.models import StatusModel
from ..sprints.models import SprintModel
from ..labels.models import LabelModel
from django.contrib.auth.models import User


class TaskModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    attachments = models.ManyToManyField(AttachmentModel,blank=True)
    status = models.ForeignKey(StatusModel, null=True, on_delete=models.SET_NULL)
    assigned_to = models.ManyToManyField(User,related_name='tasks')
    sprint = models.ManyToManyField(SprintModel, related_name='tasks')
    labels = models.ManyToManyField(LabelModel, related_name='tasks')
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)