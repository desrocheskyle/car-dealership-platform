from django.db import models
# from django.utils.timezone import now  # unused import kept but commented
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Car Make: {self.name}"


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('SPORT', 'Sport'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015),
        ]
    )

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Type: {self.type}\n"
            f"Year: {self.year}"
        )
        