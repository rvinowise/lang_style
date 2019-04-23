from . import api_phrasefinder

api = api_phrasefinder

def get_phrases_with_word(given_word) -> list:
    return api.get_phrases_with_word(given_word)