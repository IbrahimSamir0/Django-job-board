from email.policy import default
from enum import auto
from pydoc import describe
from random import choices
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

# Create your models here.
class Job(models.Model):
    # title
    title = models.CharField(max_length=100)    
    # location
    job_type =models.CharField(max_length=20,  choices=JOB_TYPE)
    describtion = models.TextField(max_length=1000)
    published_at= models.DateTimeField(auto_now=True)
    vacancy =models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)

    def __str__(self) :
        return self.title