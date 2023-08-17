from django.db import models
# Create your models here.
class userdet(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    psw=models.CharField(max_length=20)

class admindet(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    psw=models.CharField(max_length=20)

"""
class employee(models.Model):
    emid = models.IntegerField(primary_key=True)
    desig = models.CharField(max_length=30)
    file = models.FileField()
"""

class feedback(models.Model):
    fid = models.IntegerField(primary_key=True, auto_created=True)
    fname=models.CharField(max_length=100)
    emailid = models.CharField(max_length=70)
    contactno=models.CharField(max_length=20)
    feedback = models.TextField()
    status=models.BooleanField()

