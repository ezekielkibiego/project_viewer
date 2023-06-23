from django.db.models import fields
from .models import *
from django.forms import ModelForm
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','contact')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']