from dotenv import load_dotenv
import os
import requests
from pprint import pprint

# read env variables
load_dotenv()

API_URL='https://api-inference.huggingface.co/models/bigscience/bloomz'
# headers={'Authorization':os.getenv('HUGGING_FACE_ACCESS_KEY')}
headers={'Authorization':'Bearer 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'}

print(headers)

def query(payload):
    try:
        response=requests.post(API_URL,headers=headers,json=payload)
    except Exception as e:
        print(str(e))
    return response

params={'max_length':200,'temperature':2.5,'top_k':10}
output=query({
    'inputs':'India is my country, all indians are',
    'parameters':params
})

print(output)

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()