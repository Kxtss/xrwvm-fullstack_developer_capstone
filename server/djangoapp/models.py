from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# car make model
class CarMake(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    car_id = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return f"Name: {self.name},\
            Description: {self.description}, Car ID: {self.car_id}"
# car model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    CAR_TYPES = [('Sedan', 'Sedan'),
                 ('SUV', 'SUV'),
                 ('WAGON', 'Wagon'),
                 ('COUPE', 'Coupe'),
                 ('HATCHBACK', 'Hatchback'),
                 ('MINIVAN', 'Minivan'),
                 ('VAN', 'Van'),
                 ('CONVERTIBLE', 'Convertible'),
                 ('SPORTS CAR', 'Sports Car'),
                 ('TRUCK', 'Truck'),
                 ('HYBRID', 'Hybrid'),
                 ('ELECTRIC', 'Electric'),
                 ('OTHER', 'Other'),
                 ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(default=now().year,
                            validators=[MaxValueValidator(2026),
                                        MinValueValidator(2015)
                                        ],
                            null=False,
                            blank=False
                            )
    
    dealer_id = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Make: {self.car_make.name},\
            Model: {self.name}, Type: {self.type}, Year: {self.year}, Dealer ID: {self.dealer_id}"
