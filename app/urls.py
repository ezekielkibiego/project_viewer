
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:project_id>', views.like, name='like'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='index'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),

]