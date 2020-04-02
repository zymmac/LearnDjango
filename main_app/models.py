from django.db import models

# Create your models here.
class Shiba(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    birthday = models.DateField()

    def __str__(self):
        return "{} ({}) / {}".format(self.name, self.color,str(self.birthday))
