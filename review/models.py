from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    score = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)])
    contents = models.TextField()
