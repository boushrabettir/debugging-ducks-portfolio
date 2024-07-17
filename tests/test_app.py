import unittest
import json
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response=self.client.get("/")
        assert response.status_code==200
        html=response.get_data(as_text=True)
        assert "<h2>Who Am I?</h2>" in html
        assert not "no text" in html

    def test_timeline(self):
        response=self.client.get("/api/timeline_post")
        assert response.status_code==200
        assert response.is_json
        json=response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

    def test_malformed_timeline_post(self):
        response=self.client.post("/api/timeline_post", data={
            "email": "john@example.com", "content": "Hello!"
        })

        assert response.status_code==400
        html=json.loads(response.get_data(as_text=True))
        assert html['error']=='Invalid'

        response=self.client.post("/api/timeline_post", data={
            "name": "John Doe", "email": "john@example.com", "content": ""
        })

        print(f"Response {response}")
        assert response.status_code==400
        html=json.loads(response.get_data(as_text=True))
        assert html['error']=='Invalid'


        response=self.client.post("/api/timeline_post", data={
            "name": "John Doe", "email": "notanemail", "content": "Hi!"
        })
        assert response.status_code==400
        html=json.loads(response.get_data(as_text=True))
        assert html['error']=='Invalid'