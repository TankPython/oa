from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    deleted = models.IntegerField(default=0)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False, soft=True):
        if soft:
            self.deleted = 1
            self.deleted_at = timezone.now()
            self.save()
        else:
            self.delete()
            self.save()
