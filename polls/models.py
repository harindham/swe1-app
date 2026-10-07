import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @property
    def total_votes(self):
        return self.choice_set.aggregate(models.Sum('votes'))['votes__sum'] or 0


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    @property
    def vote_percent(self):
        total = self.question.total_votes
        if total == 0:
            return 0
        return round((self.votes / total) * 100)
