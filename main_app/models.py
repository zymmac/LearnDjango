from django.db import models

# Create your models here.
class Shiba(models.Model):
    colors = [
        ("Black and Tan", "Black and Tan"),
        ("Red", "Red"),
        ("Cream", "Cream"),
        ("Sesame", "Sesame"),
        ]

    name = models.CharField(max_length=128)
    color = models.CharField(max_length=13,choices=colors, default="Red")
    birthday = models.DateField()

    def __str__(self):
        return "{} ({}) / {}".format(self.name, self.color,str(self.birthday))
