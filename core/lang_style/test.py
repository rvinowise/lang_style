import unittest as test
import sys

from .collocations_checker import Collocations_checker

class Collocation_recommendations(test.TestCase):
    """
    given text, Collocation_checker must provide an object
    with better word choices
    """

    def __init__(self):
        self.checker = Collocations_checker()
        given_text = "I eat powerful tea on the morning"
        self.checker.set_test(given_text)
        self.checker.process()
        self.better_text = self.checker.get_result()

    def setUp(self):
        pass


    def test_better_noun_attribute_is_provided(self):
        choices = self.better_text[2]
        assert choices.given_word == "powerful"
        assert "strong" in choices.better_choices

    def test_right_preposition_is_provided(self):
        choices = self.better_text[5]
        assert choices.given_word == "on"
        assert "in" in choices.better_choices



