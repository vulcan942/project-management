from django.db import models

from django.contrib.auth.models import User
from ..attachments.models import AttachmentModel
from ..tasks.models import TaskModel

class CommentModel(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    attachments = models.ManyToManyField(AttachmentModel, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)