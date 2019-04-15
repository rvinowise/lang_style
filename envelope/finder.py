import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

# Ngrams with 'creature' as a member
creature_filter = lambda *w: 'wind' not in w


## Bigrams
finder = BigramCollocationFinder.from_words(
   nltk.corpus.brown.words())
# only bigrams that appear 3+ times
finder.apply_freq_filter(3)
# only bigrams that contain 'creature'
finder.apply_ngram_filter(creature_filter)
# return the 10 n-grams with the highest PMI
print(finder.nbest(bigram_measures.likelihood_ratio, 100))


## Trigrams
finder = TrigramCollocationFinder.from_words(
   nltk.corpus.brown.words())
# only trigrams that appear 3+ times
finder.apply_freq_filter(3)
# only trigrams that contain 'creature'
finder.apply_ngram_filter(creature_filter)
# return the 10 n-grams with the highest PMI
print(finder.nbest(trigram_measures.likelihood_ratio, 100))





