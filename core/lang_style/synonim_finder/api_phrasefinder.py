import requests
import json
import urllib #for properly encoded spaces in the url

base_url = 'https://api.phrasefinder.io/search' \
           '?corpus=eng-us&format=json&topk=5&query={0}'






def get_collocations_for_word(phrase) -> list:

    data = retrieve_server_data(phrase)

    print(json.dumps(data))

    '''json = retrieve_server_data(url)
    meanings = parce_server_data(json, word)
    synonims = []
    for meaning in meanings:
        synonims.extend(meaning.synonims)
    return synonims'''


def retrieve_server_data(phrase):
    params = {'corpus': 'eng-us', 'query': phrase, 'format': 'json', 'topk': 5}
    params = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    response = requests.get('https://api.phrasefinder.io/search', params)
    print(response.url)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError

    return response.json()




def parce_server_data(raw_data, given_word):

    pass




if __name__ == '__main__':
    get_collocations_for_word('furious dog')