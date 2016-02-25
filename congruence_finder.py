# -*- coding: utf-8 -*-
import sys
import codecs

reload(sys)
sys.setdefaultencoding("utf-8")

#znajduje wyrazy w związku zgody z zadanym

def check_if_word_exists_in_sentence(word, input_sentence) :
	if word in get_words_from_sentence(input_sentence) :
		return True
	else :
		return False

def is_word_a_noun(word, tags) : 
	subst_tag = tags.split(":")[0]
	return (subst_tag in ["subst", "noun"])

def check_if_words_are_in_congruence(base_word, base_word_tags, checked_word, checked_word_tags) : 
	#base_word - slowo do ktorego szukamy zaleznych
	#checked_word - aktualnie sprawdzane slowo
	#parsed_output - tagi slowa checked_word
	if (base_word == checked_word) :
		return False
	elif(not is_word_a_noun(base_word, base_word_tags)) :
		return False
	else : 
		base_tags = base_word_tags.split(":")
		checked_tags = checked_word_tags.split(":")
		base_sg_pl = base_tags[1]
		base_gender = base_tags[3]
		base_case = base_tags[2]
		if (not base_sg_pl in checked_tags) :
			return False
		else : 
			if (checked_tags[0] in ["verbfin", "praet", "pot"]) : 
				if(base_gender in checked_tags) :
					return True
				else : 
					if (base_gender in ["m1", "m2", "m3"] and ("m1" in checked_tags or "m2" in checked_tags or "m3" in checked_tags)) :
						return True
		if (checked_tags[0] in ["adj", "ppas", "pact", "num", "ppron3"]) :
				if(base_gender in checked_tags) :
					return True
				else : 
					if (base_gender in ["m1", "m2", "m3"] and ("m1" in checked_tags or "m2" in checked_tags or "m3" in checked_tags)) :
						return True
		return False

def find_congruent_words(word, sentence_dictionary, word_tags) :
	#sentence_dictionary jest w formie slowo -> (tagi, base)
	congruent_words = {}
	# if (word not in sentence_dictionary.keys()) :
	# 	return {}
	# else :
	congruent_words[word] = []
	# word_tags = sentence_dictionary[word.encode("utf-8")][0]
	for i, j in sentence_dictionary.items() : 
		checked_word = i
		checked_word_tags = j[0]
		if(check_if_words_are_in_congruence(word, word_tags, checked_word, checked_word_tags)) : 
			congruent_words[word].append(checked_word)
	return congruent_words

