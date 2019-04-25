

class Word_choices():
    """
    possible word choices for the given word, according to collocations.
    takes use of the Tag - the part of speech encoded
    """

    def __init__(self, given_word: str,
                       tag:str = None):
        self.given_word: str = given_word
        self.tag: str = tag
        self.choices: list = []


    def add_choices(self, choices):
        self.choices.extend(choices)

    def __getitem__(self, key):
        return self.choices[key]

    def __str__(self):
        info = '''{2} [{0} {1}]'''\
            .format(self.given_word, self.tag, self.__class__.__name__)+'''
        synonims: 
        '''+', '.join(self.choices)
        return info;
