import pytest

from . import text_analyser



@pytest.mark.parametrize('text, tokens', [
(
    '''They process data, it's a tough process''',
    '''PRP VBP NNS , PRP VBZ DT JJ NN'''
),
(
    '''My friends refuse to permit us to obtain the refuse permit''',
    '''PRP$ NNS VBP TO VB PRP TO VB DT NN NN'''
)
])
def test_string_tokenized(text, tokens):
    correct_tokens = tokens.split()
    tokenized_first_sentence = text_analyser.tokenize(text)[0]
    for i_word, (word, token) in enumerate(tokenized_first_sentence):
        assert token == correct_tokens[i_word]





