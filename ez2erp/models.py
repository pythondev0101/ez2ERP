from django.db import models


class Ez2ErpBaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
