import requests
import json

headers = {
    "X-RapidAPI-Key": "697a5e28c1mshe9455b0f5976c60p16167fjsnaa4655d71142",
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}


class DictionaryAPI():

    def __init__(self, word=""):
        self.word = word

    def fetch_data(self, word):
        url = "https://wordsapiv1.p.rapidapi.com/words/" + word

        try:
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                data = json.loads(response.text)
                # print("\n"+data)
                word_info = data['results'][0]
            elif response.status_code == 404:
                word_info = "NO MATCHING WORD WAS FOUND.\nYOU ENTERED AN INVALID INPUT"
        except:
            print("No internet Connection")
            word_info = "NO INTERNET CONNECTION\n\tTRY AGAIN"

        return word_info
