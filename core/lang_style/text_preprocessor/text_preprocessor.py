"""
clears and prepares input text before passing it to processors
"""

import re

def process(text):
    #text = re.sub(' +', '', text)
    text = " ".join(text.split())
    return text

'''class Text_preprocessor:

    def __init__(self):
        print("Text_preprocessor __init__")
        
      '''