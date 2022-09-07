import json
import time
from difflib import get_close_matches


class DictionaryJSON():

    def __init__(self, word=""):
        self.word = word

    def search_word(self, word):
        word = word.lower().strip()
        first_letter = word[0].upper()
        directory = "./words_data/" + first_letter + ".json"

        if first_letter.isalpha():
            with open(directory) as dir:
                dictionary_data = json.load(dir)

            if word in dictionary_data:
                word_info = dictionary_data[word]
                time.sleep(1)
            else:
                word_info = "NO MATCHING WORD WAS FOUND \n INVALID INPUT"
        else:
            try:
                with open(directory) as dir:
                    dictionary_data = json.load(dir)
            except FileNotFoundError:
                word_info= "NO MATCHING WORD WAS FOUND \n INVALID INPUT"
                print("Word does not exist.")

        return word_info

