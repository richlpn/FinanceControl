from django.db import models


class user_login_Model(models.Model):
    username = models.CharField(max_length=50,
                                default='username')
    password = models.CharField(max_length=25,
                                default='password')
    mail = models.CharField(max_length=120,
                                default='')
    joined_at = models.DateField(max_length=25,
                                auto_created=True)


# Create your models here.
