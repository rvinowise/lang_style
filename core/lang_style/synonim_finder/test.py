import pytest
import unittest


from . import synonim_finder


@pytest.fixture(scope='module', params=[
    "My friends like playing games",
    "a big house"
])
def synonim_finder_works(request):
    result = synonim_finder.process(request.param)
    return result

@pytest.fixture(params = [
    '  My  random text  with some   words'
])
def synonim_finder_initialized(request):
    finder = synonim_finder.Synonim_finder
    finder.set_text(request.param)
    yield finder
    finder.clear()


@pytest.mark.parametrize('given_text', [
    ("My friends like playing games")
])
def test_result_is_initialized(given_text):
    finder = synonim_finder.Synonim_finder()
    finder.set_text(given_text)
    for i, word in enumerate(given_text.split()):
        assert finder.words[i].given_word == word


@pytest.mark.parametrize('given_text', [
    ('a huge dwelling is built')
])
def test_provide_synonims_for_a_phrase(given_text):
    result = synonim_finder.process(given_text)
    print(result[1])
    assert 'big' in result[1]
    assert 'house' in result[2]
    assert 'make' in result[4]