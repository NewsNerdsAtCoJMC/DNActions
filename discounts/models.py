from django.db import models

class DealType(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField()
    def __str__(self):
        return self.name

class FoodType(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField()
    def __str__(self):
        return self.name

class DrinkType(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField()
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField()
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Deal(models.Model):
    deal_type = models.ManyToManyField(DealType, blank=True)
    food_type = models.ManyToManyField(FoodType, blank=True)
    drink_type = models.ManyToManyField(DrinkType, blank=True)
    location = models.ForeignKey(Location)
    deal_text = models.TextField()
    expires = models.DateTimeField()
    def __str__(self):
        return "%s, expires on %s" % (self.location, self.expires)
