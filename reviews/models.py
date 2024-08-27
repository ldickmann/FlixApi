from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, 'A Avaliação não pode ser inferior a 1 estrelas'),
            MaxValueValidator(5, 'A Avaliação não pode ser superior a 5 estrelas')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.movie.title} - {self.stars}'
