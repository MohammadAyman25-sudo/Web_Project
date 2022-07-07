from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=255, unique=True)
  ID =  models.IntegerField(primary_key=True)
  birth=models.DateField()
  gpa= models.DecimalField(max_digits=3,decimal_places=2)
  male=models.BooleanField()
  female=models.BooleanField(default=False)
  level=models.CharField(max_length=100)
  active=models.BooleanField()
  inactive=models.BooleanField(default=False)
  dep=models.CharField(max_length=255)
  mail=models.CharField(max_length=255)
  phone=models.CharField(max_length=255)

class Employee(models.Model):
    Username = models.CharField(max_length=255, unique=True)
    mail=models.CharField(max_length=255,primary_key=True)
    password=models.CharField(max_length=255)
    logedin = models.BooleanField(default=False)