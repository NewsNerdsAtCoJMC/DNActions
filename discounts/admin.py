from django.contrib import admin
from discounts.models import DealType, FoodType, DrinkType, Location, Deal

class DealTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name_slug": ("name",)}

class FoodTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name_slug": ("name",)}

class DrinkTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name_slug": ("name",)}

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name_slug": ("name",)}

admin.site.register(DealType, DealTypeAdmin)
admin.site.register(FoodType, FoodTypeAdmin)
admin.site.register(DrinkType, DrinkTypeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Deal)
