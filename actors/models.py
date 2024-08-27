from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil'),
    ('JP', 'Japão'),
    ('KR', 'Coréia do Sul'),
    ('CN', 'China'),
    ('IN', 'India'),
    ('UK', 'Inglaterra'),
    ('FR', 'França'),
    ('IT', 'Italia'),
    ('DE', 'Alemanha'),
    ('CA', 'Canada'),
    ('AU', 'Australia'),
    ('CO', 'Colombia'),
    ('CL', 'Chile'),
    ('BO', 'Bolivia'),
    ('UY', 'Uruguai'),
    ('AR', 'Argentina'),
    ('PE', 'Peru'),
    ('PT', 'Portugal'),
    ('IR', 'Irlanda'),
)


class Actor(models.Model):
    name = models.CharField(max_length=130)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
