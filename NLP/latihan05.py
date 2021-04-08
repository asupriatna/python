import nltk
# load the Brown Corpus
from nltk.corpus import brown

# total categories
print('Total Categories:', len(brown.categories()))

# print the categories
print(brown.categories())

# tokenized sentences
print('')
print('* tokenized sentences *')
res = brown.sents(categories='mystery')
print(res)

# get sentences in natural form
print('')
print('* get sentences in natural form *')
sentences = brown.sents(categories='mystery')
sentences = [' '.join(sentence_token) for sentence_token in sentences]
res = sentences[0:5] # viewing the first 5 sentences
print(res)

# get tagged words
tagged_words = brown.tagged_words(categories='mystery')

# get nouns from tagged words
nouns = [(word, tag) for word, tag in tagged_words 
    if any(noun_tag in tag for noun_tag in ['NP', 'NN'])]

res = nouns[0:10] # view the first 10 nouns

print('')
print('* get nouns from tagged words *')
print(res)

# build frequency distribution for nouns
nouns_freq = nltk.FreqDist([word for word, tag in nouns])
# view top 10 occuring nouns
res = nouns_freq.most_common(10)


print('')
print('* view top 10 occuring nouns *')
print(res)