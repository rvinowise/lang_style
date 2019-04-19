class Corrections:
    """
    the whole initial text with added better word choices to its words
    """
    def __init__(self):
        self.word_choices = []

    def __str__(self):
        return "Corrections: %s" % self.word_choices

    def __getitem__(self, key):
        return self.word_choices[key]

    def set_given_text(self, text):
        self.word_choices
        pass