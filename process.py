#!/usr/bin/python
import spacy

nlp = spacy.load('en')
corpus = open("corpus.txt", "r").read()

doc = nlp(corpus)

rankings = {}

for ent in doc.ents:
	if ent.label_ == "GPE" or ent.label_ == "NORP":
		rankings[ent.text] = rankings.get(ent.text, 0) + 1

for place in sorted(rankings.items(), key=lambda item: item[1], reverse=True):
	print("\"{}\", {}".format(place[0], place[1]))
