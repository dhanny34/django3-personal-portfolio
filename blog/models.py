from django.db import models

# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=250)
    tanggal = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.judul
