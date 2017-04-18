from rest_framework import serializers
from discounts.models import DealType, FoodType, DrinkType, Location, Deal

class DealTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealType
        fields = ('name',)

class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ('name',)

class DrinkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkType
        fields = ('name',)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name',)

class DealSerializer(serializers.ModelSerializer):
    speech = serializers.CharField(source='deal_text')
    display_text = serializers.CharField(source='deal_text')
    #data = serializers.CharField(default="{...}")
    #contextOut = serializers.CharField(default="[...]")
    source = serializers.CharField(default="Husker Deals")
    class Meta:
        model = Deal
        fields = ('speech', 'display_text', 'source')
