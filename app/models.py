from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = CloudinaryField("image",null=True)
    bio = models.TextField(max_length=300)
    contact = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proj_name =models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = CloudinaryField('image')
    repo_url = models.URLField(null=True) 
    live_link = models.URLField(null=True)

    def __str__(self):
        return f'{self.user.username} '