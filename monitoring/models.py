from django.db import models


class User(models.Model):
    username = models.TextField()
    full_name = models.TextField()
    contact = models.TextField()


class ServerLogin(models.Model):
    server_name = models.TextField()
    server_ip = models.GenericIPAddressField()
    user = models.ForeignKey(User)
    login_time = models.DateTimeField()
