import pytest
import sys

from .collocations_checker import Collocations_checker


"""
given text, Collocation_checker must provide an object
with better word choices
"""

@pytest.fixture(scope='module', params=[
                    "I eat powerful tea on the morning",
                    "huge wind",
                    "hit the door"]
                )
def execute_collocations_checker(request):
    given_text = request.param
    checker = Collocations_checker()
    checker.set_text(given_text)
    checker.process()
    better_text = checker.get_result()
    return better_text


'''def test_better_noun_attribute_is_provided(
        execute_collocations_checker):

    better_text = execute_collocations_checker
    choices = better_text[2]
    assert choices.given_word == "powerful"
    assert "strong" in choices.better_choices'''


"""def test_right_preposition_is_provided(
        execute_collocations_checker):

    better_text = execute_collocations_checker
    choices = better_text[5]
    assert choices.given_word == "on"
    assert "in" in choices.better_choices"""



