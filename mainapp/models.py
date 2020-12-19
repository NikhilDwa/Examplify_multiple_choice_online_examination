from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Questions(models.Model):
    question = models.TextField(max_length=200, default="")
    option1 = models.CharField(max_length=50, default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    mark = (('option1', 'option1'), ('option2', 'option2'), ('option3', 'option3'), ('option4', 'option4'))
    answer = models.CharField(max_length=10, choices=mark, default="")
    exam = models.ForeignKey(Exam, on_delete=True)

    def __unicode__(self):
        return self.question

    def __str__(self):
        return self.question
