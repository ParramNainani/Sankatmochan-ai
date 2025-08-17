"""
Firebase Configuration for Sankatmochan AI Backend
"""

# Firebase Project Configuration
FIREBASE_CONFIG = {
    'project_id': 'sankatmochan-ai',
    'storage_bucket': 'sankatmochan-ai.appspot.com',
    'database_url': 'https://sankatmochan-ai-default-rtdb.firebaseio.com',
    'api_key': 'AIzaSyC5pKU2DgE7ZQ28QtpX54IfTj1-3vq76Mg',
    'auth_domain': 'sankatmochan-ai.firebaseapp.com',
    'messaging_sender_id': '557911816843',
    'app_id': '1:557911816843:web:b270b830a57ab218f1b28e',
    'measurement_id': 'G-R3S023Z8DC'
}

# Firestore Collection Names
FIRESTORE_COLLECTIONS = {
    'birth_charts': 'birth_charts',
    'user_profiles': 'user_profiles',
    'daily_guidance': 'daily_guidance',
    'predictions': 'predictions'
}

# Firebase Storage Paths
STORAGE_PATHS = {
    'charts': 'charts/',
    'reports': 'reports/',
    'user_uploads': 'user_uploads/'
}

# Chart Image Settings
CHART_IMAGE_SETTINGS = {
    'format': 'png',
    'dpi': 300,
    'max_size_mb': 10,
    'allowed_formats': ['png', 'jpg', 'jpeg']
}

# Firebase Security Rules (for reference)
SECURITY_RULES = {
    'firestore': '''
    rules_version = '2';
    service cloud.firestore {
      match /databases/{database}/documents {
        // Birth charts collection
        match /birth_charts/{document} {
          allow read, write: if request.auth != null;
        }
        
        // User profiles collection
        match /user_profiles/{userId} {
          allow read, write: if request.auth != null && request.auth.uid == userId;
        }
      }
    }
    ''',
    
    'storage': '''
    rules_version = '2';
    service firebase.storage {
      match /b/{bucket}/o {
        // Charts folder
        match /charts/{allPaths=**} {
          allow read, write: if request.auth != null;
        }
        
        // User uploads folder
        match /user_uploads/{userId}/{allPaths=**} {
          allow read, write: if request.auth != null && request.auth.uid == userId;
        }
      }
    }
    '''
} 