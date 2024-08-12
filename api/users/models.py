from django.db import models

class RoleModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class PermissionModel(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)
    resource = models.CharField(max_length=100)
    actions = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password_hash = models.CharField(max_length=100)
    role = models.ManyToManyField(RoleModel)
