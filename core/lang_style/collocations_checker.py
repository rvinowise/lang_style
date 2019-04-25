

from lang_style import corrections

from lang_style.text_analyser import text_analyser
from lang_style.synonim_finder import synonim_finder

def find_word_choices_for_text(text):
    #structured_phrases = text_analyser.tokenize(text)
    structured_phrases = text_analyser.tokenize(text, 'universal')
    return find_word_choices_fot_structured_text(structured_phrases)


def find_word_choices_fot_structured_text(phrases):
    """
    :param phrases: list of tagged phrases phrases[phrase[(word, tag)]]
    :return: list(list(tuple(str,str)))
    """
    phrases1 = [synonim_finder.process(phrase) for phrase in phrases]
    for word in phrases1[0]: print(str(word))
    phrases2 = list(map(synonim_finder.process, phrases))
    for word in phrases2[0]: print(str(word))
    test = phrases1 == phrases2
    test1 = phrases1[0][1].choices == phrases2[0][1].choices

    return


if __name__=='__main__':
    text = 'We want to find synonims for this text'
    find_word_choices_for_text(text)


class Collocations_checker:
    """
    provides interface to the language styler engine
    """
    def __init__(self):
        self.corrections = corrections.Corrections()
        pass

    def set_text(self, text):
        self.text = text
        self.corrections.set_given_text(text)

    def process(self):
        self.corrections.word_choices
        pass

    def get_result(self):
        return self.corrections
