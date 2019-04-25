import pytest
import unittest


from . import synonim_finder



@pytest.mark.parametrize('given_text', [
    #"My friends like playing games"
    ([('My', 'PRP$'), ('friends', 'NNS'), ('like', 'IN'), ('playing', 'VBG'), ('games', 'NNS')])
])
def test_result_is_initialized(given_text):
    finder = synonim_finder.Synonim_finder()
    finder.set_text(given_text)
    for i, word_and_tag in enumerate(given_text):
        assert finder.words[i].given_word == word_and_tag[0]
        assert finder.words[i].tag == word_and_tag[1]


@pytest.mark.parametrize('given_text', [
    #'a huge dwelling is built quickly'
    ([('a', 'DET'), ('huge', 'ADJ'), ('dwelling', 'NOUN'),
      ('is', 'VERB'), ('built', 'VERB'), ('quickly', 'ADV')])
])
def test_provide_synonims_for_a_phrase(given_text):
    '''
    demonstration of the module's work
    :param given_text: output of nltk.word_tokenize()+nltk.pos_tag(),
                        with Universal tags (NOUN)
    :return:
    '''
    # given_text = [(word, nltk.tag.map_tag('en-ptb', 'universal', tag))
    #               for word, tag in given_text]

    result = synonim_finder.process(given_text)
    assert 'enormous' in result[1]
    assert 'house' in result[2]
    assert 'make' in result[4]
    assert 'fast' in result[5]
    print(result)
    print(result[5])

@pytest.mark.parametrize('word', [
    ('trololol')
])
def test_unknown_word_return_empty_synonims_list(word):
    result = synonim_finder.process(word)
    assert result[0].choices == []