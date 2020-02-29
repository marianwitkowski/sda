from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# przyklad relacji jeden-do-wielu (one-2-many)
class Comment(models.Model):
    body = models.TextField()
    stars = models.IntegerField(default=1,
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

class Director(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name = "reżyser"
        verbose_name_plural = "reżyserzy"

class Actor(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name = "aktor"
        verbose_name_plural = "aktorzy"

class Movie(models.Model):
    MPAA = (
        ('-', 'Brak'),
        ('G', "Rating G"),
        ('PG-13', "Rating PG-13"),
        ('NC-17', "Rating NC-17")
    )

    title = models.CharField(max_length=256, verbose_name="Pełny tytuł filmu")
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    imdb = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(null=True, blank=True)
    trailer_video = models.URLField(null=True, blank=True)
    # dodano pole przechowujace biezacy timestamp
    created = models.DateTimeField(auto_now_add=True, editable=False)
    mpaa_rating = models.CharField(choices=MPAA, max_length=5, default='X')

    #relacja M2M dla aktora
    actors = models.ManyToManyField('Actor', related_name="movies")

    def __str__(self):
        return f"{self.title} - {self.year}"

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"
