from django.urls import path
from .views import HomeView, SymptomSuggestionView

app_name = 'disease_predictor'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/symptoms/suggest/', SymptomSuggestionView.as_view(), name='symptom_suggestions'),
]
