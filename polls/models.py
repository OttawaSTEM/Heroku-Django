from django.db import models

class Question(models.Model):
    question_1 = models.CharField('Question 1', max_length=50, blank=True)