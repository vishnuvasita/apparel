from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
import random

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(default='')

    def __str__(self):
        return self.name


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,1000)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "users/{final_filename}".format(final_filename=final_filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    phone = models.IntegerField(default=None, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(default=3, null=True,blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    img = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    join_date =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = Profile(user=user)
#         profile.save()


# @receiver(post_save, sender=User)
# def create_user_profile(sender,instance,created, **kwargs):
#     if created:
#         Profile.objects.create(user = instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance , **kwargs):
#     instance.profile.save()
