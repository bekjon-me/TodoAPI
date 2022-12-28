from django.db import models
from django.contrib.auth.models import User
from .utils import cal_key
# Create your models here.


class Project(models.Model):
    "Model for Projects"
    upid = models.PositiveIntegerField()  # user-project-id
    user = models.ForeignKey(
        User, related_name='projects', on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['upid', 'user']

    def __str__(self) -> str:
        return str(
            f"User:{self.user} ID:{self.upid} Name:{self.name} "
            f"(Date:{self.created.strftime('%m/%d/%Y|%H:%M:%S')})"
        )

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            upid = cal_key(self.user, Project)
            self.upid = upid
        return super(Project, self).save(*args, **kwargs)
