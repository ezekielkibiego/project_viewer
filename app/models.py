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
    image = CloudinaryField('proj')
    repo_url = models.URLField(null=True) 
    live_link = models.URLField(null=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return f'{self.user.username} '
    
    @property
    def number_of_likes(self):
        return self.likes.count()

LIKE_CHOICES={
    ('Like','Like'),
    ('Unlike','Unlike',)
}

class Like(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,  related_name='project')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

    def _str_(self):
        return self.value