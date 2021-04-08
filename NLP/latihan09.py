import nltk
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg
import numpy as np

emma_words = gutenberg.words('shakespeare-caesar.txt')

line_lengths = [len(sentence) for sentence in emma_words]
plt.hist(line_lengths)
plt.show()

#total_tokens_per_line = [len(sentence.split()) for sentence in emma_words]
#plt.hist(total_tokens_per_line, color='orange')
#plt.show()