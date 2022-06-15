from django.db import models
from django.contrib.auth.models import User

class UserList(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campsiteId = models.ForeignKey("Campsites", on_delete=models.CASCADE)