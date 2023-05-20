from django.db import models

# Create your models here.


class Categories(models.Model):
    

    name= models.CharField(max_length=200, null=False ,blank= False)

    color_code = models.CharField(max_length=50, null=False ,blank= False)

    created_at = models.DateTimeField(auto_now_add=True, null=False ,blank= False)

    updated_at = models.DateTimeField(auto_now_add=True, null=False ,blank= False)
    