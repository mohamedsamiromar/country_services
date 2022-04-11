from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):
    rate = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=550, null=True, blank=True)

