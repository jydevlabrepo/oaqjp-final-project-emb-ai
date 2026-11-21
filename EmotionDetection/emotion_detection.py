import requests

def emotion_detector(text_to_analyze):
    """
    Use the Emotion Predict function of the Watson NLP Library.
    """
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    payload = {
        "raw_document": { "text": text_to_analyze }
    }

    # Construct the POST.
    response = requests.post(URL, json = payload, headers = headers)

    # Retrieve the emotions.
    results = response.json()['emotionPredictions'][0]['emotion']
    
    # Get the highest score emotion.
    dominant_name = max(results, key = results.get)

    # Output and formatting.
    print("{")
    for key, value in results.items():
        print(f"'{key}': {value}")
    print("'dominant_emotion':", dominant_name)
    print("}")

emotion_detector("I am so happy I am doing this.")

