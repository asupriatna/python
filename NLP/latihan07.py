import nltk
from nltk.corpus import wordnet as WordNet

word = 'hike' # taking hike as our word of interest
# get word synsets
word_synsets = WordNet.synsets(word)
print('word synsets :',word_synsets)

# get details for each synonym in synset
for synset in word_synsets:
    print(('Synset Name: {name}\n'
           'POS Tag: {tag}\n'
           'Definition: {defn}\n'
           'Examples: {ex}\n').format(name=synset.name(),
                                      tag=synset.pos(),
                                      defn=synset.definition(),
                                      ex=synset.examples()))
