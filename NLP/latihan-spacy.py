import spacy
from spacy import displacy

#text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."
sentence = "The brown fox is quick and he is jumping over the lazy dog"

nlp = spacy.load("en_core_web_sm")
doc = nlp(sentence)
#displacy.serve(doc, style="ent")
f = open("result_spacy.html", "a")
f.write(spacy.displacy.render(doc, style="dep", page="true"))
#f.write(displacy.serve(doc, style="dep"))
f.close()_spacy