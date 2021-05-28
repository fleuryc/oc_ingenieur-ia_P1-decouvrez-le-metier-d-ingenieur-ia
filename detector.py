# -*- coding: utf-8 -*-

import json
import os
import requests
import uuid
from dotenv import load_dotenv


class Detector:
    constructed_url: str
    headers: dict

    def __init__(self):
        load_dotenv()  # take environment variables from .env.

        key_var_name = 'TRANSLATOR_TEXT_SUBSCRIPTION_KEY'
        if key_var_name not in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
        subscription_key = os.environ[key_var_name]

        endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'
        if endpoint_var_name not in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
        endpoint = os.environ[endpoint_var_name]

        location_var_name = 'TRANSLATOR_TEXT_LOCATION'
        if location_var_name not in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(location_var_name))
        location = os.environ[location_var_name]

        path = '/detect?api-version=3.0'
        self.constructed_url = endpoint + path

        self.headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

    def detect_language(self, text: str):
        body = [{
            'text': text
        }]
        request = requests.post(self.constructed_url, headers=self.headers, json=body)
        response = request.json()

        return [{
            'language': response[0]["language"],
            'score': response[0]["score"]
        }]
