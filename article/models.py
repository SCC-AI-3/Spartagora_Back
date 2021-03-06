from django.db import models
from django.forms import CharField
from user.models import User
# Create your models here.

# like 모델,tag 앱 논의 필요

class Comment(models.Model):
    content = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)


class UpperCategory(models.Model):    
    upper_category = models.CharField(max_length=100)

    def __str__(self):
        return self.upper_category


class LowerCategory(models.Model):
    upper_category = models.ForeignKey(UpperCategory, on_delete=models.CASCADE)
    lower_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.lower_category


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.CharField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    lower_category = models.ForeignKey(LowerCategory, on_delete=models.CASCADE)
    



# class Like(models.Model):
#     article = models.ForeignKey(Article)
#     user = models.ForeignKey(User)