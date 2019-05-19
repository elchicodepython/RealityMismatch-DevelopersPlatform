from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    """Level of the game.
All the levels should be registered before being created. The level has
a unique identifier to be used in the level development.
    """
    # Level description
    name = models.CharField(max_length=32)
    # Level description
    description = models.CharField(max_length=256)
    # The level is playable?
    finished = models.BooleanField(default=False)
    # Entrypoint where level starts
    startpoint = models.IntegerField()
    # Number of entrypoints the level provides to future developers
    number_of_entrypoints = models.IntegerField()
    # Level author
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
