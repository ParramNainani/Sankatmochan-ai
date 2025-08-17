"""
Firebase Service for Sankatmochan AI
Handles chart image uploads and Firestore operations
"""

import os
import json
import base64
import requests
from datetime import datetime
from typing import Dict, List, Optional
import firebase_admin
from firebase_admin import credentials, storage, firestore
from google.cloud import storage as google_storage

class FirebaseService:
    """Firebase service for chart storage and management"""
    
    def __init__(self, service_account_path: str = None):
        """Initialize Firebase service"""
        self.service_account_path = service_account_path
        self._initialize_firebase()
        self.db = firestore.client()
        self.bucket = storage.bucket()
    
    def _initialize_firebase(self):
        """Initialize Firebase Admin SDK"""
        try:
            if not firebase_admin._apps:
                if self.service_account_path and os.path.exists(self.service_account_path):
                    cred = credentials.Certificate(self.service_account_path)
                    firebase_admin.initialize_app(cred, {
                        'storageBucket': 'sankatmochan-ai.appspot.com'
                    })
                else:
                    # Use default credentials (for local development)
                    firebase_admin.initialize_app()
        except Exception as e:
            print(f"Firebase initialization error: {e}")
            # Fallback to REST API approach
            self.use_rest_api = True
        else:
            self.use_rest_api = False
    
    def upload_chart_image(self, 
                          person_name: str,
                          birth_date: str,
                          birth_time: str,
                          birth_place: str,
                          chart_image_path: str,
                          api_key: str = None) -> Dict[str, str]:
        """
        Upload chart image to Firebase Storage and save metadata to Firestore
        
        Args:
            person_name: Name of the person
            birth_date: Birth date in ISO format
            birth_time: Birth time
            birth_place: Birth place
            chart_image_path: Path to the chart image file
            api_key: Firebase API key for REST API (if not using Admin SDK)
        
        Returns:
            Dictionary with upload URL and document ID
        """
        try:
            if self.use_rest_api and api_key:
                return self._upload_via_rest_api(
                    person_name, birth_date, birth_time, birth_place, 
                    chart_image_path, api_key
                )
            else:
                return self._upload_via_admin_sdk(
                    person_name, birth_date, birth_time, birth_place, 
                    chart_image_path
                )
        except Exception as e:
            raise Exception(f"Failed to upload chart image: {e}")
    
    def _upload_via_admin_sdk(self, person_name: str, birth_date: str, 
                             birth_time: str, birth_place: str, 
                             chart_image_path: str) -> Dict[str, str]:
        """Upload using Firebase Admin SDK"""
        
        # Create unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"charts/{person_name.replace(' ', '_')}_{timestamp}.png"
        
        # Upload to Firebase Storage
        blob = self.bucket.blob(filename)
        blob.upload_from_filename(chart_image_path)
        blob.make_public()
        
        # Get download URL
        download_url = blob.public_url
        
        # Save metadata to Firestore
        doc_ref = self.db.collection('birth_charts').add({
            'person_name': person_name,
            'birth_date': birth_date,
            'birth_time': birth_time,
            'birth_place': birth_place,
            'chart_image_url': download_url,
            'chart_image_path': filename,
            'created_at': firestore.SERVER_TIMESTAMP,
            'updated_at': firestore.SERVER_TIMESTAMP,
        })
        
        return {
            'download_url': download_url,
            'document_id': doc_ref[1].id,
            'storage_path': filename
        }
    
    def _upload_via_rest_api(self, person_name: str, birth_date: str,
                            birth_time: str, birth_place: str,
                            chart_image_path: str, api_key: str) -> Dict[str, str]:
        """Upload using Firebase REST API (fallback method)"""
        
        # Read image file
        with open(chart_image_path, 'rb') as f:
            image_data = f.read()
        
        # Encode image to base64
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        # Create unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"charts/{person_name.replace(' ', '_')}_{timestamp}.png"
        
        # Upload to Firebase Storage via REST API
        storage_url = f"https://firebasestorage.googleapis.com/v0/b/sankatmochan-ai.appspot.com/o"
        upload_url = f"{storage_url}?name={filename}"
        
        headers = {
            'Content-Type': 'application/octet-stream',
            'Authorization': f'Bearer {api_key}'
        }
        
        response = requests.post(upload_url, data=image_data, headers=headers)
        response.raise_for_status()
        
        # Get download URL
        download_url = f"https://firebasestorage.googleapis.com/v0/b/sankatmochan-ai.appspot.com/o/{filename}?alt=media"
        
        # Save metadata to Firestore via REST API
        firestore_url = f"https://firestore.googleapis.com/v1/projects/sankatmochan-ai/databases/(default)/documents/birth_charts"
        
        document_data = {
            'fields': {
                'person_name': {'stringValue': person_name},
                'birth_date': {'stringValue': birth_date},
                'birth_time': {'stringValue': birth_time},
                'birth_place': {'stringValue': birth_place},
                'chart_image_url': {'stringValue': download_url},
                'chart_image_path': {'stringValue': filename},
                'created_at': {'timestampValue': datetime.now().isoformat() + 'Z'},
                'updated_at': {'timestampValue': datetime.now().isoformat() + 'Z'},
            }
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        response = requests.post(firestore_url, json=document_data, headers=headers)
        response.raise_for_status()
        
        doc_data = response.json()
        document_id = doc_data['name'].split('/')[-1]
        
        return {
            'download_url': download_url,
            'document_id': document_id,
            'storage_path': filename
        }
    
    def get_all_birth_charts(self) -> List[Dict]:
        """Get all birth charts from Firestore"""
        try:
            if self.use_rest_api:
                return self._get_charts_via_rest_api()
            else:
                return self._get_charts_via_admin_sdk()
        except Exception as e:
            raise Exception(f"Failed to fetch birth charts: {e}")
    
    def _get_charts_via_admin_sdk(self) -> List[Dict]:
        """Get charts using Admin SDK"""
        docs = self.db.collection('birth_charts').order_by('created_at', direction=firestore.Query.DESCENDING).stream()
        
        charts = []
        for doc in docs:
            chart_data = doc.to_dict()
            chart_data['id'] = doc.id
            charts.append(chart_data)
        
        return charts
    
    def _get_charts_via_rest_api(self) -> List[Dict]:
        """Get charts using REST API"""
        # This would require API key and more complex implementation
        # For now, return empty list
        return []
    
    def search_charts_by_name(self, name: str) -> List[Dict]:
        """Search birth charts by person name"""
        try:
            if self.use_rest_api:
                return self._search_charts_via_rest_api(name)
            else:
                return self._search_charts_via_admin_sdk(name)
        except Exception as e:
            raise Exception(f"Failed to search birth charts: {e}")
    
    def _search_charts_via_admin_sdk(self, name: str) -> List[Dict]:
        """Search charts using Admin SDK"""
        docs = self.db.collection('birth_charts').where('person_name', '>=', name).where('person_name', '<', name + '\uf8ff').stream()
        
        charts = []
        for doc in docs:
            chart_data = doc.to_dict()
            chart_data['id'] = doc.id
            charts.append(chart_data)
        
        return charts
    
    def _search_charts_via_rest_api(self, name: str) -> List[Dict]:
        """Search charts using REST API"""
        # This would require API key and more complex implementation
        # For now, return empty list
        return []
    
    def delete_chart(self, chart_id: str) -> bool:
        """Delete birth chart and its image"""
        try:
            if self.use_rest_api:
                return self._delete_chart_via_rest_api(chart_id)
            else:
                return self._delete_chart_via_admin_sdk(chart_id)
        except Exception as e:
            raise Exception(f"Failed to delete birth chart: {e}")
    
    def _delete_chart_via_admin_sdk(self, chart_id: str) -> bool:
        """Delete chart using Admin SDK"""
        # Get chart data first
        doc_ref = self.db.collection('birth_charts').document(chart_id)
        doc = doc_ref.get()
        
        if doc.exists:
            chart_data = doc.to_dict()
            
            # Delete image from Storage
            if 'chart_image_path' in chart_data:
                blob = self.bucket.blob(chart_data['chart_image_path'])
                blob.delete()
            
            # Delete document from Firestore
            doc_ref.delete()
            return True
        
        return False
    
    def _delete_chart_via_rest_api(self, chart_id: str) -> bool:
        """Delete chart using REST API"""
        # This would require API key and more complex implementation
        # For now, return False
        return False 