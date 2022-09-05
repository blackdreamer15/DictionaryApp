import requests
import json


word = input("Enter the word you wanna search for: ").lower()


headers = {
    "X-RapidAPI-Key": "697a5e28c1mshe9455b0f5976c60p16167fjsnaa4655d71142",
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}


class DictionaryAPI():

    def __init__(self, word=""):
        self.word = word

    def fetch_data(self, word):
        url = "https://wordsapiv1.p.rapidapi.com/words/" + word
        response = requests.request("GET", url, headers=headers)
        data = json.loads(response.text)
        self.search_word(data)

    def search_word(self, data):
        word_info = data['results'][0]
        word_meaning = word_info["definition"]
        part_of_speech = word_info['partOfSpeech']
        word_synonyms = ", ".join(word_info['synonyms'])

        print(f"Definition: {word_meaning}")
        print(f"Part of speech: {part_of_speech}")
        print(f"Synonyms: {word_synonyms}")

        try:
            word_examples = "\n".join(word_info['examples'])
            print(f"Examples: \n{word_examples}")

        except:
            pass
        
        try:
            word_antonyms = ", ".join(word_info['antonyms'])
            print(f"Antonyms: {word_antonyms}")
        except:
            pass


dic = DictionaryAPI()
dic.fetch_data(word)
