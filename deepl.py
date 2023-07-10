import requests

def translate_token(token, target_language, api_key):
    # DeepL API endpoint
    url = "https://api-free.deepl.com/v2/translate"

    # API parameters
    params = {
        "text": token,
        "target_lang": target_language
    }
    headers = {
        "Authorization": f"DeepL-Auth-Key {api_key}"
    }

    try:
        # Sending POST request to DeepL API
        response = requests.post(url, data=params, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        translation = response.json()["translations"][0]["text"]

        return translation
    except requests.exceptions.RequestException as e:
        print("Translation failed:", e)

# Usage example
if __name__ == "__main__":
    translated_text = translate_token("Hello, how are you?", "fr")
    print(translated_text)