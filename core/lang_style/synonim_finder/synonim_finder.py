from ..word_choices import Word_choices
from . import api_webster

def process(given_text):
    finder = Synonim_finder()
    finder.set_text(given_text)
    finder.process()
    return finder.get_result()


class Synonim_finder:
    def __init__(self):
        self.words = []
        self.api = api_webster
        pass

    def set_text(self, given_text):
        self.words = list(map(lambda word: Word_choices(word), given_text.split()))

    def process(self):
        for word in self.words:
            self.add_synonims_to(word)

    def add_synonims_to(self, word):
        synonims = self.api.get_synonims_for_word(word.given_word)
        word.choices = synonims

    def get_result(self):
        return self.words

    @classmethod
    def clear(self):
        print("clear "+repr(self))