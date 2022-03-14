import unittest
import requests
import json


class GetSessionsTest(unittest.TestCase):

    def __init__(self, *args):
        file = open('test_settings.json')
        self.__settings_json = json.load(file)
        self.__base_url = self.__settings_json['BaseURL']
        self.__token_type = self.__settings_json['TokenType']
        self.__create_session_model = self.__settings_json['CreateSessionFullModel']
        self.__get_session_url_postfix = self.__settings_json['GetSessionUrlPostfix']
        super(GetSessionsTest, self).__init__(*args)

    def test_create_session_and_get_sessions(self):
        create_session_response = requests.post(self.__base_url, self.__create_session_model)
        create_session_response_json = create_session_response.json()
        integration_url = create_session_response_json["integrationUrl"]
        session_token = create_session_response_json["sessionToken"]
        self.assertEqual(create_session_response.status_code, 200, "Create session code should be 200")
        self.assertEqual(create_session_response_json["integrationUrl"], "https://magic.saas-3.veriff.me")

        headers = {'Authorization': self.__token_type + session_token}
        get_sessions_response = requests.get(integration_url + self.__get_session_url_postfix, headers=headers)
        self.assertEqual(get_sessions_response.status_code, 200, "Get sessions code should be 200")
        get_sessions_response_json = get_sessions_response.json()
        self.assertEqual(get_sessions_response_json["status"], "created")
        self.assertEqual(get_sessions_response_json["initData"]["language"], "ca")
        self.assertEqual(get_sessions_response_json["initData"]["preselectedDocument"]["country"], "AL")
        self.assertEqual(get_sessions_response_json["initData"]["preselectedDocument"]["type"], "DRIVERS_LICENSE")

    def test_get_sessions_without_auth_token(self):
        create_session_response = requests.post(self.__base_url, self.__create_session_model)
        create_session_response_json = create_session_response.json()
        integration_url = create_session_response_json["integrationUrl"]
        self.assertEqual(create_session_response.status_code, 200, "Create session code should be 200")
        self.assertEqual(create_session_response_json["integrationUrl"], "https://magic.saas-3.veriff.me")

        get_sessions_response = requests.get(integration_url + self.__get_session_url_postfix)
        self.assertEqual(get_sessions_response.status_code, 401, "Get sessions should return Unauthorized error")
