from django.db import models

# Create your models here.
 
class Transaction(models.Model):

    name= models.CharField(max_length=200, null=False ,blank= False)

    user= models.ForeignKey('users.User', on_delete=models.CASCADE)

    category = models.ForeignKey('categories.Categories', on_delete=models.CASCADE)

    type = models.CharField(max_length=50, null=False ,blank= False)

    amount = models.IntegerField(null=False ,blank= False)

    date = models.DateField(auto_now_add=True, null=False ,blank= False)

    created_at = models.DateTimeField(auto_now_add=True, null=False ,blank= False)

    updated_at = models.DateTimeField(auto_now_add=True, null=False,blank= False )
    
