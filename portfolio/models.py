from django.db import models

# Create your models here.
class Project(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=250)
    gambar = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.judul
