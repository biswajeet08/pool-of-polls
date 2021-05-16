from django.contrib.auth.models import User
from django.db import models

class Create_Poll(models.Model):
    heading = models.CharField("Question", max_length=150,blank=False)
    category = models.CharField(max_length=20, blank=False)
    item1 = models.CharField( max_length=100,blank=False)
    img1 = models.ImageField(upload_to="pics")
    item2 = models.CharField( max_length=100,blank=False)
    img2 = models.ImageField(upload_to="pics")
    item3 = models.CharField(max_length=100, blank=False)
    img3 = models.ImageField(upload_to="pics")
    item4 = models.CharField(max_length=100, blank=False)
    img4 = models.ImageField(upload_to="pics")
    count1 = models.IntegerField()
    count2 = models.IntegerField()
    count3 = models.IntegerField()
    count4 = models.IntegerField()
    total = models.IntegerField()
    percent1 = models.FloatField()
    percent2 = models.FloatField()
    percent3 = models.FloatField()
    percent4 = models.FloatField()


class Create_User(models.Model):
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

