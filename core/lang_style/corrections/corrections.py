from .word_choices import word_choices


class Corrections:
    """
    the whole initial text with added better word choices to its words
    """
    def __init__(self):
        self.word_choices = []

    def __str__(self):
        return "Corrections: %s" % self.word_choices
