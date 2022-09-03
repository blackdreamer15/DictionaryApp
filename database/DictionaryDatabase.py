import json

class DictionaryDatabase():
    """
    Returns a tuple of (definition, synonyms, antonyms) if word exists.
    
    Returns 'Word does not exist.' if it does not exist.

    Input should be a string.
    """
    
    
    
    def definition(word):
        word = word.lower().strip()
        first_letter = word[0]

        # knowing the first letter of the word, we can go straight to the json file to open
        if first_letter.isalpha():
            section = "./database/words_data/" + first_letter + ".json"
            with open(section) as sec:
                dictionary_data = json.load(sec)
        else:
            try:
                pass
            except FileNotFoundError:
                return "Word does not exist."
            
        # with dic data, we find all info about the word
        if word in dictionary_data:
            word_info = dictionary_data[word]
            word_meaning = word_info["definition"]
            
            
        
         
         
            if type(word_info["SYNONYMS"]) == list or type(word_info["ANTONYMS"]) == list:
                word_synonyms = ", ".join(syn for syn in word_info["SYNONYMS"] if syn.upper() != word)
                word_antonyms = ", ".join(word_info["ANTONYMS"])
            else:
                word_synonyms = word_info["SYNONYMS"]
                word_antonyms = word_info["ANTONYMS"]
            word_meanings_s = ""
            for key in word_meanings:
                if type(word_meanings[key]) == list:
                    for item in word_meanings[key]:
                        if type(item) == list:
                            for one in item:
                                word_meanings_s = word_meanings_s + "\n" + one
                        else:
                            word_meanings_s = word_meanings_s + "\n" + item

                    word_meanings_s += "\n"
                else:
                    word_meanings_s = word_meanings_s + "\n" + word_meanings[key]
            return (word_meanings_s.strip("\n"), word_synonyms, word_antonyms)
        else:
            return "Word does not exist."
        
        
    def partOfSpeech():
        pass
    def synonyms():
        pass
    def antonyms():
        pass