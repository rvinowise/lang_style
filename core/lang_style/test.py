import pytest
import unittest
import sys

from .collocations_checker import Collocations_checker

class Collocation_recommendations(unittest.TestCase):
    """
    given text, Collocation_checker must provide an object
    with better word choices
    """

    def setUp(self):
        self.checker = Collocations_checker()
        given_text = "I eat powerful tea on the morning"
        self.checker.set_text(given_text)
        self.checker.process()
        self.better_text = self.checker.get_result()


    def test_better_noun_attribute_is_provided(self):
        choices = self.better_text[2]
        assert choices.given_word == "powerful"
        assert "strong" in choices.better_choices

    def test_right_preposition_is_provided(self):
        choices = self.better_text[5]
        assert choices.given_word == "on"
        assert "in" in choices.better_choices



