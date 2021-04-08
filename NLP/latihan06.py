import nltk
# load the Reuters Corpus
from nltk.corpus import reuters
# total categories
print('Total Categories:', len(reuters.categories()))

# print the categories
print()
print('The Categories:', reuters.categories())

# get sentences in housing and income categories
sentences = reuters.sents(categories=['housing', 'income'])
sentences = [' '.join(sentence_tokens) for sentence_tokens in sentences]
res = sentences[0:5]  # view the first 5 sentences
print()
print("The Sentences in housing and income categories:", res)

# fileid based access
res = reuters.fileids(categories=['housing', 'income'])
print()
print("fileid based:", res)

print()
res=reuters.sents(fileids=[u'test/16118', u'test/18534'])
print("fileid based: test/16118, training/6000 ", res)
