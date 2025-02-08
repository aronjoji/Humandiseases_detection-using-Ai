from django.db import migrations

def add_diseases(apps, schema_editor):
    Disease = apps.get_model('disease_predictor', 'Disease')
    
    diseases = [
        # Respiratory Diseases
        {
            'name': 'COVID-19',
            'description': 'Infectious disease caused by the SARS-CoV-2 virus.',
            'symptoms': 'fever, cough, fatigue, loss of taste or smell, shortness of breath, body aches, headache',
            'treatment': 'Rest, hydration, over-the-counter medications for symptoms, antiviral medications if prescribed',
            'prevention': 'Vaccination, wearing masks, social distancing, good hand hygiene',
            'when_to_see_doctor': 'Difficulty breathing, persistent chest pain, confusion, inability to stay awake',
            'common_age_groups': 'All ages',
            'severity': 'severe'
        },
        {
            'name': 'Tuberculosis',
            'description': 'Bacterial infection primarily affecting the lungs.',
            'symptoms': 'persistent cough, coughing up blood, night sweats, fever, weight loss, fatigue',
            'treatment': 'Long-term antibiotic therapy, usually 6-9 months',
            'prevention': 'BCG vaccination, early detection, proper ventilation',
            'when_to_see_doctor': 'Persistent cough, unexplained weight loss, night sweats',
            'common_age_groups': 'All ages, higher risk in immunocompromised',
            'severity': 'severe'
        },
        
        # Cardiovascular Diseases
        {
            'name': 'Hypertension',
            'description': 'Persistently elevated blood pressure in the arteries.',
            'symptoms': 'headache, shortness of breath, nosebleeds, visual changes, chest pain',
            'treatment': 'Lifestyle changes, medications (ACE inhibitors, beta blockers, etc.)',
            'prevention': 'Regular exercise, healthy diet, stress management, limiting alcohol',
            'when_to_see_doctor': 'Regular checkups, severe headaches, chest pain',
            'common_age_groups': 'More common over 40',
            'severity': 'moderate'
        },
        {
            'name': 'Coronary Artery Disease',
            'description': 'Buildup of plaque in the heart\'s arteries.',
            'symptoms': 'chest pain, shortness of breath, fatigue, irregular heartbeat, nausea',
            'treatment': 'Medications, lifestyle changes, possible surgery',
            'prevention': 'Regular exercise, healthy diet, not smoking, stress management',
            'when_to_see_doctor': 'Chest pain, shortness of breath, irregular heartbeat',
            'common_age_groups': 'More common over 45',
            'severity': 'severe'
        },
        
        # Endocrine Disorders
        {
            'name': 'Type 2 Diabetes',
            'description': 'Metabolic disorder affecting how the body processes glucose.',
            'symptoms': 'increased thirst and urination, fatigue, blurred vision, slow healing, increased hunger',
            'treatment': 'Diet management, exercise, oral medications, possibly insulin',
            'prevention': 'Healthy diet, regular exercise, maintaining healthy weight',
            'when_to_see_doctor': 'Excessive thirst, frequent urination, unexplained weight loss',
            'common_age_groups': 'More common over 45',
            'severity': 'moderate'
        },
        {
            'name': 'Hyperthyroidism',
            'description': 'Overactive thyroid gland producing excess thyroid hormone.',
            'symptoms': 'anxiety, irritability, tremor, rapid heartbeat, weight loss, heat sensitivity',
            'treatment': 'Anti-thyroid medications, radioactive iodine, possible surgery',
            'prevention': 'Regular thyroid checkups if at risk',
            'when_to_see_doctor': 'Rapid heartbeat, unexplained weight loss, anxiety',
            'common_age_groups': '20-40 years',
            'severity': 'moderate'
        },
        
        # Neurological Conditions
        {
            'name': 'Multiple Sclerosis',
            'description': 'Autoimmune disease affecting the central nervous system.',
            'symptoms': 'fatigue, difficulty walking, numbness, weakness, vision problems, cognitive changes',
            'treatment': 'Disease-modifying therapies, symptom management medications',
            'prevention': 'No known prevention, early treatment is crucial',
            'when_to_see_doctor': 'Vision problems, weakness, coordination problems',
            'common_age_groups': '20-40 years',
            'severity': 'severe'
        },
        {
            'name': 'Parkinson\'s Disease',
            'description': 'Progressive nervous system disorder affecting movement.',
            'symptoms': 'tremor, slow movement, stiffness, balance problems, speech changes',
            'treatment': 'Medications to increase dopamine, physical therapy',
            'prevention': 'No known prevention',
            'when_to_see_doctor': 'Tremors, difficulty with movement or balance',
            'common_age_groups': 'Usually over 60',
            'severity': 'severe'
        },
        
        # Gastrointestinal Disorders
        {
            'name': 'Crohn\'s Disease',
            'description': 'Inflammatory bowel disease causing inflammation of digestive tract.',
            'symptoms': 'diarrhea, abdominal pain, fatigue, weight loss, reduced appetite',
            'treatment': 'Anti-inflammatory drugs, immune system suppressors, nutrition therapy',
            'prevention': 'No known prevention',
            'when_to_see_doctor': 'Persistent diarrhea, abdominal pain, unexplained weight loss',
            'common_age_groups': '15-35 years',
            'severity': 'moderate'
        },
        {
            'name': 'Peptic Ulcer',
            'description': 'Open sores in the lining of stomach or small intestine.',
            'symptoms': 'burning stomach pain, feeling of fullness, bloating, heartburn',
            'treatment': 'Antibiotics if H. pylori present, acid-reducing medications',
            'prevention': 'Avoid NSAIDs, limit alcohol, quit smoking',
            'when_to_see_doctor': 'Severe stomach pain, bloody stools, difficulty swallowing',
            'common_age_groups': 'All ages',
            'severity': 'moderate'
        },
        
        # Mental Health Conditions
        {
            'name': 'Major Depression',
            'description': 'Mood disorder causing persistent feelings of sadness and loss of interest.',
            'symptoms': 'persistent sadness, loss of interest, sleep changes, fatigue, difficulty concentrating',
            'treatment': 'Psychotherapy, antidepressant medications, lifestyle changes',
            'prevention': 'Regular exercise, stress management, social support',
            'when_to_see_doctor': 'Persistent sadness, thoughts of self-harm',
            'common_age_groups': 'All ages',
            'severity': 'moderate'
        },
        {
            'name': 'Bipolar Disorder',
            'description': 'Mental health condition causing extreme mood swings.',
            'symptoms': 'manic episodes, depressive episodes, changes in energy, sleep problems',
            'treatment': 'Mood stabilizers, psychotherapy, antipsychotic medications',
            'prevention': 'Regular medication, stress management, regular sleep schedule',
            'when_to_see_doctor': 'Extreme mood swings, risky behavior',
            'common_age_groups': 'Usually appears in teens or early 20s',
            'severity': 'severe'
        },
        
        # Autoimmune Conditions
        {
            'name': 'Systemic Lupus Erythematosus',
            'description': 'Autoimmune disease affecting multiple body systems.',
            'symptoms': 'fatigue, joint pain, butterfly-shaped rash, fever, skin lesions',
            'treatment': 'Anti-inflammatory medications, immunosuppressants',
            'prevention': 'Sun protection, regular medical care',
            'when_to_see_doctor': 'Unexplained rash, joint pain, fever',
            'common_age_groups': '15-45 years, more common in women',
            'severity': 'severe'
        },
        {
            'name': 'Psoriasis',
            'description': 'Autoimmune condition causing rapid skin cell growth.',
            'symptoms': 'red patches with silver scales, dry skin, itching, joint pain',
            'treatment': 'Topical treatments, light therapy, oral or injected medications',
            'prevention': 'Identify and avoid triggers, maintain healthy lifestyle',
            'when_to_see_doctor': 'Severe skin symptoms, joint pain',
            'common_age_groups': '15-35 years',
            'severity': 'moderate'
        },
        
        # Cancer Types
        {
            'name': 'Breast Cancer',
            'description': 'Cancer that forms in breast tissue.',
            'symptoms': 'breast lump, breast changes, nipple discharge, skin changes',
            'treatment': 'Surgery, radiation therapy, chemotherapy, hormone therapy',
            'prevention': 'Regular screening, healthy lifestyle, limiting alcohol',
            'when_to_see_doctor': 'Breast lumps, changes in breast appearance',
            'common_age_groups': 'More common over 50',
            'severity': 'severe'
        },
        {
            'name': 'Colorectal Cancer',
            'description': 'Cancer of the colon or rectum.',
            'symptoms': 'changes in bowel habits, rectal bleeding, abdominal pain, fatigue',
            'treatment': 'Surgery, chemotherapy, radiation therapy',
            'prevention': 'Regular screening, healthy diet, regular exercise',
            'when_to_see_doctor': 'Changes in bowel habits, rectal bleeding',
            'common_age_groups': 'More common over 50',
            'severity': 'severe'
        }
    ]
    
    for disease_data in diseases:
        Disease.objects.create(**disease_data)

def remove_diseases(apps, schema_editor):
    Disease = apps.get_model('disease_predictor', 'Disease')
    Disease.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('disease_predictor', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(add_diseases, remove_diseases),
    ]
