import requests
import json

#key = 'aed55444-63f0-4746-a40e-77f8ad3621f6'
base_url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{0}?key=aed55444-63f0-4746-a40e-77f8ad3621f6'
#base_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{0}?key=60259b4e-7d8d-44bd-8f2b-cd7053095a8e'




def get_synonims_for_word(word, tag) -> list:
    '''
    :param word: search synonims for this
    :param tag: Universal encoding (NOUN)
    :type param word: str
    :type param tag: str
    :return: list(Word_choice)
    '''
    url = base_url.format(word);
    #print(url)
    json = retrieve_server_data(url)
    meanings = parce_server_data(json,
                                 word,
                                 tag_universal_to_webster(tag))
    synonims = []
    for meaning in meanings:
        synonims.extend(meaning.synonims)
    return synonims

universal_to_api_tags = {
    'NOUN': 'noun',
    'ADJ': 'adjective',
    'VERB': 'verb',
    'ADV': 'adverb'
}
def tag_universal_to_webster(universal_tag):
    '''
    webster uses special names for parts pf speech.
    the caller code uses nltk tags ('universal' - for pure parts of speech,
    'en-ptb' - for maxumum information on forms)
    :param universal_tag: tag in Universal style (NOUN)
    :return:
    '''
    return universal_to_api_tags[universal_tag]

def retrieve_server_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError

    return response.json()

'''
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
        self.tag:str = None
        self.definition:str = None
        self.synonims = []
    def __str__(self):
        return '''<Meaning: {0}
        {1}
        {2}
        >'''.format(self.part, self.definition, self.synonims)

def parce_server_data(raw_data, searched_word, searched_tag):
    if (word_found(raw_data)):
        return collect_synonims(raw_data, searched_word, searched_tag)
    else:
        return []

def word_found(raw_data):
    """
    webster server returns a plain list of possible similar spelled words,
    if it doesn't find the searched word
    """
    return 'meta' in raw_data[0]


def collect_synonims(raw_data, searched_word, searched_tag):
    meanings = []
    for part_of_speech_block in raw_data:
        if part_of_speech_block['fl'] != searched_tag.lower():
            continue

        if (not is_exact_word(part_of_speech_block['meta']['id'], searched_word)):
            continue

        for i_definition, definition in enumerate(part_of_speech_block['shortdef']):
            meaning = Meaning()
            meaning.definition = definition
            meaning.synonims = part_of_speech_block['meta']['syns'][i_definition]
            meanings.append(meaning)

    return meanings


def is_exact_word(server_word, given_word):
    '''
    for request 'dog' server may response 'dog collar' - ignore it
    :param server_word: word returned from the server
    :param given_word: word that we are searching synonims for
    :return: whether we must consider this answer-word, or it's different
    '''
    import re
    return re.subn(r'[^a-zA-Z]','', server_word)[1] == re.subn(r'[^a-zA-Z]','', given_word)[1]

if __name__ == '__main__':
    res = get_synonims_for_word("dog", 'NOUN')
    print(res)

