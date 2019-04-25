from builtins import print

import pytest

from . import api_phrasefinder, collocation_finder


@pytest.fixture(params=[

])
def data_prepared(request):
    pass


@pytest.mark.parametrize('word, true_phrases', [
    (
        "tea",
        # those are just real data from the server, it may change occasionally
        ['for a cup of tea', 'have a cup of tea']
    )
])
def test_collocations_found(word, true_phrases):
    tested_phrases = collocation_finder.get_phrases_with_word(word)
    for i_phrase, true_phrase in enumerate(true_phrases):
        assert ' '.join(tested_phrases[i_phrase]) == true_phrase
    print(tested_phrases)


@pytest.mark.parametrize('phrases, true_frequencies', [
    (['strong tea', 'powerful tea', 'trololo blabalbla lol tea', 'bitter tea'],
     [4,2,1,3]
     )
])
def test_phrases_relative_frequency_found(phrases, true_frequencies):
    test_frequencies = api_phrasefinder.compare_phrases_frequency(phrases)
    true_sorted = sorted(tuple(zip(phrases, true_frequencies)), key=lambda x:x[1], reverse=True)
    print(true_sorted)
    for i_phrase, test_phrase in enumerate(test_frequencies):
        assert test_phrase == tuple(true_sorted[i_phrase][0].split(' '))





