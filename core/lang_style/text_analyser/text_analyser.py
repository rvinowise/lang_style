import nltk, re, pprint

def tokenize(text):
    '''
    create a parseable structure from the given raw text
    :param: text to be tokenized
    :type param: str
    :return: tokenized text in a list of sentences which are lists of words+tokens tuples
    :rtype: list[list[tuple(str,str)]]
    '''
    sent = nltk.sent_tokenize(text)
    sent = [nltk.word_tokenize(sent) for sent in sent]
    sent = [nltk.pos_tag(sent) for sent in sent]

    return sent

class Text_analyser:
    """
    create a parseable structure from the given raw text
    """
    def __init__(self):
        print("Text_analyser __init__")
        
        