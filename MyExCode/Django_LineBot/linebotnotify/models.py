from django.db import models

# Create your models here.


class User_Info(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    userId = models.TextField()
    userType = models.TextField(null=True)
    accessToken = models.TextField()
