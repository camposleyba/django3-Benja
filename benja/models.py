from django.db import models

class Foto(models.Model):

    # Podemos ver todos los tipos que necesitamos usar aca: https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types
    title = models.CharField(max_length=100) # Charfield, A string field, for small- to large-sized strings.
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='benja/images/') # Field para imagenes
    week = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.title

class Video(models.Model):

    # Podemos ver todos los tipos que necesitamos usar aca: https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types
    title = models.CharField(max_length=100) # Charfield, A string field, for small- to large-sized strings.
    description = models.CharField(max_length=250)
    video = models.FileField(upload_to='benja/videos/') # Field para imagenes
    week = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.title
