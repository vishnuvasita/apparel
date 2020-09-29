from django.db import models

# Create your models here.

class Register(models.Model):
    v_name = models.CharField(max_length=50, unique=True)
    v_email = models.EmailField(max_length=50, unique=True)
    v_password = models.CharField(max_length=20)
    v_r_password = models.CharField(max_length=20)
    v_verification_flag = models.BooleanField()

    def __str__(self):
        return self.v_name