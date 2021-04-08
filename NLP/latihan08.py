import nltk
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg

# get the items of gutenber
print(gutenberg.fileids())

emma_words = gutenberg.words('austen-emma.txt')
print(type(emma_words))

# How many tokens in the text:
print("\nToken count:", len(emma_words))

# What is the token at index 1000?
print("\ntoken at index 1000:", emma_words[1000])

# Slice from token 1400 to 1500
print("\nslice from 1400 to 1500:", emma_words[1400:1500])

token_len = []
for token in emma_words:
    token_len.append(len(token))
print("\ntoken_len:", token_len[:20])

import matplotlib.pyplot
import seaborn

