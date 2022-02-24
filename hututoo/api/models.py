from django.db import models


class QuizCategory(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateField()

    def __str__(self):
        return self.name


class Quizs(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField()
    options = models.BooleanField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name