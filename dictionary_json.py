import json
import time
import difflib


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
                # word = "learning"
                n = 5
                cutoff = 0.7

                close_matches = difflib.get_close_matches(word,
                                                          dictionary_data, n, cutoff)

                print(close_matches)
                if close_matches == []:
                    word_info = "NO MATCHING WORD WAS FOUND.\nYOU ENTERED AN INVALID INPUT"
                else:
                    word_info = ", ".join(close_matches).title()
                    word_info = f"NO MATCHING WORD WAS FOUND\nTRY THIS WORD:\n\n {word_info}"
        else:
            try:
                with open(directory) as dir:
                    dictionary_data = json.load(dir)
            except FileNotFoundError:
                word_info = "NO MATCHING WORD WAS FOUND.\nYOU ENTERED AN INVALID INPUT"
                print("Word does not exist.")

        return word_info
