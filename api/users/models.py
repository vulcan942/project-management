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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100)
    password_hash = models.CharField(max_length=100)
    role = models.ManyToManyField(RoleModel)
