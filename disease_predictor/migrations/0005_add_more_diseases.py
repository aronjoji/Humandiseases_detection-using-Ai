from django.db import migrations

def add_more_diseases(apps, schema_editor):
    Disease = apps.get_model('disease_predictor', 'Disease')
    
    diseases = [
        {
            'name': 'Migraine',
            'description': 'A neurological condition characterized by severe headaches, often accompanied by other symptoms.',
            'symptoms': 'severe headache, sensitivity to light, nausea, visual disturbances, dizziness, fatigue, neck pain',
            'treatment': 'Pain relievers, anti-nausea medications, triptans, preventive medications, lifestyle changes',
            'prevention': 'Identify and avoid triggers, maintain regular sleep schedule, manage stress, stay hydrated',
            'when_to_see_doctor': 'Severe or frequent headaches, new symptoms, headaches that worsen or don\'t respond to treatment',
            'common_age_groups': '18-44 years',
            'severity': 'moderate'
        },
        {
            'name': 'Bronchitis',
            'description': 'Inflammation of the bronchial tubes that carry air to and from the lungs.',
            'symptoms': 'persistent cough, mucus production, chest discomfort, fatigue, mild fever, shortness of breath',
            'treatment': 'Rest, hydration, over-the-counter pain relievers, humidifier use, bronchodilators if prescribed',
            'prevention': 'Avoid smoking, practice good hand hygiene, get vaccinated against flu and pneumonia',
            'when_to_see_doctor': 'Cough lasting more than 3 weeks, difficulty breathing, high fever, bloody mucus',
            'common_age_groups': 'All ages',
            'severity': 'moderate'
        },
        {
            'name': 'Gastroenteritis',
            'description': 'Inflammation of the stomach and intestines, typically resulting from viral or bacterial infection.',
            'symptoms': 'diarrhea, vomiting, nausea, stomach cramps, mild fever, headache, muscle aches',
            'treatment': 'Oral rehydration, rest, gradual return to eating, anti-diarrheal medications if needed',
            'prevention': 'Regular hand washing, proper food handling, clean drinking water',
            'when_to_see_doctor': 'Severe dehydration, bloody stools, high fever, symptoms lasting more than 3 days',
            'common_age_groups': 'All ages',
            'severity': 'moderate'
        },
        {
            'name': 'Pneumonia',
            'description': 'Infection that inflames air sacs in one or both lungs, which may fill with fluid.',
            'symptoms': 'chest pain, difficulty breathing, high fever, cough with phlegm, fatigue, confusion in elderly',
            'treatment': 'Antibiotics for bacterial pneumonia, rest, hydration, oxygen therapy if needed',
            'prevention': 'Vaccination, good hygiene, quit smoking, maintain strong immune system',
            'when_to_see_doctor': 'Difficulty breathing, chest pain, persistent high fever, confusion',
            'common_age_groups': 'Very young and elderly most at risk',
            'severity': 'severe'
        },
        {
            'name': 'Rheumatoid Arthritis',
            'description': 'Chronic inflammatory disorder affecting joints and sometimes other body systems.',
            'symptoms': 'joint pain, joint swelling, morning stiffness, fatigue, fever, loss of appetite',
            'treatment': 'Disease-modifying antirheumatic drugs (DMARDs), NSAIDs, physical therapy',
            'prevention': 'Early diagnosis and treatment, regular exercise, maintain healthy weight',
            'when_to_see_doctor': 'Persistent joint pain and swelling, morning stiffness lasting more than an hour',
            'common_age_groups': '40-60 years',
            'severity': 'severe'
        },
        {
            'name': 'Anxiety Disorder',
            'description': 'Mental health condition characterized by persistent and excessive worry.',
            'symptoms': 'excessive worry, restlessness, difficulty concentrating, sleep problems, irritability, muscle tension',
            'treatment': 'Cognitive behavioral therapy, anti-anxiety medications, relaxation techniques',
            'prevention': 'Stress management, regular exercise, adequate sleep, avoiding caffeine and alcohol',
            'when_to_see_doctor': 'Anxiety interfering with daily life, panic attacks, physical symptoms',
            'common_age_groups': 'All ages, often starts in young adulthood',
            'severity': 'moderate'
        },
        {
            'name': 'Hypothyroidism',
            'description': 'Condition where the thyroid gland doesn\'t produce enough thyroid hormone.',
            'symptoms': 'fatigue, weight gain, cold sensitivity, dry skin, depression, muscle weakness, joint pain',
            'treatment': 'Thyroid hormone replacement therapy, regular monitoring of thyroid levels',
            'prevention': 'Regular thyroid screening if at risk, maintaining healthy iodine levels',
            'when_to_see_doctor': 'Persistent fatigue, unexplained weight gain, depression',
            'common_age_groups': 'Over 60, more common in women',
            'severity': 'moderate'
        },
        {
            'name': 'Celiac Disease',
            'description': 'Immune reaction to eating gluten that damages the small intestine.',
            'symptoms': 'diarrhea, bloating, fatigue, weight loss, anemia, skin rash, joint pain',
            'treatment': 'Strict gluten-free diet, nutritional supplements if needed',
            'prevention': 'Avoid gluten-containing foods, read food labels carefully',
            'when_to_see_doctor': 'Persistent digestive issues, unexplained weight loss, fatigue',
            'common_age_groups': 'Can develop at any age',
            'severity': 'moderate'
        },
        {
            'name': 'Asthma',
            'description': 'Chronic condition affecting airways in the lungs, causing inflammation and narrowing.',
            'symptoms': 'wheezing, shortness of breath, chest tightness, coughing, especially at night',
            'treatment': 'Inhaled corticosteroids, bronchodilators, avoiding triggers',
            'prevention': 'Identify and avoid triggers, regular exercise, maintain clean environment',
            'when_to_see_doctor': 'Frequent asthma attacks, symptoms interfering with daily activities',
            'common_age_groups': 'Often starts in childhood',
            'severity': 'moderate'
        },
        {
            'name': 'Chronic Kidney Disease',
            'description': 'Progressive loss of kidney function over time.',
            'symptoms': 'fatigue, high blood pressure, swelling in feet and ankles, changes in urination, nausea',
            'treatment': 'Medications to control blood pressure, dietary changes, dialysis if severe',
            'prevention': 'Control blood pressure and diabetes, healthy diet, regular exercise',
            'when_to_see_doctor': 'Changes in urination, swelling, persistent fatigue',
            'common_age_groups': 'More common over 65',
            'severity': 'severe'
        }
    ]
    
    for disease_data in diseases:
        Disease.objects.create(**disease_data)

def remove_diseases(apps, schema_editor):
    Disease = apps.get_model('disease_predictor', 'Disease')
    for disease in ['Migraine', 'Bronchitis', 'Gastroenteritis', 'Pneumonia', 
                   'Rheumatoid Arthritis', 'Anxiety Disorder', 'Hypothyroidism',
                   'Celiac Disease', 'Asthma', 'Chronic Kidney Disease']:
        Disease.objects.filter(name=disease).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('disease_predictor', '0004_symptomquestion_alter_disease_common_age_groups_and_more'),
    ]
    
    operations = [
        migrations.RunPython(add_more_diseases, remove_diseases),
    ]
