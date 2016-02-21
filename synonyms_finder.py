# -*- coding: utf-8 -*-
import codecs
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

def prepare_list() :
	synonyms = []
	with codecs.open("polski_thesaurus.txt", encoding="utf-8", errors='ignore') as synonyms_file : 
		lines = synonyms_file.readlines() 
		for i in lines : 
			words = i.split(";")
			group = words[1:(len(words)-1)]
			synonyms.append(group)
		return synonyms

def get_synonymes_for_word(word, synonyms_list) :
	synonyms = []
	for i in synonyms_list : 
		current_group = i
		if word in current_group :
			synonyms.extend(current_group)
	return list(set(synonyms))

# test = prepare_list()
# syn = get_synonymes_for_word("irytować", test)
# print len(syn)
# for i in syn : 
# 	print i