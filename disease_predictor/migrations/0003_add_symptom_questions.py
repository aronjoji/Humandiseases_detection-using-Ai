from django.db import migrations
import json

def add_symptom_questions(apps, schema_editor):
    SymptomQuestion = apps.get_model('disease_predictor', 'SymptomQuestion')
    
    questions = [
        {
            'order': 1,
            'question': 'Are you experiencing any fever or elevated body temperature?',
            'category': 'fever',
            'follow_up_questions': json.dumps({
                'questions': [
                    'How high is your temperature (in °F)?',
                    'How long have you had the fever?',
                    'Does the fever come and go or is it constant?'
                ]
            })
        },
        {
            'order': 2,
            'question': 'Do you have any respiratory symptoms (cough, breathing difficulties)?',
            'category': 'respiratory',
            'follow_up_questions': json.dumps({
                'questions': [
                    'Is your cough dry or productive?',
                    'How long have you had these symptoms?',
                    'Do you experience shortness of breath?',
                    'Is breathing difficult when lying down?'
                ]
            })
        },
        {
            'order': 3,
            'question': 'Are you experiencing any pain or discomfort?',
            'category': 'pain',
            'follow_up_questions': json.dumps({
                'questions': [
                    'Where is the pain located?',
                    'How would you rate the pain from 1-10?',
                    'Is the pain constant or does it come and go?',
                    'What makes the pain better or worse?'
                ]
            })
        },
        {
            'order': 4,
            'question': 'Have you noticed any digestive system issues?',
            'category': 'digestive',
            'follow_up_questions': json.dumps({
                'questions': [
                    'Are you experiencing nausea or vomiting?',
                    'Have you had any changes in bowel movements?',
                    'Do you have abdominal pain or cramping?',
                    'Have you noticed any changes in appetite?'
                ]
            })
        },
        {
            'order': 5,
            'question': 'Are you experiencing unusual fatigue or weakness?',
            'category': 'fatigue',
            'follow_up_questions': json.dumps({
                'questions': [
                    'How long have you been feeling fatigued?',
                    'Does rest improve your energy levels?',
                    'Is the fatigue affecting your daily activities?',
                    'Do you feel exhausted even after sleeping?'
                ]
            })
        },
        {
            'order': 6,
            'question': 'Have you noticed any skin changes or rashes?',
            'category': 'skin',
            'follow_up_questions': json.dumps({
                'questions': [
                    'Where is the rash or skin change located?',
                    'Is it itchy, painful, or burning?',
                    'How long have you had these skin changes?',
                    'Have you used any new products recently?'
                ]
            })
        },
        {
            'order': 7,
            'question': 'Are you experiencing any neurological symptoms?',
            'category': 'neurological',
            'follow_up_questions': json.dumps({
                'questions': [
                    'Do you have headaches or migraines?',
                    'Have you experienced any dizziness or balance issues?',
                    'Are you having any vision changes?',
                    'Have you noticed any numbness or tingling?'
                ]
            })
        },
        {
            'order': 8,
            'question': 'Have you noticed any changes in your mental state or mood?',
            'category': 'mental',
            'follow_up_questions': json.dumps({
                'questions': [
                    'Are you feeling anxious or depressed?',
                    'Have you noticed changes in your sleep patterns?',
                    'Are you having difficulty concentrating?',
                    'Have these changes affected your daily life?'
                ]
            })
        },
        {
            'order': 9,
            'question': 'Are you experiencing any cardiovascular symptoms?',
            'category': 'cardiovascular',
            'follow_up_questions': json.dumps({
                'questions': [
                    'Do you have chest pain or pressure?',
                    'Have you noticed irregular heartbeats?',
                    'Do you get short of breath with activity?',
                    'Have you experienced any swelling in your legs?'
                ]
            })
        },
        {
            'order': 10,
            'question': 'Have you noticed any changes in your weight or appetite?',
            'category': 'weight',
            'follow_up_questions': json.dumps({
                'questions': [
                    'How much weight change have you noticed?',
                    'Over what period of time?',
                    'Have you changed your diet recently?',
                    'Are you experiencing increased thirst or hunger?'
                ]
            })
        }
    ]
    
    for question_data in questions:
        SymptomQuestion.objects.create(**question_data)

def remove_symptom_questions(apps, schema_editor):
    SymptomQuestion = apps.get_model('disease_predictor', 'SymptomQuestion')
    SymptomQuestion.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('disease_predictor', '0002_add_diseases'),
    ]
    
    operations = [
        migrations.RunPython(add_symptom_questions, remove_symptom_questions),
    ]
