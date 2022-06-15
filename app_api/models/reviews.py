from django.db import models
from django.contrib.auth.models import User

class Reviews(models.Model):
    
    content = models.CharField(max_length=75)
    campsite = models.ForeignKey("Campsites", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    