from django.db import migrations

def add_sample_diseases(apps, schema_editor):
    Disease = apps.get_model('disease_predictor', 'Disease')
    
    diseases = [
        {
            'name': 'Common Cold',
            'description': 'A viral infection of the upper respiratory tract that primarily affects the nose and throat.',
            'symptoms': 'runny nose, sneezing, congestion, sore throat, cough, mild headache, slight body aches, low-grade fever',
            'treatment': 'Rest, stay hydrated, over-the-counter decongestants and pain relievers. Zinc supplements and vitamin C may help reduce duration.',
            'severity': 'mild',
            'common_age_groups': 'All age groups',
            'prevention': 'Frequent hand washing, avoid touching face, maintain distance from sick people, get adequate sleep',
            'when_to_see_doctor': 'If symptoms last more than 10 days or are severe, or if you have a high fever or severe sinus pain'
        },
        {
            'name': 'Type 2 Diabetes',
            'description': 'A chronic condition that affects how your body metabolizes sugar (glucose).',
            'symptoms': 'increased thirst, frequent urination, increased hunger, unintended weight loss, fatigue, blurred vision, slow-healing sores',
            'treatment': 'Regular blood sugar monitoring, insulin therapy, oral medications, healthy diet, regular exercise',
            'severity': 'severe',
            'common_age_groups': 'Adults over 40, but increasingly seen in younger people',
            'prevention': 'Maintain healthy weight, regular exercise, balanced diet, limit processed foods and sugary drinks',
            'when_to_see_doctor': 'If you experience excessive thirst, frequent urination, extreme fatigue, or blurred vision'
        },
        {
            'name': 'Migraine',
            'description': 'A neurological condition that causes severe headaches, often accompanied by other symptoms.',
            'symptoms': 'severe headache, pulsing pain, nausea, vomiting, sensitivity to light, sensitivity to sound, aura, dizziness',
            'treatment': 'Pain relievers, anti-nausea medications, triptans, preventive medications, rest in dark quiet room',
            'severity': 'moderate',
            'common_age_groups': 'Most common between ages 18-44',
            'prevention': 'Identify and avoid triggers, maintain regular sleep schedule, manage stress, stay hydrated',
            'when_to_see_doctor': 'If migraines are severe, frequent, or interfere with daily activities'
        },
        {
            'name': 'Bronchitis',
            'description': 'Inflammation of the bronchial tubes that carry air to and from the lungs.',
            'symptoms': 'persistent cough, chest congestion, wheezing, fatigue, mild fever, shortness of breath, chest discomfort',
            'treatment': 'Rest, increased fluid intake, over-the-counter cough suppressants, humidifier use',
            'severity': 'moderate',
            'common_age_groups': 'All age groups, more common in smokers and elderly',
            'prevention': 'Avoid smoking, wear mask in polluted areas, maintain good hygiene',
            'when_to_see_doctor': 'If cough lasts more than 3 weeks, produces blood or thick mucus, or causes breathing difficulties'
        },
        {
            'name': 'Food Poisoning',
            'description': 'Illness caused by eating contaminated food or drinking contaminated water.',
            'symptoms': 'nausea, vomiting, diarrhea, stomach cramps, fever, weakness, headache, dehydration',
            'treatment': 'Stay hydrated, rest, bland diet (BRAT), probiotics, over-the-counter anti-diarrheal medication',
            'severity': 'moderate',
            'common_age_groups': 'All age groups',
            'prevention': 'Proper food handling, thorough cooking, hand washing, avoid cross-contamination',
            'when_to_see_doctor': 'If symptoms are severe, last more than 3 days, or include bloody stools or severe dehydration'
        },
        {
            'name': 'Hypertension',
            'description': 'High blood pressure that can lead to serious health problems if untreated.',
            'symptoms': 'headaches, shortness of breath, nosebleeds, chest pain, dizziness, irregular heartbeat',
            'treatment': 'Blood pressure medications, lifestyle changes, regular monitoring, stress management',
            'severity': 'severe',
            'common_age_groups': 'Adults over 50, but can affect younger people',
            'prevention': 'Regular exercise, healthy diet, limit salt intake, maintain healthy weight, avoid smoking',
            'when_to_see_doctor': 'Regular checkups recommended; immediate care if experiencing severe headaches, chest pain, or difficulty breathing'
        },
        {
            'name': 'Anxiety Disorder',
            'description': 'A mental health condition characterized by persistent feelings of worry and fear.',
            'symptoms': 'excessive worry, restlessness, difficulty concentrating, irritability, sleep problems, muscle tension, panic attacks',
            'treatment': 'Therapy (CBT), anti-anxiety medications, stress management techniques, lifestyle changes',
            'severity': 'moderate',
            'common_age_groups': 'Can affect all ages, often begins in teenage years or young adulthood',
            'prevention': 'Regular exercise, adequate sleep, stress management, mindfulness practices, healthy work-life balance',
            'when_to_see_doctor': 'If anxiety interferes with daily activities, relationships, or work'
        }
    ]
    
    for disease_data in diseases:
        Disease.objects.create(**disease_data)

def remove_sample_diseases(apps, schema_editor):
    Disease = apps.get_model('disease_predictor', 'Disease')
    Disease.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('disease_predictor', '0002_disease_common_age_groups_disease_prevention_and_more'),
    ]

    operations = [
        migrations.RunPython(add_sample_diseases, remove_sample_diseases),
    ]
