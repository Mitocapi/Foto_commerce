from django.db import models


# Create your models here.

from django.db import models


class Foto(models.Model):
    COLOUR_CHOICES = [
        ("Black", "Black"),
        ("Dark Blue", "Dark Blue"),
        ("Green", "Green"),
        ("Grey", "Grey"),
        ("Light Blue", "Light Blue"),
        ("Orange", "Orange"),
        ("Pink", "Pink"),
        ("Purple", "Purple"),
        ("Red", "Red"),
        ("White", "White"),
        ("Yellow", "Yellow"),
    ]

    name = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    main_colour = models.CharField(max_length=20, choices=COLOUR_CHOICES)
    landscape = models.BooleanField()
    actual_photo = models.ImageField(upload_to='static/photos')
    def __str__(self):
        if(self.landscape==True):
            return "Nome foto: " + str(self.name) + ", scattata da: " + str(
                self.artist_name) + ", colore principale: " + str(self.main_colour) + ", ed è una foto landscape."
        else:
            return "Nome foto: " + str(self.name) + ", scattata da: " + str(
                self.artist_name) + ", colore principale: " + str(self.main_colour) + ", ed è una foto portrait."