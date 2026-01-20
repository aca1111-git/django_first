from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        # return self.question_text   # object로 보이지 않고 문자열로 보임
        return f"{self.id} - {self.question_text} - {self.pub_date}"
        
    def was_published_recently(self):
        from django.utils import timezone
        import datetime
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

