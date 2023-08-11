from django.db import models
from django.contrib.auth.models import User

class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True)
    user_img=models.ImageField(null=True,blank=True,upload_to="images/")
    username=models.CharField(max_length=15 , unique=True )
    first_name=models.CharField(max_length=20 ,null=False)
    last_name=models.CharField(max_length=20,null=False)
    gender=models.CharField(max_length=8)
    email=models.EmailField(max_length=25,unique=True)
    phone_number=models.CharField(max_length=11 , unique=True)
    password=models.CharField(max_length=25)


class Blog(models.Model):
    title=models.CharField(max_length=50,null=True)
    blog=models.TextField(max_length=200,null=True)
    post_img=models.ImageField(null=True,blank=True,upload_to="blogs/")
    timestamp=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(Userinfo,null=False , on_delete=models.CASCADE )


    class Meta:
            ordering = ['-timestamp']
