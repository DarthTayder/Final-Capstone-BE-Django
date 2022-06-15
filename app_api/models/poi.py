from django.db import models

class Poi(models.Model) :
    
    name = models.CharField(max_length=75)
    
    def __str__(self):
        return self.name
