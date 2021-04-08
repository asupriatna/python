import nltk
import spacy
import numpy as Numpy
import pandas as Pandas

# install the package
# !pipenv install nltk spacy numpy pandas
# !python -m spacy download en_core_web_sm
# !python -m spacy download en
# following line is optional for custom vocabulary installation
nlp = spacy.load('en_core_web_sm')

sentence = "The brown fox is quick and he is jumping over the lazy dog"
words = sentence.split()
pos_tags = nltk.pos_tag(sentence.split())
data_frame = Pandas.DataFrame(pos_tags).T
print(data_frame)


