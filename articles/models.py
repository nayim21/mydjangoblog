from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title=models.CharField (max_length=20)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField()
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
def _str_(self):
    return self.title
