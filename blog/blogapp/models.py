from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length = 200)
  description = models.TextField()
  author = models.CharField(max_length = 100)
  published_date = models.DateTimeField(auto_now_add=True)
  edited_date = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to = "images/", null = True, blank= True,default = "images/default.webp")

