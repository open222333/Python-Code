from django.db import models
import uuid

# Create your models here.


class users(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    account = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    token_key = models.UUIDField(default=uuid.uuid4)
    accountState_tuple = ('Active', 'Disable')
    accountState = models.TextField(choices=accountState_tuple)
