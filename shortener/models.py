from django.db import models

# Create your models here.
class Url(models.Model):
    link=models.URLField
    urlid=models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)

def __str__(self):
    return ("Short Url for: "+self.link +" is "+self.urlid)