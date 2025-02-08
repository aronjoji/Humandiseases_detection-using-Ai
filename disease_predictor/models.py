from django.db import models

# Create your models here.

class Disease(models.Model):
    SEVERITY_CHOICES = [
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    symptoms = models.TextField(help_text="Comma-separated list of symptoms")
    treatment = models.TextField()
    prevention = models.TextField(blank=True, null=True)
    when_to_see_doctor = models.TextField(blank=True, null=True)
    common_age_groups = models.CharField(max_length=200, blank=True, null=True)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='moderate')
    
    def __str__(self):
        return self.name
    
    def get_symptom_list(self):
        return [s.strip() for s in self.symptoms.split(',')]

class SymptomQuestion(models.Model):
    question = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    follow_up_questions = models.JSONField(default=dict)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['order']

class Prediction(models.Model):
    symptoms = models.TextField()
    predicted_disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.predicted_disease.name} - {self.confidence}%"
