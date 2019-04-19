import requests
import json

#key = 'aed55444-63f0-4746-a40e-77f8ad3621f6'
base_url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{0}?key=aed55444-63f0-4746-a40e-77f8ad3621f6'
#base_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{0}?key=60259b4e-7d8d-44bd-8f2b-cd7053095a8e'







def get_collocations_for_word(phrase) -> list:
    '''url = base_url.format(word);
    print(url)'''

    params = {'corpus': 'eng-us', 'query': phrase, 'format': 'json', 'topk': 5}
    response = requests.get('https://api.phrasefinder.io/search', params)
    json = response.json()

    '''json = retrieve_server_data(url)
    meanings = parce_server_data(json, word)
    synonims = []
    for meaning in meanings:
        synonims.extend(meaning.synonims)
    return synonims'''

'''def retrieve_server_data(url):

    if responce.status_code != 200:
        raise requests.exceptions.HTTPError

    return responce.json()


from enum import Enum
class Part_of_speech(Enum):
    NONE = 0
    NOUN=1
    ADJ=2
    VERB=3
    ADV=4
'''

class Meaning:
    def __init__(self):
        self.part = "" #Part_of_speech.NONE
        self.definition = ''
        self.synonims = []
    def __str__(self):
        return '''<Meaning: {0}
        {1}
        {2}
        >'''.format(self.part, self.definition, self.synonims)

def parce_server_data(raw_data, given_word):
    meanings = []
    for part_of_speech_block in raw_data:
        if (not is_exact_word(part_of_speech_block, given_word)):
            continue

        for i_definition, definition in enumerate(part_of_speech_block['shortdef']):
            meaning = Meaning()
            meaning.part = part_of_speech_block['fl']
            meaning.definition = definition
            meaning.synonims = part_of_speech_block['meta']['syns'][i_definition]
            meanings.append(meaning)

    return meanings


def is_exact_word(raw_meaning, given_word):
    return raw_meaning['meta']['id'] == given_word

if __name__ == '__main__':
    get_collocations_for_word('furious dog')