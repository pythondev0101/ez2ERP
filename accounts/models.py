from django.db import models
from django.contrib.auth.models import User
from ez2erp.models import Ez2ErpBaseModel


class Account(Ez2ErpBaseModel):
    name = models.CharField(max_length=64)
    is_paid = models.BooleanField(default=False)


class Branch(Ez2ErpBaseModel):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    updated_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Profile(Ez2ErpBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.RESTRICT)
    is_business_owner = models.BooleanField(default=False)

    @property
    def name(self):
        return f'{self.user.first_name} {self.user.last_name}'
