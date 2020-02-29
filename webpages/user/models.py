from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):

    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    Gender=models.CharField(max_length=10)
    Address=models.TextField(max_length=250)

class Question(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('question_detail', args=[self.slug])

    def __str__(self):
        return self.title

class Answer(models.Model):
    post=models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='answers')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    answer=models.TextField()
    likes=models.ManyToManyField(User, related_name='likes', blank=True)
    created=models.DateTimeField(auto_now_add=True)
    approved=models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('question_detail', args=[self.id] )


    def approved(self):
        self.approved=True
        self.save()
    def __str__(self):
        return self.user.username
