import requests
import json
import urllib #for properly encoded spaces in the url

'''
one request to phrasefinder can contain many ngrams,
and the answer will contain their relative frequencies

we can perform 2 types of analysis:

1) get the maximum amount of long phrases with the given_word,
and search for synonims among server's collocations and 
those in the given text.
It doesn't keep the given sense, but yields better style of the resulting text
possible on Phrasefinder (query= ? given_word) 

2) get the synonims for a given word and compare frequency of each of them with
the given word
possible on Google_ngrams and Phrasefinder (query= "colloc1 given_word"/,"colloc2 given_word")

 
'''


base_url = 'https://api.phrasefinder.io/search' \
           '?corpus=eng-us&format=json&topk=5&query={0}'


def get_phrases_with_word(given_word) -> list:
    query_prev_words = '????'+given_word
    query_next_words = given_word+'????'
    raw_data = retrieve_server_data(query_prev_words)

    def parce_server_data(raw_data):
        phrases = []
        for phrase_block in raw_data['phrases']:
            phrase = []
            for token in phrase_block['tks']:
                word = token['tt']
                phrase.append(word)
            phrases.append(phrase)

        return phrases

    phrases = parce_server_data(raw_data)

    return phrases




def compare_phrases_frequency(phrases):
    '''
    :param phrases: list of str #list of list of words
    :return: list of phrases with frequencies, each phrase is a tuple of words
    :type return: dict(tuple(tuple(str..), float))
    '''
    query = '"' + '"/"'.join(phrases) + '"'
    raw_data = retrieve_server_data(query)

    def parce_server_data(raw_data):
        '''
        :param raw_data:
        :return: list of tuples (str, frequency)
        '''
        phrases = []
        for phrase_block in raw_data['phrases']:
            phrase = []
            for token in phrase_block['tks']:
                word = token['tt']
                phrase.append(word)
            frequency = phrase_block['sc']
            phrases.append((phrase, frequency))
        return phrases

    frequencies = parce_server_data(raw_data)
    frequencies = eliminate_case_sensitiveness(frequencies)

    return frequencies


def retrieve_server_data(query):
    params = {'corpus': 'eng-us', 'query': query, 'format': 'json', 'topk': 100}
    params = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    response = requests.get('https://api.phrasefinder.io/search', params)
    print(response.url)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError

    return response.json()


def eliminate_case_sensitiveness(phrases):
    '''
    joins all the variants of the same phrase, adding their frequencies
    :param phrases: list of tuples(list(words), freq) (list of phrases)
    :type param: list(tuple(list(str),float))
    :return: dict of Different phrases+frequencies
    :type return: dict(tuple(tuple(str..),float)
    '''
    total_frequencies = {}
    for phrase, frequency in phrases:
        immut_phrase = tuple(word.lower() for word in phrase)
        total_frequencies[immut_phrase] = \
            total_frequencies.get(immut_phrase, 0) + frequency

    return total_frequencies
