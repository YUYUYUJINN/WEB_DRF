from django.db import models
from rest_framework.authtoken.admin import User



class Ware(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
