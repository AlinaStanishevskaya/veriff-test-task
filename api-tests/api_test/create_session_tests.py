import unittest
import requests
import json


class CreateSessionTests(unittest.TestCase):

    def __init__(self, *args):
        file = open('test_settings.json')
        self.__settings_json = json.load(file)
        self.__base_url = self.__settings_json['BaseURL']
        self.__create_session_model = self.__settings_json['CreateSessionFullModel']
        super(CreateSessionTests, self).__init__(*args)

    def test_create_session(self):
        response = requests.post(self.__base_url, self.__create_session_model)
        response_json = response.json()
        self.assertEqual(response.status_code, 200, "Session should be created")
        self.assertEqual(response_json["integrationUrl"], "https://magic.saas-3.veriff.me")

    def test_create_session_with_full_name_only(self):
        payload = {
            "full_name": "Janina Alta",
        }

        response = requests.post(self.__base_url, payload)
        response_json = response.json()
        self.assertEqual(response.status_code, 200, "Session should be created with full_name only")
        self.assertEqual(response_json["integrationUrl"], "https://magic.saas-3.veriff.me")

    def test_create_session_without_full_name(self):
        payload = {
            "document_country": "AL",
            "document_type": "DRIVERS_LICENSE",
            "lang": "ca",
            "additionalData": {
                "isTest": "false"
            }
        }

        response = requests.post(self.__base_url, payload)
        self.assertEqual(response.status_code, 500, "Create session code should be 500")

    def test_create_session_with_not_existing_document_type(self):
        payload = {
            "document_country": "AL",
            "document_type": "not existing type",
            "lang": "ca",
            "full_name": "Janina Alta",
            "additionalData": {
                "isTest": "false"
            }
        }

        response = requests.post("https://demo.saas-3.veriff.me/", payload)
        self.assertEqual(response.status_code, 400, "Session should not be created with not existing document type")

    def test_create_session_with_not_existing_document_country(self):
        payload = {
            "document_country": "not existing country",
            "document_type": "DRIVERS_LICENSE",
            "lang": "ca",
            "full_name": "Janina Alta",
            "additionalData": {
                "isTest": "false"
            }
        }

        response = requests.post("https://demo.saas-3.veriff.me/", payload)
        self.assertEqual(response.status_code, 400, "Session should not be created with not existing document country.")

    def test_create_session_with_not_existing_lang(self):
        payload = {
            "document_country": "AL",
            "document_type": "DRIVERS_LICENSE",
            "lang": "not existing lang",
            "full_name": "Janina Alta",
            "additionalData": {
                "isTest": "false"
            }
        }

        response = requests.post("https://demo.saas-3.veriff.me/", payload)
        self.assertEqual(response.status_code, 200, "Session should be created with not existing lang.")
