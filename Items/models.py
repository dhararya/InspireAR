from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=7)
    items = models.TextField(default="")
    links = models.TextField(default="")

    def __str__(self):
        return  str(self.userid)

class Task(models.Model):
    #task name
    title = models.CharField(max_length=200)

    #Priority Level
    LOW = 1
    MODERATE = 2
    HIGH = 4
    DIFFICULTY = [
        (LOW, ('Low Priority Task')),
        (MODERATE, ('Medium Priority Task')),
        (HIGH, ('High Priority Task')),
    ]
    difficulty = models.PositiveIntegerField(
        choices = DIFFICULTY,
    )

    #Number of hours to complete task
    time = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    #coin_value
    coin_value = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

