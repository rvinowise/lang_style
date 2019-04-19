

from lang_style import corrections

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
