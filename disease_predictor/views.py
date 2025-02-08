from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
import json
from .models import Disease, SymptomQuestion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class HomeView(View):
    template_name = 'disease_predictor/home.html'
    
    def get(self, request, *args, **kwargs):
        # Get the first question and prepare its data
        first_question = SymptomQuestion.objects.filter(order=1).first()
        if first_question:
            # Parse the JSON field
            follow_up_questions = []
            if first_question.follow_up_questions:
                try:
                    json_data = json.loads(first_question.follow_up_questions) if isinstance(first_question.follow_up_questions, str) else first_question.follow_up_questions
                    follow_up_questions = json_data.get('questions', [])
                except (json.JSONDecodeError, AttributeError):
                    follow_up_questions = []
            
            context = {
                'first_question': {
                    'order': first_question.order,
                    'question': first_question.question,
                    'follow_up_questions': follow_up_questions
                }
            }
        else:
            context = {}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return render(request, self.template_name)
        
        data = json.loads(request.body)
        action = data.get('action')
        
        if action == 'get_next_question':
            return self.handle_next_question(data)
        
        return JsonResponse({'error': 'Invalid action'}, status=400)
    
    def handle_next_question(self, data):
        current_order = data.get('current_order')
        answers = data.get('answers', {})
        
        # Get next question based on current order
        next_question = SymptomQuestion.objects.filter(order=current_order + 1).first()
        
        # If no more questions, process answers and return predictions
        if not next_question:
            return self.process_answers(answers)
        
        # Parse the JSON field for follow-up questions
        follow_ups = []
        if next_question.follow_up_questions:
            try:
                json_data = json.loads(next_question.follow_up_questions) if isinstance(next_question.follow_up_questions, str) else next_question.follow_up_questions
                follow_ups = json_data.get('questions', [])
            except (json.JSONDecodeError, AttributeError):
                follow_ups = []
        
        # Prepare question data
        question_data = {
            'order': next_question.order,
            'text': next_question.question,
            'follow_ups': follow_ups
        }
        
        return JsonResponse({
            'complete': False,
            'question': question_data
        })
    
    def process_answers(self, answers):
        # Convert answers into symptoms list
        symptoms = []
        for order, answer in answers.items():
            if isinstance(order, str) and order.endswith('_followup'):
                continue
            
            question = SymptomQuestion.objects.filter(order=int(order)).first()
            if question and answer == 'Yes':
                symptoms.append(question.category)
                
                # Add follow-up details if present
                followup_key = f"{order}_followup"
                if followup_key in answers:
                    for _, detail in answers[followup_key].items():
                        if detail.strip():
                            symptoms.append(f"{question.category} - {detail}")
        
        # Get predictions based on symptoms
        predictions = self.get_predictions(symptoms)
        
        return JsonResponse({
            'complete': True,
            'predictions': predictions
        })
    
    def get_predictions(self, symptoms):
        if not symptoms:
            return []
        
        # Get all diseases
        diseases = Disease.objects.all()
        
        # Prepare text for comparison
        user_symptoms = ' '.join(symptoms)
        disease_texts = [' '.join(d.symptoms.split(',')) for d in diseases]
        
        # Calculate TF-IDF similarity
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([user_symptoms] + disease_texts)
        cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
        
        # Prepare predictions
        predictions = []
        for disease, similarity in zip(diseases, cosine_similarities):
            if similarity > 0.1:  # Threshold to filter out very low matches
                predictions.append({
                    'name': disease.name,
                    'confidence': round(similarity * 100),
                    'severity': disease.severity,
                    'description': disease.description,
                    'treatment': disease.treatment,
                    'prevention': disease.prevention,
                    'when_to_see_doctor': disease.when_to_see_doctor,
                    'common_age_groups': disease.common_age_groups
                })
        
        # Sort by confidence
        predictions.sort(key=lambda x: x['confidence'], reverse=True)
        
        return predictions[:5]  # Return top 5 predictions

class SymptomSuggestionView(View):
    def get(self, request):
        query = request.GET.get('query', '').lower()
        all_symptoms = set()
        
        for disease in Disease.objects.all():
            all_symptoms.update(disease.get_symptom_list())
        
        # Filter symptoms that match the query
        suggestions = [
            symptom for symptom in all_symptoms
            if query in symptom.lower()
        ]
        
        return JsonResponse({'suggestions': sorted(suggestions)[:10]})
