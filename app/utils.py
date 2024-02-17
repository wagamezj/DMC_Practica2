import requests

headers = {"Authorization": "Bearer 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"}

def query(payload):

    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"  
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


def query2(filename):

    API_URL = "https://api-inference.huggingface.co/models/Laxhar/anime_aesthetic_variant"
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()








