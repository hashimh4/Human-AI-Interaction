import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions
from requests.auth import HTTPBasicAuth 

authenticator = IAMAuthenticator("")
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version="",
    authenticator=authenticator
)

natural_language_understanding.set_service_url("")

response = natural_language_understanding.analyze(
    html="<html><head><title>Fruits</title></head><body><h1>Apples and Oranges</h1><p>I love apples! I don't like oranges.</p></body></html>",
    features=Features(emotion=EmotionOptions(targets=['apples','oranges']))).get_result()

print(json.dumps(response, indent=2))