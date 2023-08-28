from django.db import models


# Create your models here.

class Foto(models.Model):
    name = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    main_colour = models.CharField(max_length=50)
    landscape = models.BooleanField()

    def __str__(self):
        if(self.landscape==True):
            return "Nome foto: " + str(self.name) + ", scattata da: " + str(
                self.artist_name) + ", colore principale: " + str(self.main_colour) + ", ed è una foto landscape."
        else:
            return "Nome foto: " + str(self.name) + ", scattata da: " + str(
                self.artist_name) + ", colore principale: " + str(self.main_colour) + ", ed è una foto portrait."