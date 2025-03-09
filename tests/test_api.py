# tests/test_api.py

import unittest
import json
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register_website(self):
        payload = {
            "website_id": "test_site_001",
            "domain": "example.com"
        }
        response = self.app.post(
            '/api/webhook/register', 
            data=json.dumps(payload), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("status", data)
        self.assertEqual(data["status"], "registered")

    def test_fetch_articles_missing_website_id(self):
        response = self.app.get('/api/articles')
        self.assertEqual(response.status_code, 400)
    
    def test_fetch_article_not_found(self):
        response = self.app.get('/api/article/non_existent_article')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
