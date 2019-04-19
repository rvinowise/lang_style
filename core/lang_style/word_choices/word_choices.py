

class Word_choices:
    """
    possible word choices for the given word, according to collocations
    """
    def __init__(self, given_word: str):
        self.given_word: str = given_word
        self.choices: list = []

    def add_choices(self, choices):
        self.choices.extend(choices)

    def __getitem__(self, key):
        return self.choices[key]

