"""Detector Class

This file defines the Detector Class.
"""
import requests
import uuid
import environs
from marshmallow.validate import Length, OneOf, URL


class Detector:
    """
    A class used to call Azure's Translator service to detect the language of
    some text.

    Attributes
    ----------
    subscription_key : str
        Azure Translator service's key
    endpoint : str
        Azure Translator service's endpoint
    location : str
        Azure Translator service's location

    Methods
    -------
    detect_language(text=None)
        Prints the animals name and what sound it makes
    """

    def __init__(self):
        """Reads Azure Translator service parameters from environment variables.

        If any of TRANSLATOR_TEXT_SUBSCRIPTION_KEY, TRANSLATOR_TEXT_ENDPOINT or
        TRANSLATOR_TEXT_LOCATION are not defined or invalid in the environment,
        then an error is thrown.

        Environment variables
        ---------------------
        TRANSLATOR_TEXT_SUBSCRIPTION_KEY : str
            Azure Translator service's key.
            Must be 32 characters long.
            Should be defined in .env file or as an environment variable.
        TRANSLATOR_TEXT_ENDPOINT : str
            Azure Translator service's endpoint.
            Must be a valid URL.
            Should be defined in .env file or as an environment variable.
        TRANSLATOR_TEXT_LOCATION : str
            Azure Translator service's location.
            Must be a valid location ("francecentral").
            Should be defined in .env file or as an environment variable.

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        env = environs.Env()
        env.read_env()

        self.subscription_key = env.str(
            "TRANSLATOR_TEXT_SUBSCRIPTION_KEY", validate=[Length(equal=32)]
        )
        self.endpoint = env.str("TRANSLATOR_TEXT_ENDPOINT", validate=[URL()])
        self.location = env.str("TRANSLATOR_TEXT_LOCATION",
                                validate=[OneOf(["francecentral"])])

    def detect_language(self, text: str) -> str:
        """
            Detect the language of the input text by calling MS Azure 's
            Translator Text AI service.

        Args:
            text (str): Text that we want to detect the language of.

        Returns:
            str: Detected language in IETF format.
        """
        headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Ocp-Apim-Subscription-Region": self.location,
            "Content-type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4()),
        }
        body = [{"text": text}]
        request = requests.post(self.endpoint, headers=headers, json=body)
        response = request.json()

        return response[0]["language"]
