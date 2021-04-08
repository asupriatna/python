import nltk
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg
import numpy as np


shakespeare = gutenberg.words('shakespeare-caesar.txt')

tokens = [item.split() for item in shakespeare]
print(tokens[:5])

words = [word for sentence in tokens for word in sentence]
print('\n',words[:20])

#filter only string
import re
words = list(filter(None, [re.sub(r'[^A-Za-z]', '', word) for word in words]))
print('\n Filter:',words[:20])


from collections import Counter
words = [word.lower() for word in words]
c = Counter(words)
print('\nCollections',c.most_common(10))

#stopwords filtered
stopwords = nltk.corpus.stopwords.words('english')
words = [word.lower() for word in words if word.lower() not in stopwords]
c = Counter(words)
print('\nStop words',c.most_common(10))