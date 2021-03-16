from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    deleted = models.IntegerField(default=0)
    deleted_at = models.DateTimeField(blank=True, null=True)
    last_time = models.DateTimeField(verbose_name=u'最后操作时间', auto_now=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

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
