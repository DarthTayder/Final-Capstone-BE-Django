from django.db import models
from django.contrib.auth.models import User

class Campsites(models.Model):
    
    name = models.CharField(max_length=75)
    address = models.CharField(max_length=75)
    poi = models.ForeignKey("Poi", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="added_campsites")
    userLists = models.ManyToManyField(User, through="UserList", related_name="campsites")

    def __str__(self):
        return self.name
