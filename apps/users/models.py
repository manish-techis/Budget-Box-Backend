from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255,null=False ,blank= False)

    email = models.EmailField(unique=True, null=False ,blank= False)

    password = models.CharField(max_length=30, null=False ,blank= False)

    budget= models.IntegerField( null=False, default=0 ,blank= False)

    token= models.CharField(max_length=255, null=False ,blank= False)

    token_expire = models.DateTimeField( null=False, ,blank= False)

    created_at = models.DateTimeField(auto_now_add=True, null=False ,blank= False)
    
    updated_at = models.DateTimeField(auto_now_add=True, null=False, )