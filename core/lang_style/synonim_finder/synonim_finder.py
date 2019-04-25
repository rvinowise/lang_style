from ..word_choices import Word_choices
from . import api_webster

def process(given_text):
    '''
    :param given_text: list of tuple(word, tag),
                       tag is the Universal name of a part of speech (NOUN)
    :type param: list(tuple(str,str))
    :return:
    '''
    finder = Synonim_finder()
    finder.set_text(given_text)
    finder.process()
    return finder.get_result()


class Synonim_finder:
    def __init__(self):
        self.words:Word_choices = []
        self.api = api_webster
        pass

    def set_text(self, given_text):
        '''
        :param given_text: text[(word, tag)] tag is Universal (NOUN)
        :type param: list(tuple(str, str))
        :return:
        '''
        self.words = list(map(lambda word_tag: Word_choices(*word_tag), given_text))

    def process(self):
        for word in self.words:
            if self.worth_finding_synonims(word.tag):
                self.add_synonims_to(word)

    def worth_finding_synonims(self, tag):
        '''if there is no this Tag in the API's possible tags -
        this API can't find synonims for those (e.g. articles)'''
        return tag in self.api.universal_to_api_tags

    def add_synonims_to(self, word: Word_choices):
        synonims = self.api.get_synonims_for_word(word.given_word, word.tag)
        word.choices = synonims

    def get_result(self):
        return self.words

    @classmethod
    def clear(self):
        print("clear "+repr(self))


