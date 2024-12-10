from django.db import models
from rest_framework.exceptions import ValidationError

from task_tracker import consts, managers


def get_file_path(instance, filename):
    return f"{instance.author.username}/tasks/{instance.id}/{filename}"


class BaseModel(models.Model):
    dc = models.DateTimeField("дата создания", auto_now_add=True)
    dm = models.DateTimeField("дата изменения", auto_now=True)

    class Meta:
        abstract = True


class Task(BaseModel):
    title = models.CharField("название", max_length=255)
    author = models.ForeignKey(
        "auth.User",
        verbose_name="автор",
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    description = models.TextField("описание", blank=True)
    complete_by_date = models.DateTimeField("выполнить до", blank=True, null=True)
    file = models.FileField(
        "файл",
        upload_to=get_file_path,
        blank=True,
        null=True,
    )
    importance_status = models.CharField(
        "статус",
        max_length=255,
        choices=consts.TaskImportanceStatus.CHOICES,
        default=consts.TaskImportanceStatus.MEDIUM,
    )
    status = models.CharField(
        "статус выполнения",
        max_length=255,
        choices=consts.TaskStatus.CHOICES,
        default=consts.TaskStatus.PENDING,
    )

    # managers
    objects = models.Manager()
    completed = managers.CompletedTaskManager()
    uncompleted = managers.CompletedTaskManager()

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"
        ordering = ["-dc"]

    def __str__(self):
        return self.title

    def clean(self):
        if self.complete_by_date and self.dc <= self.complete_by_date:
            raise ValidationError("Конечная дата не может быть до даты создания задачи")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
