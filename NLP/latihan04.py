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

#pos tagging with grammer
grammar = '''
            NP: {<DT>?<JJ>?<NN.*>}  
            ADJP: {<JJ>}
            ADVP: {<RB.*>}
            PP: {<IN>}      
            VP: {<MD>?<VB.*>+}
          '''

pos_tagged_sent = nltk.pos_tag(sentence.split())
rp = nltk.RegexpParser(grammar)
parsed_sent = rp.parse(pos_tagged_sent)
print(parsed_sent)


