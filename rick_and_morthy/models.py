from django.db import models


class Character(models.Model):
    class StatusChoices(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        UNKNOWN = "Unknown"

    class GenreChoices(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        GENDERLESS = "Genderless"
        UNKNOWN = "Unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=30, choices=StatusChoices.choices)
    species = models.CharField(max_length=255)
    genre = models.CharField(max_length=30, choices=GenreChoices.choices)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name
