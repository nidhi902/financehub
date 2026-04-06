from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Financedata(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    amount=models.IntegerField()
    category=models.CharField(max_length=100)
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE)
    uploaded_at=models.DateTimeField(auto_now_add=True)