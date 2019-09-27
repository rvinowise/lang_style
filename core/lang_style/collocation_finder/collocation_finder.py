from . import api_phrasefinder

api = api_phrasefinder

def get_phrases_with_word(given_word) -> list:
    return api.get_phrases_with_word(given_word)



def compare_phrases_frequency(phrases) -> list:
    phrases_dict = api.compare_phrases_frequency(phrases)
    phrases_list = [phrase_freq for phrase_freq in phrases_dict.items()]
    phrases_list.sort(key = lambda phrase_freq: phrase_freq[1], reverse=True)
    return phrases_list
