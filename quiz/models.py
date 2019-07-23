from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    hashcode = models.CharField(max_length=50)
    quiz_url = models.URLField(max_length=200, null=True, blank=True, unique=True)
    answer = models.CharField(default="", max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    opt1 = models.CharField(max_length=50)
    opt2 = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)+"번 문제"

class Challenger(models.Model):
    user_obj = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    result = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-result', 'name']
