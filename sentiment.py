import requests
from pprint import pprint
import random

subscription_key = "6b54e4de8f394a07a8f2b71daf945b2e"
text_analytics_base_url = "https://westeurope.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"

def get_sentiment(input_reviews):
    result = []
    id = 1
    for i in input_reviews:
        dict = {
            'id': id,
            'score': i
        }
        result.append(dict)
        id += 1
    documents = {'documents': result}
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    response  = requests.post(text_analytics_base_url, headers=headers, json=documents)
    analysis = response.json()
    pprint(analysis)
    return analysis