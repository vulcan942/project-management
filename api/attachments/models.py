from django.db import models

class AttachmentModel(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='attachments/')
    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)