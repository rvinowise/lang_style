import requests
import json
import urllib #for properly encoded spaces in the url

base_url = 'https://api.phrasefinder.io/search' \
           '?corpus=eng-us&format=json&topk=5&query={0}'






def get_collocations_for_word(phrase) -> list:
    '''url = base_url.format(phrase);
    print(url)'''

    params = {'corpus': 'eng-us', 'query': phrase, 'format': 'json', 'topk': 5}
    params = urllib.parse.urlencode(params, quote_via=urllib.)
    response = requests.get('https://api.phrasefinder.io/search', params)
    #response = requests.get(url);
    print(response.url)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError
    json = response.json()
    print(json)

    '''json = retrieve_server_data(url)
    meanings = parce_server_data(json, word)
    synonims = []
    for meaning in meanings:
        synonims.extend(meaning.synonims)
    return synonims'''

'''def retrieve_server_data(url):

    if response.status_code != 200:
        raise requests.exceptions.HTTPError

    return response.json()


from enum import Enum
class Part_of_speech(Enum):
    NONE = 0
    NOUN=1
    ADJ=2
    VERB=3
    ADV=4
'''


def parce_server_data(raw_data, given_word):

    return meanings




if __name__ == '__main__':
    print(get_collocations_for_word('furious dog'))