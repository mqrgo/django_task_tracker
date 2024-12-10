from django.db import models

from task_tracker import consts, models as task_models


class CompletedTaskManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:  # NOQA ANN201
        return task_models.Task.objects.filter(status=consts.TaskStatus.COMPLETED)


class UncompletedTask(models.Manager):
    def get_queryset(self) -> models.QuerySet:  # NOQA ANN201:
        return task_models.Task.objects.exclude(status=consts.TaskStatus.COMPLETED)
