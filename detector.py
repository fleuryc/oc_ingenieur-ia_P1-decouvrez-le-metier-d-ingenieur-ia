import requests
import uuid
import environs
from marshmallow.validate import Length, OneOf, URL


env = environs.Env()
env.read_env()

SUBSCRIPTION_KEY = env.str(
    "TRANSLATOR_TEXT_SUBSCRIPTION_KEY", validate=[Length(equal=32)]
)
ENDPOINT = env.str("TRANSLATOR_TEXT_ENDPOINT", validate=[URL()])
LOCATION = env.str("TRANSLATOR_TEXT_LOCATION", validate=[OneOf(["francecentral"])])


def detect_language(text: str) -> str:
    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
        "Ocp-Apim-Subscription-Region": LOCATION,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }
    body = [{"text": text}]
    request = requests.post(ENDPOINT, headers=headers, json=body)
    response = request.json()

    return response[0]["language"]
