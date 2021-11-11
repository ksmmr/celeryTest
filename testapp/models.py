from django.db import models
from django.utils import timezone

# Create your models here.
class Day(models.Model):
    title = models.CharField("タイトル",max_length=200)
    text = models.TextField("本文")
    date = models.DateTimeField("日付",default=timezone.now)

class Number(models.Model):
    form1 = models.IntegerField(default=10)
    form2 = models.IntegerField(default=5)

class Progress(models.Model):
    now = models.IntegerField("現在の進捗", default=0)
    total = models.IntegerField("全ステップ数")

class Numbergen(models.Model):
    number1 = models.IntegerField(default=30)
    number2 = models.IntegerField(default=20)
    gen = models.IntegerField(default=100)