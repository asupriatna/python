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

sentence = "You can have data without information, but you cannot have information without data"

#pos tagging
spacy_pos_tagged = [(word, word.tag_, word.pos_) for word in nlp(sentence)]
data_frame = Pandas.DataFrame(spacy_pos_tagged).T
print(data_frame)


