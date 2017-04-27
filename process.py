#!/usr/bin/python
import spacy
import re

countries = open("countries.txt", "r").read().split("\n")

totals = [0] * len(countries)
nameToIndex = {}

for index, name in enumerate(countries):
	nameToIndex[name.lower()] = index

def addSynonyms(name, synonyms):
	index = nameToIndex[name.lower()];
	for synonym in synonyms:
		nameToIndex[synonym.lower()] = index

# hardcoded "synonyms". Perhaps using some kind of nationality and city database would help...
addSynonyms("united states", ["america", "american", "americans", "the united states", "the united states of america", "us", "usa"])
addSynonyms("syrian arab republic", ["syria", "syrian", "syrians"])
addSynonyms("viet nam", ["vietnam"])
addSynonyms("afghanistan", ["afghan"])
addSynonyms("united kingdom", ["aberdeen", "britain", "england", "scotland", "uk"])
addSynonyms("iraq", ["baghdad"])
addSynonyms("libyan arab jamahiriya", ["benghazi", "libya", "libyan"])
addSynonyms("belgium", ["brussels"])
addSynonyms("canada", ["canadian"])
addSynonyms("china", ["chinese"])
addSynonyms("denmark", ["copenhagen"])
addSynonyms("cuba", ["cuban"])
addSynonyms("united arab emirates", ["dubai"])
addSynonyms("france", ["french", "nice", "paris"])
addSynonyms("switzerland", ["geneva"])
addSynonyms("iran (islamic republic of)", ["iran", "iranians", "persians"])
addSynonyms("mexico", ["mexican", "mexicans"])
addSynonyms("germany", ["munich"])
addSynonyms("palestine", ["palestinian", "palestinians"])
addSynonyms("poland", ["polish"])
addSynonyms("czech republic", ["prague", "the czech republic"])
addSynonyms("russia", ["russian", "russians", "the soviet union"])
addSynonyms("somalia", ["somali"])
addSynonyms("korea, republic of", ["south korea"])
addSynonyms("korea, democratic people's republic of", ["north korea", "n korea"])
addSynonyms("united republic of tanzania", ["tanzania"])


nlp = spacy.load('en')
corpus = open("corpus.txt", "r").read()

doc = nlp(corpus)

rankings = {}

for ent in doc.ents:
	if ent.label_ == "GPE" or ent.label_ == "NORP":
		word = re.sub(r"[^a-z ]", "", ent.text.lower())
		index = nameToIndex.get(word, -1)
		if index == -1:
			#print(word)
			pass
		else:
			totals[index] += 1

for total in totals:
	print(total)
