from django.db import models

# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        (0, 'Manager'),
        (1, 'User'),
        (2, 'Publisher'),
        (3, 'Vip-user'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(blank=True, upload_to='avatars/')
    role = models.IntegerField(choices=ROLE_CHOICES, default=1)

    def __str__(self):
        return self.user_name

class Role(models.Model):
    name = models.CharField( 
        max_length = 40, 
        choices = User.ROLE_CHOICES, 
        default = 1) 

    def __str__(self):
        return self.name