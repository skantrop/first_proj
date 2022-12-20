from django.db import models


# Create your models here.
class Cars(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='images')
    phone = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self) -> str:
        return f'{self.title}'


class Musician(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    psevdonim = models.CharField(max_length=100, blank=True)

    def __str__(self):
        if self.psevdonim:
            return f'{self.psevdonim}'
        return f'{self.name} {self.last_name}'


class Award(models.Model):
    owner = models.ForeignKey(Musician, on_delete=models.CASCADE,
                              related_name='award', unique=True)
    year = models.DateField()
    nomination = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.owner} - {self.year} - {self.nomination}'


class Song(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Musician, on_delete=models.CASCADE,
                               related_name='songs')
    feat = models.ForeignKey(Musician, on_delete=models.SET_NULL, null=True,
                             related_name='feats', blank=True)
    poster = models.ImageField(upload_to='images/')
    year = models.DateField()

    def __str__(self):
        if self.feat:
            return f'{self.author} - {self.title} feat. {self.feat}'
        return f'{self.author} - {self.title}'
