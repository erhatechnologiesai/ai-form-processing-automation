import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestFormProcessing(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_form_submission(self):
        payload = {
            "form_id": "CONTACT-US-2026",
            "submitter_name": "Farhan Ali",
            "submitter_email": "farhan@example.com",
            "fields": {"Company ": " Erha Partner Network ", "Seats": 25}
        }
        res = self.client.post("/submit-form", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "PROCESSED")
        self.assertEqual(data["sanitized_fields"]["company"], "Erha Partner Network")

if __name__ == "__main__":
    unittest.main()
