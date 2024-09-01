from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Tweet(models.Model):
    choice = ( 
    ("Male", "Male"), 
    ("Female", "Female"), 
    ("others", "others"), 
) 
  
# declaring a Student Model  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    Gender = models.CharField(max_length = 20,choices = choice, default = 'others')
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]} - {self.Gender}'
    
