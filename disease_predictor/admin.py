from django.contrib import admin
from .models import Disease, Prediction

# Register your models here.

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'symptoms')
    search_fields = ('name', 'symptoms')

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('predicted_disease', 'confidence', 'created_at')
    list_filter = ('predicted_disease', 'created_at')
    readonly_fields = ('created_at',)
