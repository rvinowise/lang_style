import pytest
import unittest

import nose2

from .my_synonim_finder import Synonim_finder

class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.finder = Synonim_finder()
        pass

    def test_provide_synonims_for_a_phrase(self):
        pass
