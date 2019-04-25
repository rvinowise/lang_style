from . import api_phrasefinder

api = api_phrasefinder

def get_phrases_with_word(given_word) -> list:
    return api.get_phrases_with_word(given_word)



def compare_phrases_frequency(phrases) -> list:
    return api.compare_phrases_frequency(phrases)