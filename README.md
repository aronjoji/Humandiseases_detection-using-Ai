# AI-Powered Human Disease Finder

This is a Django-based web application that uses machine learning to help identify potential diseases based on input symptoms.

## Features
- User-friendly interface for symptom input
- AI-powered disease prediction
- Detailed disease information
- Responsive design

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Unix/MacOS: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to access the application.

## Note
This application is for educational purposes only and should not be used as a substitute for professional medical advice.
