from django.contrib import admin
from .attachments.models import AttachmentModel
from .projects.models import ProjectModel
from .tasks.models import TaskModel
from .users.models import UserModel
from .labels.models import LabelModel
from .comments.models import CommentModel
from .sprints.models import SprintModel
from .statuses.models import StatusModel
from .workflows.models import WorkflowModel

admin.site.register(AttachmentModel)
admin.site.register(ProjectModel)
admin.site.register(TaskModel)
admin.site.register(UserModel)
admin.site.register(LabelModel)
admin.site.register(CommentModel)
admin.site.register(SprintModel)
admin.site.register(StatusModel)
admin.site.register(WorkflowModel)
