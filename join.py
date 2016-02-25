# -*- coding: utf-8 -*-
import sys
import sentence_tokenizing
from sentence_tokenizing import * 
import online_version
from online_version import *
import offline_version
from offline_version import *
import congruence_finder
from congruence_finder import * 
import synonyms_finder
from synonyms_finder import *  

reload(sys)
sys.setdefaultencoding("utf-8")

#testy jak to się wszystko integruje
#dostępne taggery [wersja online]: "WCRFT", "Pantera", "Concrafr", "WMBT", "Polita"
#dostępne narzędzia do koreferencji: "Ruler", "Bartek"

def pretty_print(lista) :
	res = ""
	for i in lista :
		res = res + " " + i
	return res

def pretty_print_d(dict) :
	for i, j in dict.items() : 
		print i + " -> " + str(j)

def find_form(word, dict) :
	for i in dict.keys() :
		if(dict[i][1] == word) :
			return i

# print "processing started"
file_n = "plain.txt"
file_o = "sentenced.txt"
# text_contents = codecs.open(file_n, encoding="utf-8", errors='ignore').read()
# multiservice = call_multiservice(text_contents, "Concraft", "Ruler")
# sentence_dictionary = parse_multiservice_output(multiservice)[0]
# coreference_words = parse_multiservice_output(multiservice)[1]
# congruent_words = find_congruent_words("sprawą", sentence_dictionary)
# print congruent_words
# print coreference_words

# coreference = {}
# for i in coreference_words :
# 	tmp = i.split(" ")
# 	if(len(tmp)==1) :
# 		form = find_form(i, sentence_dictionary)
# 		i_tags = sentence_dictionary[form.encode("utf-8")][0]
# 		# print form + " " + i_tags
# 	else : 
# 		for w in tmp : 
# 			form = find_form(w, sentence_dictionary)
# 			# print form + " -> " + sentence_dictionary[form][0]
# 			if "noun" in sentence_dictionary[form][0] :
# 				i_tags = sentence_dictionary[form.encode("utf-8")][0]
# 				# print form + " " + i_tags
# 	words = []
# 	for j in sentence_dictionary.keys() :
# 		word = j
# 		tags = sentence_dictionary[j][0]
# 		base_form = sentence_dictionary[j][1]
# 		if (i == base_form and not(base_form == "on" and tags[4] == i_tags[4])) :
# 			words.append(j)
# 		elif (tags == i_tags) :
# 			words.append(j)
# 		elif (base_form == "on" and tags[4] == i_tags[4]) :
# 			words.append(j)
# 	coreference[i] = words
# for i,j in coreference.items() :
# 	print i + " -> " + pretty_print(j) 



# for i,j in sentence_dictionary.items() : 
# 	print i + " -> " + pretty_print(j)
call_toki(file_n, file_o)
sentences = parse_toki_output(file_o)
con = {}
for sentence in sentences : 
	print sentence
	# print "**** multiservice ****"
	if "sprawą" in sentence :
		index = sentences.index(sentence)
first_sentence = sentences[index]
multiservice = call_multiservice(first_sentence, "Concraft", "Ruler")
sentence_dictionary = parse_multiservice_output(multiservice)[0]
tags = sentence_dictionary["sprawą".encode("utf-8")][0]
congruent_words = find_congruent_words("sprawą", sentence_dictionary, tags)
# pretty_print_d(congruent_words)

# print tags
base_form = sentence_dictionary["sprawą".encode("utf-8")][1]
for i in range(index+1, len(sentences)) : 
	next_sentence = sentences[i]
	next_sentence_dictionary = parse_multiservice_output(call_multiservice(next_sentence, "Concraft", "Ruler"))
	#todo: check other nouns in sentence 
	next_congruent_words = find_congruent_words("sprawą", next_sentence_dictionary[0], tags)
	pretty_print_d(next_congruent_words)

# print index
	# multiservice = call_multiservice(sentence, "Concraft", "Ruler")
	# concraft = call_concraft(sentence)
	# sentence_dictionary = parse_multiservice_output(multiservice)[0]
	# sentence_dictionary = parse_concraft_output()
	# pretty_print_d(sentence_dictionary)
	# con = find_congruent_words("sprawą", sentence_dictionary)
	# for i, j in con.items() : 
	# 	print i + " -> " + pretty_print(j)
	# print "*****"
	# syn = prepare_list()
	# base_form = sentence_dictionary["sprawą".encode("utf-8")][1]
	# synonyms = get_synonymes_for_word(base_form, syn)
	# print synonyms
	# for i in sentence_dictionary.keys() : 
	# 	base = sentence_dictionary[i][1].encode("utf-8")
		# print base
		# print len(get_synonymes_for_word(base.encode("utf-8"), syn))
		# synonyms = get_synonymes_for_word(base, syn)
		# print base + " -> " + str(synonyms) 
		# pretty_print(get_synonymes_for_word(base.lower(), syn))
	# print len(con)
	# for i, j in con.items() : 
	# 	print i + " -> " + pretty_print(j)
	# for i, j in  parse_multiservice_output(multiservice).items() : 
	# 	print i + " -> " + j
	# print "**** concraft ****"
	# concraft = call_concraft(sentence)
	# for i, j in parse_concraft_output().items() : 
	# 	print i + " -> " + j
	# print "##############"
# print "done & saved to file"
