from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField (max_length=20)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField()
def _str_(self):
    return self.title
