from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    challenges_solved = models.IntegerField()
    level = models.IntegerField()
    pub_date = models.DateTimeField('date published')


class Expertise(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    skill = models.CharField(max_length=200)
    level = models.IntegerField(default=0)

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)