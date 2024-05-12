from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


def attachment_path(instance, filename):
    return 'otazkakmaturite/' + str(instance.film.id) + '/attachments/' + filename


class predmet(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nazev předmětu',
    help_text='Přidej k maturitní otázce předmět (PVY, PRP)')

    class Meta:
        verbose_name = 'předmět'
        verbose_name_plural = 'předmět'
        ordering = ['name']

    def __str__(self):
        return self.name


class otazkakmaturite(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    plot = models.TextField(blank=True, null=True, verbose_name='Plot')
    release_date = models.DateField(blank=True, null=True,
                                    help_text='Please use the following format: <em>YYYYMM-DD</em>.',
                                    verbose_name='Release date')
    runtime = models.IntegerField(blank=True, null=True,
                                  help_text='Please enter an integer value (minutes)',
                                  verbose_name='Runtime')
    poster = models.ImageField(upload_to='film/posters/%Y/%m/%d/', blank=True, null=True,
                               verbose_name="Poster")
    rate = models.FloatField(default=5.0,
                             validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],
                             null=True, help_text='Please enter an float value (range 1.0 - 10.0)',
                             verbose_name='Rate')
    genres = models.ManyToManyField(predmet, help_text='Zvol předmět pro tuto maturitní otázku')

    class Meta:
        verbose_name = 'otazkakmaturite'
        verbose_name_plural = 'otazkakmaturite'
        ordering = ['-release_date', 'title']

    def __str__(self):
        return f'{self.title}, year: {str(self.release_date.year)}, rate:{str(self.rate)}'

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name='File')
    TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other'),
    )
    type = models.CharField(max_length=10, choices=TYPE_OF_ATTACHMENT, blank=True,
        default='image', help_text='Select allowed attachment type',
        verbose_name='Attachment type')
    film = models.ForeignKey(otazkakmaturite, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Příloha'
        verbose_name_plural = 'Přílohy'
        ordering = ['-last_update', 'type']

    def __str__(self):
        return f'{self.title}, ({self.type})'

