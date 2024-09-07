from django.db import models

# Create your models here.
class Pet(models.model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank= True)
    descriptions = models.TextField()
    sex = models.CharField(max_length=1,choice=SEX_CHOICES,blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)

    vaccinations = models.ManyToManyField('Vaccine',blank = True)

class Vaccine(models.model):
    name = models.CharField(max_length=50)

