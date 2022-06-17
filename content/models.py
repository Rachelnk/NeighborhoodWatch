from django.db import models
from django.contrib.auth.models import User
from cloudinary import CloudinaryImage

# Create your models here.
class Profile(models.Model):

class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title', null=True)
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', null = True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile', null =True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created', null= True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated', null= True)

    def __str__(self):
      return str(self.title)

    def save_post(self):
      self.save()

    def delete_post(self):
      self.delete()

    @classmethod
    def all_posts(cls):
      return cls.objects.all()
    
    @classmethod
    def searcg_posts(cls, title):
      return cls.objects.filter(title__icontains=title).all()
    class Meta:
      verbose_name_plural = 'Posts'

