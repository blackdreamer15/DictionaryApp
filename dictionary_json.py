import json
import time as ttt
from difflib import get_close_matches
from dictionary_api import DictionaryAPI

dict_api = DictionaryAPI()


class DictionaryJSON():

    def __init__(self, word=""):
        self.word = word

    def search_word(self, word):
        word = word.lower().strip()
        first_letter = word[0].upper()

        if first_letter.isalpha():
            directory = "./words_data/" + first_letter + ".json"
            print(directory)

            with open(directory) as dir:
                dictionary_data = json.load(dir)

        else:
            try:
                pass
            except FileNotFoundError:
                return "Word does not exist."

        if word in dictionary_data:
            word_info = dictionary_data[word]
            # word_meaning = word_info["definition"]
            # part_of_speech = word_info['partOfSpeech']
            # word_synonyms = ", ".join(word_info['synonyms'])
            # word_antonyms = ", ".join(word_info['antonyms'])
            # word_examples = "\n".join(word_info['examples'])
            ttt.sleep(1)
        else:
            #     dict_api= Dictionary1()
            word_info = dict_api.fetch_data(word)

        return word_info

        # print(f"Definition: {word_meaning}")
        # print(f"Part of speech: {part_of_speech}")
        # print(f"Synonyms: {word_synonyms}")
        # print(f"Antonyms: {word_antonyms}")
        # print(f"Examples: \n{word_examples}")


# dic = Dictionary()

# word = input("Enter the word you want to search for: ")
# dic.search_word(word)
